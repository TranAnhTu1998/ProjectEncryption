
arrAlphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И',  'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
               'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ы', 'Э', 'Ю', 'Я']

strAlphabet = 'АБВГДЕЖЗИйКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def array_playfire(key):
    #matric
    m = 5
    n = 6
    arr_playfire = [[] for _i in range(m)]
    len_arr_playfire = m
    k = 0
    v = 0
    br = True
    for i in range(len_arr_playfire):
        j = 0

        while j < n and br:
            if k < len(key):
                arr_playfire[i].append(key[k])
                if k == len(key) - 1:
                    br = False
                k += 1
            j += 1

        while j < n and v < len(arrAlphabet):
            if key.find(arrAlphabet[v]) == -1:
                arr_playfire[i].append(arrAlphabet[v])
                j += 1
            v += 1

    #print(arr_playfire)
    return arr_playfire

def toString(arr):
    m = 5
    n = 6
    str = ''
    for i in range(m):
        for j in range(n):
            str += arr[i][j]
    return  str

def encode_playfire(key, str):
    str_playfire = ''
    str = str.replace(' ','')
    key = key.replace(' ', '')
    #print("str = ", str)
    #matric n * m
    m = 5
    n = 6
    array_playfire_var = array_playfire(key)
    if len(str) % 2 != 0:
        str = str[0:len(str)-1]
        #print(str)
    i = 0
    len_str = len(str)
    while i < len_str:
        char_first = str[i]
        char_second = str[i+1]
        str_playfire_var = toString(array_playfire_var)
        i_charfirst_arrplayfire = int(str_playfire_var.index(char_first) /  n)
        j_charfirst_arrplayfire = str_playfire_var.index(char_first) % n

        i_charsecond_arrplayfire = int(str_playfire_var.index(char_second) / n)
        j_charsecond_arrplayfire = str_playfire_var.index(char_second) % n


        i_first_playfire = -1
        j_first_playfire = -1
        i_second_playfire = -1
        j_second_playfite = -1

        if i_charfirst_arrplayfire == i_charsecond_arrplayfire :
            i_first_playfire = i_charfirst_arrplayfire
            j_first_playfire = (j_charfirst_arrplayfire + 1) % n
            i_second_playfire = i_charsecond_arrplayfire
            j_second_playfite = (j_charsecond_arrplayfire + 1) % n
        elif j_charfirst_arrplayfire == j_charsecond_arrplayfire:
            i_first_playfire = (i_charfirst_arrplayfire + 1) % m
            j_first_playfire = j_charfirst_arrplayfire
            i_second_playfire = (i_charsecond_arrplayfire + 1) % m
            j_second_playfite = j_charsecond_arrplayfire
        else:
            i_first_playfire = i_charfirst_arrplayfire
            j_first_playfire = j_charsecond_arrplayfire
            i_second_playfire = i_charsecond_arrplayfire
            j_second_playfite = j_charfirst_arrplayfire


        #print(i_first_playfire, j_first_playfire)
        char_first_playfire = array_playfire_var[i_first_playfire][j_first_playfire]
        char_second_playfire = array_playfire_var[i_second_playfire][j_second_playfite]
        str_playfire += char_first_playfire
        str_playfire += char_second_playfire

        #print("char_first_playfire = ", char_first_playfire)
        #print("char_second_playfire = ", char_second_playfire)
        '''print(char_first)
        print(str_playfire_var.index(char_first))
        print(i_charfirst_arrplayfire)
        print(j_charfirst_arrplayfire)'''

        i += 2
    return str_playfire


#str_encod = encode_playfire('ПОЛЕТ', 'КОДПЛЕИФЕ ИЕРАОСНОВАННАИСПОЛЬЗОВАНИИТРИЦЫБУКВ')
#print(str_encod)
