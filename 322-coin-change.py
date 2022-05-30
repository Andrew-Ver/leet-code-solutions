'''
    https://leetcode.com/problems/coin-change/
'''


def coinChange(coins: list[int], amount: int) -> int:
    coins.sort()
    
    
    for i in range(len(coins)):
        coins_required = 0
        for coin in coins[i:]:
            d, m = divmod(amount, coin)
            print(f'coin: {coin}. Even division: {d}, remainder: {m}, amount left: {amount}')
            coins_required += d
            amount = m
            if amount == 0:
                return coins_required

    if amount:
        return -1
    
    return coins_required
    

print(coinChange([186,419,83,408], 6249))