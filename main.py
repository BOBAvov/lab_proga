# import array as arr
# import time
#
#
# def f1(a):
#     b = arr.array('i')
#     for i in a:
#         if i>0:
#             b.append(i)
#     return b
#
#
# def f2(a):
#     b = [i for i in a if i>0]
#     return b
#
#
# l = [i*(-1)**(i) for i in range(10**5)]
# a2 = l
# t = time.process_time_ns()
# a1 = arr.array('i', l)
# f1(a1)
# t1 = time.process_time_ns() - t
# f2(a2)
# t2 = time.process_time_ns() - t1
# print(t1)
# print(t2)
# import functools
import math

# n = 5
# a = [1,2,3,4,5]
# b = [2,4,6,8,10]
#
# c = [0] * 2 * n
# d = []
# e = [0] * n
#
# for i in range(n):
#     c[2*i] = a[i]
#     c[2*i + 1] = b[i]
#     if a[i] == b[i]:
#         d.append(a[i])
#     e[i] = a[i] - b[i]
# print(c)
# print(d)
# print(e)

# import typing
# def div(a: int,b: int):
#     return a+b
#
# print(div('1','2'))
# print(map(int,'1 2 3'.split()))
#
#
# a = [1,2,3]
# a = map(lambda x: str(x+1),a)
# print(a)
# print("".join(a))
# def f(b,c):
#     return b**c
# a = [3,100,90]
# print(functools.reduce(f,a))
# print(len(str(functools.reduce(f,a))))


# def get_time(func):
#     import time
#     def act():
#         start = time.time()
#         a = func()
#         end = time.time()
#         print(f'Время: {end-start}')
#         return a
#     return act
#
# @get_time
# def f():
#     a = 0
#     for i in range(10**5):
#         a+=i
#     return a
#
# print(f())

# n = int(input())
# m = []
# for i in range(n):
#     k = []
#     for j in range(n):
#         k.append(abs(i-j)+1)
#     m.append(k)
# for i in m:
#     print(*i)

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# a = set(a)
# b = set(b)
# print(*a&b)
# print(*a|b)
# print(*a-b)


# a = list(map(int,input().split()))
# for i in range(len(a)):
#     mn_i = i
#     for j in range(i,len(a)):
#         if a[mn_i]>a[j]:
#             mn_i = j
#     a[mn_i],a[i] = a[i],a[mn_i]
# print(a)

# a = [list(map(int,input().split())) for i in range(int(input()))]
# n = len(a)
# q = 1
# for i in range(len(a)):
#     s = 0
#     for j in range(len(a[0])):
#         s+=a[i][j]**2
#     q*=s
# print(math.sqrt(q))


# m = []
# k = [i+1 for i in range(n)]
# k = k[::-1]+k
# k.remove(1)
#
# for i in range(n):
#     j = n-i-1
#     m.append(k[j:j+n].copy())
#
# for i in m:
#     print(*i)


# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print(i-j,end=" ")
#     print()
# print()
# for i in range(n):
#     for j in range(n):
#         print(n - i - j -1,end=" ")
#     print()
#
# for i in range(n):
#     for j in range(n):
#         if
# a = [12]
# print(id(a))
# print(id(a[0]))
# print(id(12))
#
# f = (1,2,3,[1,3])
# f[3].append(1333)
# print(f)

with open("1.txt","a+") as file:
    file.write('123\n')

file.write('63t872187')