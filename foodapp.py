#code continued



from tkinter import *



root= Tk()
root.title("Food Price")
root.geometry("300x300")
root.configure(bg="gray")

v=IntVar()
amount=IntVar()
result=IntVar()


def print_result():
    val = int(v.get())
    if val==0:
        result.set(int(entryAmount.get())* 4)   # Assuming Rs. 4 for an apple        
    elif val==1:
        result.set(int(entryAmount.get())* 5)   # Assuming Rs. 5 for an Mango        
    elif val==2:
        result.set(int(entryAmount.get())* 8)   # Assuming Rs. 8 for an Fanas        Fanas is Maharashtrian word for Jackfruit
        
label=Label(root, text="Choose item",width=20,bg="gray")
label.place(x=90,y=10)

btn1=Radiobutton(root, text="Apple",highlightbackground="gray",bg="gray",variable=v,value=0)
btn1.place(x=30,y=60)

btn2=Radiobutton(root, text="Mango",bg="gray",highlightbackground="gray",variable=v,value=1)
btn2.place(x=30,y=90)

btn3=Radiobutton(root, text="Fanas",bg="gray",highlightbackground="gray",variable=v,value=2)
btn3.place(x=30,y=120)

labelResult=Label(root, text="Result:",width=5,bg="gray",highlightbackground="gray")
labelResult.place(x=30,y=150)

entryAmount=Entry(root,width=20)
entryAmount.place(x=100,y=190)


entryResult=Entry(root,width=20,textvariable=result)
entryResult.place(x=100,y=150)

btnCal=Button(root,text="Calc",width=5,highlightbackground="gray",bg="gray",height=0, command= lambda: print_result())
btnCal.place(x=26,y=187)




root.mainloop()
