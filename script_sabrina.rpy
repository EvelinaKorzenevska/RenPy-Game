#Izvēloties Sabrinu, spēle pārlec uz sabrina label bloku  
label sabrina:
    hide screen mia_butt
    hide screen monica_butt
    show william uniform smile at right1 with dissolve 
    w "Sabrina is like an enigma, always a little mysterious. Sometimes it seems like she's looking at me, and sometimes it's like she doesn't notice me at all. She's a fun person to be with, but I don't know what she'd think if I asked her out."
    w "But still, it's worth a try!"
    hide screen sabrina_butt with dissolve
    
    stop music fadeout 1
    scene bg courtyard day with fade
    play music courtyard
    show william uniform smile with dissolve
    w "She should be around here somewhere."
    show william uniform suprized 
    w "There she is!"
    hide william with moveoutleft
    
    scene bg courtyard2 day
    show sabrina uniform smile light
    show william uniform smile light at right1 with moveinright
    w "Hi, Sabrina!"
    show sabrina uniform sad light
    s "Hi."
    show william uniform smile light
    w "How are you?"
    s "Good"
    w "I am good too. {w}I came to ask you something"
    s "About what?"
    show william confused2 light
    w "Do you want to go to the prom with me?"
    show sabrina uniform suprized light
    s "Unexpectedly. {w}Why me?"
    show william uniform smile light
    w "You're very interesting, I'd like to get to know you better."
    show sabrina uniform sad light
    s "You need to get to know me before you invite me over. {w}And in general, I like to be groomed."
    w "I don't insist that you give your answer now. We have time to get to know each other better, to go to different events, and then you can give your answer."
    show sabrina uniform smile light
    s "Well, let's have a look."
    show william uniform happy light
    w "Great, I'll text you tonight."
    s "Ok."
    
    window hide
    
    #Autora vārdi pa visu ekrānu
    a "{b}{color=#ff0000}The point of the game:{/color}{/b}"
    a "Your goal is to ask a girl to the prom. In order for her to agree to go with you, you need to score at least 10 points by doing the right actions and behaviours in her direction."
    a "Points are added for successful decisions and correct behaviour, but be careful - wrong steps can lead to loss of points!"
    a "Show sensitivity, consideration and understanding to earn her consent and become prom king!"
    a "{b}{color=#ff0000}Game Objective:{/color}{/b} {w}Score 10 points by performing the right actions to ask a girl to prom. Choose your actions and words carefully - every choice you make affects your score."
    
    nvl hide
    
    stop music fadeout 1
    scene bg male bedroom night with fade
    play music main
    show william pijama smile with dissolve
    w "I'm glad Sabrina agreed, now I have to figure out how we can get to know each other better."
    show william pijama think
    w "I need to invite her somewhere."
    show william pijama happy
    w "I know! I'll invite her out. {w}There we'll get to know each other."
    show william pijama smile at right1 with move
    #Telefona saziņa ar Sabrinu
    $ contact_name = "Sabrina"
    $ contact_icon = "images/sms_chat/icon_sabrina.png"
    python:
        for character, text in messages_list_sabrina:
            play_message_sound() 
            display_message(character, text)
            renpy.show_screen("sms_chat")
            renpy.pause()
            renpy.hide_screen("sms_chat")

    $ messages.clear()
    
    show william pijama happy
    "Yay! {w}I can't wait for tomorrow."
    
    #Sakrāto punktu paradīšana
    $ girl = point_sabrina
    show screen earned_points
    n "The points scored will be displayed on the right hand side"
    play sound plus_point
    $ point_sabrina += 1
    $ girl = point_sabrina
    n "Congratulations! You've earned + 1 point for the invitation."
    
    $ days_left -= 1
    
    scene bg male bedroom day with fade
    show william pijama smile with dissolve
    w "Oh, morning... Well, the day has finally arrived!"
    show william pijama confused
    w "Today is the meeting with Sabrina, and I think I'm a little nervous."
    w "She's the most popular girl in school, I don't know how she agreed to go out with me."
    show william pijama smile 
    w "Okay, I need to get my head together and everything will be fine. {w}I've got to go get ready."
    hide william with moveoutright
    show william smile with moveinright
    w "I'm ready!"
    show william confused
    w "I've got to think of something to talk about."
    w "Okay, just don't be shy and everything will be fine."
    show william smile