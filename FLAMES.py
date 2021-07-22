a=input('enter 1st name:    ')
b=input('enter 2nd name:    ')
def kill_duplicates_and_give_len(a,b):
    z=[]
    a=a.lower()
    b=b.lower()
    for i in a:
        for j in b:
            if i==j:
                z.append(i)
                for o in z:
                    if o==i:
                        a=a.replace(i,'',1)
                        b=b.replace(j,'',1)
                    else:
                        pass
    return len(a+b)



def Flames_finder(a,b):
    length=kill_duplicates_and_give_len(a,b)
    FLAMES={'F':'Friends','L':'Lovers','A':'Affectionate','M':'Mariage','E':'Enemies','S':'Sibling'}
    keys=list(FLAMES.keys())
    values=list(FLAMES.values())
    letter_index=0
    while len(keys)!=1:
        letter_index=letter_index+length
        if letter_index>len(keys):
            letter_index=(letter_index)%len(keys)
        keys.remove(keys[letter_index-1])
        
    return(FLAMES[keys[0]])
        
    

print('relationship stutus between ' +a+ ' and '+b+' is '+Flames_finder(a,b))
