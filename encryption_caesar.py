

arrAlphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
               'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
# Số phần tử trong chuỗi arrAlphabet - (Количество элементов в массиве)
lengAlphabet = len(arrAlphabet)


# Xuất các ký tự trong mảng arrAlphabet.
#print(*arrAlphabet, sep=' ')


# Đưa chỉ số (index) trong mảng từ một ký tự. (Функция, которая выводит индекс элемента в массиве)
def index_element(char):
    return arrAlphabet.index(char)





# Mã hóa chuỗi Caesar (Функция шифра по метод Цезаря)
def toString(arr):
    str = ''
    for char in arr:
        str += char
    return  str


def encode_caesar(str):
    arrAlphabetCaesar = []
    for char in str:
        # Mã hóa ký tự Caesar
        #print(char)
        #print(index_element(char))
        # Mã hóa một ký tự Caesar
        charCaesar = arrAlphabet[(index_element(char) + 3) % (lengAlphabet-1)]
        arrAlphabetCaesar.append(charCaesar)
    return toString(arrAlphabetCaesar)


def decoding_caesar(str):
    arrAlphabetCaesar = []
    for char in str:
        # Giải Mã hóa ký tự Caesar
        #print(char)
        #print(index_element(char))
        # Giải Mã hóa một ký tự Caesar
        charCaesar = arrAlphabet[(index_element(char) - 3) % (lengAlphabet-1)]
        arrAlphabetCaesar.append(charCaesar)
    return toString(arrAlphabetCaesar)



# Test
'''print("Шифровки Цезаря")
str1 = "ИЦРХЭЫЩШШЩРЬЩЩМДРШУРМЮПРЭЪЩЬЭРЪРШШЩТЛЧРШКЭЗЩМЖВШЩРМЮЧЛСШЩРЬЩЩМДРШУР"
print("Открытый текст : ", str1)
print("Шифрованный текст: ", encode_caesar(str1))


print("Разшифровки Цезаря")
str2 = "ЛЩУШБЮЬЫЫЬУАЬЬПЗУЫЦУПВТУБЭЬАБУЭУЫЫЬХОЪУЫНБКЬПЙЕЫЬУПВЪОФЫЬУАЬЬПЗУЫЦУ"
print("Открытый текст : ", str2)
print("Расшифрованный текст: ", decoding_caesar(str2))


print("Шифровки Цезаря")
str3 = "КОДИРОВАНИЕ"
print("Открытый текст : ", str3)
print("Шифрованный текст: ", encode_caesar(str3), sep='')
for alphabetic in arrAlphabet:
    print(alphabetic, sep=',');'''
