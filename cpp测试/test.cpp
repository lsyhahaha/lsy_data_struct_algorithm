#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
#include<stack>
#include<cstring>
#include<unordered_map>
using namespace std;


class Solution {
public:
    int maxArea(vector<int>& height) {
        int ret = 0;
        int i = 0;
        int n = height.size();
        int j = n - 1;
        while(i < j) {
            ret = max(ret, (j - i)*min(height[i], height[j]));
            int i_1 = i, i_2 = i + 1;
            int j_1 = j -1, j_2 = j;
            if (min(height[i+1], height[j]) > min(height[i], height[j-1])){
                i++;
            }else{
                j--;
            }
        }

        return ret;
    }
};

int main(){
    system("cls");
    Solution a;
    //输入数据
    vector<int> nums = {1,3,2,5,25,24,5};
    // string s = "()[]{}";
    //执行核心函数
    int ret = 0;
    ret = a.maxArea(nums);
    //输出结果
    cout << ret << endl;

    return 0;
}