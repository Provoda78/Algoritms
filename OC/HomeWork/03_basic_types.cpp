// Day 2. (1) Типы данных, ввод/вывод.

/*
Задание:
1) Вывести размер типов char, int, float, double
2) Создать переменную типа char
3) Приравнять новой переменной значение a, посмотреть на результат.
*/

#include <iostream>

int main()
{
	int a = 54377;
	char b;

	std::cout << "type of a is " << typeid(a).name() << std::endl;
	std::cout << "value of a is " << a << '\n';
	std::cout << "size of a is " << sizeof(a) << '\n';
	std::cout << '\n';
	std::cout << "size of char is " << sizeof(char) << '\n';
	std::cout << "size of int is " << sizeof(int) << '\n';
	std::cout << "size of float is " << sizeof(float) << '\n';
	std::cout << "size of double is " << sizeof(double) << '\n';
	b = a;
	std::cout << "Результат: " << b << '\n';
}
