import tkinter as tk
import mysql.connector as connector
import TrainFaces
from tkinter import messagebox
import shutil # <--- Removes the NON EMPTY directories...


mydb = connector.connect(host="localhost", user ="root", passwd="aayush123" , database="testdb")
cursor = mydb.cursor()

class ListKAKA:
    def __init__(self,Data):
        def rmv(id):
            q = "update users set isin = false where id="+str(id)
            cursor.execute(q)
            mydb.commit()

            shutil.rmtree(r'C:\Users\GIGABYTE\Desktop\Project\Faces\\'+str(D[0]))
            top.destroy()
            y = messagebox.showinfo("Alert","The Person "+D[1]+" of ID : "+str(D[0])+" has been removed from the Database and the training is started,\n which will take some time...")

            TrainFaces.TrainData()
            import MainPage



       
        top = tk.Tk()

        top.geometry("600x963")
        
        top.resizable(0,0 )
        top.title("Removal List")
        top.configure(background="#d9d9d9")


        NUMBERLab = []
        IMAGE = []
        IDLab = []
        NAMELab = []
        DEPARTMENLab = []
        REMOVEBut = []
        IDData = []
        NAMEData = []
        DEPARMENTData = []

        for i,D in enumerate(Data):



            self.NUMLab = tk.Label(top)
            
            self.NUMLab.configure(background="#d9d9d9")
            self.NUMLab.configure(disabledforeground="#a3a3a3")
            self.NUMLab.configure(font="-family {Product Sans} -size 24 -weight normal ")
            self.NUMLab.configure(foreground="#000000")
            self.NUMLab.configure(text=str(i+1)+".")

            NUMBERLab.append(self.NUMLab)

            
            
            photo = tk.PhotoImage(file=r"C:\Users\GIGABYTE\Desktop\Project\Faces\\"+str(D[0])+"\\5.png")
            
            

            self.IMG = tk.Label(top,image=photo)
            self.IMG.image = photo
            self.IMG.place(relx=0.35, rely=0.083, height=141, width=164)
            self.IMG.configure(background="#d9d9d9")
            self.IMG.configure(disabledforeground="#a3a3a3")
            self.IMG.configure(foreground="#000000")
            self.IMG.configure(text='''Label''')

            IMAGE.append(self.IMG)


            self.IdLab = tk.Label(top)
            self.IdLab.place(relx=0.21, rely=0.229, height=41, width=54)
            self.IdLab.configure(background="#d9d9d9")
            self.IdLab.configure(disabledforeground="#a3a3a3")
            self.IdLab.configure(font="-family {Product Sans} -size 12 -weight normal")
            self.IdLab.configure(foreground="#000000")
            self.IdLab.configure(text='''ID''')

            IDLab.append(self.IdLab)


            self.NAMLab = tk.Label(top)
            self.NAMLab.place(relx=0.19, rely=0.28, height=41, width=54)
            self.NAMLab.configure(activebackground="#f9f9f9")
            self.NAMLab.configure(activeforeground="black")
            self.NAMLab.configure(background="#d9d9d9")
            self.NAMLab.configure(disabledforeground="#a3a3a3")
            self.NAMLab.configure(font="-family {Product Sans} -size 12 -weight normal")
            self.NAMLab.configure(foreground="#000000")
            self.NAMLab.configure(highlightbackground="#d9d9d9")
            self.NAMLab.configure(highlightcolor="black")
            self.NAMLab.configure(text='''Name''')

            NAMELab.append(self.NAMLab)


            self.DEPLab = tk.Label(top)
            self.DEPLab.place(relx=0.12, rely=0.328, height=41, width=94)
            self.DEPLab.configure(activebackground="#f9f9f9")
            self.DEPLab.configure(activeforeground="black")
            self.DEPLab.configure(background="#d9d9d9")
            self.DEPLab.configure(disabledforeground="#a3a3a3")
            self.DEPLab.configure(font="-family {Product Sans} -size 12 -weight normal")
            self.DEPLab.configure(foreground="#000000")
            self.DEPLab.configure(highlightbackground="#d9d9d9")
            self.DEPLab.configure(highlightcolor="black")
            self.DEPLab.configure(text='''Department''')

            DEPARTMENLab.append(self.DEPLab)

            self.RMVBut = tk.Button(top,command=lambda : rmv(D[0]))
            self.RMVBut.place(relx=0.725, rely=0.253, height=54, width=97)
            self.RMVBut.configure(activebackground="#ececec")
            self.RMVBut.configure(activeforeground="#000000")
            self.RMVBut.configure(background="#800040")
            self.RMVBut.configure(disabledforeground="#a3a3a3")
            self.RMVBut.configure(font="-family {Product Sans} -size 14 -weight bold")
            self.RMVBut.configure(foreground="#ffffff")
            self.RMVBut.configure(highlightbackground="#d9d9d9")
            self.RMVBut.configure(highlightcolor="black")
            self.RMVBut.configure(pady="0")
            self.RMVBut.configure(text='''Remove''')

            REMOVEBut.append(self.RMVBut)

            self.IdData = tk.Label(top)
            self.IdData.place(relx=0.317, rely=0.242, height=21, width=224)
            self.IdData.configure(background="#d9d9d9")
            self.IdData.configure(disabledforeground="#a3a3a3")
            self.IdData.configure(font="-family {Product Sans} -size 12 -weight bold")
            self.IdData.configure(foreground="#000000")
            self.IdData.configure(text=D[0])

            IDData.append(self.IdData)

            self.NMEData = tk.Label(top)
            self.NMEData.place(relx=0.317, rely=0.292, height=21, width=224)
            self.NMEData.configure(activebackground="#f9f9f9")
            self.NMEData.configure(activeforeground="black")
            self.NMEData.configure(background="#d9d9d9")
            self.NMEData.configure(disabledforeground="#a3a3a3")
            self.NMEData.configure(font="-family {Product Sans} -size 12 -weight bold")
            self.NMEData.configure(foreground="#000000")
            self.NMEData.configure(highlightbackground="#d9d9d9")
            self.NMEData.configure(highlightcolor="black")
            self.NMEData.configure(text=D[1])

            NAMEData.append(self.NMEData)

            self.DEPData = tk.Label(top)
            self.DEPData.place(relx=0.317, rely=0.339, height=21, width=224)
            self.DEPData.configure(activebackground="#f9f9f9")
            self.DEPData.configure(activeforeground="black")
            self.DEPData.configure(background="#d9d9d9")
            self.DEPData.configure(disabledforeground="#a3a3a3")
            self.DEPData.configure(font="-family {Product Sans} -size 12 -weight bold")
            self.DEPData.configure(foreground="#000000")
            self.DEPData.configure(highlightbackground="#d9d9d9")
            self.DEPData.configure(highlightcolor="black")
            self.DEPData.configure(text=D[4])

            DEPARMENTData.append(self.DEPData)

            self.TitleLab = tk.Label(top)
            self.TitleLab.place(relx=0.133, rely=0.01, height=71, width=344)
            self.TitleLab.configure(background="#d9d9d9")
            self.TitleLab.configure(disabledforeground="#a3a3a3")
            self.TitleLab.configure(font= "-family {Product Sans} -size 17 -weight normal ")
            self.TitleLab.configure(foreground="#000000")
            self.TitleLab.configure(text='''Select The''')

            self.TitleLab2 = tk.Label(top)
            self.TitleLab2.place(relx=0.517, rely=0.021, height=51, width=54)
            self.TitleLab2.configure(background="#d9d9d9")
            self.TitleLab2.configure(disabledforeground="#a3a3a3")
            self.TitleLab2.configure(font= "-family {Product Sans} -size 17 -weight normal ")
            self.TitleLab2.configure(foreground="#800040")
            self.TitleLab2.configure(text='''One''')

        
        rely=-0.400
    


        #print(zip (NUMBERLab,IMAGE,IDLab,NAMELab,DEPARTMENLab,REMOVEBut,IDData,NAMEData,DEPARMENTData))
        
        for (numl, im, idl, nml, depl, rmb, idd, nmd, depd) in zip (NUMBERLab,IMAGE,IDLab,NAMELab,DEPARTMENLab,REMOVEBut,IDData,NAMEData,DEPARMENTData):
            rely += 0.400
            numl.place(relx=0.083, rely=0.114+rely, height=71, width=74)
            im.place(relx=0.35, rely=0.083+rely, height=141, width=164)
            idl.place(relx=0.21, rely=0.229+rely, height=41, width=54)
            nml.place(relx=0.19, rely=0.28+rely, height=41, width=54)
            depl.place(relx=0.12, rely=0.328+rely, height=41, width=94)
            rmb.place(relx=0.725, rely=0.253+rely, height=54, width=97)
            idd.place(relx=0.317, rely=0.242+rely, height=21, width=224)
            nmd.place(relx=0.317, rely=0.292+rely, height=21, width=224)
            depd.place(relx=0.317, rely=0.339+rely, height=21, width=224)


        top.mainloop()







