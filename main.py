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

    # Starting time code
    
    print("Entering timecode beginning...")
    print("Enter the hour indicator (2 digits):")
    hours = input()

    print("Enter the minutes indicator (2 digits):")
    minutes = input()

    print("Enter the seconds indicator (2 digits):")
    seconds = input()

    print("Enter the milliseconds (3 digits):")
    milliseconds = input()

    big_string_one=str(hours)+":"+str(minutes)+":"+str(seconds)+","+str(milliseconds)
    write(big_string_one)
    write(" ")
    write("-->")
    write(" ")

    # Ending time code

    print("Enter the hour indicator (2 digits):")
    hours_ = input()

    print("Enter the minutes indicator (2 digits):")
    minutes_ = input()

    print("Enter the seconds indicator (2 digits):")
    seconds_ = input()

    print("Enter the milliseconds (3 digits):")
    milliseconds_ = input()
    
    big_string_two=str(hours_)+":"+str(minutes_)+":"+str(seconds_)+","+str(milliseconds_)
    write(big_string_two)
    write("\n")

    # Subtitles

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
