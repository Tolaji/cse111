import math

class SelfEsteemScale:
    '''
    A class representing the Rosenberg self-esteem scale
    Args:
            strongly_disagree(str): strongly disagrees with self esteem statement
            disagree(str): disagrees with self esteem statement
            agree(str): agrees with self esteem statement
            strongly_agrees(str): strongly agrees with self esteem statement
    '''
    positive_choices = {'D': 0, 'd': 1, 'a': 2, 'A': 3}
    negative_choices = {'D': 3, 'd': 2, 'a': 1, 'A': 0}
    total_score = 0
  
    
    
    
    def __init__ (self):
        '''
        Initializes a new instance of SelfEsteemScale
        Args:
            strongly_disagree(str): strongly disagrees with self esteem statement
            disagree(str): disagrees with self esteem statement
            agree(str): agrees with self esteem statement
            strongly_agrees(str): strongly agrees with self esteem statement

        '''
        

    def esteem_statements_definition(self, positive_choices, negative_choices, total_score, statements):
        '''
        Initializes a new instance of SelfEsteemScale
        Args:
            strongly_disagree(str): strongly disagrees with self esteem statement
            disagree(str): disagrees with self esteem statement
            agree(str): agrees with self esteem statement
            strongly_agrees(str): strongly agrees with self esteem statement

        '''
        
        print('This program is an implementation of the Rosenberg')
        print('Self-Esteem Scale. This program will show you ten')
        print('statements that you could possibly apply to yourself')
        print('Please rate how much you agree with each of the')
        print('statements by responding with one') 
        print('-*60')
        print('D: means you strongly disagree with the statement.')
        print('d: means you disagree with the statement.')
        print('a: means you agree with the statement.')
        print('A: means you strongly agree with the statement.')
        print('-*60')
        print()
        print('1. I feel that I am a person of worth, at least on an equal plane with others.')
        input('Enter D, d, a, or A: ')
        print('2. I feel that I have a number of good qualities.')
        input('Enter D, d, a, or A: ')
        print('3. All in all, I am inclined to feel that I am a failure.')
        input('Enter D, d, a, or A: ')
        print('4. I am able to do things as well as most other people.')
        input('Enter D, d, a, or A: ')
        print('5. I feel I do not have much to be proud of.')
        input('Enter D, d, a, or A: ')
        print('6. I take a positive attitude toward myself.')
        input('Enter D, d, a, or A: ')
        print('7. On the whole, I am satisfied with myself.')
        input('Enter D, d, a, or A: ')
        print('8. I wish I could have more respect for myself.')
        input('Enter D, d, a, or A: ')
        print('9. I certainly feel useless at times.')
        input('Enter D, d, a, or A: ')
        print('10. At times I think I am no good at all.')
        input('Enter D, d, a, or A: ')
        
        # Iterate through each statement
        for statement in statements:
            response = input(statement + " (D/d/a/A): ")

        # Check if the statement is positive or negative and update the total score accordingly
        if statements.index(statement) in [0, 1, 3, 5, 6]:
            total_score += positive_choices[response]
        else:
            total_score += negative_choices[response]
        return total_score, positive_choices, negative_choices
        
def main():
    scale = SelfEsteemScale()
    scale.esteem_statements_definition()
    print(f"The person's total score is: {scale.total_score}")

if __name__ == "__main__":
    main()
    
    
    
        
        
        
        
