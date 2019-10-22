class Solution:
    @staticmethod
    def max_selling_price(length_of_rod, price_of_each_length):
        length_array = [i for i in range(length_of_rod+1)]
        price_of_each_length.insert(0, 0)
        dp = [price_of_each_length[i] for i in range(lenght_of_rod+1)]

        for i in range(1, length_of_rod+1):
            for j in range(i+1, length_of_rod+1):
                dp[j] = max(price_of_each_length[i]+dp[j-i], dp[j])
        
        return dp[-1]

if __name__=="__main__":
    t = int(input())

    while t>0:
        t-=1

        lenght_of_rod = int(input())
        price_of_each_length = list(map(int, input().strip().split()))

        print(Solution.max_selling_price(lenght_of_rod, price_of_each_length))