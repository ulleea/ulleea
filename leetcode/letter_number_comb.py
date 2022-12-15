def letterCombinations( digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    a = ord('a')
    res = ['']
    for i in digits:
        numb = int(i) - 2
        print(res)
        if numb == 5:
            st = []
            for p in range(len(res)):
                s=res.pop()
                for j in range(4):
                    st.append(s+ chr(a + numb * 3 + j))
            res=st
        elif numb == 7:
            st = []
            for p in range(len(res)):
                s=res.pop()
                for j in range(4):
                    st.append(s+ chr(a + (numb * 3 + 1) + j))
            res=st
        elif numb==6:
            st = []
            for p in range(len(res)):
                s=res.pop()
                for j in range(3):
                    st.append(s+  chr(a + (numb * 3 + 1) + j))
            res=st
        else:
            st = []
            for p in range(len(res)):
                s=res.pop()
                for j in range(3):
                    st.append(s+ chr(a + numb * 3 + j))
            res=st
    return res if res!=[''] else []


mapping = {
            '2': ['a','b','c'],
            '3':['d','e',"f"],
            '4':["g","h","i"],
            '5':["j","k","l"],
            '6':["m","n","o"],
            '7':["p","q","r","s"],
            '8':["t","u","v"],
            '9':["w","x","y","z"]
        }
digits='23'
eligible_list=[]
for digit in digits:
    eligible_list.append(mapping[digit])
print(eligible_list)