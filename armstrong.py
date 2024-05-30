num = int (input ('enter the number :'))
num1 = str(num)
digit = len(num1)

sum = 0

while num > 0:
    q = num//10
    r = num%10
    pow_dig = r**digit
    sum = sum+pow_dig
    num = q
print(sum)

if str(sum) == num1:
    print (num1,'Number is Armstrong')
else:
    print (num1,'Number is not Armstrong')
 
