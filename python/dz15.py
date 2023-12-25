import logging
import sys

logging.basicConfig(filename='transpose.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

def transpose(matrix):
    transposed_matrix = []
    try:
        for i in range(len(matrix[0])):
            tt = []
            for j in range(len(matrix)):
                tt.append(matrix[j][i])
            transposed_matrix.append(tt)

        # запись полезной информации в лог-файл
        logging.debug('Матрица успешно транспонирована')
    except Exception as e:
        # запись ошибки в лог-файл
        logging.error(f'Ошибка при транспонировании матрицы: {e}')

    return transposed_matrix


if __name__ == '__main__':
    # проверка наличия переданных параметров
    if len(sys.argv) > 1:
        # первый параметр - имя файла с матрицей, остальные параметры (если есть) - значения элементов матрицы
        filename = sys.argv[1]
        matrix = []

        try:
            # чтение матрицы из файла
            with open(filename, 'r') as f:
                for line in f.readlines():
                    matrix.append([int(x) for x in line.split()])

            # транспонирование матрицы
            transposed_matrix = transpose(matrix)

            # вывод результата
            print('Транспонированная матрица:')
            for row in transposed_matrix:
                print(row)
        except Exception as e:
            # запись ошибки в лог-файл
            logging.error(f'Ошибка при чтении матрицы из файла: {e}')
    else:
        print('Необходимо передать имя файла с матрицей в качестве параметра командной строки')


# python dz15.py matrix.txt

