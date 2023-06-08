import customtkinter
import subprocess

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

git_type =""

# "Local Git Only", "Remote Git Only", "Both Local & Remote Git"

def change_Git_Type(value: str):
    if value == "Select a Git type" or value == "":
       x = ""
    elif value == "Local Git Only":
        print("Local \nhide remote portions")
        accountName.pack_forget()
        repoName.pack_forget()
        fileDirectory.pack(padx = 30, pady = 20)
        gitMessage.pack(padx = 30, pady = 20)
        button.pack(padx = 15)
        git_type="local"
    elif value == "Remote Git Only":
        print("Remote \nhide local portions")
        fileDirectory.pack_forget()
        accountName.pack(padx = 30, pady = 20)
        repoName.pack(padx = 30, pady = 20)
        gitMessage.pack_forget()
        button.pack(padx = 15)
        git_type= "remote"
    elif value == "Both Local & Remote Git":
        print("Both \nshow all portions")
        fileDirectory.pack(padx = 30, pady = 20)
        accountName.pack(padx = 30, pady = 20)
        repoName.pack(padx = 30, pady = 20)
        gitMessage.pack(padx = 30, pady = 20)
        button.pack(padx = 15)
        git_type = "full"
    else :
        print(value)

def local_Git(directory,gitmsg):
    print("name")
    print(directory)
    print(gitmsg)
    subprocess.call("gitlocal.sh %s %s" % (str(directory),str(gitmsg)), shell=True) 
    
def remote_Git(directory,reponame,accountname):
    print("name")
    print(directory)
    print(reponame)
    subprocess.call("gitremote.sh %s %s" % (str(directory),str(reponame),str(accountname)), shell=True) 

def full_Git(directory,reponame,accountname,gitmsg):
    print("name")
    print(directory)
    print(reponame)
    subprocess.call("gitfull.sh %s %s" % (str(directory),str(reponame),str(accountname),str(gitmsg)), shell=True) 

root = customtkinter.CTk()
root.geometry("300x500")
root.title("Git Fast")

label = customtkinter.CTkLabel(master=root, text="Git FAST")
label.pack(pady=12, padx=10)
label.configure(font=('Helvetica bold',50))

options = customtkinter.CTkOptionMenu(master=root, values=["Select a Git type","Local Git Only", "Remote Git Only", "Both Local & Remote Git"], command=change_Git_Type)
options.pack(pady=10, padx=15)

frame = customtkinter.CTkFrame(master = root)
frame.pack(pady=20, padx=30, fill="both", expand="true")

accountName = customtkinter.CTkEntry(master = frame, placeholder_text="Github account name")
accountName.pack(padx = 30, pady = 20)

fileDirectory = customtkinter.CTkEntry(master = frame, placeholder_text="File Diretory")
fileDirectory.pack(padx = 30, pady = 20)

repoName = customtkinter.CTkEntry(master = frame, placeholder_text="Github Repo name")
repoName.pack(padx = 30, pady = 20)


gitMessage = customtkinter.CTkEntry(master = root, placeholder_text="Git message")
gitMessage.pack(padx = 30, pady = 20)

def runGIT():
    if str(fileDirectory.get()) != "":
        if git_type == "local":
            local_Git(fileDirectory.get(), gitMessage.get())
        elif git_type == "remote":
            remote_Git(fileDirectory.get(),repoName.get(), accountName.get())
        elif git_type == "full":
            full_Git(fileDirectory.get(),repoName.get(), accountName.get(), gitMessage.get())

button = customtkinter.CTkButton(master = root, text = "Commit & Push Repo", command=runGIT)
button.pack(padx = 15)




root.mainloop()