#include <string>
#include <iostream>
using namespace std;

int main()
{
    string r = "FBUQIUUDSHOFJOEKHDQCUMYJXJXUIQCUAUOQDTKFBEQTJEBUQHDYDWYDPZK";
    for (int j = 0; j < 26; j++)
    {
        for (int i = 0; i < r.length(); i++)
        {
            r[i] = (r[i]-'A'+1)%26 +'A';
        }
        cout << r << endl;
    }
    //row 9
    //PLEASEENCRYPTYOURNAMEWITHTHESAMEKEYANDUPLOADTOLEARNINGINZJU
    //please encrypty your name with the same key and upload to learning in zju.
    //my name is wangzuobin
    string name = "WANGZUOBIN";
    for (int i = 0; i < name.length(); i++)
        {
            name[i] = (name[i]-'A'+16)%26 +'A';
        }
        cout << name << endl;
    //result = MQDWPKERYD
}