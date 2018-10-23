
import random, numpy as np

#x軸個數, sample個數
def sam(a, b):
    global x, sample
    x=a
    sample=b
    #return sample
    
def si(s):
    global size
    size=s
    #return size

def read_sample():
    global read_cap, read_req, read_co, read_p, read_t
    
    import ast, pandas as pd
    df_cap = pd.read_csv('./n/n_cap.csv')
    df_req = pd.read_csv('./n/n_req.csv') 
    df_co = pd.read_csv('./n/n_co.csv')   
    df_p = pd.read_csv('./n/n_p.csv')      
    #df_t = pd.read_csv('./n/n_t.csv')
    
    read_cap=[[],[],[],[],[]]
    read_req=[[],[],[],[],[]]
    read_co=[[],[],[],[],[]]
    read_p=[[],[],[],[],[]]
    #read_t=[[],[],[],[],[]]  #讀p.csv時, 要改成6個(因為有6個x點)
    
    
    for i in range(x):
        for j in range(sample):  
            f_c = ast.literal_eval(df_cap.iloc[i,j])
            read_cap[i].append(f_c)
            
            f_r = ast.literal_eval(df_req.iloc[i,j])
            read_req[i].append(f_r)
            
            f_co = ast.literal_eval(df_co.iloc[i,j])
            read_co[i].append(f_co)
            
            f_p = ast.literal_eval(df_p.iloc[i,j])
            read_p[i].append(f_p)
            
            #f_t = ast.literal_eval(df_t.iloc[i,j])
            #read_t[i].append(f_t)
    

def get_sample(row, column): 
    global cap,req,u,t
    cap=read_cap[row][column]
    req=read_req[row][column]
    u=[]
    
    for i in range(size): 
        u.append([])
        for j in range(size):
           
            if read_p[row][column][j]-read_co[row][column][i]>0:
                u[i].append(read_p[row][column][j]-read_co[row][column][i])
            else: u[i].append(0)
    
    #t=read_t[row][column]
    
def initial():
    global v, merge_check, split_check, time
    
    v=[[],[]] #v[0]:聯盟組合 v[1]:聯盟利益
    merge_check=[]
    split_check=[]
   
 
def fix():
    #global co, p, u, cap, req, t
    global t
    #cap=[988, 831, 1107, 986, 836, 967, 870, 805, 968, 860] #900 (sd=110)
    #cap=[1322, 1319, 1216, 993, 1212, 1033, 1432, 1363, 1516, 1217]  #1200 (sd=110)
    #req=[887, 1050, 1133, 997, 881, 1163, 935, 941, 1090, 1028] #1000 (sd=110)
    
    #co=[390, 429, 492, 655, 487, 547, 493, 845, 657, 663] #500 (sd=110)
    #co=[1204, 1003, 1079, 968, 897, 1116, 1031, 898, 784, 1168] #1000 (sd=110)
    #p=[1100,1005,1010,1152,957,807,983,920,1209,951] #1000 (sd=110)
    
    t=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #0.6
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]




    '''
    cap=[90,80,140,100,250] #900 (sd=110)
    #cap=[1322, 1319, 1216, 993, 1212, 1033, 1432, 1363, 1516, 1217]  #1200 (sd=110)
    req=[120,100,120,180,100] #1000 (sd=110)
    
    #co=[390, 429, 492, 655, 487, 547, 493, 845, 657, 663] #500 (sd=110)
    #co=[1204, 1003, 1079, 968, 897, 1116, 1031, 898, 784, 1168] #1000 (sd=110)
    #p=[1100,1005,1010,1152,957,807,983,920,1209,951] #1000 (sd=110)
    
    t=[[0, 1, 0, 0, 1], #0.6
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0]]
    '''
    '''
    #compute u
    u=[]
    for i in range(size):
        u.append([])
        for j in range(size):
            if(p[j]-co[i]>0):
                    u[i].append(p[j]-co[i])
            else : u[i].append(0)
    '''

# generate ws graph
def ws_t(t_p):  
    import networkx as nx
    global t
    G=nx.DiGraph()
    G=nx.watts_strogatz_graph(size,4,t_p)  #t_p: 2 or 4, p=0-0.2(+0.05)
    e=nx.edges(G) #Return a list of edges.
    t=[]
    for i in range(size):
        t.append([])
        for j in range(size):
            if i==j: t[i].append(1)
            t[i].append(0)
    for i in e:
        x=i[0]
        y=i[1]
        t[x][y]=1
        t[y][x]=1

#generate random graph with probability t_p
def given_t(t_p):  #t_p: 機率
    global t  

    #t_p=0.6
    t_temp=[]  
    for i in range(size*size-size):
        if t_p==0: t_temp.append(0)
        else: t_temp.append(np.random.choice([0,1], p=[1-t_p, t_p]))
        #機率: 0出現次數:1-t_p, 1出現次數:t_p
    
    t=[]
    id=0
    for i in range(size):
        t.append([])
        for j in range(size):
            if i==j: t[i].append(1)          #自己跟自己可以互通:1
            else:
                t[i].append(t_temp[id])
                id+=1
     
    
    


    
       
    
    




