#include <iostream>
#include <string>
using namespace std;

int main(){
    string name = "";
    unsigned int age = 0;
    cout << "please enter your name?" << endl;
    cin >> name ;
    
    cout << "hello " << name << endl;
    cout << "how old are you?" << endl;
    cin >> age;
    if(!age > 0)
        age  = 0;
    cout << "You are " << age << " year(s) old." << endl;
    system("pause");
    return 0;
}
