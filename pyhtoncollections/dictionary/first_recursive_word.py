# pattern='ABABBAC'
# find first recursive character A
# ==============================================
pattern='ABABBAC'
dict={}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        print(ch,'is first recursive character')
        break
# ========================================================
# find heighest frequent word in pattern='ABABBACEEEEE'
pattern='ABABBACEEEEE'
dic={}
for ch in pattern:
    if ch not in dic:
        dic[ch]=1
    else:
        dic[ch]+=1
print(dic)
# for i,k in dic.items():
#     print(i,k)
s=sorted(dic,key=dic.get)
print(s)