#include <iostream>
#include <string>
#include <vector>
using namespace std;

string FindStr(const string &str)
{
    string temp, MaxStr;
    int MaxLen = 0;
    for (int i = 0; i < str.length(); ++i)
    {
        for (int j = str.length() - i; j != 0; --j)
        {
            temp = str.substr(i, j);
            int front = str.find(temp);
            int behind = str.rfind(temp);
            int templen = temp.length();
            if (front != behind && templen > MaxLen)
            {
                MaxStr = temp;
                MaxLen = templen;
            }
        }
    }
    return MaxStr;
}

int main()
{
    string r = "ktbueluegvitnthuexmonveggmrcgxptlyhhjaogchoemqchpdnetxupbqntietiabpsmaoncnwvoutiugtagmmqsxtvxaoniiogtagmbpsmtuvvihpstpdvcrxhokvhxotawswquunewcgxptlcrxtevtubvewcnwwsxfsnptswtagakvoyyak";
    string t;
    t = r;
    //part 1 : find length
    for (string tmp = FindStr(t); tmp.length() > 2;)
    {
        cout << tmp;
        vector<int> m;
        string l = r;
        for (int i = l.find(tmp); i != -1;)
        {
            m.push_back(i + tmp.length());
            l.erase(0, i + tmp.length());
            i = l.find(tmp);
        }
        vector<int>::iterator ite = m.begin();
        for (; ite != m.end(); ite++)
        {
            cout << *ite << " ";
        }
        cout << endl;
        int pos = 0;
        while ((pos = t.find(tmp)) != -1)
        {
            t.erase(pos, tmp.length());
        }
        tmp = FindStr(t);
    }
    //gcd:3
    //part 2:compute frequency
    string ll = "";

    for (int j = 0; j < 3; j++)
    {
        string gg = "";
        for (int i = j; i < r.length(); i += 3)
        {
            gg += r[i];
        }
        cout << gg << endl;
        int cnt[256] = {};
        for (int i = 0; i < gg.size(); i++)
            cnt[(int)gg[i]]++;
        int max = 0;

        for (int i = 0; i < 256; i++) //输出字符出现次数
        {
            if (cnt[i] > cnt[max])
                max = i;
            if (cnt[i] != 0)
                cout << (char)i << ':' << cnt[i] << endl;
        }
        cout << "max" << (char)max << ':' << cnt[max] << endl;

        cout << "....................................." << endl;
    }
    //part 3
    string key[12] = { "cex", "csx", "ctx", "gex", "gsx", "gtx", "pex", "psx", "ptx", "vex", "vsx", "vtx" };

    for (int j = 0; j < 12; j++)
    {
        string res = r;
        for (int i = 0; i < res.length(); i++)
        {
            res[i] = (res[i] - (key[j][i % 3] - 'e') - 'a' + 26) % 26 + 'a';
        }
        cout << res << endl;
    }

    // It is essential to seek out enemy agents who have come to conduct espionage against you 
    //and to bribe them to serve you give them instruction sand care for them thus doubled agents are recruited and used suntzu the art of war
}