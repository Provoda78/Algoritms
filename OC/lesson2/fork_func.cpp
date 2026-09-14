#include <sys/types.h>
#include <unistd.h>
#include <iostream>

using namespace std;

int main()
{
    pid_t pid = fork();

    std::cout << getpid() << endl;
    std::cout << getppid() << endl;

    try
    {
        while (true)
        {
            continue;
        }
    }

    catch (const std::exception &e)
    {
        std::cout << "Ручная остановка" << endl;
        std::cerr << e.what() << '\n';
    }

    if (pid > 0)
    {
        std::cout << "parent" << endl;
    }

    else if (pid == 0)
    {
        std::cout << "child" << endl;
    }

    return 0;
}