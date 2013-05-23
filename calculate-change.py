#!/usr/bin/python

def calculateChange(total, coins, sofar=""):
	for each_coin in coins:
		if each_coin == total:
			print(sofar + str(each_coin))
		elif each_coin > total:
			return ""
		else:
			calculateChange(total - each_coin, coins, sofar + str(each_coin))

calculateChange(10, [2,3,4,5])

