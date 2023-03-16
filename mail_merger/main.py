#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER="[name]"
    
with open("d:/Python/Day_33Mail Merge Project Start/Input/Names/invited_names.txt") as filename:
    names=filename.readlines()


with open("d:/Python/Day_33Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    content=letter.read()
    for name in names:
        new_name=name.strip()
        new_letter=content.replace(PLACEHOLDER,new_name)
        with open(f"d:/Python/Day_33Mail Merge Project Start/Output/ReadyToSend/letter_for_{new_name}","w") as file:
            file.write(new_letter)