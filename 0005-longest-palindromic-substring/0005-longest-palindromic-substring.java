class Solution {
    public String longestPalindrome(String s) {

        int resLen = 0;
        String res = "";

        if(s.length() < 2){
            return s;
        }

        for(int i = 0; i < s.length(); i++){
            int l = i;
            int r = i;

            while(l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)){
                if ( r - l + 1 > resLen){
                    resLen = r - l + 1;
                    res = s.substring(l, r + 1);
                }
                l -= 1;
                r += 1;
            }

            l = i;
            r = i + 1;

            while(l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)){
                if ( r - l + 1 > resLen){
                    resLen = r - l + 1;
                    res = s.substring(l, r + 1);
                }
                l -= 1;
                r += 1;
            }


        }

        return res;
        
        
    }
}