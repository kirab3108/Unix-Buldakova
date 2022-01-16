def encode(stroka, key):
    list_str, list_key = [i for i in (stroka, key)] #2 списка a и b элементов строки и ключа
    ls=[]
    for a in range(len(list_str)): #идеим по длине строки
        for i, j in [(list_str[a],list_key[a])]: #идем по элементам двух списков символов строки и ключа
            ls.append(ord(i) ^ ord(j)) #побитовое или(XOR)
    rez= "".join(map(chr,ls)) # соединяем в строку все эелементы после побитового или
    return rez

def decode(stroka, key):
    list_str, list_key = [i for i in (stroka, key)]
    ls=[]
    for a in range(len(list_str)):
        for i , j in [(list_str[a],list_key[a])]:
            ls.append(ord(i) ^ ord(j))
    rez= "".join(map(chr,ls))
    return rez



msg = input("Введите текст: ")
k=input("Введите ключ(строка): ")
while len(k)<len(msg):
    k+=k;    
sh_msg=encode(msg,k) #закодированное предложение
print("закодированное предложение",sh_msg)
rez=decode(sh_msg,k) #раскодированное предложение
print("раскодированное предложение",rez)
