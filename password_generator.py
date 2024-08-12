from numpy import random
letters=['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','c','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','+','=','-','_','{','}','|']
print('Welcome to Password Generator!')
no_letters=int(input("How many letters you want in your password?\n "))
no_symbols=int(input("How many symbols you want in your symbols?\n"))
no_numbers=int(input("How many numbers you want in your password?\n"))
passwords_list=[]
for i in range(no_letters):
    char=random.choice(letters)
    passwords_list+=char
for i in range(no_symbols):
    char=random.choice(symbols)
    passwords_list+=char
for i in range(no_numbers):
    char=random.choice(numbers)
    passwords_list+=char
print(passwords_list)
password=" "
for char in passwords_list:
    password+=char
print(password)