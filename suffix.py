def solution(words):
    '''
    This is a function that loop through a sentence and 
    remove the suffix of a particular word that has suffix
    and return the base word and also return the first eight letters
    of a word that is longer than eight
    '''
    input_string = words.split()
    suffix = ['ing','ly','ed']
    output = []
    condition = False
    while True:
        for word in input_string:
            for letters in suffix:
                if word.endswith(letters):
                    step = len(word) - len(letters)
                    ans = word[:step]
                    output.append(ans)
                    condition =  False
                    break
                condition = True
                continue
            while condition  == True:
                if len(word) > 8:
                    ans = word[:8]
                    output.append(ans)
                    condition = False
                else:
                    output.append(word)
                    condition = False
        final_answer = ' '.join(output)
        return final_answer
print(solution('an extremly  dangerous dog is barking'))
#print(solution('a boy is jump quick'))
