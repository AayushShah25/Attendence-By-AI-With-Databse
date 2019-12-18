import tkinter as tk
import sys
import Names
import mysql.connector as connector


mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
cursor = mydb.cursor()

q = "SELECT COUNT(ID) FROM USERS"
cursor.execute(q)
result = cursor.fetchall()
incrementedID = int(result[0][0]) + 1


window = tk.Tk()


window.geometry("700x700")
window.maxsize(1920, 1080)
window.resizable(0, 0)
window.title("Main Page")
window.configure(background="#d9d9d9")

#DEFs

def ADD():
    window.destroy()
    Names.EnterData(incrementedID)




# BUTTONS

#--------------------------------------------------------------------------------------------

Btn1 = tk.Button(window,text='Add A Person',
                                font="-family {Product Sans} -size 14 -weight bold",
                                command= ADD)
Btn1.place(relx=0.057, rely=0.043, height=200, width=200)

#--------------------------------------------------------------------------------------------

Btn2 = tk.Button(window,text='Remove A Person',
                                font="-family {Product Sans} -size 14 -weight bold")
Btn2.place(relx=0.614, rely=0.043, height=200, width=200)


#--------------------------------------------------------------------------------------------



Btn3 = tk.Button(window,text='Show Unknowns',
                                font="-family {Product Sans} -size 14 -weight bold")
Btn3.place(relx=0.057, rely=0.386, height=200, width=200)

  #--------------------------------------------------------------------------------------------

Btn4 = tk.Button(window,text='Generate Report',
                                font="-family {Product Sans} -size 14 -weight bold")
Btn4.place(relx=0.614, rely=0.386, height=200, width=200)
 
 #--------------------------------------------------------------------------------------------

Btn5 = tk.Button(window,text='Hold a Person for Leave',
                        font="-family {Product Sans} -size 14 -weight bold",wraplength="200",
                        )

Btn5.place(relx=0.337, rely=0.701, height=200, width=200)




window.mainloop()
