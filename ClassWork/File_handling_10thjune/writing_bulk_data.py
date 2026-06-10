'''Program to input 10 sentences from the user and write them to a file.'''
# Open the file in write mode
filev = open('sentences.txt', 'w')
#to create a blank list to store sentences
sentences = []
#message to user
print("Enter 10 sentences:")
# Loop to get 10 sentences from the user
for i in range(10):
    #input of sentence from user
    sentence = input()
    #-----------------------------------------
    # Appending new line character to the sentence
    sentence += '\n'
    # Append the sentence to the list
    sentences.append(sentence)
    print("----------------------------------------------")
# Write all sentences to the file at once
filev.writelines(sentences)
print("Data successfully written into the file")
# Close the file
filev.close()