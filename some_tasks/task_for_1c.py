dict1={}
dict2={}
dict3={}
dict4={}
dict5={}
#В задании сказано, что необходимо обработать текст  так, чтобы он эффективно выдавал ответ по введенному ключу.
#В условиях задачи считаем, что дефис не является частью слова, также считаем, что все числительные записанны словами
#Я обработал текст так, что все возможные ключи длины 1 хранятся в словаре dict1, все возможные ключи длины 2 хранятся в словаре dict2..
#В словаре ключу соответствует введенное ключ-слово, значению ключа соответствует необходимый к выводу ответ.
#Я решил брать словари, так как они не включают в себя повторы ключей, а поиск по словарю в питоне происходит за O(1)
#Таким образом мы тратим основное время на обработку текста, но максимально эффективно отвечаем на запросы.
a=[[ord('A')-1,ord('Z')+1],[ord('a')-1,ord('z')+1],[ord('А')-1,ord('Я')+1],[ord('а')-1,ord('я')+1]]
with open('F:\\python\\pythonProject4sem\\text.txt', 'r', encoding="utf-8") as f:#здесь вставьте путь к обрабатываемому файлу
    qwe=[]
    for line in f:
        b=line
        b=b.split()
        for i in b:
            qwe.append(i)
n=len(qwe)
z=0
for i in range(n):
    j=0
    while j<len(qwe[i]): # здесь я проверяю, что код символа лежит в промежутках соответствующих буквам => символ является буквой.
        if (ord(qwe[i][j])>a[0][0] and ord(qwe[i][j])<a[0][1]) or (ord(qwe[i][j])>a[1][0] and ord(qwe[i][j])<a[1][1]) or (ord(qwe[i][j])>a[2][0] and ord(qwe[i][j])<a[2][1]) or (ord(qwe[i][j])>a[3][0] and ord(qwe[i][j])<a[3][1])  :
            j+=1
        else:
            qwe[i]=qwe[i][:j]+qwe[i][(j+1):]
            if len(qwe[i])==0:
                z+=1
array=[]
for i in range(n):
    if qwe[i]!='':
        array.append(qwe[i])
qwe=array
n=len(qwe)
for i in range(n):
    s = qwe[i][0]
    dict1[s]=i
    if i+1<n and len(qwe[i+1])>1:
        s=s+qwe[i+1][1]
        dict2[s]=i
    if i + 2 < n and len(qwe[i + 2]) > 2:
        s=s+qwe[i+2][2]
        dict3[s]=i
    if i + 3 < n and len(qwe[i + 3]) > 3:
        s=s+qwe[i+3][3]
        dict4[s]=i
    if i + 4 < n and len(qwe[i + 4]) > 4:
        s = s + qwe[i + 4][4]
        dict5[s] = i
while a!='0':# в задании сказано, что программа должна отвечать на несколько запросов сразу, поэтому использую while, для того, чтобы корректно завершить программу введите "0"
    a=input()
    n=len(a)
    if a!='0':
        if n==1:
            print(dict1[a])
        if n==2:
            print(dict2[a])
        if n==3:
            print(dict3[a])
        if n==4:
            print(dict4[a])
        if n==5:
            print(dict5[a])