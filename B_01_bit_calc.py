# generates headings
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# displays instructions
def instructions():
    statement_generator("instructions", "-")
    print('''
- Please choose a data type (image/text/integer)
- This program assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel)
- For text, we assume that ascii encoding is being used (8 bits per character)
- Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit
- When finished, type xxx to exit
    ''')

# ask what kind of file
def get_filetype():

   while True:

        response = input("File type: ").lower()

        # check i or exit code
        if response == "xxx" or response == "i":
            return response
        # check integer
        elif response in ['integer', 'int']:
            return "integer"
        # check image
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"
        # check text
        elif response in ["text", 'txt', 't']:
            return "text"
        else:
            print("Please enter a valid file type")

# Ask user for width and loop they enter a number that is more than zero
def int_check(question, low):

    error = f"please enter number that is more then or equal to {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def image_calc():
    pass

    width = int_check("Width: ", 1)
    height = int_check("Height: ", 1)

# calc number of pix and then times by 24
    num_pixels = width * height
    num_bits = num_pixels * 24

    answer = (f"Number of pixels: {width} x {height} = {num_pixels}"
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer

def integer_calc():
    pass
    #ask for integer
    integer = int_check("Integer: ", 0)

    # convert to bin
    raw_binary = bin(integer)

    #remove 0b
    binary = raw_binary[2:]
    num_bits = len(binary)

    answer = f"{integer} in binary is {binary}. We ned {num_bits} to represent it."

    return answer

def calc_text_bits():
    pass

    # get text
    response = input("Enter some text: ")

    #calculate bits
    num_chars = len(response)
    num_bits = num_chars * 8

    #set up answer
    answer = (f"{response} has {num_chars} characters."
              f"\nWe need {num_chars} x 8 bits to represent it"
              f"\nwhich is {num_bits} bits")

    return answer

# main routine

want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")
# display instructions if needed
if want_instructions == "":
    instructions()

while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break

    # if pick i ask if they want image or integer
    if file_type == 'i':

        want_image = input("Please <enter> for an integer or any key for image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)

    else:
        text_ans = calc_text_bits()
        print(text_ans)
