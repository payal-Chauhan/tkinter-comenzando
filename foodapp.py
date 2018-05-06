#code continued



from tkinter import *



root= Tk()
root.title("Food Price")
root.geometry("300x300")
root.configure(bg="gray")

v=StringVar()
x=StringVar()
label=Label(root, text="Choose item",width=20,bg="gray")
label.place(x=90,y=10)

btn1=Radiobutton(root, text="Apple",highlightbackground="gray",bg="gray",variable=v,value="Apple")
btn1.place(x=30,y=60)

btn2=Radiobutton(root, text="Mango",bg="gray",highlightbackground="gray",variable=v,value="Mango")
btn2.place(x=30,y=90)

btn3=Radiobutton(root, text="Fanas",bg="gray",highlightbackground="gray",variable=v,value="Fanas")
btn3.place(x=30,y=120)

labelResult=Label(root, text="Result:",width=5,bg="gray",highlightbackground="gray")
labelResult.place(x=30,y=150)

entryResult=Entry(root,width=20)
entryResult.place(x=100,y=150)

btnCal=Button(root,text="Calc",width=5,highlightbackground="gray",bg="gray",height=0)
btnCal.place(x=26,y=187)

str=StringVar()
str.set("heylo")
entryAmount=Entry(root,width=20)
print(dir(entryAmount))
entryAmount.place(x=100,y=190)
print(entryAmount.get())


root.mainloop()