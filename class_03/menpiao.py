# -*- coding: utf-8 -*-
import datetime
import time
"""
@Author:ZongShuRen
@Time:2021/6/26 20:05
"""
class Park:
    def __init__(self, price=100):
        self.price = price

    # 判断是否为工作日,工作日返回1，非工作日返回0
    def workDay(self):
        workTime = ['09:00:00', '18:00:00']
        dayOfWeek = datetime.datetime.now().weekday()
        # dayOfWeek = datetime.today().weekday()
        beginWork = datetime.datetime.now().strftime("%Y-%m-%d") + ' ' + workTime[0]
        endWork = datetime.datetime.now().strftime("%Y-%m-%d") + ' ' + workTime[1]
        beginWorkSeconds = time.time() - time.mktime(time.strptime(beginWork, '%Y-%m-%d %H:%M:%S'))
        endWorkSeconds = time.time() - time.mktime(time.strptime(endWork, '%Y-%m-%d %H:%M:%S'))
        if (int(dayOfWeek) in range(5)) and int(beginWorkSeconds) > 0 and int(endWorkSeconds) < 0:
            return 1
        else:
            return 0
    def cost_ticket(self):
        count = 0
        day = Park().workDay()
        man = input('请输入要购买的成人票')
        child = input('请输入要购买的儿童票')
        if day == 1:
            chengren = int(man)*self.price
            ertogn = int(child)*self.price*0.5
            count = chengren+ertogn
            print('总票价为{0}元'.format(count))

        elif day == 0:
            chengren = int(man) * 1.2 * self.price
            ertogn = int(child) * 1.2 * self.price * 0.5
            count = chengren + ertogn
            print('总票价为{0}元'.format(count))
        else:
            print('日期不详')
        return count



if __name__ == '__main__':
    b = Park().cost_ticket()
    print(b)