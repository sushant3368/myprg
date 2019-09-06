29 July 2019

Sushant Pandilwar

def a_void():                      # program to return none
	a=1
	b=2
	c=a+b
x=a_void()
print(x)



# access elements from list

l1 = ['a','b','c','d','e','f']           # using list index
print(l1[3])
print(l1[-1])
print(l1[-6])
print(l1[-3])

l2 = ['sushant',[1,2,3,4,5],6,7,'z']     #nested indexing
print(l2[0])
print(l2[0][4])
print(l2[1])
print(l2[1][3])
print(l2[4])


# slicing the list

l3 = ['h','e','l','l','o','w','o','r','l','d','p','q','r','s']
print(l3[5:10])
print(l3[:-9])
print(l3[10:])
print[l3[:]]


# change or add elements in python

l4 = ['w','x','y','z']        #changing elements in list
l4[0] = 'a'
print(l4)
l4[1:4] = ['b','c','d']
print(l4)

l4.append('f')                #adding one element at end of list
print(l4)

l4.extend(['g','h','i'])      #adding several elements at end of list
print(l4)

l4 = l4 + ['j','k','l']       #combining two lists
print(l4)     

l4.insert(4,'e')              #inserting one element at desired location
print(l4)

l4[6:6] = [1,2,3,4]           #inserting multiple elements at desired location
print(l4)


# delete elements from list

l5 = ['e','l','e','p','h','a','n','t']    #deleting one element from list
del l5[3]
print(l5)

del l5[2:5]                               #deleting multiple elements from list
print(l5)

del l5                                    #deleting entire list
print(l5)


# removing elements from list

l6 = ['p','a','n','d','i','l','w','a','r']    #removing one element from list
l6.remove('i')
print(l6)
l6[5:7] = []
print(l6)

print(l6.pop())                               #remove and return last element from list
print(l6)

print(l6.pop(3))                              #remove and return desired element from list
print(l6)

l6.clear()                                    #empty a list
print(l6)




l7 = ['b','e','n','g','a','l','u','r','u']      #find the index of 1st matched element
print(l7.index('u'))

print(l7.count('u'))                            #returns the count of item passed in argument
print(l7.count('b'))

l7.sort()                                       #sorts the list in ascending oeder
print(l7)

l7.reverse()                                    #reverse the srder of the list
print(l7)


l8 = [1,2,3,4]                                    #copying list
new_l8 = l8.copy()
new_l8.append(6)
print("old list: ",l8)
print("new list: ",new_l8)



# list comprehension

m5 = [5*x for x in range(11)]                  #creating a list using a condition
print(m5)

m10 = []                                   #list using for loop
for x in range(11):
	m10.append(10*x)
print(m10)


# list membership test

a1 = [p+q for p in ['Python ','R '] for q in ['Language','Programming']]
print(a1)

print('Python Programming' in a1)            #list membership test
print('C Language' in a1)
print('C++ Programming' not in a1)
print('R Language' not in a1)


# iteration through list

for planet in ['Earth','Mercury','Venus','Jupiter']:
	print("The %s is a Planet" % planet)