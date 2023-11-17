import numpy as np
from array import *
import random
from numpy.random.mtrand import randint

target = 0
random_transaction = []
max_val = 0
captureIndividual = []
def Population():
    global target,random_transaction, trans_count
    sample = []
    sample_2 = []
    sample = transaction
    sample_2 = transaction
    random_transaction = np.random.randint(0,2,(trans_count,trans_count))
    print(random_transaction)
    random_transaction_temp = np.random.randint(0, 2, (trans_count,trans_count))         # We will use this later to build the next Generation
    summation = np.zeros((trans_count,trans_count))
    print("sum",summation)
    random_transaction = np.append(random_transaction, summation, axis=1)
    
    Transaction(sample,sample_2)

def Transaction(sample,sample_2):
    global trans_count, captureIndividual
    for q in range(trans_count):
        for i in range(trans_count):
            addition1 = sum(np.multiply(sample, random_transaction[i, 0:trans_count]))  # Calculating Total sum
            if addition1 == target:
                captureIndividual = random_transaction[i, 0:trans_count]
                max_val = addition1
            random_transaction[i, trans_count] = addition1
            addition2 = sum(np.multiply(sample_2, random_transaction[i, 0:trans_count]))
            if addition2 == max_val:
                captureIndividual = random_transaction[i, 0:trans_count]
                max_val = addition2
            random_transaction[i, trans_count + 1] = addition2
    print("capture", captureIndividual)
    print("max_val",max_val)
    
    #pass
    
    
    
    #pass
#driver code

#transaction = []
#trans_count = int(input("Daily transaction: "))
#loop = trans_count
#while loop!=0:
    #status,amount = input("enter statement: ").split(" ")
    ##print(status)
    #if status == "l":
        #transaction.append(-1*int(amount))
    #else:
        #transaction.append(int(amount))
    #loop -=1
#print(transaction)



#print(random_transaction)

graph_matrix = []                   # 2D matrix that will read the file
transaction = []                     # 1D list of integers gotten by manipulating the first 2D matrix


# ============================== reading text file and inputting in the matrix ===========================

with open("input.txt", 'r') as file:
    lines = file.readlines()
for line in lines:
    graph_matrix.append(line.split())
print("Input : ", graph_matrix)
count = graph_matrix[0]
print("trans",count)
trans_count = int(count[0])                     # number of transactions                           # number of individuals per Generation

# ============================== converting matrix to 1D suitable model ==================================

for row in range(len(graph_matrix)):        # we don't need the column because l or d sits on the first index
    if graph_matrix[row][0] == 'l':         # if the amount was being lend
        transaction.append(-1 * int(graph_matrix[row][1]))  # we consider lend as negative
    elif graph_matrix[row][0] == 'd':       # if the amount was being deposited
        transaction.append(int(+1 * graph_matrix[row][1]))  # we consider deposit as positive
print("Values : ", transaction)
Population()