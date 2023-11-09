import csv

# Indexes of the columns
I_NUMBER_INDEX = 0
NAMES_INDEXES = 1

def main():
    
    #student_data = read_dictionary("students.csv")
    
    # Call compound list
    compound_list = read_dictionary('students.csv', NAMES_INDEXES)
    
    
    # Get I-Number of student name
    student_name = input('Provide the I-Number of the student you wish to find: ')
    
    # Find the corresponding student name in dictionary
    if student_name in compound_list:
        
        print(student_name)
        
    else:
        print('Student I-Number does not exists')
    

    

def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """

    # Empty list to store data
    compound_list = []
    
    # the CSV file for reading
    with open(filename, 'rt') as csv_file:
        
        # Reader object to read from the opened csv file
        reader = csv.reader(csv_file)
        
        # Skip the first line as it contains only headings
        next(reader)
        
        # Read the other lines into a dictionary
        for row in reader:
            
            # If current row not blank append to compound list
            if len(row) != 0:
                
                print(row)
                
                # Append to compound list
                compound_list.append(row)
                
    # Return the compound list
    return compound_list
    
# Call main to start the program
if __name__ == "__main__":
    main()
