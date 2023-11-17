import random

def population_generator():  
    population = []

    while len(population) < 100:
        new_population = []

        for i in range(transaction_count):  
            new_population.append(random.randint(0, 1))

        if (sum(new_population) > 0) and (new_population not in population):
            population.append(new_population)
    #print("population",population)
    return population

####################################################################################


def chromosome_crossover(father_chrom, mother_chrom): 
    crossing_point = transaction_count // 2 #need to change

    offspring1 = father_chrom[0: crossing_point] + mother_chrom[crossing_point: ]
    offspring2 = mother_chrom[0: crossing_point] + father_chrom[crossing_point: ]

    #print("offspring1",offspring1)
    #print("offspring2",offspring2)
    return offspring1, offspring2

#####################################################################################################################

def gene_mutation(gene):  
    index = random.randint(0, transaction_count-1)
    if gene[index] == 0:
        gene[index] = 1
    else:
        gene[index] = 0

#####################################################################################################################

def fitness(gene):  
    summation = 0
    for index in range(len(gene)):
        if gene[index]:
            summation += amount[index]
            
    #print(summation)
    return abs(target - summation)  

#####################################################################################################################


def genetic_algorithm():  
    population = population_generator()  
    children = []

    for iteration_count in range(1000):
        while len(population) > 1:
            index1 = random.randint(0, len(population)-1)
            index2 = random.randint(0, len(population)-1)

            while index1 == index2:
                index2 = random.randint(0, len(population) - 1)

            
            father_chrom = population[index1]
            mother_chrom = population[index2]

            
            offspring1, offspring2 = chromosome_crossover(father_chrom, mother_chrom)
          
            gene_mutation(offspring1)
            gene_mutation(offspring2)

            if fitness(offspring1) == 0:  
                #print(fitness_offspring1)  
                return offspring1
            if fitness(offspring2) == 0:  
                #print(fitness_offspring2)  
                return offspring2

          
            if sum(offspring1) == 0:
                offspring1 = None
            if sum(offspring2) == 0:
                offspring2 = None

       
            if offspring1:
                children.append(offspring1)
            if offspring2:
                children.append(offspring2)

            #clear the old gen
            population.remove(father_chrom)
            population.remove(mother_chrom)

        if len(population) == 1:  
            if fitness(population[0]) == 0:  
                #print(population_count) 
                return population[0]

        #new gen coming
        population = children  
        children = []  

    return -1  


#driver code##############################################################
file = open('Input_file.txt', 'r')
transaction_count = int(file.readline())
#print(transaction_count)

statement = []
amount = []

for line in file.readlines():
    #print(line)
    line = line.split(" ")
    if len(line) >= 2:
        statement.append(line[0])
        if line[0] == "l":
            amount.append(-1*int(line[1]))
        else:
            amount.append(1*int(line[1]))
    else:
        break

#print(statement)
#print(amount)
file.close()



target = 0
transaction_combination = genetic_algorithm()
#print("transaction_combination",transaction_combination)
#print(statement)
if sum(transaction_combination) == 0:
    print(-1)
else:
    print("".join(map(str, transaction_combination)))