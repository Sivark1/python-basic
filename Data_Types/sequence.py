#List
l=[1,2,5,"Siva",3,4,5,6]     
print(l)
print(type(l))

l.append("Hello")
l.extend(["Good Mrng",8,9,10])
l.remove(3)
l.pop(1)
print(l)
l1 = ["hello","how r u"]
l2 = ["hi","Fine"]
print(l1 + l2)
print(l2 * 3)
print(l[0:3])
print(l[4:])


#Tuple
t = (1,2,3,2,1,2,2,2,"Rama",5.5,9)
print(t)
print(type(t))

print(t.count(2))
print(t.index(1))
print(t)

#To add items we need to convert to list and tha modify than change to tuple

t1=list(t)
t1.append("Thunder soft")
t=tuple(t1)
print(t)

t2=("It","cse")
t += t2
print(t)

#Tuple packing and unpacking
a = 10,20,30
print(a)
a,b,c = 10,20,30
print(a,b,c)

#Set
s = {1,2,3,4,"Sai"}
print(s)
print(type(s))

s.add(100)
print(s)
s.discard(1)
print(s)

#Set opeartions
s1={1,2,3,4,5}
s2={5,6,7,8,9}
print(s1|s2) #union
print(s1&s2) #Intersection
print(s1 - s2) #Difference
print(s1^s2)  #Symmetric diff


#Dictionary
d={"Dict":"data","Gadget":"Laptop"}
print(d)
print(type(d))
print(d.items())
print(d.keys())
print(d.values())
print(d.get("Dict"))

d2 = d.copy()
print(d2)

#Nested Dictonary
myfamily = {
    "child1":{
        "name":"siva",
        "Year":2002
    },
    "child2":{
        "name":"sai",
        "Year":1999
    }
}
print(myfamily)