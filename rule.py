from banzhaf import * 

def rule(fs_temp, parameters, ms, r): 
  
    old_payoff, new_payoff=compute_payoff(fs_temp, parameters)
    
    #compare
    #################### R1: at least one player's payoff improve without decreasing other's payoff
    if r==1:
        d=1  # decreasing other's payoff?
        if ms==1:  #merge  
            for i in range(len(new_payoff)):
                if new_payoff[i] > old_payoff[i]: 
                    d=0
                   
                elif new_payoff[i] < old_payoff[i]:    
                    d=1
                    break
                    
        else:     #split
            for i in range(len(new_payoff)):
                if old_payoff[i] > new_payoff[i]: 
                    d=0
                   
                elif old_payoff[i] < new_payoff[i]: 
                    d=1
                    break
                    
        if d==0: return True  
        else: return False
    ##################### R2: at least one player's payoff improve, but may hurt others
    elif r==2:  #no split operation
        if ms==1:  #merge  
            for i in range(len(new_payoff)):
                if new_payoff[i] > old_payoff[i]: 
                    return True 
        return False
        
    ##################### R3: all strictly improve    
    elif r==3: 
        count=0
        if ms==1:  #merge  
            for i in range(len(new_payoff)):
                if new_payoff[i] > old_payoff[i]: count+=1
                    
        else:     #split
            for i in range(len(new_payoff)):
                if old_payoff[i] > new_payoff[i]: count+=1
                    
        if count==len(new_payoff): 
            return True
        else:
            return False