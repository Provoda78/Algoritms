// Day 3. Функции.
/*--------------------------------------------------------
Задание:
1) Изучите пример определения и вызова функции.
2) Какой тип имеет var?
--------------------------------------------------------*/

#include <iostream>

int example_foo(int a, int b)
{
	std::cout << "cout from example_foo\n";
	return a + b;
}

int main()
{
	std::cout << "main begin\n";
	auto var = example_foo(1, 3);
	std::cout << var << '\n';
	std::cout << typeid(var).name() << '\n';
	std::cout << "main end\n";
}
