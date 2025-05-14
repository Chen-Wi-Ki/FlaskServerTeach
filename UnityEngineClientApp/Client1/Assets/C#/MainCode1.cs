using System.Collections;
using System.Text;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

public class MainCode1 : MonoBehaviour
{
    public ToggleGroup ToggleGroupGender;
    public InputField InputName, InputPassword, InputHeight, InputWeight, InputBirthday;
    public Button SubmitButton;
    public Text CallBackMessage;
    public void PostCode()
    {
        string gender = ToggleGroupGender.GetFirstActiveToggle().name;
        string name = InputName.text;
        string password = InputPassword.text;
        float height = float.Parse(InputHeight.text);
        float weight = float.Parse(InputWeight.text);
        string birthday = InputBirthday.text;
        StartCoroutine(PostToServer(gender, name, password, height, weight, birthday));
    }
    IEnumerator PostToServer(string gender, string name, string password, float height, float weight, string birthday)
    {
        string jsonData = JsonUtility.ToJson(new PostData
        {
            gender = gender,
            name = name,
            password = password,
            height = height,
            weight = weight,
            birthday = birthday
        });
        print(jsonData);
        // change UTF8 of byte[]
        byte[] jsonBytes = Encoding.UTF8.GetBytes(jsonData);
        // Build UnityWebRequest
        using (UnityWebRequest www = new UnityWebRequest("https://wiciar.com/bmi/submit", "POST"))
        {
            www.uploadHandler = new UploadHandlerRaw(jsonBytes);
            www.downloadHandler = new DownloadHandlerBuffer();
            www.SetRequestHeader("Content-Type", "application/json");

            yield return www.SendWebRequest();

            if (www.result == UnityWebRequest.Result.Success)
            {
                CallBackMessage.text = "Success¡G" + www.downloadHandler.text;
            }
            else
            {
                CallBackMessage.text = CallBackMessage.text + "error¡G" + www.downloadHandler.text;
            }
        }
    }
    [System.Serializable]
    public class PostData
    {
        public string gender;
        public string name;
        public string password;
        public float height;
        public float weight;
        public string birthday;
    }
    // Start is called before the first frame update
    void Start()
    {
        
    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
