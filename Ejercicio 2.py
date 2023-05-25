from tkinter import Tk,Label,Entry,Button,Frame,PhotoImage,END,Scrollbar

root=Tk()
root.geometry("771x542")
root.resizable(0,0)
root.iconbitmap("favicon.ico")
root.title("Product Management")
root.config(bg="black")

#Table
class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(frTable, width=11,font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

lst = [(1,'Alet','Milk',3,200),
       (2,'Nesquik','Cereal',1,130),
       (3,'Isadora','Beans',5,200),
       (4,'Pepsi','2L Soda',3,130),
       (5,'Canoil','Oil',2,80),
       (6,"Pirelli","Tires",4,800)]

total_rows = len(lst)
total_columns = len(lst[0])

#Images

trashBin=PhotoImage(file= r"C:\Users\Ivan Armenta\Documents\Python Tkinter\TAP 2\delete-756.png")
search=PhotoImage(file= r"C:\Users\Ivan Armenta\Documents\Python Tkinter\TAP 2\search.png")

#Frames

#Main Frame
frMain=Frame(root)
frMain.place(x=20,y=20,width=731,height=502)
frMain.config(bg="brown",bd=3,relief="ridge")

#Table Frame
frTable=Frame(frMain)
frTable.place(x=15,y=240,width=695,height=240)

#Labels

#List1
li1=Label(frMain,text="ID Product:")
li1.place(x=30,y=20)
li1.config(fg="white",bg="brown",font=("Calibri",15,"bold"))

#List2
li2=Label(frMain,text="Name:")
li2.place(x=70,y=60)
li2.config(fg="white",bg="brown",font=("Calibri",15,"bold"))

#List3
li3=Label(frMain,text="Description:")
li3.place(x=23,y=100)
li3.config(fg="white",bg="brown",font=("Calibri",15,"bold"))

#List4
li4=Label(frMain,text="Quantity:")
li4.place(x=45,y=140)
li4.config(fg="white",bg="brown",font=("Calibri",15,"bold"))

#List5
li5=Label(frMain,text="Price:")
li5.place(x=78,y=180)
li5.config(fg="white",bg="brown",font=("Calibri",15,"bold"))

#Entries

#Entry List1
enLi1=Entry(frMain)
enLi1.place(x=150,y=20,width=250,height=30)
enLi1.config(bg="brown",fg="white",font=("Calibri",13),bd=3,relief="sunken")

#Entry List2
enLi2=Entry(frMain)
enLi2.place(x=150,y=60,width=250,height=30)
enLi2.config(bg="brown",fg="white",font=("Calibri",13),bd=3,relief="sunken")

#Entry List3
enLi3=Entry(frMain)
enLi3.place(x=150,y=100,width=250,height=30)
enLi3.config(bg="brown",fg="white",font=("Calibri",13),bd=3,relief="sunken")

#Entry List4
enLi4=Entry(frMain)
enLi4.place(x=150,y=140,width=250,height=30)
enLi4.config(bg="brown",fg="white",font=("Calibri",13),bd=3,relief="sunken")

#Entry List5
enLi5=Entry(frMain)
enLi5.place(x=150,y=180,width=250,height=30)
enLi5.config(bg="brown",fg="white",font=("Calibri",13),bd=3,relief="sunken")

#Buttons

#Clear Button
clrBtn=Button(frMain)
clrBtn.place(x=510,y=20)
clrBtn.config(image=trashBin,bg="Brown")

#Search Button
srchBtn=Button(frMain)
srchBtn.place(x=430,y=20)
srchBtn.config(image=search,bg="Brown")

#Back Button
srchBtn=Button(frMain,text="Back")
srchBtn.place(x=590,y=20)
srchBtn.config(fg="Violet",bg="Brown",font=("Calibri",20,"bold"),bd=0)

#Save Button
svBtn=Button(frMain,text="Save")
svBtn.place(x=430,y=90,width=250,height=35)
svBtn.config(fg="White",bg="Green",font=("Calibri",20,"bold"))

#Delete Button
delBtn=Button(frMain,text="Delete")
delBtn.place(x=430,y=140,width=250,height=35)
delBtn.config(fg="White",bg="Red",font=("Calibri",20,"bold"))

#Update Button
updBtn=Button(frMain,text="Update")
updBtn.place(x=430,y=190,width=250,height=35)
updBtn.config(fg="White",bg="Orange",font=("Calibri",20,"bold"))

#Table

t=Table(frTable)

tableBar=Scrollbar(frTable,orient="vertical")
tableBar.set(0.2, 0.5)
tableBar.place(x=677,y=0,height=240)


root.mainloop()