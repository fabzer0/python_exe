def recMc(coin_value_list, change):
    min_coins = change
    if change in coin_value_list:
        return 1
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + recMc(coin_value_list, change-1)
            if num_coins < min_coins:
                min_coins = num_coins
        return min_coins

print(recMc([1,5,10,25],63))
