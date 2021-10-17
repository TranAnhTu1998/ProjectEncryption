#Шифр "Лессенка"
def encode_cypher_ladder(in_str):
    arr_str = [[], []]
    #arr_str.append([])
    b = True
    for char in in_str:
        if b:
            arr_str[0].append(char)
            b = False
        else:
            arr_str[1].append(char)
            b = True
    return arr_str
    #print(arr_str) #test


str = "ВЩИТЗЬЛОНЕНИУШИЗЕГАЕТСЮЕНОЙОСВЕПТ"
print("Шифр \"Лессенка\"")

print("Открытый тескт : ", str)
#print("Шифрованный текст : ", encode_cypher_ladder(str))
print('Шифрованный тескт :', *encode_cypher_ladder(str)[0], *encode_cypher_ladder(str)[1], sep='')
