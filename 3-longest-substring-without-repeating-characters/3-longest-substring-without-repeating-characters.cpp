class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int len = s.length();
        int result = 0;
        int check[256];
        for(int i=0;i<len;i++){
            memset(check,0,sizeof(check));
            int j=i;
            for(;j<len;j++){
                if(check[s[j]]){
                    break;
                }
                check[s[j]] = 1;
            }
            if((j-i)>result){
                result = j-i;
            }
        }
        return result;
    }
};