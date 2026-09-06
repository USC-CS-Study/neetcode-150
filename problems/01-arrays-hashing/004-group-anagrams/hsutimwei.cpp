class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> mp;
        for(auto s:strs)
        {
            string s1=s;
            sort(s1.begin(),s1.end());
            mp[s1].push_back(s);
        }
        vector<vector<string>> ans;
        for(auto &[m,p]:mp)
        {
            ans.push_back(p);
        }
        return ans;

    }
};
