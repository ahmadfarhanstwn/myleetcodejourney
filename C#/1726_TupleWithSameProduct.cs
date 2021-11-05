public class Solution {
    public int TupleSameProduct(int[] nums) {
        Dictionary<int,int> dick = new Dictionary<int,int>();
        int output = 0, product = 0, sum = 0;
        for(int i = 0; i < nums.Length;i++){
            for(int j = i+1; j < nums.Length; j++){
                product = nums[i] * nums[j];
                if (dick.ContainsKey(product)){
                    dick[product] += 1;
                } else{
                    dick.Add(product, 1);
                }
            }
        }
        foreach(KeyValuePair<int,int> key in dick){
            if (key.Value > 0){
                sum = key.Value - 1;
                while(sum > 0){
                    output += 8 * sum;
                    sum--;
                }
            }
        }
        return output;
    }
}