#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

struct Num
{
    Num() {}
    Num(int x_) : x(x_) {}

    int x;
};



bool isLess(const Num &lhs, const Num &rhs)
{
    return (lhs.x < rhs.x);
}

bool operator <(const vector<Num> &lhs, const vector<Num> &rhs)
{
    return std::lexicographical_compare(lhs.begin(), lhs.end(),
                                        rhs.begin(), rhs.end(),
                                        isLess);
}

bool isLess2D(const vector<vector<Num> > &lhs, const vector<vector<Num> > &rhs)
{
    return std::lexicographical_compare(lhs.begin(), lhs.end(),
                                        rhs.begin(), rhs.end());
}

int main(int argc, char *argv[])
{
    cout << "Hello, World!\n";

    {
        vector<Num> a(10, 0), b(10, 1), c(10, 2);
        vector<vector<Num> > a2d(2, a), b2d(2, b);
        cout << isLess2D(b2d, a2d) << endl;
    }

    return EXIT_SUCCESS;
}
