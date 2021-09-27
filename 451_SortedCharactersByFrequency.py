class Solution:
    def frequencySort(self, s: str) -> str:
        county = sorted(dict(collections.Counter(s)).items(), key= lambda x : -x[1])
        output = ''
        for i in county:
            output += i[0] * i[1]
        return output