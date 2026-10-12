#include <mpi.h>
#include <stdio.h>

double f(double x)
{
    return 4.0 / (1.0 + x * x);
}

int main(int argc, char *argv[])
{
    int error = MPI_Init(&argc, &argv);
    if (error != MPI_SUCCESS)
        return 1;

    int rank, size;

    error = MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    if (error != MPI_SUCCESS)
    {
        MPI_Abort(MPI_COMM_WORLD, error);
        return 1;
    }

    error = MPI_Comm_size(MPI_COMM_WORLD, &size);
    if (error != MPI_SUCCESS)
    {
        MPI_Abort(MPI_COMM_WORLD, error);
        return 1;
    }

    int N;
    MPI_Status status;

    // Процесс 0 читает N и рассылает остальным.
    if (rank == 0)
    {
        FILE *file = fopen("N.dat", "r");
        if (file == NULL)
        {
            printf("Не удалось открыть N.dat\n");
            MPI_Abort(MPI_COMM_WORLD, 1);
            return 1;
        }

        int read = fscanf(file, "%d", &N);
        fclose(file);

        if (read != 1 || N <= 0)
        {
            printf("Неверное значение N\n");
            MPI_Abort(MPI_COMM_WORLD, 1);
            return 1;
        }

        for (int p = 1; p < size; p++)
        {
            error = MPI_Send(&N, 1, MPI_INT, p, 1,
                             MPI_COMM_WORLD);
            if (error != MPI_SUCCESS)
            {
                MPI_Abort(MPI_COMM_WORLD, error);
                return 1;
            }
        }
    }
    else
    {
        error = MPI_Recv(&N, 1, MPI_INT, 0, 1,
                         MPI_COMM_WORLD, &status);
        if (error != MPI_SUCCESS)
        {
            MPI_Abort(MPI_COMM_WORLD, error);
            return 1;
        }
    }

    // Границы своего участка.
    int block = N / size;
    int begin = rank * block;
    int end = (rank == size - 1) ? N : (rank + 1) * block;

    // Считаем площади трапеций на своём участке.
    double h = 1.0 / N;
    double local_sum = 0.0;

    for (int i = begin; i < end; i++)
    {
        double x1 = i * h;
        double x2 = (i + 1) * h;
        local_sum += h * (f(x1) + f(x2)) / 2.0;
    }

    // Собираем частичные суммы у процесса 0.
    if (rank == 0)
    {
        double sum = local_sum;

        for (int p = 1; p < size; p++)
        {
            double part;
            error = MPI_Recv(&part, 1, MPI_DOUBLE, p, 2,
                             MPI_COMM_WORLD, &status);
            if (error != MPI_SUCCESS)
            {
                MPI_Abort(MPI_COMM_WORLD, error);
                return 1;
            }

            sum += part;
        }

        printf("N = %d, процессов = %d\n", N, size);
        printf("pi = %.15f\n", sum);
    }
    else
    {
        error = MPI_Send(&local_sum, 1, MPI_DOUBLE, 0, 2,
                         MPI_COMM_WORLD);
        if (error != MPI_SUCCESS)
        {
            MPI_Abort(MPI_COMM_WORLD, error);
            return 1;
        }
    }

    error = MPI_Finalize();
    if (error != MPI_SUCCESS)
        return 1;

    return 0;
}