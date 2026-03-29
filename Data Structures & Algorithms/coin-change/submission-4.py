class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        elif amount < coins[0]:
            return -1
        arr = [-1] * (amount + 1)
        arr[0] = 0
        for i in coins:
            if i < len(arr):
                arr[i] = 1
        
        for i in range(len(arr)):
            if i < coins[0]:
                continue
            min_coins = 10**6 if arr[i] == -1 else arr[i]
            for j in range(len(coins)):
                prev_amt = i - coins[j]
                if prev_amt >= 0 and arr[prev_amt] != -1:
                    min_coins = min(min_coins, arr[prev_amt] + 1)
            arr[i] = min_coins if min_coins != 10**6 else -1
        print(arr)
        return arr[amount]
                    