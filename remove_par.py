#change parentheses

def trans(fs):  #[[1],[2,3]]->[1,2,3]
    f_t=str(fs)
    f_t=f_t.replace("]","")  #remove right parenthesis
    f_t=f_t.replace("[","")
    f_t=f_t.replace(" ","")
    item=[]
    for i in f_t.split(','):
        item.append(int(i))
    item=sorted(item)
    return item

def t_trans(tt):  #(1,)->[1]  #(1, 2)->[1,2]
    f_t=str(tt)
    f=[]
    if(len(tt))<2:
        f_t=f_t.replace("(","[")
        f_t=f_t.replace(")","]")
        f_t=f_t.replace(",","")
    else:    
        f_t=f_t.replace("(","[")
        f_t=f_t.replace(")","]")
    f_t=eval(f_t)
    return f_t