// Day 2. (4) Основы указателей.

/*
Задание (3):
1) Изучить работу программы.
2) Создать переменную типа float.
3) Созать указатель на новую переменную.
4) Изменить переменную, через указатель.
*/

#include <iostream>

int main()
{
	int a = 10;
	int *ptr = &a; // Инициализация указателя адресом 'a'

	float b = 52.2;
	float *ptr_f = &b;

	std::cout << "value of a = " << *ptr << '\n';
	std::cout << "address of a = " << ptr << '\n';

	*ptr = 1; // Изменяется значение
	std::cout << "new value of a = " << a << '\n';

	ptr += 1; // Изменяется указатель (!!!)
	std::cout << "??? = " << *ptr << '\n';

	std::cout << '\n';
	std::cout << "value of b = " << *ptr_f << '\n';
	std::cout << "address of b = " << ptr_f << '\n';

	*ptr_f = 42.2;
	std::cout << "new value of b = " << b << '\n';
}
