a = int(input("Enter a number to print 0-9: ")) 
x = ["0 0 0 0 0 0 0", "5           1", "5           1","6 6 6 6 6 6 6","4           2", "4           2", "3 3 3 3 3 3 3"]

if a == 0:
 
    print(x[0].replace("0","*"))
    print(x[1].replace("1","*").replace("5","*"))
    print(x[2].replace("1","*").replace("5","*"))
    print(x[3].replace("6"," "))
    print(x[4].replace("2","*").replace("4","*"))
    print(x[5].replace("2","*").replace("4","*"))
    print(x[6].replace("3","*"))


elif a==1:
    print(x[0].replace("0"," "))
    print(x[1].replace("1","*").replace("5"," "))
    print(x[2].replace("1","*").replace("5"," "))
    print(x[3].replace("6"," "))
    print(x[4].replace("2","*").replace("4"," "))
    print(x[5].replace("2","*").replace("4"," "))
    print(x[6].replace("3"," "))  

elif a==2:
    print(x[0].replace("0","*"))
    print(x[1].replace("1","*").replace("5"," "))
    print(x[2].replace("1","*").replace("5"," "))
    print(x[3].replace("6","*"))
    print(x[4].replace("2"," ").replace("4","*"))
    print(x[5].replace("2"," ").replace("4","*"))
    print(x[6].replace("3","*"))            

elif a==3:
    print(x[0].replace("0","*"))
    print(x[1].replace("1","*").replace("5"," "))
    print(x[2].replace("1","*").replace("5"," "))
    print(x[3].replace("6","*"))
    print(x[4].replace("2","*").replace("4"," "))
    print(x[5].replace("2","*").replace("4"," "))
    print(x[6].replace("3","*"))    
            
elif a==4:
    print(x[0].replace("0"," "))
    print(x[1].replace("1","*").replace("5","*"))
    print(x[2].replace("1","*").replace("5","*"))
    print(x[3].replace("6","*"))
    print(x[4].replace("2","*").replace("4"," "))
    print(x[5].replace("2","*").replace("4"," "))
    print(x[6].replace("3"," "))                               

elif a==5:
    print(x[0].replace("0","*"))
    print(x[1].replace("1"," ").replace("5","*"))
    print(x[2].replace("1"," ").replace("5","*"))
    print(x[3].replace("6","*"))
    print(x[4].replace("2","*").replace("4"," "))
    print(x[5].replace("2","*").replace("4"," "))
    print(x[6].replace("3","*"))  

elif a==6:
    print(x[0].replace("0","*"))
    print(x[1].replace("1"," ").replace("5","*"))
    print(x[2].replace("1"," ").replace("5","*"))
    print(x[3].replace("6","*"))
    print(x[4].replace("2","*").replace("4","*"))
    print(x[5].replace("2","*").replace("4","*"))
    print(x[6].replace("3","*"))          

elif a==7:
    print(x[0].replace("0","*"))
    print(x[1].replace("1","*").replace("5"," "))
    print(x[2].replace("1","*").replace("5"," "))
    print(x[3].replace("6"," "))
    print(x[4].replace("2","*").replace("4"," "))
    print(x[5].replace("2","*").replace("4"," "))
    print(x[6].replace("3"," ")) 

elif a==8:
    print(x[0].replace("0","*"))
    print(x[1].replace("1","*").replace("5","*"))
    print(x[2].replace("1","*").replace("5","*"))
    print(x[3].replace("6","*"))
    print(x[4].replace("2","*").replace("4","*"))
    print(x[5].replace("2","*").replace("4","*"))
    print(x[6].replace("3","*"))           

elif a==9:
    print(x[0].replace("0","*"))
    print(x[1].replace("1","*").replace("5","*"))
    print(x[2].replace("1","*").replace("5","*"))
    print(x[3].replace("6","*"))
    print(x[4].replace("2","*").replace("4"," "))
    print(x[5].replace("2","*").replace("4"," "))
    print(x[6].replace("3","*"))    

else:
    print("Enter a valid no: btwn 0 - 9 to print")
