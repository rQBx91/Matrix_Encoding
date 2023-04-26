import numpy as np
import numpy.linalg as la
from vars import table
import time


stime = 0

def Main():
    # input values from user and validate them 
    input_string = input('Input string: ').upper().strip()

    key_dimention = int(input('key dimention: '))

    key = list(map(int,input("key: ").strip().split()))[:key_dimention**2] 

    key = np.matrix(key, dtype=int).reshape(key_dimention,key_dimention)
    if (la.det(key) == 0):
        print('\nInvalid key: key matrix can not be inversed!')
        exit()

    global stime
    stime = time.time()

    # replace each character with assosiated value
    # if not found assign value of '_'
    input_matrix = []
    for char in input_string:
        if char in table.keys():
            input_matrix.append(table[char])
        else:
            input_matrix.append(table['_'])

    # append '_' to fit the size
    while(len(input_matrix) % key_dimention != 0):
        input_matrix.append(table['_'])  

    # reshape the input matrix for calcuation
    input_matrix = np.matrix(input_matrix, dtype = int).reshape(len(input_matrix)//key_dimention, key_dimention).T

    print(f'\nInput matrix:\n{input_matrix}')

    # encode the input matrix
    encoded_matrix = key.dot(input_matrix)

    print(f'\nEncoded matrix:\n{encoded_matrix}')

    # reshape the encoded matrix to 1 row and map the values from 0 to size-of-table
    encoded_matrix = (encoded_matrix%(len(table))).T.reshape(1,encoded_matrix.size)

    # convert the reshaped matrix to an encoded string
    encoded_string = ''
    for id,char in enumerate(np.nditer(encoded_matrix)):
            # get the character assisiated to each value from table
            result = dict((new_val,new_k) for new_k,new_val in table.items()).get(encoded_matrix[0,id])
            # get the character assisiated to each value from table
            encoded_string += result
    
    print(f'\nEncoded string:\n{encoded_string}\n')
    # END OF Main()

if __name__ == "__main__":
    Main()
    print("Encode time: {0:.2f} ms\n".format( (time.time() - stime) * 1000) )