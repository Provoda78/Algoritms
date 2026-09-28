// Day 3. Случайные числа.
/*--------------------------------------------------------
Задание:
1) Изучите работу функции std::rand();
2) Изучите механизм вычисления случайного числа с плавающей точкой.
3) Какого типа переменная d?
4) Какой тип и значение имеет RAND_MAX?
5) Создайте функцию, возвращающую случайное число с плавающей точкой.
6) Создайте функцию, возвращающее случайное число с плавающей точкой,
	из заданного диапазона;
--------------------------------------------------------*/

#include <iostream>
#include <cstdlib> // std::rand() живет тут
#include <typeinfo>

double random_float()
{
	return static_cast<double>(std::rand()) / static_cast<double>(RAND_MAX);
}

double random_float_range(double min, double max)
{
	return min + (max - min) * random_float();
}

int main()
{
	std::srand(10); // Установка seed для псевдослучайного генератора.

	std::cout << "random i value: " << std::rand() << '\n';
	std::cout << "random i value: " << std::rand() << '\n';
	std::cout << "random i value: " << std::rand() << '\n';
	std::cout << "random i value: " << std::rand() << '\n';

	auto d = std::rand() / static_cast<double>(RAND_MAX);

	std::cout << "random d value: " << d << '\n';
	std::cout << "type of d: " << typeid(d).name() << '\n';
	std::cout << "RAND_MAX type: " << typeid(RAND_MAX).name() << '\n';
	std::cout << "RAND_MAX value: " << RAND_MAX << '\n';

	std::cout << "random float: " << random_float() << '\n';
	std::cout << "random float in [2, 5): " << random_float_range(2.0, 5.0) << '\n';
}
