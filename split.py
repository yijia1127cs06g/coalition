import  itertools , global_var
from remove_par import *
from ip import *
from rule import *
from copy import deepcopy


def all_partitions(fi):
    a=[]
    for j in range(1,len(fi)):
        for i in itertools.combinations(fi,j):
            a.append(i)
    for i in range(len(a)):
        a[i]=t_trans(a[i])
    k=0
    aa=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if not bool(set(a[i]) & set(a[j])) and len(a[i])+len(a[j])==len(fi):
                aa.append([])
                aa[k].append(a[i])
                aa[k].append(a[j])
                k+=1
                break
    
    return aa
    
def split(fs):
    #temp = deepcopy(fs)
    for fi in fs:
        if len(fi)>1 and fi not in global_var.split_check:
            global_var.split_check.append(fi)
            for i in all_partitions(fi):   
           
                if i[0] not in global_var.v[0]:
                    
                    v[0].append(i[0])
                    v[1].append(ip(i[0])[0])
                
                if i[1] not in global_var.v[0]:
                    
                    v[0].append(i[1])
                    v[1].append(ip(i[1])[0])
                
                
                if rule(i, 0, 3):   #(fs_temp, merge/split, rule)
                    print("!!!! split happens !!!!!")
                    fs.remove(sorted(i[0]+i[1]))
                    fs.append(i[0])
                    fs.append(i[1])
                    sorted(fs)
                    return True

    return False
