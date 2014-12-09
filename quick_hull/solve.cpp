#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

int n;
struct point
{
    int x,y;
    point(){}
    void input()
    {
        cin>>x>>y;
    }
};
const double eps = 1e-8;
double Fabs(double a)
{
    if (a<0)
        return -a;
    return a;
}
bool Equal(double a, double b)
{
    return Fabs(a-b) <= eps;
}
bool Less(double a, double b)
{
    return !Equal(a,b) && a<b;
}
struct line
{
    int a, b, c;
    line(){}
    line(point f, point s)
    {
        a = s.y - f.y;
        b = f.x - s.x;
        c = -(a*f.x + b*f.y);
    }
    double dist(const point &p)
    {
        return Fabs(a*p.x + b*p.y + c)/sqrt((double)a*a + b*b);
    }
    bool isLeft(const point &p)
    {
        return a*p.x + b*p.y + c < 0;
    }
    bool isRight(const point &p)
    {
        return a*p.x + b*p.y + c > 0;
    }
};
vector<point> vertex;

void input()
{
    cin>>n;
    vertex.resize(n);
    for (int i=0;i<n;i++)
        vertex[i].input();
}
void GetPointsLeftByLine(const vector<point> &vertex,  const vector<int> &setPoints,
                         line &LINE, vector<int> &leftSetPoints)
{
    for (size_t i=0;i<setPoints.size();i++)
    {
        if (LINE.isLeft(vertex[setPoints[i]]))
            leftSetPoints.push_back(setPoints[i]);
    }
}
void QuickHull(const vector<point> &vertex, vector<int> &convexHull,
               int leftPos, int rightPos, const vector<int> &setPoints)
{
    if (setPoints.size() == 0)
    {
        convexHull.push_back(rightPos);
        return ;
    }
    line LR(vertex[leftPos],vertex[rightPos]);
    // Находим точку, наиболее удаленную от прямой LR

    int topPos = setPoints[0];
    line topLine = line(vertex[leftPos],vertex[topPos]);
    double maxDist = LR.dist(vertex[topPos]);

    for (size_t i=1;i<setPoints.size();i++)
    {
        if (setPoints[i] != leftPos && setPoints[i] != rightPos)
        {
            double curDist = LR.dist(vertex[setPoints[i]]);
            // равноудаленные точки
            if (Equal(maxDist,curDist))
            {
                // но угол у новой точки больше
                if (topLine.isLeft(vertex[setPoints[i]]))
                {
                    topPos = setPoints[i];
                    topLine = line(vertex[leftPos],vertex[topPos]);
                }
            }
            if (Less(maxDist,curDist))
            {
                maxDist = curDist;
                topPos = setPoints[i];
                topLine = line(vertex[leftPos],vertex[topPos]);
            }
        }
    }

    vector<int> S11;
    line LT = line(vertex[leftPos],vertex[topPos]);
    // формируем множество точек, находящихся слева от прямой LT
    GetPointsLeftByLine(vertex,setPoints,LT,S11);
    QuickHull(vertex, convexHull,leftPos,topPos,S11);

    vector<int> S12;
    line TR = line(vertex[topPos],vertex[rightPos]);
    // формируем множество точек, находящихся слева от прямой TR
    GetPointsLeftByLine(vertex, setPoints,TR,S12);
    QuickHull(vertex, convexHull, topPos, rightPos, S12);
}

void QuickHull(const vector<point> &vertex, vector<int> &convexHull)
{
    // нельзя построить выпуклую оболочку
    if (vertex.size() < 3)
        return;
    // поиск самой левой и самой правой точки
    int leftPos = 0, rightPos = 0;
    for (size_t i=1;i<vertex.size();i++)
    {
        if (Less(vertex[i].x, vertex[leftPos].x))
            leftPos = i;
        else if(Less(vertex[rightPos].x, vertex[i].x))
            rightPos = i;
    }

    line LR(vertex[leftPos],vertex[rightPos]);
    vector<int> S1; // точки выше прямой LR
    vector<int> S2; // точки ниже прямой LR
    for (size_t i=0;i<vertex.size();i++)
    {
        if (i != leftPos && i != rightPos)
        {
            if (LR.isLeft(vertex[i]))
                S1.push_back(i);
            else if (LR.isRight(vertex[i]))
                S2.push_back(i);
        }
    }
    QuickHull(vertex, convexHull, leftPos, rightPos, S1);
    QuickHull(vertex, convexHull, rightPos, leftPos, S2);
}
double dist(const point &a,const point &b)
{
    return sqrt((double)(a.x - b.x)*(a.x - b.x) + (a.y - b.y)*(a.y-b.y));
}
double findP(const vector<point> &vetex,const vector<int> &convexHull)
{
    double res = 0;
    for (size_t i=0;i<convexHull.size();i++)
        res += dist(vertex[convexHull[i]],
                    vertex[convexHull[(i+1)%convexHull.size()]]);
    return res;
}
void solve()
{
    vector<int> convexHull;
    QuickHull(vertex, convexHull);
    printf("%0.1f",findP(vertex, convexHull));
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    input();
    solve();
    return 0;
}