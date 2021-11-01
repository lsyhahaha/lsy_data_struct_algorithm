#include<iostream>
#include<stack>
using namespace std;
int main(){
    //初始化
    stack <string> s;
    stack <string> ss;
    // 函数在栈顶增加元素
    s.push("s");
    // 此函数用于将一个堆栈的内容与[另一个相同类型]的堆栈交换，但是大小可能会有所不同
    s.swap(ss);
    // 此函数用于将新元素插入堆栈容器，新元素添加到堆栈顶部
    s.emplace();
    cout << s.empty() << endl;
    cout << s.size() << endl;
    cout << s.top() << endl;

    return 0;
}