# from number to default excel index (e.g A -> 1, AA -> 27, etc) 
def column_number_to_excel_index(col_number):
    col_label = ''
    quotient = col_number

    while quotient:
        quotient, remainder = divmod(quotient, 26)
        # adding 64 for correct ASCII values
        col_label = chr(remainder + 64) + col_label
    return col_label

def excel_index_to_number(excel_column):
    # take the left most letter, pop it out, multiply it by 26 * the length -1
    # e.g. AB -> pop A -> A is worth 26*1 + ord(Z) - ord(A)
    # leaves B
    # pop B -> B = 26 * 0 + ord(Z) - ord(B) = 2
    excel_column = list(excel_column)
    result = 0
    while excel_column:
        val = excel_column.pop(0) # get the leftmost letter
        if len(excel_column): 

            result += 26 * len(excel_column) * (ord(val) - ord('A') + 1)
        else:
            result += ord(val) - ord('A')
            
    return(result)

if __name__ == '__main__':
    input_col = input('Enter in an Excel column:')
    # excel_index = column_number_to_excel_index(input_col)
    numerical_index = excel_index_to_number(input_col)
    print(numerical_index)
    # print('Excel Column Equivalent:', excel_index)
