
#factorial of given number using  recursive functional programming
def factorial(n):
 if n==0:
  return 1
 else:
  return n*factorial(n-1)
a=int(input("enter a non negative integer "))
print(factorial(a))
