'''
#ques 1> Printing A

a = int(input("Enter no of rows: "))
s=a//2


for j in range(0,a):
    if j == 0 or j == s:
        for i in range(0,a):
            print("*",end="\t")
        print()
    else:
        for x in range(0,a):
            if x == 0 or x == a-1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()

'''
'''
#===========================================================
#ques 2> Printing B

a = int(input("Enter no of rows: "))
s = (a//2)

for x in range(0,a):
    if x == 0 or x == a-1:
        for j in range(0,a):
            if j == a-1:
                print(" ",end="\t")
            else:
                print("*",end="\t")
        print()
    elif x == s:
        for c in range(0,a):
            if c == a-1:
                print(" ",end="\t")
            else:
                print("*",end="\t")

        print()
    else:
        for i in range(0,a):
            if i == 0 or i == a-1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
'''
'''
#===========================================================
#ques 3> Printing C

a = int(input("Enter no of rows: "))

for j in range(0,a):
    if j == 0 or j == a-1:
        for i in range(0,a):
            print("*",end="\t")
        print()
    else:
        for x in range(0,a):
            if x == 0:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
'''
'''
#===========================================================
#ques 4> Printing D

a = int(input("Enter no of rows: "))

for j in range(0,a):
    if j == 0 or j == a-1:
        for i in range(0,a-1):
            print("*",end="\t")
        print()
    else:
        for x in range(0,a):
            if x == 0  or x == a-1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
'''
'''
#===========================================================
#ques 5> Printing E

a = int(input("Enter no of rows: "))
s = a//2

for j in range(0,a):
    if j == 0 or j == a-1 or j == s:
        for i in range(0,a):
            print("*",end="\t")
        print()
    else:
        for c in range(0,a):
            if c == 0:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
'''
'''

#===========================================================
#ques 6> Printing F

a = int(input("Enter no of rows: "))
s= a//2
#print(s)
for j in range(0,a):
    if j == 0:
        for i in range(0,a):
            print("*",end="\t")
        print()
    elif j == s:
        for x in range(0,a-2):
            print("*",end="\t")
        print()
    else:
        for c in range(0,a):
            if c == 0:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
'''
'''
#===========================================================
#ques 7> Printing G
a = int(input("Enter no of rows: "))
s = a//2
g = 1

for j in range(0,a):
    if j == 0 or j == a-1:
        for i in range(0,a):
            if i == 0:
                print(" ",end="\t")
            else:
                print("*",end="\t")
        print()
    elif j == s:
        for c in range(0,a):
            if c == g:
                print(" ",end="\t")
            else:
                print("*",end="\t")
        print()
    elif j > s and j < a:
        for x in range(0,a):
            if x == 0 or x == a-1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
    else:
          for y in range(0,a):
            if y == 0:
                print("*",end="\t")
            else:
                print(" ",end="\t")
          print()
'''
'''
#===========================================================
#ques 8> Printing H

a = int(input("Enter no of rows: "))
s = a//2

for j in range(0,a):
    if j == s:
        for x in range(0,a):
            print("*",end="\t")
        print()
    else:
        for i in range(0,a):
            if i == 0 or i == a-1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
'''
'''
#===========================================================
#ques 9> Printing I

a = int(input("Enter no. of rows : "))
s = a//2
if a % 2 == 0:
    v = 1
else:
    v = 0

for j in range(0,a):
    if j == 0 or j == a-1:
        for i in range(0,a-v):
            print("*",end="\t")
        print()
    else:
        for x in range(0,a-v):
            if x == s-v:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()

'''
'''
#===========================================================
#ques 10> Printing J

a = int(input("Enter no. of rows : "))
for j in range(0,a):
    if j < a-2:
        for i in range(0,a):
            if i == a-1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
    elif j == a-2:
        for x in range(0,a):
            if x == 0 or x == a-1:
                a = int(input("Enter no. of rows : "))
            else:
                print(" ",end="\t")
        print()
    else:
        for c in range(0,a):
            if c == 0 or c == a-1:
                print(" ",end="\t")
            else:
                print("*",end="\t")
        print()
'''
'''
#===========================================================
#ques 11> Printing K

a = int(input("Enter no. of rows : "))
s = a//2
k = a-3
print(3)

print(k)

for j in range(0,a):
    for i in range(0,a-2):
        if i == k or i == 0:
            print("*",end="\t")
        else:
            print(" ",end="\t")
    if j < s:
        k -= 1
    else:
        k += 1

    print()                               # not completed
'''
'''
#===========================================================
#ques 12> Printing L

a = int(input("Enter no. of rows : "))

for j in range(0,a):
    if j < a-1:
        for i in range(0,a):
            if i == 0:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
    else:
        for x in range(0,a):
            print("*",end="\t")
'''
'''
#===========================================================
#ques 13> Printing M

a = int(input("Enter no. of rows : "))
c = 1
s =int(a/2)
if a % 2 == 0:
    m = 1
    #s = s + 1
else:
    m = 0
    #s = s
print("m = ",m)
print(s)
#-----     -----     -----     -----     -----
for j in range(0,a):
    if j == 0 or j > s:
        for i in range(0,a+m):
            if i == 0 or i == (a-1)+m:
                print("*",end="\t")
            else:
                print("-",end="\t")
        print()
    else:
        for x in range(0,a+m):
            if x == 0 or x == (a-1)+m or x == j or x == j+s:
                print("m",end="\t")
            else:
                print("-",end="\t")

        print()
                                          #-----Not completed
'''
'''
#===========================================================
#ques 14> Printing N

a = int(input("Enter no. of rows : "))
c = 1
for j in range(0,a):
    if j == 0 or j == a-1:
        for i in range(0,a):
            if i == 0 or i == a-1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
    else:
        for x in range(0,a):
            if x == 0 or x == a-1 or x == c:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
        c += 1
'''
'''
#===========================================================
#ques 15> Printing O

a = int(input("Enter no. of rows : "))
for j in range(0,a):
    if j == 0 or j == a-1:
        for i in range(0,a):
            if i == 0 or i == a-1:
                print(" ",end="\t")
            else:
                print("*",end="\t")
        print()
    else:
        for x in range(0,a):
            if x == 0 or x == a-1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
'''
'''
#===========================================================
#ques 16> Printing P

a = int(input("Enter no. of rows : "))
s = a//2
for j in range(0,a):
    if j == 0 or j == s:
        for x in range(0,a):
            if x == 0 or x < a-1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
    elif j < s:
        for i in range(0,a):
            if i == 0 or i == a-1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
    else:
        for i in range(0,a):
            if i == 0:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
'''
'''
#===========================================================
#ques 17> Printing Q

a = int(input("Enter no. of rows : "))
s = a//2
if a  % 2 == 0:
    s = s
else:
    s = s + 1
q = 0
print(s)
for j in range(0,a):
    if j == 0 or j == a-1:
        for i in range(0,a):
            if i == 0 or i == a-1:
                print("-",end="\t")
            else:
                print("*",end="\t")
        print()
    elif j == s + q :
        for c in range(0,a):
            if c == 0 or c == (s + q) or c == a-1:
                print("*",end="\t")
            else:
                print("-",end="\t")
        print()
    else:
        for x in range(0,a):
            if x == 0 or x == a-1:
                print("*",end="\t")
            else:
                print("-",end="\t")
        print()
    q += 1
'''
'''

#===========================================================
#ques 18> Printing R

a = int(input("Enter no. of rows : "))
s = a//2
r = s
print(s)
for j in range(0,a):
    if j == 0 or j == s:
        for x in range(0,a):
            if x == 0 or x < a-1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
    elif j < s:
        for i in range(0,a):
            if i == 0 or i == a-1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
    else:
        for i in range(0,a):
            if i == 0 or i == r:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()

        r += 1
'''
'''
#===========================================================
#ques 19> Printing S

a = int(input("Enter no. of rows : "))
s = a//2
if a % 2 == 0:
    a = a+1
else:
    a = a
print(s)
for j in range(0,a):
    if j == 0:
        for x in range(0,a):
            if x > 0:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
    elif j == a-1:
        for x in range(0,a):
            if x < a-1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
    elif j == s:
        for x in range(0,a):
            if x > 0 and x < a-1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
    elif j < s:
        for x in range(0,a):
            if x == 0:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
    elif j > s:
        for x in range(0,a):
            if x == a-1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
'''
'''
#===========================================================
#ques 20> Printing T

a = int(input("Enter no. of rows : "))
s = a//2
if a % 2 == 0:
    a = a+1
else:
    a = a
print(s)
for j in range(0,a):
    if j == 0:
        for x in range(0,a):
                print("*",end="\t")
        print()
    else:
        for x in range(0,a):
            if x == s:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
'''
'''
#===========================================================
#ques 21> Printing U

a = int(input("Enter no. of rows : "))

for j in range(0,a):
    if j < a-1:
        for i in range(0,a):
                if i == 0 or i == a-1:
                    print("*",end="\t")
                else:
                    print(" ",end="\t")
        print()
    else:
        for x in range(0,a):
                if x == 0 or x == a-1:
                    print(" ",end="\t")
                else:
                    print("*",end="\t")
        print()
'''
'''
#===========================================================
#ques 22> Printing V

a = int(input("Enter no. of rows : "))
s = a//2
inc = 0
dec = a-1
print(s)
for j in range(0,a):
    if j < s:
        for i in range(0,a):
                if i == 0 or i == a-1:
                    print("*",end="\t")
                else:
                    print(" ",end="\t")
        print()
    if j >= s:
        for x in range(0,a):
                if x == inc or x == dec  :
                    print("*",end="\t")
                else:
                    print(" ",end="\t")
        print()
        inc += 1
        dec -= 1
                                # Not Perfect
'''
'''

#===========================================================
#ques 23> Printing W

a = int(input("Enter no. of rows : "))
s = a//2
inc = s
dec = s
print(s)
for j in range(0,a):
        if j == 0 or  j < s:
            for i in range(0,a):
                if i == 0 or i == a-1:
                    print("*",end="\t")
                else:
                    print("-",end="\t")
            print()

        else:
            for x in range(0,a):
                if x == inc or x == dec or x == 0 or x == a-1:
                    print("*",end="\t")
                else:
                    print(" ",end="\t")
            print()
            inc += 1
            dec -= 1
'''
'''
#===========================================================
#ques 24> Printing X

a = int(input("Enter no. of rows : "))
s = a//2
inc = 0
dec = a-1
print(s)
for j in range(0,a):
            for i in range(0,a):
                if i == inc or i == dec:
                    print("*",end="\t")
                else:
                    print(" ",end="\t")
            print()
            inc += 1
            dec -= 1
'''
'''
#===========================================================
#ques 25> Printing Y
a = int(input("Enter no. of rows : "))
s = a//2
inc = 0
dec = a-1
print(s)
for j in range(0,a):
    if j < s:
            for i in range(0,a):
                if i == inc or i == dec:
                    print("*",end="\t")
                else:
                    print(" ",end="\t")
            print()
            inc += 1
            dec -= 1
    else:
        for i in range(0,a):
                if i == s:
                    print("*",end="\t")
                else:
                    print(" ",end="\t")
        print()
'''
'''
#===========================================================
#ques 26> Printing Z
a = int(input("Enter no. of rows : "))

inc = 0
dec = a-2

for j in range(0,a):
    if j == 0 or j == a-1:
        for i in range(0,a):
                if i < a:
                    print("*",end="\t")
                else:
                    print(" ",end="\t")
        print()
    elif j == 1 or j < a-1:
            for i in range(0,a):
                if i == dec:
                    print("*",end="\t")
                else:
                    print(" ",end="\t")
            print()
            dec -= 1
'''
