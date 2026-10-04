# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init:
    $ vpoints = 0

    $ epoints = 0

    $ rpoints = 0
    
    $ hpoints = 0
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

define i = Character("The Creature") 

define j = Character("Robert's sister")

define k = Character("THE AUTHOR OF THIS GAME???")

define l = Character("PeRcY sHeLlY...")

define m = Character("Robert and Henry simultaneously")

define n = Character("You")

define o = Character("Kate")

define p = Character("Everyone")


#I'm just going to write the actual thing in comments
#setting: baltimore


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.f

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

    e "Yes."

    n "Yes."

    if vpoints < 0:
        menu:
            "None of them were that big anyway.":
                $ vpoints -= 1
                jump three
                
            
            "say nothing":
                jump three
    elif vpoints > 0:                                                                                                                        
        menu: 
            "Hey Victor, what do you want to see first? Let's go see that.":
                jump victor_route
            
            "*Stay with the group*":
                jump three

    else:
        jump three


label three:
    "As the group enters the aquarium:"
    h "Wow."

    f "This is amazing!"

    "The two of them try to wander off but elizabeth stops them."

    e "Let's all stay together, okay?"

    menu:
        
        "Thanks Elizabeth.":
            n "I'm glad you came on this trip."
            n "I know you didn't want to come, but it's so much better with you here."
            $ epoints += 1
            jump five

        "What should we see first?":
            jump four
     
 

label victor_route:

    e "*Sees you trying to cheer Victor up and smiles* We'll let you two go. Have fun!"

    f "** See you soon!"

    h "BYE!!!!"

    g "*laughs* Henry, please calm down before you have a heart attack."
return

            

label four:
    
    h "IWANTTOSEEJELLYFISH!!!!!!!"
    p "*Laughs*"
    e "I guess that's decided then! Let's go see some jellyfish."
    
    #scene change, only show robert, they're having a private conversation.

    f "Hey, ___. are you having fun?"

    menu: 
        "I am, and thanks for checking. you're a good person, Robert I really like you.":
            f "Awww ... really like you too. *he's tearing up a little*"
            jump robert_choice

        "I am so far.":
            f "Glad to hear it!"
            jump six

label robert_choice:

    k "HELLO. SORRY TO INTERRUPT YOUR STORY, BUT PLEASE MAKE THE NEXT CHOICE CORRECTLY."
    k "I'M QUITE ATTACHED TO ROBERT, AND IF YOU DON'T MAKE HIM HAPPY IT WONT END WELL."

    menu:
        "*HUG HIM PLEASE*":
            jump robert_route

        "Dont hug him and be incorrect, but just know you were warned":
            $ rpoints -= 1000000000
            jump six
        


label five: 
    show elizabeth_blushing
    e "I... thank you."
    e "I'm glad you're here too."
    menu:
        "*Hold her hand*":
            jump elizabeth_route

        "*Smile at her*":
            n "(Calling to the group) Where should we go first?"
            jump four

label elizabeth_route:
    return

label six:

    h "OHMYGODCOMEHERETHEJELLYFISHARESOCOOL!!!!!"

    f "Let's go join the group."
    if rpoints < 0:
        f "We... we can finish our discussion later"
    

    #scene change, everyone's there, there's a cool picture of jellyfish.

    h "___, isn't this the coolest place in the world ever to exist like ever?"

    menu:
        "It's adorable how excited you are.":
            $ hpoints += 1
            show henry_blushing
            h "adsfsfsdfsdfsdfssfdsfsdfsdfdf"
            e "*laughs* ___, stop teasing him!"
            if vpoints >= 0:
                g "But Elizabeth, It's so entertaining when they do that!"
            else:
                g "Yeah, ____, Stop it!"
            
            menu:
                "*Keep Pushing*":
                    jump henry_route

                "*Leave him alone*":
                    jump seven
        
        "It's pretty cool.":
            h "Yeah!"
            jump seven

label henry_route:
    n "But you like being teased, right?"
    show henry_blushing_harder
    h "I..."
    h "Only when you do it..."
    "*You're blushing too, and everyone else is watching you two, fascinated*"
    h "Okay fine! I like you, okay? and I'm being awkward about it and now you won't like me and and and and..."
    menu:
        "HUG HIM":
            jump henry_ending
        "HUG HIM":
            jump henry_ending
        "HUG HIM":
            jump henry_ending

label seven:
    e "Let's go see the coral reef exhibit! It sounds amazing."
    p "Yeah!"

    #scene change to coral reef
    if rpoints < 0:
        jump creature_death
    elif epoints > vpoints and epoints > hpoints:
        jump other_elizabeth_route
    elif vpoints > epoints and vpoints > hpoints :
        jump other_victor_route
    elif hpoints > vpoints and hpoints > epoints: 
        jump other_henry_route
    else:
        jump no_route

    
label other_elizabeth_route: 
    e "Wow. look at this! I think it's so beautiful that even Henry is speechless. and..."
    e "*inhales nervously* You... you know what else is beautiful?"
    e "You. You're beautiful, ___."
    if vpoints >= 0:
        e "And you're so kind."
    e "and thoughtful."
    e "Do you, I don't know, want to do something together? Like a date?"
    e "My only experience with dating would have been my marriage to Victor."
    e "But I didn't actually like him. everything about him"
    e "He's so obsessive, and he was a terrible dad to The Creature. And he's just creepy."
    
    #The creature wanders by and overhears

    i "That's true, he just abandoned me in his lab after obsessing over me for years."
    i "Once he starts something he never stops." 

    e "Uh... Thanks for that I guess?"

    #the creature leaves.
    e "Anyway, I'm sorry if I'm not good at this..."
    n "Stop that, you're doing great."
    e "*inhales* so... do you want to?"
    n "I would love to."

    #ending card
    
    return

label other_victor_route:
    "2"
    return

label other_henry_route:
    "3"
    return

label robert_route:
    "4"
    return

label no_route:
    "5"
    return

label creature_death:
    "why would you do that?"
    return

label henry_ending:
    "awwww"


