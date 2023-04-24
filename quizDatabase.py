from tkinter import *
from tkinter import messagebox as mb
import json
import mysql.connector




def started():
    global usernameN, startFrame,myQuesFrame
    myQuesFrame = Frame(gui, width=800, height=450)
    myQuesFrame.place(x=0, y=0)
    myQuesFrame.configure(bg='#A5D7E8')
    startFrame.destroy()
    quiz = Quiz()
    


myQuesFrame = None
timeleft = 60


class Quiz:

    def __init__(self):

        self.q_no = 0

        self.display_title()
        self.display_question()

        self.opt_selected = IntVar()

        self.opts = self.radio_buttons()

        self.display_options()

        self.buttons()

        self.data_size = len(question)

        self.correct = 0
        global timeleft
        if timeleft == 60:
            self.countdown()

    def countdown(self):
         global timeLabel
         global timeleft
         if timeleft == 0:
             self.display_result()
             gui.destroy()
         if timeleft > 0:
             timeleft -= 1
             timeLabel.config(text="Time Left:"+str(timeleft))
             timeLabel.after(1000, self.countdown)

    def display_result(self):
        global Name

        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"

        score = int(self.correct / self.data_size * 100)

        global timeleft
        timeleft = -1

        global nameSignUp, emailSignUp, usernameSignUp, passwordSignUp,  signUpF,logSignBtnF,loginF,myQuesFrame
        
        signUpF = Frame(gui, width=800, height=450)
        signUpF.place(x=0, y=0)

        SignUpLabel = Label(signUpF, text="Result", font=(
         "ariel", 26, "bold", "underline"), bg='#A5D7E8')
        SignUpLabel.place(x=340, y=20)

        namesignUpLabel = Label(signUpF, text="Name:",
                             bg='#A5D7E8', font=("ariel", 16, "bold"))
        namesignUpLabel.place(x=230, y=120)
        nameSignUp = Label(signUpF, text=Name, bg="#A5D7E8", fg="#5F264A",font=(
            "ariel", 16, "bold"))
        nameSignUp.place(x=400, y=120)

        emailsignUpLabel = Label(signUpF, text="Score:",
                              bg='#A5D7E8', font=("ariel", 16, "bold"))
        emailsignUpLabel.place(x=230, y=160)
        emailSignUp = Label(signUpF, text=score, bg="#A5D7E8", font=(
            "ariel", 16, "bold"),fg="#5F264A")
        emailSignUp.place(x=400, y=160)

        usernamesignUpLabel = Label(
        signUpF, text="Correct:", bg='#A5D7E8', font=("ariel", 16, "bold"))
        usernamesignUpLabel.place(x=230, y=200)
        usernameSignUp = Label(
            signUpF, text=self.correct, bg="#A5D7E8", font=(
                "ariel", 16, "bold"),fg="#5F264A")
        usernameSignUp.place(x=400, y=200)

        passwordSignUpLabel = Label(signUpF, text="Wrong:", font=(
         "ariel", 16, "bold"), bg='#A5D7E8')
        passwordSignUpLabel.place(x=230, y=240)
        passwordSignUp = Label(signUpF, text=wrong_count,
                               bg="#A5D7E8", font=(
                                   "ariel", 16, "bold"), fg="#5F264A")
        passwordSignUp.place(x=400, y=240)

        submitsignup = Button(signUpF, text="Home", command=homePage,
                           width=10, bg="#0B2447", fg="white", font=("ariel", 16, "bold"))
        submitsignup.place(x=330, y=300)

        signUpF.configure(bg='#A5D7E8')
        myQuesFrame.destroy()
       



    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:

            return True

    def next_btn(self):

        if self.check_ans(self.q_no):

            self.correct += 1

        self.q_no += 1

        if self.q_no == self.data_size:

            self.display_result()

            # gui.destroy()
        else:

            self.display_question()
            self.display_options()

    def buttons(self):
        global timeLabel
        timeLabel = Label(myQuesFrame, text="Time Left:" +
                          str(timeleft), font=("Helvetica", 16))
        timeLabel.configure(bg="#A5D7E8")
        timeLabel.place(x=100, y=70)

        next_button = Button(myQuesFrame, text="Next", command=self.next_btn,
                             width=10, bg="#0B2447", fg="white", font=("ariel", 16, "bold"))

        next_button.place(x=350, y=390)

        quit_button = Button(myQuesFrame, text="Quit", command=gui.destroy,
                             width=5, bg="red", fg="white", font=("ariel", 16, " bold"))

        quit_button.place(x=700, y=70)

    def display_options(self):
        val = 0

        self.opt_selected.set(0)

        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):

        q_no = Label(myQuesFrame, text=question[self.q_no], width=60,
                     font=('ariel', 16, 'bold'), anchor='w')
        q_no.configure(bg="#A5D7E8")

        q_no.place(x=70, y=140)

    def display_title(self):

        title = Label(myQuesFrame, text="Quiz Hunger !!",
                      width=50, bg="#0B2447", fg="white", font=("ariel", 20, "bold"), pady=10)

        title.place(x=0, y=2)

    def radio_buttons(self):

        q_list = []

        y_pos = 180

        while len(q_list) < 4:

            radio_btn = Radiobutton(myQuesFrame, text=" ", variable=self.opt_selected,
                                    value=len(q_list)+1, font=("ariel", 14))

            q_list.append(radio_btn)

            radio_btn.place(x=100, y=y_pos)

            radio_btn.configure(bg="#A5D7E8")
            y_pos += 40

        return q_list
    
#main gui creating
gui = Tk()
gui.geometry("800x450")
gui.title("Quiz App")

#jason file for questions
with open('data.json') as f:
    data = json.load(f)


question = (data['question'])
options = (data['options'])
answer = (data['answer'])


def homePage():
     global timeleft
     timeleft = 60
     global usernameN, startFrame, nameOfCurrentUser
     startFrame = Frame(gui, width=800, height=450)
     startFrame.place(x=0, y=0)

     WelComeUser = Label(startFrame, text=nameOfCurrentUser+",",
                         bg="#A5D7E8", fg="#0B2447", font=("ariel", 26, "bold"))
     WelComeUser.place(x=140, y=60)

     WelCome = Label(startFrame, text="Welcome to Quiz Hunger !!",
                     bg="#A5D7E8", fg="#5F264A", font=("ariel", 22, "bold"))
     WelCome.place(x=270, y=62)

     l2 = Label(startFrame, text="Click on Start Quiz to Start !",
                bg="#A5D7E8", fg="#19376D", font=("ariel", 20, "bold"))
     l2.place(x=160, y=160)

     enter = Button(startFrame, text="Start Quiz",  width=10, bg="#5F264A",
                    fg="white", font=("ariel", 16, "bold"), command=started)
     enter.place(x=320, y=270)
     emailSignUp.delete(0,END)
     usernameSignUp.delete(0,END)
     passwordSignUp.delete(0,END)

def clearInfo():
    usernameLogIn.delete(0,END)
    passwordLogIn.delete(0,END)

def submitFormSign():
     global nameSignUp, emailSignUp, usernameSignUp, passwordSignUp, mycursor,Name,signUpF, nameOfCurrentUser
     name = nameSignUp.get()
     email = emailSignUp.get()
     usernameSign = usernameSignUp.get()
     passwordSign = passwordSignUp.get()
     data = (name, email, usernameSign, passwordSign)     
     print(data)
     nameOfCurrentUser=usernameSign
     Name=name
     if usernameSign == "" or passwordSign == "" or email == "" or name=="":
         mb.showerror("Error", "All fields are required !")
     else:
          try:
             global mydb
             mydb = mysql.connector.connect(host="localhost", user="root",passwd="root")
            #  global mycursor
             mycursor = mydb.cursor()  
             print("Connected....!!!!!!!")   
          except:
             print("Error..........")

          try:
             query ="create database userdata"
             mycursor.execute(query)
             query="use userdata"
             mycursor.execute(query)
             query ="create table data(id int auto_increment primary key not null,name varchar(20),email varchar(20),username varchar(100),password varchar(20))"
             mycursor.execute(query)

             print("databse created....!!!!!!")
          except:
             mycursor.execute('use userdata')
          
          query ="select * from data where username=%s"
          mycursor.execute(query,(usernameSign,))

          row = mycursor.fetchone()
          if row != None:
              mb.showerror("Error","Username Already Exists !")
          else:   
             query = "INSERT INTO data(name,email,username,password) VALUES(%s, %s, %s, %s )"

             data = (name, email, usernameSign, passwordSign)
             mycursor.execute(query, data)
             mydb.commit()
             mydb.close()
             mb.showinfo("Welcome..", "Sign Up Successful !!")
             clear()
             signUpF.destroy()
             homePage()



def submitFormLogin():
    global usernameLogIn, passwordLogIn, nameOfCurrentUser, loginF, mycursor

    usernameLoginCh = usernameLogIn.get()
    passwordLoginCh = passwordLogIn.get()
    print(usernameLoginCh,passwordLoginCh)
    
    if usernameLoginCh=="" or passwordLoginCh=="":
        mb.showerror("Error","All fields are required !")
    else:
        global mydb, mycursor,Name

        try:
             global mydb,mycursor
             mydb = mysql.connector.connect(
                 host="localhost", user="root",passwd="root",database="userdata")
             global mycursor
             mycursor = mydb.cursor()
             print("Login connected...!!!!!")
        except:
             print("Error....")  
        
        query = "use userdata"
        mycursor.execute(query)
        query="select * from data where username=%s and password=%s"
        mycursor.execute(query,(usernameLoginCh,passwordLoginCh))
        row = mycursor.fetchone()

        if row !=None:
            nameOfCurrentUser=row[3]
            Name=row[1]
            mb.showinfo("Success","Login successful !")
            clearInfo()
            homePage()
            loginF.destroy()
            
        else:
            mb.showerror("Error", "Invalid Username or Password .")
            LoginForm()
            
    
def LoginForm():
     global usernameLogIn, passwordLogIn, logSignBtnF, loginF
     

     loginF = Frame(gui,width=800,height=450)
     loginF.place(x=0,y=0)
     
     loginLabel = Label(loginF, text="Login", font=(
         "ariel", 26, "bold","underline"), bg='#A5D7E8', fg="#0B2447")
     loginLabel.place(x=330,y=40)
     
     usernameLogInLabel = Label(
         loginF, text="Username:", bg='#A5D7E8', font=("ariel", 20, "bold"))
     usernameLogInLabel.place(x=200,y=140)
     usernameLogIn = Entry(loginF,font=22)
     usernameLogIn.place(x=380,y=140)

     passwordLogInLabel = Label(
         loginF, text="Password:", font=("ariel", 20, "bold"),bg='#A5D7E8')
     passwordLogInLabel.place(x=200, y=190)
     passwordLogIn = Entry(loginF, font=22)
     passwordLogIn.place(x=380,y=190)
      
     submitLogin = Button(loginF, text="Login", command=submitFormLogin,
                          width=10, bg="#0B2447", fg="white", font=("ariel", 16, "bold"))
     submitLogin.place(x=320, y=300)

     gotohome = Button(loginF, text="Home", command=logSignBtn,
                           width=8, bg="#19376D", fg="white", font=("ariel", 12, "bold"))
     gotohome.place(x=280, y=400)
     gotosignup= Button(loginF, text="Sign Up", command=SignForm,
                        width=8, bg="#19376D", fg="white", font=("ariel", 12, "bold"))
     gotosignup.place(x=400, y=400)
     loginF.configure(bg='#A5D7E8')

     logSignBtnF.destroy()


def SignForm():
     global nameSignUp, emailSignUp, usernameSignUp, passwordSignUp,  signUpF,logSignBtnF, loginF
         
     signUpF = Frame(gui, width=800, height=450)
     signUpF.place(x=0, y=0)

     SignUpLabel = Label(signUpF, text="Sign Up", font=("ariel", 26, "bold","underline"), bg='#A5D7E8')
     SignUpLabel.place(x=340, y=20)

     namesignUpLabel = Label(signUpF, text="Name:", bg='#A5D7E8', font=("ariel", 16, "bold"))
     namesignUpLabel.place(x=230, y=120)
     nameSignUp = Entry(signUpF, font=18)
     nameSignUp.place(x=400, y=120)

     emailsignUpLabel = Label(
         signUpF, text="Email:", bg='#A5D7E8', font=("ariel", 16, "bold"))
     emailsignUpLabel.place(x=230, y=160)
     emailSignUp = Entry(signUpF, font=18)
     emailSignUp.place(x=400, y=160)

     usernamesignUpLabel = Label(
         signUpF, text="Username:", bg='#A5D7E8', font=("ariel", 16, "bold"))
     usernamesignUpLabel.place(x=230, y=200)
     usernameSignUp = Entry(signUpF, font=18)
     usernameSignUp.place(x=400, y=200)

     passwordSignUpLabel = Label(signUpF, text="Password:", font=("ariel", 16, "bold"), bg='#A5D7E8')
     passwordSignUpLabel.place(x=230, y=240)
     passwordSignUp = Entry(signUpF, font=18)
     passwordSignUp.place(x=400, y=240)
     
     submitsignup = Button(signUpF, text="Sign Up", command=submitFormSign,
                           width=10, bg="#0B2447", fg="white", font=("ariel", 16, "bold"))
     submitsignup.place(x=330, y=300)
     gotohome = Button(signUpF, text="Home", command=logSignBtn,
                       width=8, bg="#19376D", fg="white", font=("ariel", 12, "bold"))
     gotohome.place(x=300, y=400)
     gotologin = Button(signUpF, text="Login", command=LoginForm,
                        width=8, bg="#19376D", fg="white", font=("ariel", 12, "bold"))
     gotologin.place(x=420, y=400)

     signUpF.configure(bg='#A5D7E8')

     logSignBtnF.destroy()


def logSignBtn():
     global loginBtn, SignUpBtn, logSignBtnF
     logSignBtnF = Frame(gui,width=800,height=450)
     logSignBtnF.place(x=0,y=0)
     
     WelCome = Label(logSignBtnF, text="Welcome to Quiz Hunger !!",bg="#A5D7E8", fg="#0B2447", font=("ariel", 26, "bold"))
     WelCome.place(x=170, y=60)

     WelComeN = Label(logSignBtnF, text="Login or Sign Up to start the Quiz !!!",bg="#A5D7E8", fg="#5F264A", font=("ariel", 24, "bold"))
     WelComeN.place(x=110, y=130)

     loginBtn = Button(logSignBtnF, text="Login",  width=10, bg="#0B2447",
                    fg="white", font=("ariel", 16, "bold"), command=LoginForm)
     loginBtn.place(x=200, y=250)

     SignUpBtn = Button(logSignBtnF, text="Sign Up",  width=10, bg="#0B2447",
                    fg="white", font=("ariel", 16, "bold"), command=SignForm)
     SignUpBtn.place(x=420, y=250)
     
     logSignBtnF.configure(bg='#A5D7E8')
     

logSignBtn()

gui.mainloop()
