#wha
init:
    $ vpoints = 0

    $ epoints = 0

    $ rpoints = 0
    
    $ hpoints = 0
    
    image elizabeth_blushing = "elizabeth_blushing.png"
    
    image elizabeth happy = "elizabeth_happy.png"

    image bg school bus = "school-bus.jpg"
    
    image henrietta_blushing = "codel1.png"

    image henrietta_blushing_harder = "codel1.png"

    image henrietta happy = "codel90.png"

#points sysetem
    #if vpoints < 0:
        #e "1"
    #elif vpoints > 0:
        #e "2"
   #else:
       #e "3"
        
    
define e = Character("Elizabeth")

define f = Character("Roberta Walden <3")

define g = Character("vIcToRiA fRaNkEnStEiN")

define h = Character("HENRIETTA CLERVALLLLL!!!!")

define i = Character("The Creature") 

define j = Character("Roberta's sister")

define k = Character("THE AUTHOR OF THIS GAME???")

define l = Character("PeRcY sHeLlY...")

define m = Character("Roberta and Henrietta simultaneously")

define n = Character("You")

define o = Character("Kate")

define p = Character("Everyone")


#I'm just going to write the actual thing in comments
#setting: baltimore


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg school bus

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.f
    show henrietta happy

    # These display lines of dialogue.

    h "OHMYGODGUYSWE'REHERETHEBUSRIDEWASSOLONGBUTNOWWEREINBALTIMORE!!!!!!!!!!"
    
    scene bg school bus

    show elizabeth happy

    e "Roberta, can you please translate for those of us that don't speak 'excited Henrietta?'"
    scene bg school bus

    f "I think she's just happy to be off the bus."

    scene bg school bus

    g "The facade of an aquatic habitat shall be quite exhilarating."

    g "Alas, I shall have to leave you, my dear friends, as  I-"

    scene bg school bus

    "*WHACK*"

    g "owww"
    
    show elizabeth happy

    e "Sorry, Victoria, but you were being annoying again. We talked about this!"

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
            e "Safie, be nice please."
            n "Fine."
            jump two

        

label two:
    o "Come on everyone, let's go inside."
    
    e "Okay."

    f "Yay!"

    g "Fine..."

    scene bg school bus

    show henrietta happy

    h "Let's go, Victoria! I'm sure you'll have fun. You just said it would be."

    g "You understood any of those words?"
    
    m "Yes."

    e "Yes."

    n "Yes."

    if vpoints < 0:
        menu:
            "None of them were that big anyway.":
                $ vpoints -= 1
                jump three
                
            
            "Say nothing":
                jump three
    elif vpoints > 0:                                                                                                                        
        menu: 
            "Hey Victoria, what do you want to see first? Let's go see that.":
                jump victoria_route
            
            "*Stay with the group*":
                jump three

    else:
        jump three


label three:
    "As the group enters the aquarium:"
    h "Wow."

    f "This is amazing!"

    "The two of them try to wander off but Elizabeth stops them."

    show elizabeth_happy
    
    e "Let's all stay together, okay?"

    menu:
        
        "Thanks Elizabeth.":
            n "I'm glad you came on this trip."
            n "I know you didn't want to come, but it's so much better with you here."
            $ epoints += 1
            jump five

        "What should we see first?":
            jump four
     
 

label victoria_route:

    e "*Sees you trying to cheer Victoria up and smiles* We'll let you two go. Have fun!"

    f "See you soon!"

    h "BYE!!!!"

    g "*laughs* Henrietta, please calm down before you have a heart attack."
return

            

label four:
    
    h "IWANTTOSEEJELLYFISH!!!!!!!"
    p "*Laughs*"
    e "I guess that's decided then! Let's go see some jellyfish."
    
    #scene change, only show roberta, they're having a private conversation.

    f "Hey, Safie, are you having fun?"

    menu: 
        "I am, and thanks for checking. you're a good person, Roberta, and I really like you.":
            f "Awww... I really like you too. *she's tearing up a little*"
            jump roberta_choice

        "I am so far.":
            f "Glad to hear it!"
            jump six

label roberta_choice:

    k "HELLO. SORRY TO INTERRUPT YOUR STORY, BUT PLEASE MAKE THE NEXT CHOICE CORRECTLY."
    k "I'M QUITE ATTACHED TO ROBERTA, AND IF YOU DON'T MAKE HER HAPPY IT WONT END WELL."

    menu:
        "*HUG HER PLEASE*":
            jump roberta_route

        "Dont hug her and be incorrect, but just know you were warned":
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
    
    show henrietta happy

    h "OHMYGODCOMEHERETHEJELLYFISHARESOCOOL!!!!!"

    f "Let's go join the group."
    if rpoints < 0:
        f "We... we can finish our discussion later"
    

    #scene change, everyone's there, there's a cool picture of jellyfish.

    h "Safie, isn't this the coolest place in the world ever to exist like ever?"

    menu:
        "It's adorable how excited you are.":
            $ hpoints += 1
            show henrietta_blushing
            h "adsfsfsdfsdfsdfssfdsfsdfsdfdf"
            e "*laughs* Safie, stop teasing her!"
            if vpoints >= 0:
                g "But Elizabeth, It's so entertaining when she do that!"
            else:
                g "Yeah, Safie, Stop it!"
            
            menu:
                "*Keep Pushing*":
                    jump henrietta_route

                "*Leave her alone*":
                    jump seven
        
        "It's pretty cool.":
            h "Yeah!"
            jump seven

label henrietta_route:
    n "But you like being teased, right?"
    show henrietta_blushing_harder
    h "I..."
    h "Only when you do it..."
    "*Everyone else is watching you two, fascinated*"
    h "Okay fine! I like you, okay? and I'm being awkward about it and now you won't like me and and and and..."
    menu:
        "HUG HER":
            jump henrietta_ending
        "HUG HER":
            jump henrietta_ending
        "HUG HER":
            jump henrietta_ending

label seven:
    e "Let's go see the coral reef exhibit! It sounds amazing."
    p "Yeah!"

    #scene change to coral reef
    if rpoints < 0:
        jump creature_death
    
    elif vpoints > epoints and vpoints > hpoints:
        jump other_victoria_route
    elif vpoints < 0:
        jump victoria_hate_confession
    elif epoints > vpoints and epoints > hpoints:
        jump other_elizabeth_route
    elif hpoints > vpoints and hpoints > epoints: 
        jump other_henrietta_route
    else:
        jump no_route

    
label other_elizabeth_route: 
    e "Wow. look at this! I think it's so beautiful that even Henry is speechless. and..."
    show elizabeth_blushing
    e "*inhales nervously* You... you know what else is beautiful?"
    e "You. You're beautiful, Safie."
    if vpoints >= 0:
        e "And you're so kind."
    e "and thoughtful."
    e "Do you, I don't know, want to do something together? Like a date?"
    e "My only experience with dating would have been my marriage to Victoia."
    e "But I didn't actually like her. everything about her is a red flag."
    e "She's so obsessive, and she was a terrible mom to The Creature. And she's just creepy."
    
    #The creature wanders by and overhears

    i "That's true, she just abandoned me in her lab after obsessing over me for years."
    i "Once she starts something she never stops." 

    e "Uh... Thanks for that I guess?"

    #the creature leaves.
    e "Anyway, I'm sorry if I'm not good at this..."
    n "Stop that, you're doing great."
    e "*inhales* so... do you want to?"
    n "I would love to."

    #ending card
    
    return

label other_victoria_route:
    "2"
    return

label other_henrietta_route:
    
    return

label roberta_route:
    "4"
    return

label no_route:
    "5"
    return

label creature_death:
    #creature pops up and grabs safie
  
    i "Why would you do that?"
    n "Do what?"
    i "You didn't hug Roberta!"
    n "What?"
    i "I saw you two talking and she was crying and you should have hugged her."
    #insert mary shelley
    k "I TOLD YOU TO MAKE THE RIGHT CHOICE."
    "*SNAP*"
    #show corpse
    #show robert kneeling, crying
    show bg creature_death_ending_card
    return

label henrietta_ending:
    #show hug
    n "I like you too. You're always so cheerful, and it makes everyone else so happy."
    n "And even when Victoria was awful to you you went on that trip with her." 
    n "You love the world and life, and you have a great sense of wonder."
    n "I love you."
    #show henrietta_ending_card
    return

label victoria_hate_confession:
    g "Hey, Safie."
    menu:
        "Yeah?":
            #animate a slap type thing
            g "I hate you."
            g "You're not a good enough friend to me and you're kinda just mean."
        "*ignore her*":
            g "You disgust me." 
            g "You don't pay attention to me, and you dismiss everything I say."
            g "'I will be with you on your wedding night.'"
            g "you left that note, didn't you?"
            g "Don't worry, I'll be ready for you."
            #show victoria_hate_ending_card
    return