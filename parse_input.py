import re
import numpy as np

def process_file(arg):
    #Input: a list containing parsed values of the form [-N, -y, -M, -a, -s, -i] from the parse_input module
    #Output: Data file in np.ndarray, each line of input file corresponds to a row, each number from file in a column
    N, i = arg[0], arg[5] #N and i values
    no_data = True
    with open(i) as file:
        for line in file:
            temp = re.findall(r'\d+', line) #Extract all numbers
            temp_data=list(map(float, temp)) #Map to float
            if len(temp_data) != N:
                raise TypeError("Error. Improper number of columns")
            if no_data: #Test if first line
                return_data=np.array(temp_data).reshape(1,N)
                no_data = False
            else:
                return_data=np.concatenate((return_data, np.array(temp_data).reshape(1,N)), axis=0) #Merge with current line
    return return_data
