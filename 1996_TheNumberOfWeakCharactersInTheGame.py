class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0],x[1]))
        strongest = 0
        pointer = 1
        weak = 0
        while pointer < len(properties) and strongest < len(properties):
            if properties[strongest][0] > properties[pointer][0] and properties[strongest][1] > properties[pointer][1]:
                weak += 1
                pointer += 1
            else:
                strongest = pointer
                pointer += 1
        return weak