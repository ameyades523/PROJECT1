def count_words(text):
    #function to count number of words
    word_count = 0
    in_word = False  # Boolean to track if we are currently in a word

    for char in text:
        if char != ' ':  
            if not in_word:  
                word_count += 1
                in_word = True  
        else:
            in_word = False  
    
    return word_count

def main():
    # Get input from the user
    text_input = input("enter paragraph ")

   #while loop to check empty input
    while not text_input.strip():  
        print("no words found")  
        text_input = input("enter paragraph ")  

    
    word_count = count_words(text_input)
    print("the paragraph contains", word_count, "words")  

# Run the program
if __name__ == "__main__":
    main()
