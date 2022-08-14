num=int(input('Enter any Number: '))
flag = False
for i in range(2,num):
    if num % i == 0:
        flag = True
        break
if flag == True:
    print('Number is not prime')
else:
    print('Number is prime')
    

    
