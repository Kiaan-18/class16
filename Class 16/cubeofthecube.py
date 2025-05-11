def cube(num):
    return num*num*num
def div_three(num):
    if num%3==0:
        return cube(num)
    else:
        return False
num=int(input("Enter a number:"))
print(div_three(num))