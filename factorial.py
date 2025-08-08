# %%
num=int(input("Enter a number!"))
def fact(num,acc=1):
    if num==1:return acc
    return fact(num-1,acc*num)
result=fact(num)
print(f"Factorial of {num} is:",result)
# %%
