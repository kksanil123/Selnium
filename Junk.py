# # import unittest
# #
# # class ExpectedFailureTestCase(unittest.TestCase):
# #     @unittest.expectedFailure
# #     def test_fail(self):
# #         self.assertEqual(1, 0, "broken")
# #
# #
# # if __name__ == '__main__':
# #     unittest.main()
# # else:
# #     print(f"__name__ is {__name__}."

'''a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if a>b:
    if a>c:
        print("a is bigger")
    else:
        print("c is bigger")
elif b>c:
    print("b is bigger")
else:
    print("c is bigger")'''
# a=int(input("enter"))
# for i in range(0, a//2+1):
#        print(' ' * i, end=' ')
#        for j in range(0, a):
#                print("*", end =' ')
#        if(a == 0):
#                print("*")
#        else:
#         print("")
#        a = a-2
'''x = 0
for i in range(10,-1, -2):
    if i in range(10, -1, -2):
        if i == 0:
            print('*')
        else:
            pass
        print(x * ' '+ i*'* ')
    else:
        print("I am out..")
    x = x+1'''
'''for n in range(2, 10):
    for x in range(2, n):
          if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
           print(n, 'is a prime number')'''
# print([(i) for i in range(0,21,2)])
'''
# i=0
# while i<=10:
#     t=2*i
#     print(t,end=" ")
#     i=i+1'''
# a = input().split(" ")
# print(a)

print(__name__)