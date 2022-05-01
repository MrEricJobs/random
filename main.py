import random
import time

start = int(input("시작 번호: "))
end = int(input("마지막 번호: "))
line = int(input("줄: "))
while((end - start + 1) % line != 0):
    line = int(input("줄: "))
each_line = (end - start + 1) // line
number_list = range(start, end + 1)
random_list = random.sample(number_list, end)
f = open('./result/' + time.strftime('%Y년 %m월 %d일 %H시 %M분 %S초', time.localtime(time.time())) + '.txt', 'w')
for x in range(each_line):
    for y in range(line):
        for i in range(len(str(end)) - len(str(random_list[x + (each_line * y)]))):
            f.write('0')
        f.write(str(random_list[x + (each_line * y)]) + ' ')
    f.write('\n')