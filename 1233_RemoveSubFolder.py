class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        withoutSubFolder = [folder[0]]
        i, x = folder[0]+'/', len(folder[0])+1
        for z in folder[1:]:
            if z[:x] != i:
                withoutSubFolder.append(z)
                i, x = z+'/', len(z)+1
        return withoutSubFolder