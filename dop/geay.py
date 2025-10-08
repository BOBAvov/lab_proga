import time
def bin_to_gray(n):
    return n ^ (n >> 1)
for num in range(1,10**7):
    gray = bin_to_gray(num)
    # print(f"bin: {num:b}; gray: {gray:b}")
print(time.process_time())