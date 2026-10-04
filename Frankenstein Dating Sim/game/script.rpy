# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init:
    $ vpoints = 0

#points sysetem:
    #if vpoints < 0:
        #e "1"
    #elif vpoints > 0:
        #e "2"
   #else:
       #e "3"
        
    
define e = Character("Elizabeth")

define f = Character("Robert Waldon <3")

define g = Character("vIcToR fRaNkEnStEiN")

define h = Character("HENRY CLERVALLLLL!!!!")

define i = Character("The Creature???") 

define j = Character("Robert's sister")

define k = Character("Mary Shelley????")

define l = Character("PeRcY sHeLlY...")

define m = Character("Robert and Henry simultaneously")

define n = Character("You")

define o = Character("Kate")


#I'm just going to write the actual thing in comments
#setting: baltimore


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    h "OHMYGODGUYSWE'REHERETHEBUSRIDEWASSOLONGBUTNOWWEREINBALTIMORE!!!!!!!!!!"
    
    show Elizabeth happy

    e "Robert, can you please translate for those of us that don't speak 'excited Henry?'"

    f "I think he's just happy to be off the bus."

    g "The facade of an aquatic habitat shall be quite exhilarating."

    g "Alas, I shall have to leave you, my dear friends, as  I-"

    "*WHACK*"

    g "owww"

    e "Sorry, Victor, but you were being annoying again. We talked about this!"

    e "You don't actually know what any of those words mean."

    e "And you used a thesaurus to memorize those two sentences! I heard you practicing for weeks."

    e "You're still not going to convince anyone you solved mortality."

    g "But I did..."

    m "It's okay, I believe you!"

    menu:

        "Me too!":
            $ vpoints += 1
            g "*sighs* Thanks, you guys, but I know you're just being nice..."
            jump two       
        "*say nothing*":
            g "*sighs* Thanks, you guys, but I know you're just being nice..."
            jump two

        "Really? I don't.":
            $ vpoints -= 1
            g "Hmph. well at least they do."
            e "____, be nice please."
            n "Fine."
            jump two

        

label two:
    o "Come on everyone, let's go inside."
    
    e "Okay."

    f "Yay!"

    g "Fine..."

    h "Let's go, Victor! I'm sure you'll have fun. You just said it would be."

    g "You understood any of those words?"
    
    m "Yes."

    e "yes"

    n "Yes"

    if vpoints < 0:
        menu:
            "None of them were that big anyway.":
                vpoints -= 1
                
            
            ""



