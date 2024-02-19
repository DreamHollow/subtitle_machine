sequence=0

def write(value):
    if value != str:
        string=str(value)
    f.write(string)

def process_time():
    global sequence
    sequence+=1
    write(sequence)
    write("\n")

    print("Enter the hour indicator (2 digits):")
    hours = input()

    print("Enter the minutes indicator (2 digits):")
    minutes = input()

    print("Enter the seconds indicator (2 digits):")
    seconds = input()

    print("Enter the milliseconds (3 digits):")
    milliseconds = input()

    # Combine all this data into a huge string

    big_string=str(hours)+":"+str(minutes)+":"+str(seconds)+","+str(milliseconds)
    write(big_string)
    write("\n")

    print("Please write the appropriate subtitle:")
    subtitle_string = input()
    write(subtitle_string)
    write("\n")

    print("Enter more timecodes and subtitles? If no, program ends.")
    print("Yes or no?")
    decision = input()

    if decision == "yes":
        write("\n") # create space for new sequence
        return
    elif decision == "no":
        print("Exit command given, stopping process.")
        print("Thank you for using Subtitle Machine!")
        exit(0)
    else:
        print("Input not recognized, ending program.")
        exit(1)


print("Welcome to the Subtitle Machine.")
print("\n")
print("This program writes SRT compatible file formats.")
print()
print("A sequence counter will automatically increase after entry finishes.")
print()

print("What is the name of the SRT file?")
file_title = input()
extension = ".srt"
title = file_title + extension

# Open up the newly named file for edit
f = open(title, "a")

entering_more_data=True

while(entering_more_data):
    process_time()

f.close()