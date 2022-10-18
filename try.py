
def missingWords(s,t):

    slist = s.split(' ')
    tlist = t.split(' ')

    

    count = []

    for i in slist:
        count.append(i)

    for j in tlist:
        if j in count:
            res.append(j)


    return res
    # print(slist,tlist)



s = 'I am using hac to imp prog'
t = 'am hac to imp'
print(missingWords(s,t))