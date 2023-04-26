import numpy as np
import numpy.linalg as la
from vars import table
import time

stime = 0

def Main():
    # input values from user and validate them 
    coded_string = input('Coded string: ').upper().strip()

    key_dimention = int(input('key dimention: '))

    key = list(map(int,input("key: ").strip().split()))[:key_dimention**2] 

    key = np.matrix(key, dtype=int).reshape(key_dimention,key_dimention)
    if (la.det(key) == 0):
        print('\nInvalid key: key matrix can not be inversed!')
        exit()

    global stime
    stime = time.time()

    # replace each character with assosiated value
    coded_matrix = []
    for char in coded_string:
        if char in table.keys():
            coded_matrix.append(table[char])
        else:
            raise ValueError("Unknown character.")
            
    # reshape the coded matrix for calcuation
    coded_matrix = np.matrix(coded_matrix, dtype = int).reshape(len(coded_matrix)//key_dimention, key_dimention).T

    # find the reverse of key matrix on mod of size-of-table
    det = la.det(key)
    mod_inverse_key = la.inv(key) * det * np.sign(det) * pow(round(abs(det)), -1, len(table))
    mod_inverse_key = mod_inverse_key.round().astype(int)
    mod_inverse_key = mod_inverse_key % len(table)

    # decode the matrix
    decoded_matrix = mod_inverse_key.dot(coded_matrix) % len(table)

    print(f'\nDecoded matrix:\n{decoded_matrix}')

    # reshape for string conversion
    decoded_matrix =  decoded_matrix.T.reshape(1, decoded_matrix.size)

    # convert to string
    decoded_string = ''
    for id,char in enumerate(np.nditer(decoded_matrix)):
            # get the character assisiated to each value from table
            result = dict((new_val,new_k) for new_k,new_val in table.items()).get(decoded_matrix[0,id])
            # get the character assisiated to each value from table
            decoded_string += result
    
    print(f'\nDecoded string:\n{decoded_string}\n')
    # END OF Main()
    
if __name__ == "__main__":
    Main()
    print("Decode time: {0:.2f} ms\n".format( (time.time() - stime) * 1000) )