import numpy as np
import itertools


def add_two_colum(array_1,array_2,column_1,column_2):
    '''
    description : take 2 array and add two column column 1 and column 2 from each array
    :param array_1:  2d array
    :param array_2:  2d array
    :param column_1: index of first column
    :param column_2: index of second column
    :return: output 1d array
    '''
    output=[]
    array_len=len(array_1)
    for i in range(array_len):
        output.append(array_1[i][column_1]+array_2[i][column_2])
    return output

def add_two_colum_as_2_col(column_1,column_2):
    '''
    description : taking 1d array colm 1 and colm 2 and sum them
    :param column_1:  1d array
    :param column_2:  1d array
    :return: output , 1d array
    '''
    array_len=len(column_1)
    output=[]
    for i in range(array_len):
        output.append(column_1[i]+column_2[i])
    return output

def remove_redundant(string,redundant):
    '''
    description : built in, take input a1b1a1c1 -> a1b1c1
    :param string:
    :param redundant:
    :return:a1+b1+c1
    '''
    output=string.split(redundant)
    output[0]=redundant
    output_str=""
    for i in range(len(output)):
        output_str=output_str+output[i]+"+"

    output_str=output_str[0:len(output_str)-1]
    return output_str


def filter_final_form(final_form):
    '''
    description : clear the final form from the redundant, and re assign the values
    :param final_form:
    :return:
    '''
    i=0
    for element in final_form:
        # this is a1b1a1c1d1
        first_and_second_charchter= element[0]+element[1]
        output=remove_redundant(element,first_and_second_charchter)
        final_form[i]=output
        i=i+1

def return_array_column(array,column_number):
    '''
    description : return 1d array, given from 2d array input with column index = column number
    :param array: 2d array
    :param column_number: int , index
    :return: 1d array
    '''
    array_len = len(array)
    output=[]
    for i in range(array_len):
        output.append(array[i][column_number])
    return output

def set_array_column(arrayx,column_number,column):
    '''
    description : set a column in 2d array, given the 1d column
    :param arrayx: 2d array
    :param column_number:  int, the number of the colum
    :param column: 1d array, the given column
    :return: void
    '''
    array_len = len(arrayx)
    for i in range(array_len):
        arrayx[i][column_number]=column[i]


def create_array_from_another(main):
    '''
    descritpion : insted of using .copy(), use this for safe copy array
    :param main: 2d array i need a copy of it
    :return: 2d array same value as main
    '''
    create_dumy=main.copy()
    array_size=len(main)
    for i in range(array_size):
        create_dumy[i]=main[i].copy()
    return create_dumy

def count_each_element_in_a_colum(array):
    '''
    description : count how many times the column has this element in it
    :param array: 2d array
    :return: dictionary has all the combinations count
    '''
    if is_empty(array):
        return []
    number_of_coulmn=len(array[0])


    output_dictionary={}
    for column_number in range(number_of_coulmn):
        #for ever column
        previous_element = {}
        this_column=return_array_column(array,column_number)
        #print(this_column,"this")
        #print(this_column,"the column")
        for element in this_column:
            if element in previous_element:
                continue
            else:
                previous_element.update({element:1})
                output_dictionary.update({element:this_column.count(element)})
        #print(previous_element,"the element in this colum")
    return output_dictionary

def print_2d_array(array):
    '''
    description : print 2d array
    :param array: 2d array
    :return: void
    '''
    if array !=[]:
        array_len = len(array)
        numper_of_coulm=len(array[0])
        for i in range(array_len):
            print(array[i][0:numper_of_coulm])


def reform_array(array):
    '''
    description : swap the column with the rows
    :param array: 2d array
    :return: 2d array
    '''
    dump=create_array_from_another(array)
    output=[]
    for i in range(len(dump[0])):
        output.append(return_array_column(dump,i))

    return output

def from_array_to_string_with_plus(array):
    '''
    description: take array of string and add + between every element
    :param array: array of string
    :return: array of string with + between every element
    '''
    output=""
    for element in array:
        output=output+element+"+"

    return output[0:len(output)-1]

def combine_array_column_with_couple_of_size_x(array,couple_size):
    '''
    description: make every possible combination of size couple_size for a row in array
    like a,b,c with couple size of 2 becomes-> a+b,a+c,b+c and so on
    :param array: 2d array contain the data
    :param couple_size: int, variable of the combination size
    :return: a new output array made of the combination
    '''
    array_len=len(array)
    number_of_column=len(array[0])

    if couple_size > number_of_column:
        return []

    output_array=[]
    for row in range(array_len):

        row_elements = []
        for subset in itertools.combinations(array[row], couple_size):
            one_element_in_row = []
            for element in subset:
                one_element_in_row.append(element)

            one_element_in_row_str=from_array_to_string_with_plus(one_element_in_row)
            row_elements.append(one_element_in_row_str)
        output_array.append(row_elements)

    return output_array

def is_empty(array):
    '''
    description : check if the array is empty or no
    :param array: 1d array or 2d array
    :return: true if it's empty, false if it'snot  empty
    '''
    if array==[]:
        return True
    else:
        return False

def return_elements_with_min_support(dictionary,min_support):
    '''
    description: taking dictionary and return list of the elements in this dictionary that
    passed the min support
    :param dictionary: dictionary contain the variable name and the support value for it
    :param min_support: min support value, int
    :return: list os names of passed variables
    '''
    success_list=[]
    for element in dictionary:
        support=dictionary[element]
        if support >=min_support:
            success_list.append(element)
    return success_list


def main(array,min_support):
    '''
    description: main function that get the min support item set for the given table
    :param array: 2d array contain data
    :param min_support: int, min support value
    :return: the min sets item and dictionary containing the support of all previous success min sets
    '''
    not_empty=True
    prev_list=[]
    prev_count_dictionary=[]
    iterator=1
    while not_empty:
        if iterator==1:
            count_dictionary = count_each_element_in_a_colum(array)
        else:

            combine_matrix=combine_array_column_with_couple_of_size_x(array,iterator)

            #print_2d_array(combine_matrix)
            count_dictionary = count_each_element_in_a_colum(combine_matrix)



        list_of_success=return_elements_with_min_support(count_dictionary,min_support)
        iterator = iterator+1
        if is_empty(list_of_success):
            output_dic={}
            for element in prev_count_dictionary:
                output_dic.update(element)

            return prev_list,output_dic
        else:
            prev_list=list_of_success
            prev_count_dictionary.append(count_dictionary)

def get_combination_of_min_set(string):
    '''
    description: taking string like,  A+B+C and makes every possible combination rule of this string
    like A->B+C,B->A+C,A+B->C and so on ...
    and return an dictionary made of this rules
    :param string: rule A+B+C
    :return: dictionary containing every rule left hand side and right hand side
    '''
    new_string=string.split("+")
    conf={}

    for L in range(1, len(new_string) ):
        for subset in itertools.combinations(new_string, L):
            left_hand=[]
            right_hand = []
            for element in subset:
                left_hand.append(element)
            for element in new_string:
                if left_hand.count(element)<1:
                    right_hand.append(element)

            left_hand = from_array_to_string_with_plus(left_hand)
            right_hand = from_array_to_string_with_plus(right_hand)
            conf.update({left_hand:right_hand})

    return conf

def get_conf_lift(small_dict,big_dict,all_elements,min_conf):
    '''
    description: get he conf, lift and leverage of a rule give the min_conf as first phase filter
    :param small_dict:string, the rule as left condition, example: A+b->c+d , A+b is the small dict
    :param big_dict: dictionary contain all elements support, like support of col_1:0 = 522, support of col_1:0 and col_2:1 =255
    :param all_elements: the whole rule as string, A+B->C+D
    :param min_conf: min value for conf
    :return:
    '''
    output_dictionary=[]
    for element in small_dict:
        left_value=big_dict[element]/5822
        total_value=big_dict[all_elements]/5822
        right_value = big_dict[small_dict[element]]/5822

        conf=total_value/left_value


        if (conf>=min_conf):
            #print("rule :",element,"->",small_dict[element])
            #print("conf = ",conf)

            rule_name=element+"->"+small_dict[element]
            rule_conf=conf
            lift = total_value / (right_value*left_value)
            rule_lift =lift
            #print("lift = ",lift)

            lev = total_value - (right_value * left_value)
            rule_lev=lev
            #print("leverage = ",lev)


            #print("============")
            temp_dictionary={"rule":rule_name,"conf":rule_conf,"lift":rule_lift,"leverage":rule_lev}
            output_dictionary.append(temp_dictionary)

    return output_dictionary






def sort_sets_based_on_support(sets,all_dictionary):
    '''
    description : sort array of min sets(string) in the order of the support value
    :param sets: 1d array of strings
    :param all_dictionary: contain all min sets support
    :return:1d array of string, sorted min sets
    '''
    def sort_key_for_set_support(set):
        return all_dictionary[set]

    sorted_sets= sorted(sets,key=sort_key_for_set_support,reverse=True)

    return sorted_sets

def sort_array_based_on_lift(rules):
    '''
    description : take array of dictionary example of first element {"name" : "X->y, "lift": value,"leverage" : value }
    :param rules: 1d array of dictionaries of the rules
    :return:sorted array of dictionary based on the lift
    '''

    def sort_key_for_set_lift(dictionray):
        return dictionray["lift"]
    sorted_on_lift=sorted(rules,key=sort_key_for_set_lift,reverse=True)
    return sorted_on_lift
#key_for_dicionary_to_search(test_array)



def main_exe(min_support,min_conf,data_size=5822,array_number_of_col=[12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],test_array=[]):
    '''
    description: run to use function
    :param min_support: min support of the user input
    :param min_conf: min confidence of the user input
    :param data_size: the number of rows
    :param array_number_of_col: number of cols in the data file
    :param test_array: test array if given
    :return:
    '''
    print("\nrunning...\n")
    ########################### cleansing the data ##########################
    data = np.loadtxt('ticdata2000.txt', delimiter="\t", skiprows=0,
                      usecols=array_number_of_col)
    data = data.transpose()
    new_data = data.tolist()


    col_names=[
               " MFALLEEN : "," MFGEKIND : "," MFWEKIND : "," MOPLHOOG : "," MOPLMIDD : "," MOPLLAAG : ",
               " MBERHOOG : "," MBERZELF : "," MBERBOER : "," MBERMIDD : "," MBERARBG : "," MBERARBO : "
               ]

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            new_data[i][j] = col_names[i] + str(int(data[i][j]))+" "

    new_data = np.array(new_data)
    new_data = new_data.transpose()
    new_data = new_data.tolist()
    if not is_empty(test_array):
        new_data=test_array
    min_support = (data_size * min_support)

    ##################################################################################

    ################### running the min support function ##################
    min_sets, all_dictionary = main(new_data, min_support)
    print("min sets : ")
    ########sorting#########
    min_sets=sort_sets_based_on_support(min_sets,all_dictionary)
    for set in min_sets:
        print(set,", with support =",all_dictionary[set]/data_size)
        print()
    print("===========================================")
    ##############################################################################

    ############# running the min conf ###################
    array_of_conf_lift_lev_dictionary=[]
    for set in min_sets:
        output = get_combination_of_min_set(set)
        array_of_conf_lift_lev_dictionary.extend(get_conf_lift(output, all_dictionary, set, min_conf))
    ############## sorting ############
    array_of_conf_lift_lev_dictionary_sorted=sort_array_based_on_lift(array_of_conf_lift_lev_dictionary)
    for element in array_of_conf_lift_lev_dictionary_sorted:
        print(element)
        print("===========================================")


if __name__=='__main__':
    min_support=input("please enter the min support = ")
    min_conf=input("please enter the min confidence = ")
    min_support=float(min_support)
    min_conf=float(min_conf)
    ###########running the main##################
    main_exe(min_support,min_conf)
