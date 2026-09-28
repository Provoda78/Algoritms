// Day 2. (3) Использование cmath.

/*
Задание:
1) Изменить программу на расчет синуса градусов, а не радиан.
2) Выяснить какой тип имеет 'sin_v'.

Комментарий: Число 'пи' задано именем M_PI в cmath.
*/

// на каких-то компиляторах необходимо
// определять _USE_MATH_DEFINES для работы констант
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <typeinfo>

int main()
{
	double a_deg;
	std::cout << "a(deg) = ";
	std::cin >> a_deg;

	double a_rad = a_deg * M_PI / 180.0;
	auto sin_v = std::sin(a_rad);

	std::cout << "sin(a) = " << sin_v << '\n';
	std::cout << "type of sin_v: " << typeid(sin_v).name() << '\n';
}
