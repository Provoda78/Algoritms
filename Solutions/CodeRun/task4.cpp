#include <iostream>
#include <vector>

long long a, b;
long long M;

struct Matrix
{
    long long a;
    long long b;
    long long c;
    long long d;

    Matrix(long long a, long long b, long long c, long long d) : a(a), b(b), c(c), d(d) {}

    Matrix operator*(const Matrix &other)
    {
        return Matrix((a * other.a + b * other.c) % M,
                      (a * other.b + b * other.d) % M,
                      (c * other.a + d * other.c) % M,
                      (c * other.b + d * other.d) % M);
    }
};

Matrix power(Matrix A, long long p)
{
    Matrix res(1, 0, 0, 1);

    while (p > 0)
    {
        if (p % 2 != 0)
        {
            res = res * A;
        }
        A = A * A;
        p >>= 1;
    }
    return res;
}

void approxmate()
{
    long long x, y, n;
    std::cin >> x >> y >> n;

    if (n == 0)
    {
        std::cout << ((x % M + M) % M) << "\n";
        return;
    }
    if (n == 1)
    {
        std::cout << ((y % M + M) % M) << "\n";
        return;
    }

    Matrix mat = Matrix(a, b, 1, 0);
    Matrix suf = power(mat, n - 1);

    long long Fn = (suf.a * y + suf.b * x) % M;

    std::cout << Fn << "\n";
}

int main()
{
    // Помогите мне...

    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::cin >> a >> b;
    std::cin >> M;
    int q;
    std::cin >> q;

    for (int i = 0; i < q; i++)
    {
        approxmate();
    }

    return 0;
}