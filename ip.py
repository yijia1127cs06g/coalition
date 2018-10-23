
import pulp, global_var

def ip(fs, parameters):
    size = len(parameters['server_cost'])
    
    my_lp_problem = pulp.LpProblem("My LP Problem", pulp.LpMaximize)
    
    q=[]
    k=0
    for i in range(size):
        q.append([])
        for j in range(size):  
            k=i*size+j+1
            q[i].append([pulp.LpVariable('q%d' %k , lowBound=0, cat='Integer')])
 
    #objective
    my_lp_problem += pulp.lpSum(parameters['topology'][i][j] * parameters['utility'][i][j] * q[i][j] for i in fs for j in fs), 'utility'

    
    ####################### mpf constraint
    #capacity constraints
    
    for i in fs:  #給出去的
        my_lp_problem += pulp.lpSum([q[i][j]  for j in fs]) <= parameters['server_capacity'][i]
    
    ####################### as & lsf constraint 
    #capacity constraints
    #for i in fs:  
     #   my_lp_problem += pulp.lpSum([q[i][j]  for j in fs  if i!=j]) <= parameters['server_capacity'][i]-parameters['user_request'][i]
    
    ####################### mpf & lsf & as constraint
    #demand constraints
    for i in fs: #別人給的
        my_lp_problem += pulp.lpSum([q[j][i]  for j in fs]) <= parameters['user_request'][i]
    
    ####################### lsf & lso constraint
    #for i in fs:  
     #   my_lp_problem += pulp.lpSum(q[i][i] ) == min(parameters['server_capacity'][i], parameters['user_request'][i])
    
    
    
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