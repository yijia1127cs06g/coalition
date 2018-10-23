
import global_var, random, itertools
from remove_par import *
from ip import *
from rule import *

def merge_two_


def check_edge(ft):  #[0,1,2] have common edge?
    first = ft[0]
    second = ft[1]
    for i in first:
        for j in second:
            # if i==j: continue
            if global_var.t[i][j]: return True
            if global_var.t[j][i]: return True
    return False

def create_visit(method, CS):
    visit=[]   #record non-checked member
    if method==3:
        for i in itertools.combinations(CS, 2):           
            if check_edge(i)==False: 
                continue
            else:
                visit.append(list(i))  # use t_trans before
    else:
        for i in itertools.combinations(CS, 2):
            visit.append(list(i))   # use t_trains before
            
    return visit

def merge(CS, parameters, method):
    

    #initial visit list
    visit = create_visit(method,CS)
    
    while(len(visit)>0 ):  
        
        #choose non-checked member
        ready_merge=random.choice(visit)      
        visit.remove(ready_merge)
        
        if ready_merge in parameters['merge_checklist']:
            continue
        
        parameters['merge_checklist'].append(ready_merge)
        
        
        # merge two coalition
        # fs_t2=trans(fs_temp)  #[[0,1],[2]]->[0,1,2]
        
        merged = itertools.chain.from_iterable(ready_merge)
        if merged not in parameters['coalition_and_value'][0]:
            parameters['coalition_and_value'][0].append(merged)
            parameters['coalition_and_value'][1].append(ip(merged, parameters)[0])
            
        #method 2 
        if method==2:
            if check_edge(fs_t2)==False :continue  

        #check if merge happen
        if rule(merged ,parameters, 1, 3) == True:   #(merged, parameters, merge/split, rule)
            CS[CS.index(ready_merge[0])] = merged.copy()
            CS.remove(ready_merge[1])
            visit = create_visit(method, CS)
            