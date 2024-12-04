def count_words(text):
    
    #function to count words of sentence 
    
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
    
    text_input = input("enter paragraph ")

    
    if not text_input.strip():
        print("no words found")
    else:
        # Call the count_words function and display the result
        word_count = count_words(text_input)
        print("the paragraph contains", word_count, "words")

#calling main
if __name__ == "__main__":
    main()
