package wi.ki.client1;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;
import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import com.android.volley.Request;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.RequestQueue;
import com.android.volley.toolbox.Volley;
import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {
    RadioGroup radioGroupGender;
    EditText editTextName,editTextPassword,editTextBirthday,editTextHeight,editTextWeight;
    TextView TextViewRequest;
    final String SERVER_URL = "http://wiciar.com/bmi/submit";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
        radioGroupGender = findViewById(R.id.radioGroupGender);
        editTextName = findViewById(R.id.editTextName);
        editTextPassword = findViewById(R.id.editTextPassword);
        editTextBirthday = findViewById(R.id.editTextBirthday);
        editTextHeight = findViewById(R.id.editTextHeight);
        editTextWeight = findViewById(R.id.editTextWeight);
        TextViewRequest = findViewById(R.id.TextViewRequest);
    }

    public void OnClick_Submit(View v)
    {
        int selectedGenderId = radioGroupGender.getCheckedRadioButtonId();
        String gender = "";
        if (selectedGenderId == R.id.radioMale) {
            gender = "male";
        } else if (selectedGenderId == R.id.radioFemale) {
            gender = "female";
        }
        String name = editTextName.getText().toString();
        String password = editTextPassword.getText().toString();
        String birthday = editTextBirthday.getText().toString();
        String heightStr = editTextHeight.getText().toString();
        String weightStr = editTextWeight.getText().toString();

        RequestQueue queue = Volley.newRequestQueue(this);
        try {
            JSONObject postData = new JSONObject();
            postData.put("name", name);
            postData.put("birthday", birthday);
            postData.put("height", Float.parseFloat(heightStr));
            postData.put("weight", Float.parseFloat(weightStr));
            postData.put("password", password);
            postData.put("gender", gender);

            JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(
                    Request.Method.POST,
                    SERVER_URL,
                    postData,
                    response -> {
                        try {
                            TextViewRequest.setText(response.getString("message"));
                        } catch (JSONException e) {
                            Toast.makeText(this, "error: message null.", Toast.LENGTH_SHORT).show();
                        }
                    },
                    error -> Toast.makeText(MainActivity.this, "password error.", Toast.LENGTH_LONG).show()
            );

            queue.add(jsonObjectRequest);

        } catch (Exception e) {
            Toast.makeText(this, "error: " + e.getMessage(), Toast.LENGTH_SHORT).show();
        }
    }
}