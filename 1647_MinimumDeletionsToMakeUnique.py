class Solution:
    def minDeletions(self, s: str) -> int:
        output = 0
        sett = set()
        nums = sorted(list(dict(collections.Counter(s)).values()), reverse = True)
        while len(nums) > 0:
            b = nums.pop(0)
            if b not in sett:
                sett.add(b)
            else:
                while b > 0:
                    b -= 1
                    output += 1
                    if b not in nums and b not in sett:
                        sett.add(b)
                        break
        return output