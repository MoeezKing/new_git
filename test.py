# print('hello world')

# print(type(True))

# name = 'ali' # simple case
# firstName = 'ali' # Camel case
# FirstName = 'ali' # pascal case
# first_name = 'ali' # snake case
# firstname = 'ali' # number case

# print("\U0001F910   ")

# num = 9
# if num == 9:
#     print('U got it')

# edu = int(input("Enter your Education :"))
# age= int(input("Enter Your Age: "))
# height = float(input("Enter Your Height: "))

# if (edu>=12 and age >=18 and age <=32):
#     print("You are select")
# elif (edu>=12 and  height>=5.6):
#     print("You are select")
# elif(age >=18 and age <=32 and height>=5.6):
#     print("You are select")    
# else:
#     print("You are not select")    

# marks = int(input("Enter your marks : "))

# total_marks = int(input("Enter your total marks : "))

# print(f"Your percentage is {(marks/total_marks)*100}%")

# assignment number !
# bonus = int(input("Enter the bonus price that you got : "))
# bonus_percentage = float(input("Enter the percentage of bonus you got : "))

# print(f"Your salary is {(bonus/bonus_percentage)*100}")

# s = 'Hello worrld is a string'
# b = s.split('rr')

# print(s, b)

# capitalizing 1st word
# a = 'hello'
# b = 'world'
# c = a+' '+b
# print(a.capitalize()+ ' '+ b.capitalize())
# print(c.title())

#Most repeated world in paragraph
# p ="""Paragraphs can contain many different kinds of information. A paragraph could contain a series of brief examples or a single long illustration of a general point. It might describe a place, character, or process; narrate a series of events; compare or contrast two or more things; classify items into categories; or describe causes and effects. Regardless of the kind of information they contain, all paragraphs share certain characteristics. One of the most important of these is a topic sentence."""
# pl= p.split()
# dic = {}

# for word in pl:
#     count = 0
#     for string_word in pl:
#         if word == string_word:
#             count = count + 1
#     dic[word]= count

# most_repeated = None
# max_count = 0

# for word in pl:
#     count = dic.get(word)
#     if max_count < count:
#         max_count=count
#         most_repeated=word

# print(f"The {most_repeated} is repeaded most upto {max_count}")
# print(dic)

# p ='jarawala faisalabad lahore'

# a,b,c = p.split()

# # print(a.capitalize()+' '+b.capitalize()+' '+c.capitalize())

# # print(f"J{a[1:]} F{b[1:]} L{c[1:]}") #usong f string
# # print("J{} F{} L{}".format(a[1:], b[1:], c[1:])) # using format method

# print(f"{p[0:1].upper()}{p[1:len(a)+1]} {p[len(a)+1:len(a)+2].upper()}{p[len(a)+2:len(a)+len(b)+2]}{p[len(a)+len(b)+2:len(a)+len(b)+3].upper()}{p[len(a)+len(b)+3:]}")
# print(f"{p[0:1]}{p[1:len(a)+1].upper()} {p[len(a)+1:len(a)+2]}{p[len(a)+2:len(a)+len(b)+2].upper()}{p[len(a)+len(b)+2:len(a)+len(b)+3]}{p[len(a)+len(b)+3:].upper()}")


# # print(p[len(a)+len(b)+2:len(a)+len(b)+3].upper())

# print(p[0:1]+p[1:9].upper()+' '+p[9:10]+p[10:19].upper()+' '+p[20:21]+p[21:].upper())
# a=a.replace('j','J')
# b=b.replace('f','F')
# c=c.replace('l','L')
# print(a+' '+b+' '+c)


# assignment 2  
# p = "Jarawala Faislabad Lahore Karachi Multan"
# p=p.replace('J','j').replace('F','f').replace('L','l').replace('K','k').replace('M','m')
# print(p)

# most repeated word in para version 2
# p = 'Paragraphs can contain many different kinds of information. A paragraph could contain a series of brief examples or a single long illustration of a general point. It might describe a place, character, or process; narrate a series of events; compare or contrast two or more things; classify items into categories; or describe causes and effects. Regardless of the kind of information they contain, all paragraphs share certain characteristics. One of the most important of these is a topic sentence.'
# sp = p.lower().split()
# most_repeated = None
# max_count = 0
# for word in sp:
#     count = 0
#     for check_word in sp:
#         if word == check_word:
#             count = count +1
#             if count > max_count:
#                 max_count = count
#                 most_repeated = word

# print(f"{most_repeated} is most repeated word in paragraph ,it have appear upto {max_count} times")


# ls = list(['lahore','karachi', 'lahore', 'lahore'])
# print(ls)
# ls.remove('lahore')
# print(ls)
# ls.clear()
# print(ls)

# ls = ["lahore","karachi","Multan"]
# t=[]
# for i in ls:
#     # t.append(i.capitalize())
#     # z= i[0:1].upper() + i[1:-1].lower()+ i[-1:].upper()
#     z= i[0:1].lower() + i[1:2].upper()+ i[2:-2].lower()+ i[-2:-1].upper() + i[-1:].lower()
#     t.append(z)
# print(t)

# for i in range(11):
#     print(f"5 X {i} = {i*5}")
    

# x = ["lahore","karachi","Multan","Bhawalpur","Muree"]
# lp = []
# for i in x:
#     lp.insert(0,i)
# print(lp)    



#assignment 3
# list of 10 cities and reverse list ,and 1st and last in lower
# ls = ['lahore', 'karachi', 'islamabad', 'quetta', 'peshawar','murree','jarawala', 'faisalabad', 'attock', 'multan']
# nl = []
# print(ls)
# for i in ls:
#     nl.insert(0, i)

# print(nl)
# ls.clear()

# for i in nl:
#     n = i[0:1].upper()+i[1:-1].lower()+i[-1:].upper()
#     ls.append(n)

# print(ls)

# reversing list
# ls = ['lahore', 'karachi', 'islamabad', 'quetta', 'peshawar','murree','jarawala', 'faisalabad', 'attock', 'multan']
# print(ls)
# n = []
# for i in ls:
#     n[0:0] = [i]

# print(n)


# for loop using range()
# ls = ['lahore', 'karachi', 'islamabad']

# for x in range(len(ls)):
#     print(ls[x], x)

#while loop

# i = 0
# ls = ['lahore', 'karachi', 'islamabad']
# while i< len(ls):
#     print(ls[i], i)
#     i = i+1

# 2 table
# for i in range(1,11):
#     # print("2 * {} = {}".format(i, 2*i))
#     print(f"2 * {i} = {2*i}")

# LIST comprehension

# list_name = [expression for item in another_list_or_any_function condition]
# expression -> the element that will be append in LIST
# item -> smae item as in for loop
# another_list_or_any_function -> you can use any other list or any function like range() etc from where item can be extracted
# condition -> use if statement for condition 

# ls = [x for x in range(10)]
# print(ls)


#coventional way
# ls = ['karachi', 'lahore', 'jarawala', 'lion']
# nl = []

# for x in ls:
#     if 'a' in x:
#         nl.append(x)

# print(nl)


# using LIST comprehension method
# ls = ['karachi', 'lAhore', 'jarawala', 'lion']
# # nl = [x.capitalize() for x in ls if 'a' in x]
# nl = [x[0].upper()+x[1:].lower() for x in ls if "a" in x.lower()]

# print(nl)

# 1st and last letter in uppercase
# ls = ["karachi", "jarawala", "fasialabad", "kivi","test"]
# ls2 = [x[0].upper()+x[1:-1].lower()+x[-1:].upper() for x in ls]
# print(ls2)

# num1 = int(input("Enter 1st value = "))
# num2 = int(input("Enter 2nd value = "))

# ls = [num1, num2]
# print(ls)

# num =int(input("Enter your value :"))

# i = num -1
# while i>=1:
#     num = num * i
#     i= i -1

# print(f"Factorial is {num}")


# count = 0
# # ls =list((str(x) for x in range(0,101) if "3" in str(x)))
# # print(len(ls))
# for x in range(1,101):
#     x= str(x)
#     if '3' in x:
#         count=count+1

# print(f"3 is appeared {count} times")


#tuple
# tup = ('hello', 'world')
# t1= ('hello')
# t2= ('hello',)

# print(type(tup))
# print(type(t2))
# print(type(t1))

#pass by refernce 
# a=["10", '20']
# b=a
# b[0]= '15'

# print(a)
# print(b)

# tuple

# t = tuple(["lahore","karachi","jarawala"])
# ls = list((t))
# nl = [x[0:1].upper()+x[1:].lower() for x in ls]
# t = tuple((nl))
# print(t)

t1= ("Fasilabad","jarawala","Lahore")
t2= (1,2,3,4,5,6,7)

# 5 methods
# method 1
# t3 = t2+ t1
# t3 = t3[len(t2):] + t3[: len(t2)]
# print(t3)

# method 2
# t3 = t2+t1
# l = list((t3))
# l.reverse()
# t3 = tuple((l))
# print(t3)

# Method 3
# t3 = t2+t1
# t3 = t3[::-1]
# print(t3)


# Method 4
# t3 = t2 + t1
# l1 = list((t3))
# l2 = []
# for x in l1:
#     l2.insert(0, x)
# t3 = tuple((l2))
# print(t3)

# method 5
# t3 = t2+ t1

# l1 = []
# for x in range(len(t2), len(t3)):
#     l1.append(t3[x])

# for x in range(0, len(t2)):
#     l1.append(t3[x])

# t3 = tuple((l1))

# print(t3)



