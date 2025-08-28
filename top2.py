from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTK
root = Tk()
root.title('Denomination counter')
root.configure(bg='light blue')
root.geometry('650x400')
upload = Image.open("app_img.jpg")
upload = upload.resize((300,300))
image = imageTk.PhotoImage(upload)
Label = Label(root, image=image, bg='light blue')
Label.place(x=180, y=20)
label1 = Label(root,text="hey user! Welcome to denomination counter application.",bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)
def Msg():
    Msgbox = messagebox.showino("Alert", "Do you want to calculate the denomination count")
    if Msgbox == 'ok':
        topwin()
button = Button(root,text="let's get started ",command= Msg,bg='brown',fg = 'white')
button.place(x=260, y=360)
def topwin():
    top = Toplevel()
    top.title("Denomination calculater")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")
    label = Label(top, text="Enter total amount",bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="here are the number of notes for each denomination", bg='light grey')
    l1 = Label(top, text="2000",bg = 'light grey')
    l2 = Label(top, text="100",bg = 'light grey')
    l3 = Label(top, text="500",bg = 'light grey')
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    def caculater():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            
            t1.insert(END, str(note2000))
            t1.insert(END, str(note500))
            t1.insert(END, str(note100))
            
        except ValueError:
            messagebox.showerror("Error","please enter a valid")
    btn = Button(top, text='caculate', command=caculater, bg='brown',fg='white')
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)
    
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    top.mainloop()
root.mainloop()
    