import time
t= time.strftime("%H:%M:%S")
print(t) 
hour= int(time.strftime("%H"))

if (hour<12):
    print("Good Morning, Sir")
else:
    if (hour>=12) and (hour<16):
        print("Good Afternoon, Sir")
        
    if (hour>=16) and (hour<20):
        print("Good Evening, Sir")
    if (hour>=20):
        print("Good Night, Sir")



      
