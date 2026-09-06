class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        for(auto n:nums)
        {
            mp[n]++;
        }
        map<int,vector<int>,greater<int>> mp2;
        for(auto &[m,p]:mp)
        {
            mp2[p].push_back(m);
        }
        vector<int> ans;
        for(auto &[m,p]:mp2)
        {
            for(auto n:p)
            {
                ans.push_back(n);
                k--;
            }
            
            if(k==0)
                break;
        }
        return ans;
    }
};
