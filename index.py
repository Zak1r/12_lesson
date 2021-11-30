# i = 0

# while i <= 10:
#     if i % 2 == 1: break
#     print(i)
#     i+=1

# if True:
#     pass

# while int(input('Enter number')) > 0: 
#     pass

# for i in range(5):
#     if int(input('Enter number')) < 0: break

# print('Now you will be asked to enter 2 numbers that will be divided and the answer will be printed')
# a = int(input('Enter 1st number: '))
# b = int(input('Enter 2nd number. Note that you cannot use 0: '))

# if b == 0:
#     i = 1
#     while True:
#         # Если пользователь ввел нуль больше 3-х раз
#         if i > 3: 
#             print('Stupid asshole. Do not you know math?')
#         else: print('Please enter non-zero value')
#         b = int(input('Enter 2nd number. Note that you cannot use 0: '))
#         if b != 0: 
#             print(a / b)
#             break
#         i+=1
# else:
#     print(a / b)



# a = int(input('Enter 1st number: '))
# i = 1
# while True:
#     b = int(input('Enter 2nd number. Note that you cannot use 0: '))
#     try:
#         print(a / b)
#         break
#     except ArithmeticError:
#         print('АААААА ПОЖАР БЕГИТЕ!')
#     except ZeroDivisionError:
#         if i > 3: print('Stupid asshole. Do not you know math?')
#         else: print('Please enter non-zero value')
#     i+=1


# while True:
#     a = int(input('Enter positive number: '))
#     if a > 0: break
#     else: print('You were asked to enter positive number: ')

# while True:
#     try:
#         a = int(input('Enter positive number: '))
#         if a < 0: raise ValueError('You were asked to enter positive number: ')
#         else: break
#     except ValueError as ve:
#         print(ve)


while True:
    num = int(input('Enter prime number: '))
    for factor in range(2, num):
        if num % factor == 0: raise ValueError('Your number is not prime')