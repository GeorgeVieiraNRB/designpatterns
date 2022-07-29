def stringInvert(word):
    st=''
    for x in range(len(word)-1,-1,-1):
        st+=word[x]
    return st
stringInvert('coala')
stringInvert('macaco')
