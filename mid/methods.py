list = ['larry', 'curly', 'molly','molly']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print list  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print list.index('curly')    ## 2

m=list.remove('curly')         ## search and remove that element
print(m)
n=list.pop(1)
print n
 ## removes and returns 'larry'
print list  ## ['xxx', 'moedhhh', 'shemp', 'yyy', 'zzz']
x=list.count('molly')
print x
#string methods
s=list[1]
res=s[1:3]
print res
# s.replace ("rry" ,"m")
# print s
