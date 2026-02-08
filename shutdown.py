def allowshutdown():
    print("Shutting down...")
def noshutdown():
    print("Abort Shutt down...")
def errorshutdown():
    print("Sorry sir! answer in yess or no")
input=input("Can i shutt down Yess/No : ")
if input=="yess":
    allowshutdown()
elif input=="no":
    noshutdown()
else:
    errorshutdown()