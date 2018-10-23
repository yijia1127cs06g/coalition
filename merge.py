
import global_var, random, itertools
from remove_par import *
from ip import *
from rule import *


def check_edge(ft):  #[0,1,2] have common edge?
    first = ft[0]
    second = ft[1]
    for i in first:
        for j in second:
            # if i==j: continue
            if global_var.t[i][j]: return True
            if global_var.t[j][i]: return True
    return False

def create_visit(method, fs):
    global visit
    visit=[]   #record non-checked member
    if method==3:
        for i in itertools.combinations(fs, 2):
           
            if check_edge(i)==False: 
                continue
            visit.append(t_trans(i))
    else:
        for i in itertools.combinations(fs, 2):
            visit.append(t_trans(i))

def merge(CS, parameters, method):
    

    #initial visit list
    create_visit(method,CS)
    
    while(len(visit)>0 ):  
        
        #choose non-checked member
        fs_temp=random.choice(visit)      
        visit.remove(fs_temp)
        
        if fs_temp in parameters['merge_checklist']:
            continue
        else:
            parameters['merge_checklist'].append(fs_temp)
        
        fs_t2=trans(fs_temp)  #[[0,1],[2]]->[0,1,2]
        if fs_t2 not in global_var.v[0] :
            global_var.v[0].append(fs_t2)
            global_var.v[1].append(ip(fs_t2)[0])
            
        #method 2 
        if method==2:
            if check_edge(fs_t2)==False :continue  

        #check if merge happen
        if rule(fs_temp, 1, 3):   #(fs_temp, merge/split, rule)
            fs[fs.index(fs_temp[0])]=fs_t2
            fs.remove(fs_temp[1])
            create_visit(method, fs)
         
    return  fs