class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        output = []
        # minimum
        for i in range(len(count)):
            if count[i] > 0:
                output.append(float(i))
                break
        
        # maximum
        for m in range(len(count)-1,-1,-1):
            if count[m] > 0:
                output.append(float(m))
                break
        
        #mean
        summy = 0
        lenny = 0
        for m in range(len(count)):
            if count[m] > 0:
                summy += m * count[m]
                lenny += count[m]
        output.append(float(summy/lenny))
        
        #median
        counted = 0
        median = 0
        if lenny % 2 == 1:
            for m in range(len(count)):
                if count[m] > 0:
                    counted += count[m]
                    if lenny//2 < counted:
                        median = float(m)
                        break
            output.append(float(m))
        else:
            midl, midr = 0,0
            for m in range(len(count)):
                if count[m] > 0:
                    counted += count[m]
                    if lenny//2 < counted:
                        midr = m
                        break
            counted = 0
            for m in range(len(count)):
                if count[m] > 0:
                    counted += count[m]
                    if (lenny//2)-1 < counted:
                        midl = m
                        break
            output.append(float((midl+midr)/2))
            
        #mode
        output.append(float(count.index(max(count))))
        
        return output