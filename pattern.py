def pat1(i: int):
    """
    This generates a right angled triangle
    *
    **
    ***
    ****
    *****

    @param i: NUmber of lines to include
    @param char: the character you want to print in the pattern
    @return:
    """
    char='*'
    print("pattern 1")
    for i in range(i):
        print(char * (i+1))
    print("_______________")
pat1(5)

def pat_01(i:int, char="*"):
    for val in range(1,i+1):
        no_of_of_space=i-val
        print(" "*no_of_of_space+char*val)
    print("-----------------")
pat_01(5)
"""
    This generates a right angled triangle
    *****
    ****
    ***
    **
    *
    @param i: NUmber of lines to include
    @param char: the character you want to print in the pattern
    @return:
    """
def pat2(i: int):
    print("pattern 2")
    char='*'
    for i in range(i,0,-1):
        print(char * i)
    print("_______________")
pat2(5)

"""
    This generates a right angled triangle
    *****
     ****
      ***
       **
        *

    @param i: NUmber of lines to include
    @param char: the character you want to print in the pattern
    @return:
    """
def pat3(i:int):
    print("pattern 3")
    char='*'
    for val in range (1,i+1):
        #print(val)
        no_of_space=val
        print(" "*no_of_space + char * (i-val))
    print("_______________")
pat3(5)
"""
    This generates a right angled triangle
    *****
    *****
    *****
    *****
    *****

    @param i: NUmber of lines to include
    @param char: the character you want to print in the pattern
    @return:
    """
def pat4(i:int):
    print("pattern 4")
    char = '*'
    for val in range(i):
        print(char*i,end=" ") # Passing the whitespace to the end parameter (end=' ')
        # indicates that the end character has to be identified by whitespace and not a newline
        print()
    print("_______________")
pat4(5)

"""
    This generates a right angled triangle
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *

    @param i: NUmber of lines to include
    @param char: the character you want to print in the pattern
    @return:
    """
def pat5(i:int, char='*'):
    print("pattern 5")
    for val in range(i):
        print(char * (val+1))
    for val in range(i-1,0,-1):
        print(char *val)
    print("_______________")
pat5(5)
def pat6(i:int,char="*"):
    print("pattern 6")
    for val in range(1,i+1):
        no_of_of_space=i-val
        print(" "*no_of_of_space+char*val)
    for val in range(1, i + 1):
        # print(val)
        no_of_space = val
        print(" " * no_of_space + char * (i - val))
    print("_______________")
pat6(5)