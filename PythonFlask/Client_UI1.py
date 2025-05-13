import tkinter as tk
import requests

root = tk.Tk()
root.title('BMI Input')
root.geometry('720x720')

gender = tk.StringVar()
name = tk.StringVar()
password = tk.StringVar()
birthday = tk.StringVar()
height = tk.StringVar()
weight = tk.StringVar()
jsonText = tk.StringVar()
serverText = tk.StringVar()

radio_btn1 = tk.Radiobutton(root,text='Male',font=('Arial',30,'bold'),variable=gender,value='male')
radio_btn2 = tk.Radiobutton(root,text='Female',font=('Arial',30,'bold'),variable=gender,value='female')
radio_btn1.select()

labelName = tk.Label(root, text='Name:')
entryName = tk.Entry(root,font=('Arial',30,'bold'),textvariable=name)

labelPassword = tk.Label(root, text='Password:')
entryPassword = tk.Entry(root,show='*',font=('Arial',30,'bold'),textvariable=password)

labelHeight = tk.Label(root, text='Height(m):')
entryHeight = tk.Entry(root,font=('Arial',30,'bold'),textvariable=height)

labelWeight = tk.Label(root, text='Weight(kg):')
entryWeight = tk.Entry(root,font=('Arial',30,'bold'),textvariable=weight)

labelBirthday = tk.Label(root, text='Birthday(UTC):')
entryBirthday = tk.Entry(root,font=('Arial',30,'bold'),textvariable=birthday)

Jsonlabel = tk.Label(root,textvariable=jsonText,font=('Arial',20,'bold'),fg='#f00')

Serverlabel = tk.Label(root,textvariable=serverText,font=('Arial',20,'bold'),fg='#00f')

def submit():
    global gender,name,password,birthday,height,weight,jsonText
    temp =f'gender={gender.get()}\nname={name.get()}\npassword={password.get()}\nbirthday={birthday.get()}\nheight={height.get()}\nweight={weight.get()}'
    jsonText.set(temp)
    url = 'http://wiciar.com/bmi/submit'
    jsonSet = {'name': name.get(),
               'password': password.get(),
               'birthday':birthday.get(),
               'gender':gender.get(),
               'height':float(height.get()),
               'weight':float(weight.get())}
    #print(jsonSet)
    try:
        response = requests.post(url, json=jsonSet)
        serverText.set(response.json()['message'])
        print('Response JSON:', response.json())
    except:
        serverText.set('Server Link error!!!')
        print('Status Code:', response.status_code)
    
submit_btn1 = tk.Button(root,command=submit,text='PassData',font=('Arial',30,'bold'),padx=10,pady=10,activeforeground='#f00')

radio_btn1.grid(column=0, row=0) 
radio_btn2.grid(column=1, row=0)
labelName.grid(column=0, row=1)
entryName.grid(column=1, row=1)
labelPassword.grid(column=0, row=2)
entryPassword.grid(column=1, row=2)
labelHeight.grid(column=0, row=3)
entryHeight.grid(column=1, row=3)
labelWeight.grid(column=0, row=4)
entryWeight.grid(column=1, row=4)
labelBirthday.grid(column=0, row=5)
entryBirthday.grid(column=1, row=5)
submit_btn1.grid(column=1, row=6)
Jsonlabel.grid(column=1, row=7)
Serverlabel.grid(column=1, row=8)
# 顯示按鈕
root.mainloop()  # 放在主迴圈中