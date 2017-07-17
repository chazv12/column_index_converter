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
    # take the left most letter, pop it out, get it's value (base 26 to decimal)
    excel_column = list(excel_column)
    result = 0
    while excel_column:
        left_letter = excel_column.pop(0) # get the leftmost letter
        letter_value = ord(left_letter) - ord('A') 
        if len(excel_column): 
            result += 26 ** len(excel_column) * (letter_value + 1)
        else:
            result += letter_value + 1
    # result is one indexed, like Excel & VBA        
    return result

def column_difference(col1,col2):
    # returns the number of columns between 2 excel indices
    return abs(excel_index_to_number(col1) - excel_index_to_number(col2))

if __name__ == '__main__':
    
    input_col = input('Enter in an Excel column:').upper().strip()
    # excel_index = column_number_to_excel_index(input_col)
    numerical_index = excel_index_to_number(input_col)
    print(numerical_index)
    # print('Excel Column Equivalent:', excel_index)
