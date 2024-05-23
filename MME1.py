#write the function for print the third in the list
def print_third_dog_names(dog_lists):
    for dog_list in dog_lists:
        if len(dog_list)>= 3: #check if the list has at least 3 elements
            print(dog_list[2]) #print the third dog
M = [('Baxter','Bingo','Balius'),
     ('Rover','Ruffles','Ran'),
     ('Kane','Kibbles','Kratos')]
#call the function with the list of list
print_third_dog_names(M)