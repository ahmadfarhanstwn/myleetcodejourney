public class Solution {
    public int MinOperations(int[][] grid, int x) {
        List<int> a = new List<int>();
        for(int i = 0; i < grid.Length; i++){
            for(int j = 0; j < grid[i].Length; j++){
                a.Add(grid[i][j]);
            }
        }
        a.Sort();
        int median = a[a.Count/2];
        int output = 0;
        for(int z = 0; z < a.Count; z++){
            if (Math.Abs(median-a[z])%x == 0){
                output += Math.Abs(median-a[z])/x;
            } else{
                return -1;
            }
        }
        return output;
    }
}