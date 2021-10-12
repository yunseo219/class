money = 17579
Coins = 23,6,5,3,1

def DPChange(money, Coins):
    MinNumCoins = [0]
    for m in range(1, money + 1):
        MinNumCoins.append(money + 1) #infinite
        for coin in Coins:
            if m >= coin:
                if MinNumCoins[m - coin] + 1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m - coin] + 1
    return MinNumCoins[money]

print(DPChange(money, Coins))