"""
Filename: text-based_adventure_game.py
Author: <Myers, Aiden>
Created: <10/8/25>
Instructor: Holtslander
Description:
    <A text based adventure game taking place in an unfamiliar time and place.>
Dependencies: parser
"""

# Import statements
from parser import Parser

# This is a dictionary
# It is a place to store variables you want to use in your story Instead of having to create and manage many different
# variables, we can just store and quickly access them here.
# Inserting a new entry: player_vars["key"] = "value"
# If you want to store a user generated value: player_vars["player"] = input("Please type your name")
# "key" is your variable name and "value" is what you are storing. (It can also be an integer. Just remove the quotes.)
#
# Accessing an entry: player_vars["key"]
# e.g.
# print(player_vars["key"])
#
# You can also overwrite an entry by just assigning a new value e.g.: player_vars["key"] = "value2"
player_vars = {
    "player" : "Henry"
}

# This is the entry point for the program. It the program should start and stop here.
# For now, all your code should be in the main function
def main():
    """
    The entry point and driver of the narrative game program.
    :return: None
    """

    # This creates a new parser object. You can use it to print your text files
    # parser.dprint("example.txt", player_vars, pause=0.1)
    # The dict and pause arguments can be omitted if you do not want a delay and do not want to format the output.
    parser = Parser()

    # Your code goes under this line.
    parser.dprint("welcome_text.txt", pause = 0.008)

    parser.dprint("Start", pause = 0.008)
    c1 = input()
    if c1 == "1":
        parser.dprint("South", pause = 0.008)
        c2 = input()
        if c2 == "1":
            parser.dprint("Chase", pause = 0.008)
            c3 = input()
            if c3 == "1":
                parser.dprint("Ending 1", pause = 0.008)
            else:
                parser.dprint("Ending 2", pause = 0.008)
        else:
            parser.dprint("Clearing", pause = 0.008)
            c6 = input()
            if c6 == "1":
                parser.dprint("Prayer", pause = 0.008)
            else:
                parser.dprint("Deeper", pause = 0.008)
    
    elif c1 == "2":
        parser.dprint("Nearby", pause = 0.008)
        c4 = input()
        if c4 == "1":
            parser.dprint("Packed Food", pause = 0.008)
            c5 = input()
            if c5 == "1":
                parser.dprint("Truth", pause = 0.008)
            else:
                parser.dprint("Lie", pause = 0.008)
        else:
    
    else:
        parser.dprint("North", pause = 0.008)



    # Clean up code. Do not write any code past this line.
    parser.destroy()
    parser = None

# This tells the program to start with the main function.
if __name__ == "__main__":
    main()




