class Solution:
    def maximumTime(self, time: str) -> str:
        if time[0] == '?':
            if time[1] == '0' or time[1] == '1' or time[1] == '2' or time[1] == '3' or time[1] == '?':
                time = '2' + time[1:]
            else:
                time = '1' + time[1:]
        if time[1] == '?':
            if time[0] == '0' or time[0] == '1':
                time = time[:1] + '9' + time[2:]
            else:
                time = time[:1] + '3' + time[2:]
        if time[3] == '?':
            time = time[:3] + '5' + time[4:]
        if time[4] == '?':
            time = time[:4] + '9'
        return time