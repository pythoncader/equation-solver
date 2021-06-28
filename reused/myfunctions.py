def clear():
    try:
        import replit
        replit.clear()
        print("You are using replit\n")
    except Exception:
        import os
        returnvalue = os.system("cls")
        print("You are using a Windows PC\n")
        if returnvalue != 0:
            os.system("clear")
            print("You are using OSX or Linux\n")