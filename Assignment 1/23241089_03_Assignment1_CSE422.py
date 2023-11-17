
def a_star_search_algo(start,end,h_dict,pc_dict):
    #f(n) = h(n)+g(n)
    path_list = [(0,start,start)]#f(n),child,parent
    while True:
        path_list.sort()
        
        node = path_list[0]
        #print(node)
        current_node = node[1]
        if current_node == end:
            #print(current_node)
            break
        #print("h")
        parent_node = node[2]
        #print(node)
        path_cost = node[0]-h_dict[current_node]
        if path_cost<0:
            path_cost = 0
    
        for i in pc_dict[current_node]:
            #print(i)#(B,1)
            
            path_list.append((path_cost+i[1]+h_dict[i[0]],i[0],parent_node+"0"+i[0]))
        path_list.pop(0) 
        #break
    #print(path_list)

    
    print("Path:",end="")
    for i in path_list[0][2]:
        if i!="0":
            print(i,end="")
        else:
            print(" --> ",end="")
    print()
    print('Total distance:',path_list[0][0],"km")
        
    
    #pass

parent_child_dict = {}
parent_child_count = 0
heuristic_dict={}
heuristic_count = 0

try:
    with open("Input file.txt") as file:
        #print(file.read())
        while True:
            file_contents = file.readline().split(" ")
            if len(file_contents)<2:
                break
            else:
                #print(file_contents)
                heuristic_dict[file_contents[0]] = int(file_contents[1])
                heuristic_count +=1
                child_list = []
                for i in range(2,len(file_contents)-1,2):
                    child_list.append((file_contents[i],int(file_contents[i+1])))
                parent_child_dict[file_contents[0]] = child_list
                parent_child_count+=1
                #print(child_list)
                
except FileNotFoundError:
    print("Missing")
#print("heuristic_dict",heuristic_dict)
#print("#################################################")
#print("parent_child_dict", parent_child_dict)

start_node = input("Enter Full form of Starting Place: ")
end_node = input("Enter Full form of Ending Place: ")
if start_node in heuristic_dict and end_node in heuristic_dict:
    a_star_search_algo("Arad","Bucharest",heuristic_dict,parent_child_dict)
else:
    print("NO PATH FOUND")