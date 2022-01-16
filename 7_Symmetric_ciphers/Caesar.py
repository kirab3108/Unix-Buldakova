def encrypt(k:int,  m:str)->str:
    m_arr = []
    rez = ""
    for c in m:
        m_arr.append(ord(c))
    m_arr = [(i+k)%65536 for i in m_arr]
    for i in m_arr:
        rez+=chr(i)
    return rez


def decrypt(k, c):
    c_arr = []
    rez = ""
    for i in c:
        c_arr.append(ord(i))
    c_arr = [(i-k)%65536 for i in c_arr]
    for i in c_arr:
        rez+=chr(i)
    return rez

def decrypt_without_key(c):
    alph={}
    for i in c:
        if i in alph:
            alph[i]+=1
        else:
            alph[i]=1
    max_al=0
    max_k=-1
    for i in alph:
        if alph[i]>max_al:
            max_al=alph[i]
            max_k=i
    k=ord(max_k)-ord(" ")
    return decrypt(k, c)

msg = input("Введите текст: ")
k=int(input("Введите ключ(число): "))
sh_msg=encrypt(k, msg)
print(sh_msg)
rez_msg=decrypt(k, sh_msg)
rez=decrypt_without_key(sh_msg)
print(rez)
