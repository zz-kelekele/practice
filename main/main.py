#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/8 20:12
@Author  : zz
@File    : main.py.py
@Software: PyCharm
@Desc    : 运行测试
"""
import math


def coin_change(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    coins = [186, 419, 83, 408]
    amount = 6249
    result = coin_change(coins, amount)
    print(result)
