import serial
from firebase import firebase
from time import sleep
from datetime import datetime
import serial.tools.list_ports


ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))


ser = serial.Serial("COM2", 9600)
print(ser.readline())

a=[]
str1=str(ser.readline())
print(str1)
a=str1.split(",")

TEMP=a[0]
TEMP=TEMP[8:][:-2]
print(TEMP)

Fire=a[1]
Fire=Fire[0:]
print(Fire)

Smoke=a[2]
Smoke=Smoke[0:]
print(Smoke)

res =1
i=0
time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)

while res:
     cc=str(1234)
     #print(cc)
     val=cc
     firebase1 = firebase.FirebaseApplication('https://forest-fire-b3b80-default-rtdb.firebaseio.com/', None)##paste your firebase url
     
     for i in range(0,4):
             #string1="123"
             string1=str(ser.readline())
             string1=string1[9:][:-6]
             data =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':TEMP,
               'time': datetime.now().strftime("%H:%M")              
          }
             result = firebase1.patch('https://forest-fire-b3b80-default-rtdb.firebaseio.com/'+ '/TEMP_data/'+ str(i), data)##paste your firebase url
             print(result)
             
     for i in range(0,4):
             #string1="123"
             string2=str(ser.readline())
             string2=string2[9:][:-6]
             data1 =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':Fire,
               'time': datetime.now().strftime("%H:%M")              
          }
             result1 = firebase1.patch('https://forest-fire-b3b80-default-rtdb.firebaseio.com/'+ '/Fire_data/'+ str(i), data1)##paste your firebase url
             print(result1)

     for i in range(0,4):
             #string1="123"
             string3=str(ser.readline())
             string3=string3[9:][:-6]
             data2 =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':Smoke,
               'time': datetime.now().strftime("%H:%M")              
          }
             result2 = firebase1.patch('https://forest-fire-b3b80-default-rtdb.firebaseio.com/'+ '/Smoke_data/'+ str(i), data2)##paste your firebase url
             print(result2)
     
     res=0
