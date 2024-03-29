# **Итоговая проверочная работа.**

Данная работа необходима для проверки знаний и навыков по итогу прохождения первого блока обучения на программе разработчик.

Для полноценного выполнения проверочной работы необходимо:

1. Создать репозиторий на GitHub
2. Нарисовать блок-схему алгоритма (можно обойтись блок-схемой основной содержательной части, если вы выделяете её в отдельный метод)
3. Снабдить репозиторий оформленным текстовым описанием решения (файл README.md)
4. Написать прграмму, решающую поставленную задачу
5. Использовать контроль версий в работе над этим небольшим проектом (не должно быть так что всё залито одним коммитом, как минимум этапы 2, 3 и 4 должны быть расположены в разных коммитах)

## **Задача**:

Написать программу, которая из имеющегося массива строк формирует массив из строк,
длина которых меньше либо равна 3 символа. Первональный массив ввести с клавиатуры,
либо задать на старте выполнения алгоритма. При решении не рекомендуется пользоваться коллекциями,
лучше обойтись исключительно массивами.

## **Примеры**:

["hello", "2", "world", ":-)"] -> ["2", ":-)"]

["1234", "1567", "-2", "computer science"] -> ["-2"]

["Russia", "Denmark", "Kazan"] -> []


## Решение задачи:

Для решения задачи, необходимо написать программу, состоящую из двух методов. 

В первом задаём два массива строк, первый из которых будет содержать строки с различной длиной (колличеством символов), а второй будет заполняться строками с длиной в 3 символа после соответствующей проверки:

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

Второй метод отвечает за вывод получившегося (второго) массива:

    void PrintArray(string[] array1, string[] array2)
    {
        for (int i = 0; i < array2.Length; i++)
        {
            Console.Write($"{array2[i]}\t ");
        }
    }

Необходимо задать эти два массива:

    string[] matrix1 = new string[] {"hello", "2", "world", ":-)"};
    string[] result1 = new string[matrix1.Length];.


Вызываем методы следующим образом:

    GetArray(matrix1, result1);
    PrintArray(matrix1, result1);