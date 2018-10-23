import numpy as np, matplotlib.pyplot as plt
import global_var
from remove_par import *
from ip import *
from banzhaf import *
from merge import merge
from split import split


def generate_topology(size,prob):
    topology = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(np.random.choice([0,1], p=[1-prob, prob]))
        topology.append(row)
        
    return topology

def generate_parameter(size, mean, variance):
    return list(np.random.normal(mean, variance, size))

def compute_utility(server_cost, user_price):
    utility = []
    for cost in server_cost:
        row = []
        for price in user_price:
            if price - cost > 0:
                row.append(price-cost)
            else:
                row.append(0)
        utility.append(row)
    
    return utility


def initial():
    v=[[],[]] #v[0]:聯盟組合 v[1]:聯盟利益
    merge_check=[]
    split_check=[]


def algo(parameters):
    size = len(parameters['server_cost'])
    coalition_and_value = [[],[]]

    coaition_structure = []
    
    
    '''Initial each smallest coalition value'''
    for i in range(size):
        coalition_structure.appned([i])
        coalition_and_value[0].append([i])
        coalition_and_value[1].append(parameters['utility'][i][i] * min(parameters['server_capacity'][i], parameters['user_request'][i]))
    
    
    ''' Set Paramters '''
    parameters['coalition_and_value'] = coalition_and_value
    parameters['merge_checklist'] = []
    parameters['split_checklist'] = []
    
    ''' Merge and Split '''
    while True:
        # Specify each rule for merge and split
        merge(coalition_structure,parameters,3) 
        split_happens = split(coalition_structure,parameters)
        if split_happens == True:
            break
        
    


'''
def algo():
    
    ################################# initial coalition structure & v
    global_var.initial()  
    fs=[]             
    ################################# initial the utility of each coalition
    for i in range(global_var.size):
        fs.append([i])   
        global_var.v[0].append([i])
        global_var.v[1].append(min(global_var.cap[i],global_var.req[i])*global_var.u[i][i])
             
    ################################# 

    i = 1
    print("=== Stop when merge result equals to split result ===")
    
    while True:
           
        merge(fs, 3)   

        print("= Iteration", i,"=")
        print("\t\tmerge result", fs)

        repeat = split(fs)
        print("\t\tsplit result", fs)
        if repeat != True:
            break
        i +=1
    print()
    ################################# calculate total utility of coalition

    total_utility=0
        
    for fs_id in fs:
        total_utility += global_var.v[1][global_var.v[0].index(fs_id)]
    print("=== Final CS ===")
    print("\t\tCS:",fs)
    print("\t\tvalue:",[global_var.v[1][global_var.v[0].index(x)] for x in fs])
    print("\t\ttotal:",total_utility)

    total_u.append(total_utility)
   
    ################################# calculate the total resources provided from providers
    #total_resource=0
    #resource=[]
    #for fs_id in fs:
    #    utility, v_name, v_value=ip(fs_id)
    #    for i in v_value:
    #        if i==None: v_value.remove(i)
    #    resource.append(v_value)
    #    total_resource+=sum(v_value)
    #print("\t\tresoure:", resource)
    #print("\t\ttotal:", total_resource)
    #total_r.append(total_resource)
'''    
##################### main        
#total_u_mean=[]  # 記錄每筆utility平均
#total_r_mean=[]  # 記錄每筆allocated resource平均

''' 
This is Necessary 
global_var.si(10)
global_var.fix() 
global_var.sam(5,10)  # x軸個數, sample個數
global_var.read_sample()
'''
#print("capacity", global_var.cap)
#print("cost", global_var.read_co[0])
#print("request", global_var.req)
#print("payment", global_var.read_p[0])


def trial(size, iteration):
    utility_list=[]
    for i in range(iteration):
        topology = generate_topology(size, 0.6) # Random generate topology based on probability
        parameters = {}
        parameters['server_cost'] = generate_parameter(size, 100, 25)
        parameters['user_price'] = generate_parameter(size, 100, 25)
        parameters['server_capacity'] = generate_parameter(size, 100, 25)
        parameters['user_request'] = gernerate_parameter(size, 100, 25)
        parameters['utility'] = compute_utility(parameters['server_cost'], parameters['user_price'])
        
    
    
    

'''
k = 1
for i in range(global_var.x): # x軸個數
    total_u=[]
    #total_r=[]
    #global_var.si(10+5*i)
    
    for j in range(global_var.sample):  #50個樣本
        print("======== Case %d =========="%k)

        global_var.get_sample(i,j)

        print("=== Configuration ===")
        print("\tcapacity:", global_var.cap)
        print("\tcost:", global_var.read_co[0])
        print("\trequest:", global_var.req)
        print("\tpayment:", global_var.read_p[0])
        #print("\tutility:", global_var.u)
        print()

        algo()  
        k += 1
    #total_r_mean.append(sum(total_r)/len(total_r))
    total_u_mean.append(sum(total_u)/len(total_u))
'''
def main():
    pass