#比较+和append的时间效率
import time
import random #导入随机函数库
start1 = time.time()
s = list()
l = [random.randint(0,100) for i in range(50)] 随机生成50个0-100的随机整数
for i in l:
    s = s + [i]
print(s)
stop1 = time.time()
print('Total:',start1-stop1)

start2 = time.time()
s = list()
l = [random.randint(0,100) for i in range(50)]
for i in l:
    s.append(i)
print(s)
stop2 = time.time()
print('Total:',start2-stop2)
