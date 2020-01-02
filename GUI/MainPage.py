import tkinter as tk
from tkinter import messagebox
import os
import sys
import Names
import mysql.connector as connector
import webbrowser
import Hold
import Remove
import ReList
import TrainFaces
import FindImprove

class MAINCALL():

    def __init__(self):

        mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
        cursor = mydb.cursor()

        q = "SELECT COUNT(ID) FROM USERS"
        cursor.execute(q)
        result = cursor.fetchall()
        incrementedID = int(result[0][0]) + 1


        window = tk.Toplevel()


        window.geometry("700x700")
        window.maxsize(1920, 1080)
        window.resizable(0, 0)
        window.title("Main Page")
        window.configure(background="#d9d9d9")

        #DEFs
        
        def Improve():
            window.destroy()
            FindImprove.FindForImprove()
            
        def ADD():
            window.destroy()
            Names.EnterData(incrementedID)

        def Removefn():
            Remove.RemoveField()

        def showUnkowns():

            try:

                if (webbrowser.open(r'C:\Users\GIGABYTE\Desktop\Project\Unknowns\\')):
                    pass
                else:
                    print (' No File Found Error ')
                    
            except Exception:

                print('Error in opening the Folder ')

        def hold():
            window.destroy()
            Hold.Hold()

        def release():
            window.destroy()
            ReList.ListKAKA()
            
        def Train():

            
            
            num_of_persons = os.listdir('../Faces')
            

            if len(num_of_persons) <= 1:
                y = messagebox.showinfo("Can't ! ","Only one person is there... Please Add more to get ahead and train the model. \n To add, please click on ADD MORE")
                
            else:
                window.destroy()
                TrainFaces.TrainData()
                print("Model Has Been Trained !!")



        # BUTTONS

        #--------------------------------------------------------------------------------------------

        Btn1 = tk.Button(window,text='Add A Person',
                                        font="-family {Product Sans} -size 14 -weight bold",
                                        command= ADD)
        Btn1.place(relx=0.057, rely=0.043, height=200, width=200)

        #--------------------------------------------------------------------------------------------

        Btn2 = tk.Button(window,text='Remove A Person',
                                        font="-family {Product Sans} -size 14 -weight bold", command=Removefn)
        Btn2.place(relx=0.614, rely=0.043, height=200, width=200)


        #--------------------------------------------------------------------------------------------



        Btn3 = tk.Button(window,text='Show Unknowns',
                                        font="-family {Product Sans} -size 14 -weight bold",
                                        command = showUnkowns)
        Btn3.place(relx=0.057, rely=0.386, height=200, width=200)

          #--------------------------------------------------------------------------------------------

        train = tk.Button(window, text = "Train System", font="-family {Product Sans} -size 14 -weight bold", command=Train, bg = "#800040", fg="#FFFFFF")
        train.place(relx=0.375, rely=0.350, height=100, width=150)


        Improve = tk.Button(window, text = "Improve for Training", font="-family {Product Sans} -size 14 -weight bold", bg = "#800040", fg="#FFFFFF", wraplength="100", command = Improve)
        Improve.place(relx=0.375, rely=0.600, height=100, width=150)
        




        #-------------------

        Btn4 = tk.Button(window,text='Generate Report',
                                        font="-family {Product Sans} -size 14 -weight bold")
        Btn4.place(relx=0.614, rely=0.386, height=200, width=200)
         
         #--------------------------------------------------------------------------------------------

        Btn5 = tk.Button(window,text='Hold a Person for Leave',
                                font="-family {Product Sans} -size 14 -weight bold",wraplength="200",
                                command = hold)

        Btn5.place(relx=0.057, rely=0.701, height=200, width=200)

        #-----------------------------

        Btn6 = tk.Button(window,text='Release a Person from Leave',
                                font="-family {Product Sans} -size 14 -weight bold",wraplength="200",
                                command=release)

        Btn6.place(relx=0.614, rely=0.701, height=200, width=200)





        window.mainloop()
