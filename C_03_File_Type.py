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



# main routine
while True:
    file_type = get_filetype()

    # if pick i ask if they want image or integer
    if file_type == 'i':

        want_image = input("Please <enter> for an integer or any key for image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"You chose {file_type}")

    if file_type == "xxx":
        break