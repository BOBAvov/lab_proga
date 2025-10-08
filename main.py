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

n = 5
a = [1,2,3,4,5]
b = [2,4,6,8,10]

c = [0] * 2 * n
d = []
e = [0] * n

for i in range(n):
    c[2*i] = a[i]
    c[2*i + 1] = b[i]
    if a[i] == b[i]:
        d.append(a[i])
    e[i] = a[i] - b[i]
print(c)
print(d)
print(e)