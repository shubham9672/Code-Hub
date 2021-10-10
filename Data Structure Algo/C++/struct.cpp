#include <iostream>
#include <cmath>
using namespace std;

struct Point {
    int x = 0;
    int y = 0;
};

int dist(Point pt1, Point pt2) {
    int a = pt1.x - pt2.x;
    int b  = pt1.y - pt2.y;
    return sqrt(pow(a,2) + pow(b,2));
}

int main() {
    Point pt1;
    Point pt2;
    pt1.x = 12;
    pt1.y = 43;
    pt2.x = 32;
    pt2.y = 1;
    printf("%d", dist(pt1,pt2));
    return 0;
}
