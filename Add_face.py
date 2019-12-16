import cv2
import matplotlib.pyplot as plt
import os
import time
import mysql.connector as connector


class AddFace:

    def __init__(self):
        mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
        cursor = mydb.cursor()

        q = "SELECT COUNT(ID) FROM USERS"

        cursor.execute(q)
        result = cursor.fetchall()

        kaka = cv2.CascadeClassifier('../DATA/face.xml')

        record = cv2.VideoCapture(0)
        count = 0


            

        name = int(result[0][0]) + 1
        name = str(name)
        os.mkdir('../faces/'+name)
        goodNAMES = False
        print("Folder Created as ID : ", name, "<---- In Path -----> " , os.getcwd() )
        time.sleep(3)
          
            
            
            


        while True:
            
            _ , frame = record.read()
            
            
            
            gry_frame = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY )
            
            
            detection = kaka.detectMultiScale ( gry_frame, 1.2, 5 )
            
            
            if len(detection) != 1:
                pass
            else:
                x,y,w,h = detection[0]
                count += 1
                cv2.imwrite('../faces/'+name +"/"+str(count)+".jpg", frame[y:y+h, x:x+w])
                cv2.rectangle(frame,(x,y), ((x+w), (y+h)), (255,0,0),3)
                
                   
                
                
            cv2.putText(frame, "Samples Taken : {}/75 ".format(count),(10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,200), 2)
                
            
            cv2.imshow("KAKA",frame)
            if count > 75:
                break
            
            if cv2.waitKey(30) & 0xFF == 27:
                break
            
            
        cv2.destroyAllWindows()
        record.release()


        q= "insert into users (name) values ('AAYUSH')"
        cursor.execute(q)
        mydb.commit()