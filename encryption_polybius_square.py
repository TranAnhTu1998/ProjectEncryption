

arrAlphabet = [['А', 'Б', 'В', 'Г', 'Д', 'Е'],
               ['Ж', 'З', 'И', 'К', 'Л', 'М'],
               ['Н', 'О', 'П', 'Р', 'С', 'Т'],
               ['У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш'],
               ['Щ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']]  # Mảng chứa chữ cái tiếng nga.

# print(arrAlphabet[1][1]) #Test mảng dữ liệu


class IndexArr2x:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def setRow(self, row):
        self.row = row

    def setCol(self, col):
        self.col = col

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col


# Thuật toán mã hóa Polybius Square


def index_element(char):
    indexAlphabest = IndexArr2x(-1, -1)
    for i in range(len(arrAlphabet)):
        for j in range(len(arrAlphabet[i])):
            if char == arrAlphabet[i][j]:
                indexAlphabest.setRow(i)
                indexAlphabest.setCol(j)
                return indexAlphabest


def encode_polybius_square(str):
    arrOut = []
    for elem in str:
        #print("elem : ", elem)
        index2x = index_element(elem)
        #print("row:", index2x.row) #Test row
        #print("col:", index2x.col) #Test col

        if index2x.getRow() == -1 or index2x.getCol() == -1:
            return "ERROR"
        else:
            row = index2x.row
            col = index2x.col
            arrOut.append(row+1)
            arrOut.append(col+1)
    #print(toString(arrOut))
    str_out = ''.join(e.__str__() for e in arrOut)
    return str_out


def decode_polybius_square(str):
    i = 0
    str_out = ''
    #print("len(str)-2 = ", len(str)-2)
    while i <= len(str)-2:
        #print("i = ", i)
        #print("int(str[i]) = ", int(str[i]))
        #print("int(str[i+1]) = ", int(str[i+1]))
        #print("arrAlphabet[int(str[i]) - 1][int(str[i+1])-1] = ", arrAlphabet[int(str[i])-1][int(str[i+1])-1])
        str_out += arrAlphabet[int(str[i])-1][int(str[i+1])-1]
        i += 2
    return str_out

'''str = "АЛФАВИТ"
print("Шировка Квадрат Полибия")
print("*Открытый текст: ", str)
print("*Шифрованный текст: ", encode_polybius_square(str))


str = "11254211132336"
print("Разшировка Квадрат Полибия")
print("*Открытый текст: ", str)
print("*Pазшифрованный текст : ", decode_polybius_square(str))'''


