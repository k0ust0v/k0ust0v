#include<iostream>
#include<vector>
void printSubsequences(const std::vector<int>& a, std::vector<int>& b, int index) {
    if(index < 0) {
        for(int i = 0; i < b.size(); ++i) {
            std::cout<<b[i]<<",";
        }
        std::cout<<std::endl;
        return;
    }
    b.push_back(a[index]);
    printSubsequences(a, b, index - 1);

    b.pop_back();
    printSubsequences(a, b, index - 1);
}



int main() {
    std::vector<int> a{1, 3, 4, 5};
    std::vector<int> b;
    printSubsequences(a, b, a.size() - 1);
    return 0;
}