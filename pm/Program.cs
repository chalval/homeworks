/* Написать программу, которая из имеющегося массива строк формирует массив из строк,
длина которых меньше либо равна 3 символа. Первональный массив ввести с клавиатуры,
либо задать на старте выполнения алгоритма. При решении не рекомендуется пользоваться коллекциями,
лучше обойтись исключительно массивами.
Примеры:
["hello", "2", "world", ":-)"] -> ["2", ":-)"]
["1234", "1567", "-2", "computer science"] -> ["-2"]
["Russia", "Denmark", "Kazan"] -> [] */

void GetArray(string[] array1, string[] array2)
{
    int count = 0;
    for (int i = 0; i < array1.Length; i++)
    {
        if(array1[i].Length <= 3)
        {
            array2[count] = array1[i];
            count++;
        }
    }
}

void PrintArray(string[] array1, string[] array2)
{
    for (int i = 0; i < array2.Length; i++)
    {
        Console.Write($"{array2[i]}\t ");
    }
}

string[] matrix1 = new string[] {"hello", "2", "world", ":-)"};
string[] result1 = new string[matrix1.Length];

GetArray(matrix1, result1);
PrintArray(matrix1, result1);

// проверяю сразу все примеры, чтобы не перебивать их по очереди

Console.WriteLine();

string[] matrix2 = new string[] {"1234", "1567", "-2", "computer science"};
string[] result2 = new string[matrix2.Length];

GetArray(matrix2, result2);
PrintArray(matrix2, result2);

Console.WriteLine();

string[] matrix3 = new string[] {"Russia", "Denmark", "Kazan"};
string[] result3 = new string[matrix3.Length];

GetArray(matrix3, result3);
PrintArray(matrix3, result3);