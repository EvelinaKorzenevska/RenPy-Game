#Izvēloties Mīju, spēle pārlec uz mia label bloku    
label mia:
    hide screen monica_butt
    hide screen sabrina_butt
    show william uniform smile with dissolve
    w "Mia is so smart, she gets excellent grades all the time. She's nice to talk to, interested in everything. But I'm afraid she has bigger plans than just dancing with a boy in her class."
    w "But still, it's worth a try!"
    hide screen mia_butt with dissolve
    
    scene bg courtyard day with fade
    show william uniform smile with dissolve
    w "She should be around here somewhere."
    show william uniform suprized 
    w "There she is!"
    hide william with moveoutleft
    
    scene bg courtyard2 day with fade
    show mia uniform smile1 with dissolve
    show william uniform smile light at right1 with moveinright
    w "Hi, Mia!"
    show mia uniform smile light
    m "Hi, [char_name]"
    show william uniform smile light
    w "How are you?"
    m "Good, you?"
    w "Good too. {w}I came to ask you something"
    m "About what?"
    w "Do you want to go to the prom with me?"
    show mia uniform suprized light
    m "Unexpectedly. {w}I mean, we don't even know each other."
    w "I don't insist that you give your answer now. We have time to get to know each other, and then you can give your answer."
    show mia uniform smile light
    m "Let's give it a try."
    show william uniform happy light
    w "Great, I'll text you tonight."
    m "Well"
    
    #Dialoglodziņa paslēpšana
    window hide
    
    #Autora vārdi pa visu ekrānu
    a "{b}{color=#ff0000}The point of the game:{/color}{/b}"
    a "Your goal is to ask a girl to the prom. To get her to agree to go with you, you need to {b}score at least 10 points{/b} by taking the right action in the {b}remaining 7 days{/b}. "
    a "Points are added for successful decisions and correct behaviour, but be careful - wrong steps can lead to loss of points!"
    a "Show sensitivity, consideration and understanding to earn her consent and become prom king!"
    a "{b}{color=#ff0000}Game Objective:{/color}{/b}"
    a "Score 10 points in 7 days by performing the right actions to ask a girl to prom. Choose your actions and words carefully - every choice you make affects your score."
    
    nvl hide
    
    scene bg male bedroom night with fade
    show william pijama smile with dissolve
    w "I'm glad Mia agreed, now I have to figure out how we can get to know each other better."
    show william pijama think
    w "I need to invite her somewhere."
    show william pijama happy
    w "I know! I'll invite her out. {w}There we'll get to know each other."
    show william pijama smile
    w "I'm gonna text her."
    show william pijama smile at right1 with move
    
    #Telefona saziņa ar Mīju
    $ contact_name = "Mia"
    $ contact_icon = "images/sms_chat/icon_mia.png"
    python:
        for character, text in messages_list_mia:
            play_message_sound() 
            display_message(character, text)
            renpy.show_screen("sms_chat")
            renpy.pause() #Aptur darbību, līdz spēlētājs noklikšķinās vai veiks citu darbību, lai to turpinātu.
            renpy.hide_screen("sms_chat")

    #Ziņojumu dzēšana pirms nākamā dialoga
    $ messages.clear()
    
    show william pijama happy
    w "Yay! {w}I can't wait for tomorrow." 