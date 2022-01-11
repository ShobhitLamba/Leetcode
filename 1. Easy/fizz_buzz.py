class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for num in range(1, n + 1):
            curr = ""
            if num % 3 == 0:
                curr += "Fizz"
            if num % 5 == 0:
                curr += "Buzz"
            if not curr:
                curr = str(num)
            ans.append(curr)

        return ans    
