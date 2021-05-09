def opening():
    """ Just prints the opening of the game.
    :return: None
    """
    HANGMAN_ASCII_ART = """       _    _
      | |  | |
      | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
      |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
      | |  | | (_| | | | | (_| | | | | | | (_| | | | |
      |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                           __/ |
                          |___/ \n"""
    MAX_TRIES = 6
    print (HANGMAN_ASCII_ART, MAX_TRIES, sep = "")
    
def check_win(secret_word, old_letters_guessed):
    """Checks if the player already guessed all of the letters of the secret word.
    Returns True or False.
    :param secret_word: the secret word
    :param old_letters_guessed: the old letters guessed by the user
    :type secret_word: str
    :type old_letters_guessed: list of strings
    :return: True or False
    :rtype: bool
    """
    correct_letters_count = 0
    for letter in secret_word:
        if letter in old_letters_guessed:
            correct_letters_count +=1
    if correct_letters_count == len(secret_word):
        return True
    else:
        return False
    
def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {0: """
    x-------x""", 1: """
    x-------x
    |
    |
    |
    |
    | """, 2:"""
    x-------x
    |       |
    |       0
    |
    |
    | """, 3: """
    x-------x
    |       |
    |       0
    |       |
    |
    | """, 4: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    | """, 5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    | """, 6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    | """}
    print (HANGMAN_PHOTOS[num_of_tries])

def choose_word(file_path, index):
    """Gets a path of a text file with a repertoire of words and an integer.
    Return the number of unique words(not duplicates) and 
    :param file_path: path to a file
    :param index: number of desired word
    :type file_path: str
    :type index: int
    :return: the word in the position of the entered integer(index)
    :rtype: str    # used to be a tuple
    """
    file = open(file_path, "r")
    file_as_string = file.read()
    words_repertoire = file_as_string.split(" ")
    unique_words = []
    for word in words_repertoire:
        if word not in unique_words:
            unique_words.append(word)
    number_of_words = len(unique_words)
    count = 0
    word_position = 0
    while count < index:
        chosen_word = words_repertoire[word_position]
        word_position += 1
        if word_position == words_repertoire.index(words_repertoire[-1]) + 1:
            word_position = 0
        count += 1
    file.close()     
    # used to return number_of_words as well. as part of a tuple.
    return chosen_word
    
def check_valid_input(letter_guessed, old_letters_guessed) :
    """Checks if the user input is valid.
    :param letter_guessed: letter guessed by the user. str.
    :param old_letters_guessed: list of the old letters guessed. list.
    :return: True or False 
    :rtype: bool
    """
    if letter_guessed.isalpha() == False :
        return False
    elif len(letter_guessed) > 1 :
        return False
    elif old_letters_guessed.count(letter_guessed) > 0 or old_letters_guessed.count(letter_guessed.lower()) > 0:
        return False
    else:
        return True
    
def show_hidden_word(secret_word, old_letters_guessed=[]):
    """Returns the secret word containing only the correct guesses with the rest of it as underscores and spaces.
    :param secret_word: the secret word the user must find. str.
    :param old_letters_guessed: list of the old letters guessed. list.
    :return: the parts of the secret word the user found so far.
    :rtype: str
    """
    word_so_far = ["_", " "] * len(secret_word)
    for number in range(len(secret_word)):
        if secret_word[number] in old_letters_guessed:
            word_so_far[number*2] = secret_word[number]
    word_so_far = "".join(word_so_far)
    return word_so_far

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """If there is an input error return False, print X and all the old letters guessed.
    Otherwise return True and add the new typed letter to the list of the old ones.
    :param letter_guessed: str
    :param old_letters_guessed: list
    :rtype: bool
    """
    # The first line joins, lowers, and sort the old letters alphabetly. Used later for printing the old letters at False cases.
    old_letters_guessed_joined = " -> ".join(sorted(old_letters_guessed, key=str.lower)).lower()
    if check_valid_input(letter_guessed, old_letters_guessed) == False:
        print ("X")
        print (old_letters_guessed_joined)
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        return True

def main():
    opening()
    repertoire_path = input("Please enter a file path to a word repertoire, txt file: ")
    word_position_chosen = int(input("Please enter a positive integer: "))
    secret_word_chosen = choose_word(repertoire_path, word_position_chosen)
    num_of_tries = 0
    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word_chosen))

    old_letters_guessed = []
    while check_win(secret_word_chosen, old_letters_guessed) == False:
        letter_guess = input("Guess a letter: ").lower()
        if try_update_letter_guessed(letter_guess, old_letters_guessed) == False:
            continue
        if letter_guess not in secret_word_chosen:
            print ("):")
            num_of_tries += 1
            print_hangman(num_of_tries)
        if num_of_tries == 6:
            print("YOU LOSE.")
            break
        print(show_hidden_word(secret_word_chosen, old_letters_guessed))
    if check_win(secret_word_chosen, old_letters_guessed) == True:
        print("YOU WIN!")
    
if __name__ == "__main__":
    main()