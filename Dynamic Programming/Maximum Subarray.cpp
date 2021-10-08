//Input : [5,4,-1,7,8]
//output: 23

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_so_far=nums[0];
        int curr_sum=nums[0];
        for(int i=1;i<nums.size();i++){
            curr_sum=max(nums[i],curr_sum+nums[i]);
            if(curr_sum>max_so_far){
                max_so_far=curr_sum;
            }
        }
        return max_so_far;
    }
};
