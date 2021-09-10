class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        filtered = []
        for i in restaurants:
            if i[2] >= veganFriendly and i[3] <= maxPrice and i[4] <= maxDistance:
                filtered.append((i[1], i[0]))
        
        filtered = sorted(filtered, reverse=True)
        return [r[1] for r in filtered]