arrAlphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
               'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', '.', ':', ';', '?', '!',  '(', ')', '-', '“']
# Số phần tử trong chuỗi arrAlphabet - (Количество элементов в массиве)
lengAlphabet = len(arrAlphabet)

'''ap = []
for i in range(lengAlphabet):
    ap.append(i)

print(ap)'''

# Đưa chỉ số (index) trong mảng từ một ký tự. (Функция, которая выводит индекс элемента в массиве)
def index_element(char):
    return arrAlphabet.index(char)

# Mã hóa chuỗi Caesar (Функция шифра по метод Цезаря)
def encode(str, bn):
    bn = bn % (lengAlphabet-1)
    arrAlphabetCaesar = []
    for char in str:
        # Mã hóa ký tự Caesar
        charCaesar = arrAlphabet[(bn - index_element(char))]
        arrAlphabetCaesar.append(charCaesar)
    return (arrAlphabetCaesar)


#Ключи
bn = 5573223
# Test
print("Шифровки одноразового шифровального блокнота")
str1 = "ИЦРХЭЫЩШШЩРЬЩЩМДРШУРМЮПРЭЪЩЬЭРЪРШШЩТЛЧРШКЭЗЩМЖВШЩРМЮЧЛСШЩРЬЩЩМДРШУР"
print("Открытый текст : ", str1)
print("Шифрованный текст: ", *encode(str1, bn), sep='')



print("\nРазшифровки одноразового шифровального блокнота")
str2 = "ЛЩУШБЮЬЫЫЬУАЬЬПЗУЫЦУПВТУБЭЬАБУЭУЫЫЬХОЪУЫНБКЬПЙЕЫЬУПВЪОФЫЬУАЬЬПЗУЫЦУ"
print("Открытый текст : ", str2)
print("Расшифрованный текст: ", *encode(str2, bn), sep='')



