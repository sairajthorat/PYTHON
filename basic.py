#constant
PI=3.14
PI=5
print(PI) 
'''here value of PI will change
   cuz in python constant does't 
   exist but we just fill it by 
   using capital letters'''


#literal
#numeric

binary_literal=0b1111 #15
print(binary_literal)

octal_literals=0o14 #12
print(octal_literals)

hexadecimal=0x11 #17
print(hexadecimal)

str1="A"
print(str1)

str2="""MULTILINE STRING CAN BE WRITE"""
print(str2)

str3="sairaj"\
"thorat"\
"sangam"
print(str3) #sairajthoratsangam

#type conversion

#implicit------done by compiler
#for EX
a=1
a="sairaj"

#explicti------done by programer
b=1
b=float(b)
print(type(b))
print(b) #0.1


#input output  operation
'''c=int(input("Roll no"))''' #input store value in string int converting value in integer type
'''print(c)'''


#standard data type

lst=["a",5,"saiarj",3.14,1+2j]
print(type(lst))
print(lst)
lst[2]="thorat"
print(lst)
print(lst[0:1]) #a
print(lst[ :1]) #a
print(lst[1:1]) #
print(lst[2:3]) #thorat
print(lst[2:]) #['thorat', 3.14, (1+2j)]

tple=(1,2,"pqr",2.5)
print(type(tple))
#tple[0]=5  we cannot replace value in tuple
print(tple)

#SET

set={1,"abc",5.5}
print(type(set))#every item is unique


#dict

dict={"name":"sairaj","age":18,"state":"maharastra"}
print(type(dict))
print(dict)
print(dict["name"])
dict["name"]="thorat"
print(dict)