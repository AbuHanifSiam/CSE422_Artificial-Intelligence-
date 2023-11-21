import random
import math

min = -math.inf
max = math.inf
node_visit = 0
tree_depth = 0


def maximizer(cur_depth, index, terminal_nodes,alpha,beta):
    global tree_depth, node_visit
    #print("maximizer depth",cur_depth)
    if cur_depth == tree_depth:
        node_visit+=1
        #print("break maximizer depth", cur_depth)
        return terminal_nodes[index]
    v = min
    for i in range(0,branch):
        #beta = math.inf
        v_prime = minimizer(cur_depth+1,index*2+i, terminal_nodes, alpha, beta)
        #print("maximizer value", v_prime)
        if v<v_prime:
            v = v_prime
        if alpha < v:
            alpha = v
             
        if alpha>=beta:
            #2130print("max break")
            break
        #print("maximizer alpha-beta",alpha, beta)
    return v
    
def minimizer(cur_depth, index, terminal_nodes, alpha, beta):
    global tree_depth, node_visit
    #print("minimizer depth", cur_depth)
    if cur_depth == tree_depth:  # leaf node
        node_visit+=1
        #print("break minimizer depth", cur_depth)
        return terminal_nodes[index]
    v = beta
    
    for child in range(0,branch):
        v_prime = maximizer(cur_depth+1,index*2+child,terminal_nodes, alpha, beta)
        #print("minimizer value",v_prime)
        
        if v>v_prime:
            v = v_prime
            
        if beta > v:
            beta = v
        if alpha >=beta:
            #print("min break")
            break
        #print("minimizer alpha-beta", alpha, beta)
    return v

def alpha_beta_pruning(terminal_nodes):
    return maximizer(0, 0, terminal_nodes,min,max)



id = input("Enter Id: ")
initial_hp = int(id[-1:-3:-1])
#print(initial_hp)
branch = int(id[2])#3
tree_depth = (int(id[0])*2)#2
nodes_count = branch**tree_depth
terminal_nodes = []

min_limit, max_limit = input("enter minimum and maximum value: ").split(" ")
print(f"Depth and Branches ratio is {tree_depth}:{branch}")
for i in range(nodes_count):
    terminal_nodes.append(random.randint(int(min_limit),int(max_limit)))
print("Terminal States (Leaf Nodes) are ",terminal_nodes)

#terminal_nodes = [18,13,5,12,10,5,13,7,17,8,6,8,5,11,13,18]
point = alpha_beta_pruning(terminal_nodes)
print("Left life(HP) of the defender after maximum damage caused by the attacker is", initial_hp-point)
#print(alpha,beta)
print("After Alpha-Beta Pruning Leaf Node Comparisons",node_visit)

