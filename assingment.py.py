#1330
A,B=map(int,input().split())
if A>B:
    print(">")
elif A<B:
    print("<")
else:
    print("==")
#9498
시험성적=int(input())
if 100>=시험성적>=90:
    print("A")
elif 89>=시험성적>=80:
    print("B")
elif 79>=시험성적>=70:
    print("C")
elif 69>=시험성적>=60:
    print("D")
else:
    print("F")
#2753
연도=int(input())
if 연도%4==0 and 연도%100!=0:
    print("1")
elif 연도%4==0 and 연도%400==0:
    print("1")
else:
    print("0")
#14681
x=int(input())
y=int(input())
if x>0 and y>0:
    print("1")
elif x<0 and y>0:
    print("2")
elif x<0 and y<0:
    print("3")
else:
    print("4")
