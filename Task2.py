#Why does print_list() not correctly print out the elements a_list?

def print_list(a_list):
#BEFORE: for i in range(1, len(a_list)):
    for i in range(len(a_list)):
        #BEFORE: print('Element {} = {}'.format(str(i), str(a_list[i])))
        print('Element {} = {}'.format(str(i+1),str(a_list[i])))

a_list = [1, 2, 3, 5, 7, 9]
print_list(a_list)

#ISSUE: Python list starts with 0 rather than 1, so in order to change that we need to tell a system that i should be +1 (otherwise it will be 0 and will print only 5 elements) and to remove i from a loop statement.
