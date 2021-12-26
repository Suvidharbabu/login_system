print("               Login Page                 ")
def Newuser():
    db=open("Database.txt",'reeee')
    Username=input("Create Username:")
    Password=input("Create Password:")
    Password1=input("Re-Enter Password:")
    u=[]
    p=[]
    for i in db:
      a,b = i.split(", ")
      b = b.strip()
      u.append(a)
      p.append(b)
    data = dict(zip(u,p)) #Created dictionary for Username and password to match
    #print (data)
    emailchar = ["@","."]
    special_char=["!","#","$","%","&","@",","]
    specialchar1= ['!','#','$','%','&',',']
    condition="@."

    if not any(char in emailchar for char in Username):
      print("Enter vaild email address")
      Newuser()
    if Username[0].isdigit():
      print("First letter should not be number, Enter valid email address")
      Newuser()
    if Username[0] in emailchar:
      print("Enter valid email address")
      Newuser()
    if Username[0] in special_char:
      print("Enter valid email address")
      Newuser()
    if condition in Username:
      print("Enter valid email address")
      Newuser()
    if Username in specialchar1:
      print("Enter valid email address")
      Newuser()

    if Password!=Password1:
        print("Password does not match")
        Newuser()
    elif Username in u:
        print("Username exists")
        Newuser()
    else:
        if len(Password)<=5:
            print("Password is too short")
            Newuser()
        if len(Password)>16:
            print("Password should not be greater than 16")
            Newuser()
        if not any(char.isdigit() for char in Password):
            print("Password should have atleast one numeric")
            Newuser()
        if not any(char.isupper() for char in Password):
            print("Password should have atleast one uppercase letter")
            Newuser()
        if not any(char.islower for char in Password):
            print("Password should have atleast one lowercase letter")
            Newuser()
        if not any(char in special_char for char in Password):
            print("Password should have atleast one special character")
            Newuser()
        else:
            db=open("Database.txt",'a')
            db.write(Username+ ", "+Password+"\n")
            print("Succesfully Registered")

def access():
    db=open("Database.txt","r")
    Username=input("Enter your username:")
    Password=input("Enter your password:")

    if not len(Username or Password)<1:
        u = []
        p = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            u.append(a)
            p.append(b)
        data = dict(zip(u, p))

        try:
            if data[Username]:
                try:
                    if Password==data[Username]:
                        print("Login Success")
                        print("Hi",Username)
                    else:
                        print("Incorrect Password")
                except:
                    print("Incorrect Username or password")
            else:
                print("Username or Password doesn't exists")
        except:
            print("Username or password doesn't exists, Registration required")
            option = input("Do you want to register as Newuser: Yes or No,")
            if option=="Yes":
                Newuser()
            else:
                print("Login denied")
    else:
        print("Please enter the value")
        access()

def Reset():
    db=open("Database.txt","r")
    Username=input("Enter your Username:")
    u = []
    p = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        u.append(a)
        p.append(b)
    data = dict(zip(u, p))

    if Username in u:
        print(f"Your account Password:{data[Username]}")
    else:
        print("Username doesn't exists")
        Newreg=input("Do you want to register? Yes or No")
        if Newreg=="Yes":
            Newuser()
        else:
            print("Need valid Username")

def Dbase(Input=None):
  Input=input("Sign up or Login or Forgot Password:")
  if Input=="Sign up":
    Newuser()
  elif Input=="Login":
    access()
  elif Input=="Forgot Password":
    Reset()
  else:
    print("Enter valid option")
    Dbase()
Dbase()