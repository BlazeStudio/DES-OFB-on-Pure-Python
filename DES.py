import PySimpleGUI as sg
#Таблицы DES
#Матрица начальной перестановки IP
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Таблица первоначальной подготовки ключа
P_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# Таблица сдвигов
Shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Матрица завершающей обработки ключа
P_2 = [14, 17, 11, 24, 1, 5, 3, 28,
       15, 6, 21, 10, 23, 19, 12, 4,
       26, 8, 16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55, 30, 40,
       51, 45, 33, 48, 44, 49, 39, 56,
       34, 53, 46, 42, 50, 36, 29, 32]

# Функция расширения E
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# Функция преобразования S
S = [

    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
     ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
     ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
     ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
     ],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
     ],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
     ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
]

# Конечная перестановка P
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

# Матрица обратной IP
IP_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]



def text_to_bits(text, ending): #Функция перевода текста в битовую строку
    bits = bin(int.from_bytes(text.encode('windows-1251', 'surrogatepass'), 'big'))[2:]
    bits = bits.zfill(8 * ((len(bits) + 7) // 8))
    while (len(bits) != ending) and not(len(bits) > ending):
        bits = "0" + bits #Заполняет нулевыми битами, если строка ещё не заполнена
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits): #Функция перевода битовой строки в текст
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('windows-1251', 'surrogatepass') or '\0'

def nsplit(s, n):  # #Функция делит список на подсписки размером n
    return [s[k:k + n] for k in range(0, len(s), n)]

class des():
    def __init__(self):
        self.key = None
        self.text = None
        self.keys = list()
        self.open_message = None

    def run(self, IV, key, text):
        if len(key) > 8:
            key = key[:8]  # Если ключ больше 8 байт, обрезается остальная часть

        self.key = key
        self.text = IV
        self.open_message = text
        self.generatekeys() # Генерируются все ключи на 16 раундов
        text_blocks = nsplit(self.open_message, 8) #Создаются 8-ми байтные блоки из открытого текста
        print('Блоки - ', text_blocks)
        results, final_res = '', ''
        for open_message in text_blocks:  #Цикл всех блоков
            open_message = text_to_bits(open_message, 64)
            block = text_to_bits(self.text, 64) #Формируется 64 битная строка
            print('Вектор в двоичной системе -  ', block)
            block = self.permut(block, IP) #Преобразование начальной перестановки IP
            print(f'Начальная перестановка IP - {len(block)} бит - {block}')
            l, r = nsplit(block, 32)  #Формирование g и d 32-битовых блоков
            print(f'L - {len(l)} бит -{l} \nR - {len(r)} бит -{r}')
            just = None
            for i in range(16):  #Цикл идёт 16 раундов
                print(f'***///////////////////////  РАУНД {i+1}  ///////////////////////***')
                print("\n")
                r_e = self.permut(r, E)  # Функция расширения E до 48 бит
                print(f'Расширение E - {len(r_e)} бит - {r_e}')
                print(f'Ключ - {len(self.keys[i])} бит - {self.keys[i]}')
                just = self.xor(self.keys[i], r_e) #xor с ключом i-го раунда
                print(f'Xor E с ключом - {len(just)} бит - {str(just)}')
                just = self.substitute(just)  #Функция преобразований S, образование 8-ми 4-битовых блоков
                print(f'Преобразование S - {len(just)} бит - {just}')
                just = self.permut(just, P) #Конечная перестановка P
                print(f'Перестановка P - {len(just)} бит - {just}')
                just = self.xor(l, just) #xor двух 32-битовых строк
                print(f'Xor перестановки P и L - {len(just)} бит - {just}')
                l = r
                r = just
                print(f'L - {len(l)} бит -{l} \nR - {len(r)} бит -{r}')
                print("\n")
            result = self.permut(r + l, IP_1)  #Обратная перестановка IP^-1
            result = ''.join(map(str, result))
            print('Результат -  ', result)
            print('Исходное  -  ', open_message)
            self.text = text_from_bits(result)
            result2 = self.xor(result, open_message)
            result2 = ''.join(map(str, result2))
            print('XOR и Итог - ', result2)
            results = text_from_bits(result2)
            final_res += results
        return final_res

    def substitute(self, r_e):  #Функци преобразований S
        subblocks = nsplit(r_e, 6)  #Разбивает 48-битную строку на 8 блоков по 6 бит
        result = list()
        for i in range(len(subblocks)):  #Цикл для всех блоков
            block = subblocks[i]
            row = int(str(block[0]) + str(block[5]), 2)  #Строка - первый и последний бит блока
            column = int(''.join([str(x) for x in block[1:][:-1]]), 2)  #Столбцы - оставшиеся биты(2,3,4,5)
            val = S[i][row][column]  #Берётся значение, в соответствии с таблицей S
            bits2 = bin(val)[2:]  #Переводит значение в двоичную
            while (len(bits2) != 4) and not (len(bits2) > 4):
                bits2 = "0" + bits2
            result += [int(x) for x in bits2]  #Добавляет в список блоки по 4 бита
        return result

    def xor(self, t1, t2):  #Функция xor
        return [int(x) ^ int(y) for x, y in zip(t1, t2)]
    def permut(self, block, table):  #Возвращает данные из таблицы
        return [block[x - 1] for x in table]

    def generatekeys(self):  #Функция генерации ключенй
        self.keys = []
        key = text_to_bits(self.key, 64) #Создание 64-битовой строки
        # print("КЛЮЧ -  ", key)
        key = self.permut(key, P_1)  #Матрица первоначальной подготовки ключа
        # print("Матрица первоначальной подготовки ключа -  ", key)
        c, d = nsplit(key, 28)  #Разделение ключа на два 28-битовых куска
        # print("C -  ", c)
        # print("D -  ", d)
        for i in range(16):  #16 раундов
            c, d = self.shift(c, d, Shift[i])  #Сдвиг по таблице
            # print(i, "Сдвиг по таблице c -  ", c)
            # print(i, "Сдвиг по таблице d -  ", d)
            tmp = c + d
            self.keys.append(self.permut(tmp, P_2))  #Матрица завершающей обработки ключа
            # print("Завершающая обработка -  ", self.keys[i])

    def shift(self, g, d, n):  #Сдвиг
        return g[n:] + g[:n], d[n:] + d[:n]


if __name__ == '__main__':
    sg.theme('LightBlue')
    layout = [  [sg.Text('Data Encryption Standard(Output Feedback)', font=("Helvetica", 18, "bold"), expand_x=True, justification='center')],
            [sg.Text('Вектор ', font=("Helvetica", 11)), sg.InputText("Forever", key='vector', font=("Helvetica", 11))],
            [sg.Text('Ключ    ', font=("Helvetica", 11)), sg.InputText("Would", key='key', font=("Helvetica", 11))],
            [sg.Text('Текст   ', font=("Helvetica", 11)), sg.InputText("Be Alone", key='text', font=("Helvetica", 11))],
            [sg.Button('Запустить')],
            [sg.Text('Зашифрованный текст: ', font=("Helvetica", 11)), sg.InputText("", key='encrypt', font=("Helvetica", 11), use_readonly_for_disable=True, disabled=True)],
            [sg.Text('Расшифрованный текст: ', font=("Helvetica", 11)), sg.InputText("", key='decrypt', font=("Helvetica", 11), use_readonly_for_disable=True, disabled=True)],
            [sg.Output(size=(200, 30))]
                ]

    window = sg.Window('DES OFB', layout, size=(1366,768))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Запустить':
            vector = values['vector']
            key = values['key']
            text = values['text']
            d = des()
            result = d.run(vector, key, text)
            print('Перевод из двоичной - ', result.split(' '))
            result2 = d.run(vector, key, result)
            print('Перевод из двоичной - ', result2)
            window['encrypt'].update(value=result)
            window['decrypt'].update(value=result2)


    window.close()