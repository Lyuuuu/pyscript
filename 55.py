# -*- coding:utf-8 -*-
#基于小黄车的一点想法
#集卡算法

import random as ran


def easyCard():
	return ran.randint(1,4)


def f5():
	return ran.randint(1,5)


def f():
	flag = -1
	a = []
	while flag == -1:
		for i in range(4):
			a.append(easyCard())
		if 5 == f5():
			a.append(5)
			flag = 0
		else:
			flag = -1
	return a


if __name__ == "__main__":
	print(f())
