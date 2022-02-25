import parse_input
import parse_file
import M
import a
import s
import sys

#Script to be ran with proper input. Utilizes modules to print requested statistics.
parsed_inputs = parse_input.parse_input(sys.argv[1:]) #[-N, -y, -M, -a, -s, -i]
parsed_data = parse_file.process_file(parsed_inputs)
if parsed_inputs[2]==1:
    return_value = M.main(parsed_data, parsed_inputs[1])
    print("Min of y: "+str(return_value[0]))
    print("Max of y: "+str(return_value[1]))
if parsed_inputs[3]==1:
    return_value = a.main(parsed_data, parsed_inputs[1])
    print("Mean of Columns: "+ str(return_value[0]))
    print("Mean Square of Columns " + str(return_value[1]))
if parsed_inputs[4]==1:
    print('Ratio of columns: ' + str(s.main(parsed_data, parsed_inputs[1])))
