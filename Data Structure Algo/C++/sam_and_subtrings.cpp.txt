/** Sam and substrings
    https://www.hackerrank.com/challenges/sam-and-substrings/problem
*/

#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'substrings' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING n as parameter.
 */

long long substrings(string n) {
    long long sum = 0;
    long curelem;
    long mod = 1000000007;
    long long ones = 1;
    for (long i = n.size () -1 ; i >=0; --i) {
        curelem = n[i] - '0';
        sum += ((curelem * (i + 1) * ones)% 1000000007) ;
        ones = ((ones * 10) + 1) % mod;
        sum %= 1000000007;
    }
    return sum;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n;
    getline(cin, n);

    long long result = substrings(n);

    fout << result << "\n";

    fout.close();

    return 0;
}