# from number to default excel index (e.g A -> 1, AA -> 21, etc) 
def column_number_to_excel_index(col_number):
    col_label = ''
    quotient = col_number

    while quotient:
        quotient, remainder = divmod(quotient, 26)
        # adding 64 for correct ASCII values
        col_label = chr(remainder + 64) + col_label
    return col_label

# def excel_index_to_number(excel_column):

if __name__ == '__main__':
    input_col = input('Enter in decimal number:')
    excel_index = column_number_to_excel_index(input_col)
    print('Excel Column Equivalent:', excel_index)
