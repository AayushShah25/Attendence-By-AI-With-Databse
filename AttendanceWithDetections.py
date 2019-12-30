import cv2
import numpy as np
import os
from datetime import date
from datetime import datetime
from DetectMotion import Movement

#import matplotlib.pyplot as plt
from keras.models import load_model
from FaceEmmbedings2 import FaceNet
import mysql.connector as connector

#### DATE CHAEKING

mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
cursor = mydb.cursor()

q  = "select datekaka from checkdate limit 1"

cursor.execute(q)
datecheck = cursor.fetchone()

datecheck = datecheck[0]

var = datetime.now()
todaydate = var.strftime("%d%m%y")
print(datecheck)
print(todaydate)


if datecheck != todaydate:
    pass

else:

    #### TRUNCATE
    mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
    cursor = mydb.cursor()

    q = "TRUNCATE attendance";

    cursor.execute(q)
    mydb.commit()

    #### ENTER DATA

    mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
    cursor = mydb.cursor()

    q = "insert into attendance(id,name,hold) select id,name,hold from users where isin = 1"

    cursor.execute(q)
    mydb.commit()

    #### Update Date

    mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
    cursor = mydb.cursor()

    q = "update checkdate set datekaka = '"+todaydate+"'"
    print(q)
    cursor.execute(q)
    mydb.commit()









#### GET DETAILS

mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
cursor = mydb.cursor()

q = "SELECT name FROM attendance"
cursor.execute(q)
result = cursor.fetchall()

today = date.today()
today = today.strftime("%d-%m-%y")

try:
    os.mkdir('./Unknowns/'+today)
except FileExistsError:
    pass


# =============================================================================
# A Function to check the SAME ELEMENTS in the list
# =============================================================================
def AllSame(l):
    
    if len(l) == 0:
        return False
    
    return l.count(l[0]) == len(l)


# =============================================================================
# Function Ended
# =============================================================================
    
people = {}



for i,name in enumerate(result):

    people[i] = name[0]

print(people)

model=load_model('face_recognizer.MODEL')
cascade = cv2.CascadeClassifier('./data/Face.xml')

label=None
Vectorizer= FaceNet()



guessFaces = []


record = cv2.VideoCapture(0)



_, prev = record.read()
_, frame = record.read()
canvas = np.zeros((480,640,3))

while True: # Just for Check ( Continuous check )
    
    
    Code_Positive = False # A Variable to get entry Directly after matching 25 Faces
    if  not Movement(prev, frame):

        canvas = np.zeros((480,640,3))
        prev = frame



    else:
        
#        plt.subplot(121)
#        plt.imshow(prev)
#        plt.subplot(122)
#        plt.imshow(frame)
#        plt.show()
        Code_Positive = False
        cv2.destroyWindow('NO DETECTION')
        countSec = 100
        while countSec != 0: # Detection ( An Original while True loop )

                faces = []
                coordinates = []

                _, frameA = record.read()
                frameF = cv2.flip(frameA,1)

                gry_frame = cv2.cvtColor(frameF, cv2.COLOR_BGR2GRAY)

                detect = cascade.detectMultiScale(gry_frame, 1.2, 10)

                for x,y,w,h in detect:

                    faces.append( frameF[y:y+h, x:x+w] )
                    coordinates.append((x,y,w,h))
                    
                if len(detect) != 0:
                    
                    countSec = 100






                if(faces is not None):
                    for i in range(len(faces)):
                        face1 = faces[i]

                        coordinate =coordinates[i]

                        FaceIsolated = face1

                        face1 =cv2.resize(face1,(160,160))

                        face1=face1.astype('float')/255.0
                        face1=np.expand_dims(face1,axis=0)

                        feed=Vectorizer.calculate(face1)
                        feed=np.expand_dims(feed,axis=0)

                        prediction=model.predict(feed)[0]

                        result=int(np.argmax(prediction)) # 3

                        if(np.max(prediction)>0.9999):
                            for i in people:

                                if(result==i):

                                    label=people[i]
                                    guessFaces.append(people[i])
                                    
                                    if len(guessFaces) == 25:
                                        
                                        if AllSame(guessFaces):
                                            
                                            print("Went in 25 : ")
                                            if guessFaces[0] != 'Unknown':
                                                Code_Positive = True
                                            else:
                                                Code_Positive = False
                                            
                                            
                                        
                                        
                                        
                                    print("Guess Faces len : " , len(guessFaces))
                                    
                                    if len(guessFaces) >= 50 or Code_Positive :
                                        
                                        print("Inside 50 ")



                                        count = {}

                                        for I in guessFaces:

                                            count[I] = guessFaces.count(I)


                                        count = dict( (v,k) for k,v in count.items() )

                                        print(count)
                                        print(count[max(count)])
                                        
                                        if count[max(count)] == 'Unknown': 
                                            
                                            print('Max Unknown FOUND -- Resetting the Variables' )
                                            
                                            guessFaces = [] 
                                            continue
                                    
                                        if max(count) >= 45 or Code_Positive :
                                            ##Provide a Label and Do Stuff

                                            print ("Inside More than 45 : Getting Attend !!")

                                            resultRev = dict((v,k) for k,v in people.items())
# =============================================================================
#                                             
#                                             if 'Unknown' in count.values():
#                                                 
#                                                 
#                                                 
#                                                 temp = dict((v,k) for k,v in count.items())
#                                                 
#                                                 if temp['Unknown'] > 20:
#                                                     
#                                                     print (' More Unknown Faces Found in this Session ')
#                                                     guessFaces = []
#                                                     continue
#                                                 
#                                                 del temp
#                                                 
#                                                 
# =============================================================================

                                            a_person_ID = resultRev[count[max(count)]] # Aayush is the biggest, then return the Id of him from the People. 

                                            pos = int(a_person_ID)+1
                                            mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
                                            cursor = mydb.cursor()
                                            check = "select attend from attendance where ID ="+str(pos)

                                            cursor.execute(check)
                                            resultYN = cursor.fetchall()
                                            print("Result came : ", resultYN)

                                            if resultYN[0][0] == 1:

                                                label=people[i]+" You are Present !!! Go Home !"
                                                
                                                guessFaces = []
                                                Code_Positive = False

                                            elif (resultYN[0][0] == None or resultYN[0][0] == 0):
                                                mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
                                                cursor = mydb.cursor()
                                                checkforHold = "select hold from attendance where id="+str(pos)

                                                cursor.execute(checkforHold)
                                                resYes = cursor.fetchall()

                                                if resYes[0][0] == 0:
                                                    mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")

                                                    q = "update attendance set ATTEND = true where id ="+str(pos)

                                                    cursor = mydb.cursor()
                                                    cursor.execute(q)
                                                    mydb.commit()
                                                    guessFaces = []
                                                    Code_Positive = False

                                                else:

                                                    label = "Unknown"
                                                    now= datetime.now()
                                                    now= now.strftime("%H%M%S")
                                                    try:

                                                        cv2.imwrite("./Unknowns/"+today+"/"+str(now)+".png", FaceIsolated)

                                                    except Exception:
                                                        print('Error in Saving the Unknown face... Please Restart the System.')

                                                    guessFaces = []
                                                    Code_Positive = False




                                        else:

                                            guessFaces = []
                                            Code_Positive = False









                        else:
                            now= datetime.now()
                            now= now.strftime("%H%M%S")
                            try:

                                cv2.imwrite("./Unknowns/"+today+"/"+str(now)+".png", FaceIsolated)

                            except Exception:
                                print('Error in Saving the Unknown face... Please Restart the System.')
                                
                                

                            label='Unknown'
                            print('Found Unknown Face')
                            guessFaces.append(label)



                        cv2.putText(frameF,label+" : "+str(len(guessFaces)),(coordinate[0],coordinate[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,200),2)

                        cv2.rectangle(frameF,(coordinate[0],coordinate[1]),(coordinate[0] + coordinate[2] , coordinate[1] + coordinate[3]),(123,234,1),3)

                        
                cv2.imshow('Recognizition',frameF)
                
                countSec -= 1
                prev = frameA
                if cv2.waitKey(1) & 0xff == ord('q') :
                    break
                
                
            
        cv2.destroyWindow('Recognizition')










# =============================================================================
# The Ending Part
# =============================================================================

    cv2.imshow("NO DETECTION", canvas)

    
    _, frame = record.read()

    if cv2.waitKey(100) & 0xff == 27:
        break


cv2.destroyAllWindows()
record.release()


month = date.today()
month = month.strftime("%B-%Y")

f_list = os.listdir(r'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/')


if month not in f_list:
    
    os.mkdir(r'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/'+month)


mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
cursor = mydb.cursor()

q = "SELECT ID,name,attend FROM attendance INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/"+month+"/"+ str(today) +".csv' FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n';"

try:
    
    print('Normal')
    cursor.execute(q)
    print('Normal DONE !')
    
except Exception:
    print('Exeption')    
    os.chmod('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/'+str(month)+'/',0o777)
    try:
        
        print('Second')
        os.remove(r'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/'+str(month)+'/'+ str(today) +'.csv')
        cursor.execute(q)
        print('Second Done')
    except FileNotFoundError:
        
        cursor.execute(q)
