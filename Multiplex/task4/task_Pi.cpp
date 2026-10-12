#include <mpi.h>
#include <stdio.h>
#include <iostream>
#include <fstream>

double func(double x)
{
    return 4.0 / (1.0 + x * x);
}

int main(int argc, char *argv[])
{
    int e = MPI_Init(&argc, &argv);

    if (e != MPI_SUCCESS)
    {
        std::cout << "Ошибка подключения MPI" << std::endl;
        return 1;
    }

    int rank;

    e = MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    if (e != MPI_SUCCESS)
    {
        std::cout << "Ошибка получения номера процесса" << std::endl;

        MPI_Abort(MPI_COMM_WORLD, e);
        return 1;
    }

    int size;

    e = MPI_Comm_size(MPI_COMM_WORLD, &size);
    if (e != MPI_SUCCESS)
    {
        std::cout << "Ошибка получения числа процессоров" << std::endl;

        MPI_Abort(MPI_COMM_WORLD, e);
        return 1;
    }

    int N;
    MPI_Status status;

    if (rank == 0)
    {
        std::ifstream file("N.dat");
        if (file.is_open())
        {
            file >> N;
            file.close();
        }

        else
        {
            std::cerr << "Ошибка чтения файла N.dat, базовое значение: N = 1000000" << std::endl;
            N = 1000000;
            MPI_Abort(MPI_COMM_WORLD, 1);
            return 1;
        }

        for (int i = 1; i < size; i++)
        {
            int e = MPI_Send(&N, 1, MPI_INT, i, 1, MPI_COMM_WORLD);
            if (e != MPI_SUCCESS)
            {
                MPI_Abort(MPI_COMM_WORLD, e);
                return 1;
            }
        }
    }

    else
    {
        int e = MPI_Recv(&N, 1, MPI_INT, 0, 1,
                         MPI_COMM_WORLD, &status);

        if (e != MPI_SUCCESS)
        {
            MPI_Abort(MPI_COMM_WORLD, e);
            return 1;
        }
    }

    int block = N / size;
    int begin = rank * block;
    int end = (rank == size - 1) ? N : (rank + 1) * block;

    double h = 1.0 / N;
    double local_sum = 0.0;

    for (int i = begin; i < end; i++)
    {
        double x1 = i * h;
        double x2 = (i + 1) * h;
        local_sum += h * (func(x1) + func(x2)) / 2.0;
    }

    if (rank == 0)
    {
        double sum = local_sum;
        for (int i = 1; i < size; i++)
        {
            double part;
            int e = MPI_Recv(&part, 1, MPI_DOUBLE, i, 2, MPI_COMM_WORLD, &status);
            if (e != MPI_SUCCESS)
            {
                MPI_Abort(MPI_COMM_WORLD, e);
                return 1;
            }

            sum += part;
        }

        std::cout << "N = " << N << " " << "количество процессов: " << size << std::endl;
        std::cout << "PI = " << sum << std::endl;
    }

    else
    {
        int e = MPI_Send(&local_sum, 1, MPI_DOUBLE, 0, 2,
                         MPI_COMM_WORLD);
        if (e != MPI_SUCCESS)
        {
            MPI_Abort(MPI_COMM_WORLD, e);
            return 1;
        }
    }

    e = MPI_Finalize();
    if (e != MPI_SUCCESS)
    {
        return 1;
    }

    return 0;
}