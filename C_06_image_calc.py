# Ask user for width and loop they
# enter a number that is more than zero
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

#main routine
image_ans = image_calc()
print(image_ans)