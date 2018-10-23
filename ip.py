
import pulp, global_var

def ip(fs):

    my_lp_problem = pulp.LpProblem("My LP Problem", pulp.LpMaximize)
    
    q=[]
    k=0
    for i in range(global_var.size):
        q.append([])
        for j in range(global_var.size):  
            k=i*global_var.size+j+1
            q[i].append([pulp.LpVariable('q%d' %k , lowBound=0, cat='Integer')])
 
    #objective
    my_lp_problem += pulp.lpSum(global_var.t[i][j] * global_var.u[i][j] * q[i][j] for i in fs for j in fs), 'utility'

    
    ####################### mpf constraint
    #capacity constraints
    
    for i in fs:  #給出去的
        my_lp_problem += pulp.lpSum([q[i][j]  for j in fs]) <= global_var.cap[i]
    
    ####################### as & lsf constraint 
    #capacity constraints
    #for i in fs:  
     #   my_lp_problem += pulp.lpSum([q[i][j]  for j in fs  if i!=j]) <= global_var.cap[i]-global_var.req[i]
    
    ####################### mpf & lsf & as constraint
    #demand constraints
    for i in fs: #別人給的
        my_lp_problem += pulp.lpSum([q[j][i]  for j in fs]) <= global_var.req[i]
    
    ####################### lsf & lso constraint
    #for i in fs:  
     #   my_lp_problem += pulp.lpSum(q[i][i] ) == min(global_var.cap[i], global_var.req[i])
    
    
    
    my_lp_problem.solve()
    #print(my_lp_problem)
    #show variable value
    v_name=[]
    v_varvalue=[]
    for v in my_lp_problem.variables():
        v_name.append(v.name)
        v_varvalue.append(v.varValue)
        #print(v.name, "=", v.varValue)
    
    utility=pulp.value(my_lp_problem.objective)
    if utility==None:
        utility=0
    return utility, v_name, v_varvalue