
from tkinter import * 
import tkinter as tk
from tkinter import ttk
import mysql.connector as connector

class EnterData():

    mydb = connector.connect(host = "localhost", user = "root", passwd="aayush123", database = "testdb")

    cursor = mydb.cursor()

    IDdb=0
    NAMEdb=""
    AGEdb=0
    GENDERdb =""
    POSTdb=""
    CONTACT=0
    ADDRESSdb=""

    


    def __init__(self):

        def Provide():
            self.IDdb = ID_ENTRY.get()
            self.NAMEdb = NAME_ENTRY.get()
            self.AGEdb = Spinbox1.get()
            self.GENDERdb = g
            print(self.NAMEdb,self.AGEdb,self.IDdb,self.GENDERdb)

        window = tk.Tk()

        window.geometry("600x850")
        window.resizable(0, 0)
        window.title("New windowlevel")
        window.configure(background="#d9d9d9")

        # ID Area ------------------------------------------------
        ID = tk.Label(window,background="#d9d9d9",
                            font="-family {Product Sans} -size 14",
                            foreground="#000000",
                            text='''ID''')
        ID.place(relx=0.033, rely=0.059, height=91, width=144)

        ID_ENTRY = tk.Entry(window,background="white",
                            font="TkFixedFont",
                            foreground="#000000")
        ID_ENTRY.place(relx=0.317, rely=0.094,height=30, relwidth=0.19)

        
        ############################################################

        # Name Area ------------------------------------------------

        Label1_6 = tk.Label(window,background="#d9d9d9",
                                font="-family {Product Sans} -size 14",
                                foreground="#000000",
                                text='''Name''')

        Label1_6.place(relx=0.033, rely=0.164, height=91, width=144)


        NAME_ENTRY = tk.Entry(window,background="white",
                                    font="TkFixedFont",
                                    foreground="#000000")

        NAME_ENTRY.place(relx=0.315, rely=0.197,height=30, relwidth=0.523)

        
        ############################################################

        # Age Area ------------------------------------------------
        Label1_7 = tk.Label(window,background="#d9d9d9",
                                    font="-family {Product Sans} -size 14",
                                    highlightbackground="#d9d9d9",
                                    text='''Age''')
        Label1_7.place(relx=0.033, rely=0.27, height=91, width=144)


        Spinbox1 = tk.Spinbox(window, from_=18.0, to=50.0,background="white",
                                                        buttonbackground="#d9d9d9")
        Spinbox1.place(relx=0.317, rely=0.305, relheight=0.022
                , relwidth=0.142)

        
        ############################################################


        # Gender Area ------------------------------------------------

        g = StringVar()

        Label1_8 = tk.Label(window)
        Label1_8.place(relx=0.033, rely=0.363, height=91, width=144)
        Label1_8.configure(background="#d9d9d9")
        Label1_8.configure(font="-family {Product Sans} -size 14")
        Label1_8.configure(text='''Gender''')

        Radiobutton1 = tk.Radiobutton(window)
        Radiobutton1.place(relx=0.317, rely=0.399, relheight=0.029
                , relwidth=0.097)

        Radiobutton1.configure(background="#d9d9d9")
        Radiobutton1.configure(foreground="#000000")
        Radiobutton1.configure(justify='left')
        Radiobutton1.configure(text='''Male''')
        Radiobutton1.configure(value="Male")
        Radiobutton1.configure(variable = g)


        Radiobutton1_4 = tk.Radiobutton(window)
        Radiobutton1_4.place(relx=0.5, rely=0.397, relheight=0.029
                , relwidth=0.097)

        Radiobutton1_4.configure(background="#d9d9d9")
        Radiobutton1_4.configure(foreground="#000000")
        Radiobutton1_4.configure(justify='left')
        Radiobutton1_4.configure(text='''Female''')
        Radiobutton1_4.configure(value="Female")
        Radiobutton1_4.configure(variable = g)

        
        ############################################################


        # Post Area ------------------------------------------------
        Label1_9 = tk.Label(window)
        Label1_9.place(relx=0.033, rely=0.457, height=91, width=144)
        Label1_9.configure(background="#d9d9d9")
        Label1_9.configure(font="-family {Product Sans} -size 14")
        Label1_9.configure(text='''Employee Post''')
        Label1_9.configure(wraplength="100")

        TCombobox1 = ttk.Combobox(window)
        TCombobox1.place(relx=0.317, rely=0.498, relheight=0.048
                , relwidth=0.272)


        ############################################################

        # Contact Area ------------------------------------------------

        Label1_10 = tk.Label(window)
        Label1_10.place(relx=0.033, rely=0.583, height=91, width=144)
        Label1_10.configure(background="#d9d9d9")
        Label1_10.configure(font="-family {Product Sans} -size 14")
        Label1_10.configure(text='''Contact''')


        Entry1_3 = tk.Entry(window)
        Entry1_3.place(relx=0.317, rely=0.615,height=30, relwidth=0.523)
        Entry1_3.configure(background="white")
        ############################################################

        # Address Area ------------------------------------------------

        Label1_11 = tk.Label(window)
        Label1_11.place(relx=0.033, rely=0.692, height=91, width=144)
        Label1_11.configure(background="#d9d9d9")
        Label1_11.configure(font="-family {Product Sans} -size 14")
        Label1_11.configure(text='''Address''')

        Text1 = tk.Text(window)
        Text1.place(relx=0.317, rely=0.715, relheight=0.157, relwidth=0.557)
        Text1.configure(background="white")
        Text1.configure(undo="1")
        ############################################################






        Button1 = tk.Button(window, command=Provide)
        Button1.place(relx=0.733, rely=0.938, height=34, width=87)
        Button1.configure(background="#d9d9d9")
        Button1.configure(pady="0")
        Button1.configure(text='''Button''')





        
        window.mainloop()


        

