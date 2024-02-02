# datatypes , operators
# int ,float,list,tuple,range,dict

x=50
print(type(x))

#  list 
marks = [10,20,30]
print(type(marks))
print(marks)

print(marks[2])
print(marks[0:2])

# nested list

age =[4,10,12,[24,35,12]]

print(age)
age[1]=4
print(age)
print(age[2]) 
print(age[3])
print(age[3][1])
age.append(56)
print(age)

# list = []
# tuple =() 

class1=(1,2,3,4,5)
print(class1[3])
print(class1[0:])
print(class1[0:2])
print(class1[0:4])

# tuples can't be modified
# class1[2]=5
# class1.append(33)
# print(class1[3])

# range 

for i in range (12):
    print(i) 
    print("\n")
    print("\n")
    print("\n")
# range (start,end,increment)
for i in range (10,15):
    print(i)
for j in range (6,12,2):
    print(j)

# dictionary
emp ={ 
    'EmpNo':12,
    'EmpName' : "PIYUSH",
    'Salary' : 350000000
    }

print(emp)
print(emp ['EmpName'])

# set it can't have repeated value
p1 ={1,2,3,4,1,2,3,4}
print(p1)
p2 = {1,4,3,5,2,3,6}
print(p2)
p2.add(7)
print(p2)
print(frozenset(p2))
p3=frozenset(p2)
print(p3)


print(dir(list))
print(dir(set))


# typecasting
x=69.76
print(type(x))
print("type of x is " + str(type(x)))

y=int(x)
z=bool(x)
print(type(y))
print(x)
print(y)
print(z)
a=str(x)
print(a)
print(type(a))

# for typecasting 
# into string =str
# into int =int
# into float =float
# into complex =complex
# into list =list
# into tuple =tuple


# operators

print(7/2)
print(7//2)

a=20
b=30
c=50
a+=b
print(a)
c=b=a
print(c)
print(a is b)
print(a<b and b>c)
p4=[1,2,3,4,5]
print(1 in p4)
print(6 in p4)
print(6 not in p4)




 