def tokenize(lines):
    words = [] # initializes empty list and stores tokens
    for line in lines: # Starts a for loop to iterate through each line the 'lines'list
        start = 0 # Initializes the variable to keep track of the starting index
        while start < len(line): # This line starts a while loop to skip over any whitespace characters at the beginning of the line
            while start < len(line) and line[start].isspace(): # This line starts a nested while loop to skip over any whitespace characters at the beginning of the line. The loop continues as long as start is less than the length of the line and the current character is a whitespace character.
                start = start + 1 # The start variable is incremented by 1 after each iteration of the loop.
            end = start # This line initializes the end variable to the value of start. The end variable will keep track of the ending index of a token in the line.
            if end < len(line): # This line checks if end is less than the length of the line. If this is true, the code inside the if statement will run.
                if end < len(line) and line[end].isdigit(): # This line checks if end is less than the length of the line and the current character is a digit. If this is true, the code inside the if statement will run.
                    end = start
                    while end < len(line) and line[end].isdigit():
                        end = end + 1
                    words.append(line[start:end].lower())
                    start = end
                elif start < len(line) and line[start].isalpha():
                    end = start
                    while end < len(line) and line[end].isalpha():
                        end = end + 1
                    words.append(line[start:end].lower())
                    start = end
                else:
                    end +=1
                    words.append(line[start:end])
                    start = end

    return words

def countWords(words, stopWords):
    x = {}
    for char in words:
        if char in stopWords:
            pass
        elif not char in x:
            x[char] = 1
        else:
            x[char] += 1
    return x

def printTopMost(frequencies, n):
    for word, freq in sorted(frequencies.items(), key=lambda x: -x[1]):
        if (n<= 0):
            break
        print(word.ljust(20) + str(freq).rjust(5))
        n -= 1

