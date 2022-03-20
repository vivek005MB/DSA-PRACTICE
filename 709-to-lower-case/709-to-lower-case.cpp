class Solution {
public:
    string toLowerCase(string s) {
        string ans = s;
        int offset = 'a' - 'A'; //for python it was ord('a') - ord('A')
        for(int i=0;i < s.size(); i++){
            if(ans[i] >= 'A' && ans[i] <= 'Z'){
                ans[i] = ans[i] + offset;
            }
        }
        return ans;
        
    }
};