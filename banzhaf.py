#compute the Banzhaf value 
from itertools import combinations,chain
from ip import ip
from remove_par import *
import global_var

def create_pvset(player_set):   #所有組合 ex.[1,2]->[[],[1],[2],[1,2]]

    pv_set=[[[],0]]
    _ls=list(chain.from_iterable(combinations(player_set,i) for i in range(1,len(player_set)+1)))
    for i in _ls:  
        if list(i) not in global_var.v[0]:
            global_var.v[0].append(list(i))
            global_var.v[1].append(ip(i)[0])
        pv_set.append([list(i),global_var.v[1][global_var.v[0].index(list(i))]])
    return pv_set

def compute_banzhaf(pv_set,player_set):

    vv=[]
    total=[]
    beta=[]
    for i in range(len(player_set)):
        vv.append([])  
        total.append(0)
        beta.append([])  
    
    k=0
   
    for player in player_set:  
        for i in range(len(pv_set)):
            #if pv_set中有目前要檢查的玩家    #ex. player1
            if player in pv_set[i][0]:      #ex. [1,2]
                pv_set[i][0].remove(player)
                for j in range(len(pv_set)):
                    #判斷pv_set中除了目前玩家外的其他玩家  ex. [2]
                    if pv_set[j][0]==pv_set[i][0]: 
                        pv_set[i][0].append(player)
                        break
                vv[k].append(pv_set[i][1]-pv_set[j][1])   #ex. v[1,2]-v[2]
          
        beta[k]=sum(vv[k])/len(vv[k])
        k+=1
    
    
    total_beta=0
    _v=0
    payoff=[]
    bv=[]
    for i in range(len(player_set)):
        payoff.append([])
        bv.append([])
            
    for i in range(len(player_set)):
        total_beta+=beta[i]
    
    if(total_beta==0):
        for i in range(len(player_set)):
            payoff[i]=0
    else:    
        for i in range(len(pv_set)):      
            if player_set == pv_set[i][0]:
                _v=pv_set[i][1]    #total_value
        
        for i in range(len(player_set)):
            bv[i]=beta[i]/total_beta
            payoff[i]=bv[i]*_v
        
    return payoff



def compute_payoff(fs_temp):  ##[[1,2,3],[4,5]]
    
    ##################################compute origin payoff
    p=[]
    for j in fs_temp:
        if len(j)>1:
            pv_set=create_pvset(j)   
            payoff=compute_banzhaf(pv_set, j)  
        else: payoff=global_var.v[1][global_var.v[0].index(j)]
        p.append(payoff)
    
    p=str(p)
    p=p.replace("]","")  #remove right parenthesis
    p=p.replace("[","")
    old_payoff=[]
    for i in p.split(','):
        old_payoff.append(float(i))
    #print(old_payoff)
    #################################compute new payoff
    fs_t2=trans(fs_temp)
    pv_set=create_pvset(fs_t2)
    new_payoff=compute_banzhaf(pv_set, fs_t2)
    #print(new_payoff) 
    return old_payoff, new_payoff
