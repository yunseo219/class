"""
Inverse Burrows-Wheeler Transform Problem: Reconstruct a string from its Burrows-Wheeler transform.

Input: A string Transform (with a single "$" symbol).
Output: The string Text such that BWT(Text) = Transform.

Sample Input:
TTCCTAACG$A

Sample Output:
TACATCACGT$
"""
#ValueError: 9 is not in list

def inverse_bwt(transform):
    # create a list of tuples containing each character and its index in the transform
    tuples = [(char, i) for i, char in enumerate(transform)]
    
    # sort the list of tuples by character
    sorted_tuples = sorted(tuples)
    
    # get the index of the original row (the row that ends with "$")
    original_row_index = transform.index("$")
    
    # initialize the "last" column to the sorted characters in the last column
    last_column = [t[0] for t in sorted_tuples]
    
    # initialize the "first" column to the last column
    first_column = last_column.copy()
    
    # iterate through the characters in the last column
    for i in range(len(transform) - 1):
        # insert the "last" column as a new column to the left of the "first" column
        first_column = [last_column[j] + first_column[j] for j in range(len(transform))]
        
        # sort the "first" column
        sorted_first_column = sorted(first_column)
        
        # update the "last" column to be the last character in each string in the sorted "first" column
        last_column = [string[-1] for string in sorted_first_column]
    
    # find the row in the "first" column that corresponds to the original row (the row that ends with "$")
    original_row = first_column[original_row_index]
    
    # reconstruct the original string from the last column and the original row
    reconstructed = original_row
    for i in range(len(transform) - 2, -1, -1):
        char = last_column[original_row_index]
        original_row_index = first_column.index(original_row_index)
        reconstructed = char + reconstructed
    
    # return the reconstructed string, without the "$" character at the end
    return reconstructed[:-1]

transform = "TTCCTAACG$A"
text = inverse_bwt(transform)
print(text)
