import sys
import os

def parse_input(args):
    #Input: argument list containing all options and corresponding values
    #Output: A list containing values of mandatory options called, 0 for an optional argument not called, and 1 for optional arguments called
    return_value = [0, 0, 0, 0, 0, 0] #corresponds to [-N, -y, -M, -a, -s, -i]
    input_flag = False #If next value of args should be input value
    for j in range(len(args)):
        if input_flag: #Skip parsing if input value
            input_flag = False
            continue
        working_arg = args[j]
        if len(working_arg) > 2 and working_arg[0] == '-': #Check for compact form, then break up arguments
            new_working_arg = []
            for k in range(len(working_arg)-1):
                if not working_arg[k+1] in ("M", "N", "a", "s", "i", "y"):
                    raise TypeError("Error. "+working_arg[k+1]+" is invalid option.")
                else:
                    new_working_arg.append(working_arg[k+1])
            if len(set(new_working_arg).intersection({'N', "i", "y"}))>1: #Check if contains multiple mandatory arguments
                raise TypeError("Error. Invalid input. Must separate -N, -i, and -y options.")
            working_arg = new_working_arg
        if "N" in working_arg: #Check if -N option called
            try: #Extract -N value
                arg = args[j+1]
                return_value[0]=int(arg)
            except:
                print("Error. -N must take int input")
                sys.exit()
            else: #Check if valid -N value
                if int(arg) < 2:
                    raise TypeError("Error. -N must be >= 2")
            input_flag = True
        elif "y" in working_arg: #Check if -y option called
            try: #Extract -y value
                arg = args[j+1]
                return_value[1]=int(arg)
            except:
                print("Error. -y must take int input")
                sys.exit()
            input_flag = True
        elif "i" in working_arg: #Check if -i called
            try: #Extract -i value
                arg = args[j+1]
                return_value[5]=arg
            except:
                print("Error. -i must take input")
                sys.exit()
            input_flag = True
        if  "M" in working_arg:
            return_value[2]=1
        if "a" in working_arg:
            return_value[3]=1
        if "s" in working_arg:
            return_value[4] = 1
            
    #Ensure valid input
    if return_value[0] == 0:
        raise TypeError("Error. No input for -N")
    if return_value[1] == 0:
        raise TypeError("Error. No input for -y")
    if return_value[5]==0:
        raise TypeError("Error. No input for -i")
    if sum(return_value[2:5]) == 0:
        raise TypeError("Error. Please call at least one of -M, -a, -s")
    if type(return_value[1]) != int or return_value[1] > return_value[0]:
        raise TypeError("Error. -y must be int <= N")
    if type(return_value[5]) != str or not os.path.isfile(return_value[5]):
        raise TypeError("Error. -i must be string of valid datafile name")
        
    return return_value

