public class Solution {
    public double AverageWaitingTime(int[][] customers) {
        double sum = 0;
        int start = customers[0][0];
        for (int i = 0; i < customers.Length; i++)
        {
            start = Math.Max(start, customers[i][0]);
            start += customers[i][1];
            sum += start - customers[i][0];
        }
        return sum / customers.Length;
    }
}