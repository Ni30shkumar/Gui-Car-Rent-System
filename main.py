from tkinter import *
from tkinter import messagebox
class car_rent_system:
    def __init__(self):
        self.Total_cars = 100

    def bill_printing(self):
        pass

    def car_on_rent(self):
        var = messagebox.askyesno("Notification", "Cars in Agency :" + str(self.Total_cars) + " \n To confirm Yes/No....",)
        if var == True:
            car1 = Tk()
            car1.title("Costumer Portal")
            car1.config(bg="red")
            car1.geometry("500x300")
            label2 = Label(car1, text="Your Name", font=("times", 15, "bold"),anchor="w",bg="red")
            label2.place(x=15, y=60, height=30, width=150)
            Frame(car1,bg="black").place(x=15,y=89,height=2,width=100)
            label3 = Label(car1, text="Your Aadhar ", font=("times", 14, "bold"),anchor="w")
            label3.place(x=15,y=100,height=30,width=150)
            Frame(car1, bg="black").place(x=15, y=120, height=2, width=100)
            label4 = Label(car1, text="Required Car ", font=("times", 14, "bold"),anchor="w")
            label4.place(x=15,y=145,height=30,width=150)
            Frame(car1, bg="black").place(x=15, y=169, height=2, width=100)
            label5 = Label(car1, text="How Many Days ", font=("times", 14, "bold"),anchor="w")
            label5.place(x=15,y=188,height=30,width=150)
            Frame(car1, bg="black").place(x=15, y=190, height=2, width=100)

            name = StringVar()
            aadhar = StringVar()
            cars = StringVar()
            days = StringVar()
            entry1 =  Entry(car1,textvariable=name,font=("chillers",15, "bold"))
            entry1.place(x=200,y=60,height=30,width=250)
            entry2 =  Entry(car1,textvariable=aadhar,font=("chillers",15, "bold"))
            entry2.place(x=200,y=100,height=30,width=250)
            entry3 =  Entry(car1,textvariable=cars,font=("chillers",15, "bold"))
            entry3.place(x=200,y=145,height=30,width=250)
            entry4 =  Entry(car1,textvariable=days,font=("chillers",15, "bold"))
            entry4.place(x=200,y=188,height=30,width=250)

            button = Button(car1,text="Sumit",font=("times",20,"bold"),bg="blue",fg="white",activebackground="white",activeforeground="black")
            button.place(x=180,y=240,height=40,width=140)
            car1.mainloop()
    def car_deposit(self):
       pass
    def potal_exite(self):
        pass

car = Tk()
car.title("Car Agency")
car.geometry("500x500+400+120")

label1 = Label(car,text="Car Rent Agency ",font=("times",25,"bold"))
label1.place(x=10,y=17,height=40,width=480)

car_rent = car_rent_system()  #  create an intence of  the  car_ent_system class

button1 = Button(car, text="RENT",font=("times",20,"bold"),bg="blue",fg="white",activebackground="white",activeforeground="black",
                command = car_rent.car_on_rent)
button1.place(x=160,y=100,height=80,width=180)
button2 = Button(car, text="Deposit",font=("times",20,"bold"),bg="blue",fg="white",activebackground="white",activeforeground="black",
                 command=car_rent.car_deposit )
button2.place(x=160,y=210,height=80,width=180)
button3 = Button(car, text="Exit",font=("times",20,"bold"),bg="blue",fg="white",activebackground="white",activeforeground="black",
                 command=car_rent.potal_exite)
button3.place(x=160,y=330,height=80,width=180)

car.mainloop()


