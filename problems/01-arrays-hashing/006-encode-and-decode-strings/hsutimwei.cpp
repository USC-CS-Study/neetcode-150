class Solution {
public:

    string encode(vector<string>& strs) {
        string s1;
        for(auto &s:strs)
        {   
            s1+=s;
            s1+=char(-1);
        }
        return s1;
    }

    vector<string> decode(string s) {
        vector<string> ans;
        string s1;
        for(auto &c:s)
        {   
            if(c==-1)
            {
                ans.push_back(s1);
                s1.clear();
            }
            else
            {
                s1+=c;
            }
        }
        return ans;
    }
};