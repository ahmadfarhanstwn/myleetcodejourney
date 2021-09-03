class Solution:
    def reformatDate(self, date: str) -> str:
        monthDict = {
            "Jan" : '01', 
            "Feb" : '02', 
            "Mar" : '03', 
            "Apr" : '04', 
            "May" : '05', 
            "Jun" : '06', 
            "Jul" : '07', 
            "Aug" : '08', 
            "Sep" : '09', 
            "Oct" : '10', 
            "Nov" : '11', 
            "Dec" : '12'
        }
        if len(date) == 13:
            return date[9:] + '-' + monthDict[date[5:8]] + '-' + date[:2]
        else:
            return date[8:] + '-' + monthDict[date[4:7]] + '-0' + date[:1]