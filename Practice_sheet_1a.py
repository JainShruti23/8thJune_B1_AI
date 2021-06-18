#Ques2
print(5**9)
print(3//2)
print(7//3)
print(6==6)
a=20
a+=30
a%=3
print(a)
print(True*False)
print(True&False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print(True is False)
print(False is 'False')
print(((True==False)or (False>True)) and (False<=True))

#Ques3
s1 = "Nice to have it"
s2 = "here"
print(s1+" "+s2)

#Ques4
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

#Ques5
a.insert(0, s1)
a.append(s2)
print(a)

#Ques6
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
print(color_list_1-color_list_2)

#Ques7
alpha = "abcdefghijklmnopqrstuvwxyz"
string = input("Enter string: ")
s = string.lower()
l= s.count
c=0
for i in alpha:
    c = 0
    for j in s:
        if (i==j):
            c = 1
            break
        elif(j==" "):
            continue
    if(c==0):
        break

if(c==0):
    print("Not a pangram string")
else:
    print("Pangram string")

#Ques8
print(eval('{0}+{0}{0}+{0}{0}{0}'.format(input('Enter the number: '))))

#Ques9
items = input("Input comma separated sequence of words: ")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

#Ques10
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
hmarks = (max(d['Marks']))
location = [i for i, t in enumerate(d['Marks']) if t==hmarks]
print(d['Student'][location[0]])





        