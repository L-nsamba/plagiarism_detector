
print("")
print("===========================")
print("PLAGIARISM DETECTOR")
print("===========================")
print("")

def file_reader():

    """"Function that reads the files 'essay1.txt'
        and 'essay2.txt' entered by the user
        and stores their respective content
        in two different dictionaries"""

    while True:
        try:
            #Prompt for user to enter specified essay names.
            file_name = input("Enter 'essay1.txt' or 'essay2.txt' : ")
            print("")
            if file_name == 'essay1.txt':
                #Variable to open and read the content of the specified essay.
                fhand = open('essay1.txt', 'r')
                content = fhand.read()
                print("*** Essay content *** ")
                #Print message to display the essay content
                print(content)
                fhand.close()
                break

            elif file_name == 'essay2.txt':
                #Variable to open and read the content of the specified essay.
                fhand = open('essay2.txt', 'r')
                content = fhand.read()
                print("*** Essay content *** ")
                print("")

                #Print message to display the essay content
                print(content)
                fhand.close()
                break

            else:
                """Print message displayed when user enters a file name
                    that is not either 'essay1.txt' or 'essay2.txt'"""
                print("Incorrect essay file name.")

                """"Error message displayed when main file is run from
                    location where essay files are not present or in the
                    case of permission restrictions"""
        except (FileNotFoundError, PermissionError):
            print("File Not Found. Access correct folder to run program")

    """Creation of a dictionary to store words keys and values
    which will display words and number of appearances"""
    word_dict = dict()

    for lines in content.split():
        #Striping essay lines to remove white space
        lines = lines.rstrip()
        #Splitting strings in the essays into a list of substrings
        words = lines.split()

        #Targeting individual words in the list of substrings
        for word in words:
            word = word.lower().strip(".,!?\"'()")

            """Adding new words to the dictionary created, under keys section
            and adding one to the value section each time a word reappears"""
            word_dict[word] = word_dict.get(word, 0) + 1

    return word_dict, file_name

#List to store the file names
selected_essays = []

#Calling the file reader function to prompt user to enter the file names
print("Essay 1: ")
"""Output returned from the first essay entered by user
is stored in this function with a file name variable"""
essay1_words, essay1_name = file_reader()

#Storing the file name into the selected essays list
selected_essays.append(essay1_name)


print("")
print("Essay 2: ")
"""Output returned from the second essay entered by user
is stored in this function with a file name variable"""
essay2_words, essay2_name = file_reader()

#Error handling if user enters the same essay name twice
if essay2_name in selected_essays:
    print("")
    print("Warning: You have entered the same file name twice!")
    print("Plagiarism percentage will be 100%.")

    while True:
        #Offering user a chance to exit program or continue with the two same essays
        decision = input("Do you wish to continue? [y/n]: ")
        if decision == "y":
            print("Continuing with plagiarism detector.")
            break
        elif decision == "n":
            print("Enter 'essay2.txt' or 'essay1.txt' but not both.")
            quit()
        else:
            print("Invalid entry")

#Identifying common words in both essays
common_words = set(essay1_words) & set(essay2_words)

#Creation of word search function
def word_searcher():

        """"Function that displays menu with prompts
            to either display common words, search
            for specific word or calculate the plagiarism
            percentage"""


        while True:
            print("")
            print("===========================")
            print(" MAIN MENU ")
            print("===========================")
            print("")
            print("1. Display common words in both essays")
            print("2. Search for specific word.")
            print("3. Calculate Plagiarism Percentage.")
            print("4. Exit program. ")
            print("")

            user_selection = input("Enter choice[1-4]: ")
            if user_selection == "1":
                print("===========================")
                print("COMMON WORDS IN BOTH ESSAYS")
                print("===========================")


                """Extracting the value corresponding to appearances
                in the respective dictionaries where both essay list substrings were stored"""
                for word in sorted(common_words):
                    print("")
                    print(f"""WORD: '{word}'
Appearances in Essay 1: {essay1_words[word]}
Appearances in Essay 2: {essay2_words[word]}""")
                    print("")


            elif user_selection == "2":
                while True:
                    """Prompt for user to enter a word of choice to determine if it appears in any of the
                    essays and how may times it appears"""
                    search_word = input("Enter the word you are searching for: ").lower().strip(".,!?[]\"'")


                    """Error handling for cases where user does not enter any text
                        or enters an integer or float instead of a string"""
                    if not search_word or not search_word.isalpha():
                        print("Error: You must enter a word.")
                        continue
                    break

                """Variable that look through the dictionaries where the essay content
                    was stored and stored the number of times it appears"""
                essay_one_count = essay1_words.get(search_word, 0)
                essay_two_count = essay2_words.get(search_word, 0)

                #Verification of if a word exists in one or none of the essays
                if essay_one_count == 0 and essay_two_count >= 1:
                    print(f"Appearances in essay two: {essay_two_count}. Word not in essay one.")
                elif essay_two_count == 0 and essay_one_count >= 1:
                    print(f"Appearances in essay one: {essay_one_count}. Word not found in essay two.")
                elif essay_one_count == 0 and essay_two_count == 0:
                    print("Word not found in both essays")
                else:
                    print("")
                    print(f"""WORD: '{search_word}':
Appearances in Essay 1 : {essay_one_count}
Appearances in Essay 2 : {essay_two_count} """)



            elif user_selection == "3":
                print("")
                print("===========================")
                print("PLAGIARISM CHECKER")
                print("===========================")
                print("")


                #Extracting the unique words in both essays
                unique_words  = set(essay1_words) | set(essay2_words)

                """"Finding the similarity score through dividing the number
                    of common words by number of unique words and multiplying
                    by 100% to get it as a percentage score """
                similarity_score = float((len(common_words)/ len(unique_words)) * 100)
                #Rounding off the similarity score to the nearest 2 decimal places
                similarity_score = round(similarity_score, 2)

                #Print message for if similarity score is below or above 50%
                if similarity_score < 50 :
                    print(f"Similarity score: {similarity_score}%")
                    print(f"Your similarity score of {similarity_score}% is below the plagiarism warning.")
                elif similarity_score >= 50 :
                    print(f"Warning: Your similarity score of {similarity_score}% is above the plagiarism warning.")
                else:
                    break

            elif user_selection == "4":
                print("Exiting the program...")
                break
            else:
                print("Invalid selection. Please try again")

#Calling function to run the word_searcher logic
word_searcher()
