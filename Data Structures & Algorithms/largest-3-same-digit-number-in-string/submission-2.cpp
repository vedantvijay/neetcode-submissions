class Solution {
public:
    string largestGoodInteger(string num) {
        string max_ans = "";
        

        for (int i = 0; i + 2 < num.length(); i++) {

            if (num[i] == num[i+1] && num[i+1] == num[i+2]) {

                string current = num.substr(i, 3);

                if (current > max_ans) {
                    max_ans = current;
                }
            }
        }
        
        return max_ans;
    }
};