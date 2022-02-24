import re
import numpy as np

def process_file(arg):
    N, y, i = arg[0], arg[1], arg[5]
    no_data = True
    with open(i) as file:
        for line in file:
            temp = re.findall(r'\d+', line)
            temp_data=list(map(int, temp))
            if len(temp_data) != N:
                raise TypeError("Error. Improper number of columns")
            if no_data:
                return_data=np.array(temp_data)
                no_data = False
            else:
                return_data=np.stack((return_data, np.array(temp_data)))
    return return_data