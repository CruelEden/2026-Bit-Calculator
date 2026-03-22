# generates headings
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# displays instructions
def instructions():
    statement_generator("instructions", "-")

    print('''
instructions go here.
- instruction 1
- instruction 2
- etc   
    ''')


# main routine here
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")
# display instructions if needed
if want_instructions == "":
    instructions()

print("program continues")