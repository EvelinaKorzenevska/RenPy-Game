#Spēle sākas
label start:
    stop music fadeout 1
    scene bg school day with fade
    
    "The final year of school was upon us, and with each passing week the end of this important stage felt stronger." 
    "Time, which seemed endless, suddenly begins to speed up, leaving less and less chance for change."
    "Our protagonist was only a few months away from graduation. Every day at school reminded him that a new life lay ahead, unknown and exciting at the same time."
    "But there's something that he can't stop thinking about."
    "Everyone around him is finding someone - someone who's been in a relationship for a while, someone who's just starting out, and he's still single."
    "The thought that there could be someone to share these last few months with never leaves him."
    "In the meantime, there's a new day ahead, exams, the expectation of something more. Perhaps something will change very soon."

    show william uniform smile
    
    #renpy.input - ļauj ievadīt jebkuru mainīgo
    $ char_name = renpy.input("To start the game, think of a name for the main character", length=12, default="William", allow="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz").strip().capitalize() #strip - izdzēst liekas atstarpes, capitalize - pirmais burts mainās uz lielo
    if char_name == "":
        $ char_name = "William"
    
    scene bg classroom day with fade
    play music classroom
    show teacher smile with dissolve
    t "Hi. {w}Since your prom is coming up, today we're going to talk about preparations."
    
    "Knock, knock, knock"
    show teacher sad
    t "Who's late?"
    show william uniform confused light at right2 with moveinright
    show teacher sad light
    w "Sorry I'm late."
    t "This is the last time I'll forgive you. Next time you'll go to the principal!"
    show william uniform confused2 light
    w "It won't happen again."
    t "Sit down!"
    hide william with moveoutleft
    show teacher smile
    t "Let's continue with the lesson"
    t "Since prom is just around the corner, it's time to think about the most important thing - who you will share this special evening with,"
    t "because prom will be remembered not only for the atmosphere, but also for who will be there for you at this important moment."
    t "And now, it's time to look for and invite your other half, the one you're ready to spend this evening with - the one who will share not only dancing with you, but also memories for a lifetime."
    t "You still have 7 days, {w}that's it for today."
    
    scene bg corridor day with fade
    show william uniform sad with dissolve
    show screen days_left_display
    w "The teacher said it's time to invite your significant other to the prom. There's {b}only 7 days{/b} left to invite someone. {w}But I don't have anyone."
    w "I look at my classmates and they've already decided who they're going with. And me? {w}Still single..."
    w "Time seems to be running out, and I still haven't found someone I want to spend the evening with. I don't want to go with just anyone just so I'm not alone."
    w "Prom is supposed to be special, but how can it be special if no one's around?"
    show william uniform smile
    w "All right, I've made up my mind."
    w "It's time not to stand on the sidelines and wait for a miracle, but to take action myself. {w}Just who I should invite?"
    show william uniform suprized
    w "Oh, I'm about to start class, I'll decide there."
    
    scene bg classroom two day with fade
    play music classroom
    show william uniform smile with moveinright
    w "So, who should I invite?"
    w "There are three pretty girls. Should I pick one of them?"
    hide william with dissolve
    
    #Izsaucam funkciju, kas aktivizē pogu ar meiteņu informāciju
    show screen mia_butt
    show screen sabrina_butt
    n "Click on the girl you like to find out more about her. If you want to continue, close all the blocks."
    
    w "Sounds like I'm at a casting call. {w}And who should I choose to invite to the prom?"
    menu:
        "Who to invite to the prom?"
        
        "Mia":
            jump mia
        
        "Sabrina":
            jump sabrina