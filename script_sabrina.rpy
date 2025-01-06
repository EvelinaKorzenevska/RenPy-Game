#Izvēloties Sabrinu, spēle pārlec uz sabrina label bloku  
label sabrina:
    hide screen mia_button
    show william uniform smile at right1 with dissolve 
    w "Sabrina is like an enigma, always a little mysterious. Sometimes it seems like she's looking at me, and sometimes it's like she doesn't notice me at all. She's a fun person to be with, but I don't know what she'd think if I asked her out."
    w "But still, it's worth a try!"
    hide screen sabrina_button with dissolve
    
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
     w "It's time to get out."
    
    show screen map_button_sabrina
    $ current_location = "home2"
    $ next_location = "park2"
    n "To go to the meeting, open the map and find the park."

    return


label park2:
    stop music fadeout 1
    hide screen map_button_sabrina
    play music park
    if next_location == "park2":
        scene bg park afternoon with fade
        show william smile light at right1 with moveinright
        show sabrina unhappy light at left2 with moveinleft
        w "Hi!"
        s "Hi."
        show screen information
        show william confused light
        w "You look great."
        s "I known."
        show william happy light
        w "I'm glad you came."
        s "Honestly, I didn't think you'd have the guts to invite me."
        show william smile light
        w "Yeah, I did. Sometimes you gotta do something out of the ordinary, right?"
        show sabrina sad light
        s "What's on your mind, anyway? You think I accept any invitation?"
        w "You know, to be honest. I just wanted to get to know you better. {w}You know, besides the ‘prettiest and most popular girl in school’ image that everyone sees."
        show sabrina laught light
        s "Oh, is that so? So you thought you could ‘get to know’ me in one walk in the park?"
        w "Well, it's a start. Maybe you want to know something about me, too."
        s "Let's see. {w}All right, come on, tell me what's so interesting about you. Or do you think I should just tell you everything about me?"
        w "Okay, well, here's the thing: I love photography."
        show william confused light
        w "I didn't think I'd be the first to tell you this, but, um. photography is like a way for me to see things that other people don't normally see."
        show sabrina smile light
        s "A picture? And what, you'd like to take a picture of me, wouldn't you?"
        show william smile light
        w "Sabrina, you're being filmed by everyone around you. I'm more interested in seeing the real you, without that image."
        w "I think there's someone behind that perfect facade that not many people know. I'd like to see her."
        show sabrina confused light
        s "You know, you're the first person who's ever said those things to me..... {w}Okay, you have a chance, but only one."
        play sound plus_point
        $ point_sabrina += 1
        $ girl = point_sabrina
        n "You managed to surprise Sabrina +1 point."
        w "Nice."
        hide screen information
        
        menu:
            "What question to ask Sabrina?"
            
            "About hobbie":
                $ question_choiсe = "hobbie"
                call hobbie from _call_hobbie
            
            "About friends":
                $ question_choiсe = "friends"
                call friends from _call_friends
                
        
        show william confused light
        w "I'm curious to know, since you're popular, you must have had a lot of suitors?"
        w "You just make such an impression...that all guys probably want to get to know you better."
        show sabrina unhappy light
        s "Maybe they do, but that doesn't mean I do. Some are just trying to play around. Others are looking for company so they can be more popular too. And I get bored quickly."
        show william smile light
        w "I see. And how did they try to surprise you?"
        s "Gave all sorts of gifts, even strange ones sometimes, they wrote poems dedicated to me, also sang songs under the house, and many other things, I can't even remember now."
        show william happy light
        w "wow, it must be cool to get presents, huh?"
        s "Not really, they often give such rubbish that you don't know where to put it. Also, before giving something, no one asks me what I like at all."
        s "For example, I've always got bouquets of roses, both small and big, because guys think everyone likes roses. And I hate them, I like chamomiles."
        w "But it's still nice to get presents."
        s "Yeah, I really liked it at first, but now that it happens every day, it's getting boring."
        w "Maybe, I don't know."
        if question_choiсe == "hobbie":
            call friends from _call_friends_1
        elif question_choiсe == "friends":
            call hobbie from _call_hobbie_1
        
        call free_time from _call_free_time
        
        scene bg park night with fade
        show william smile light at right1
        show sabrina smile light at left2
        show screen money_display
        n "Now your money will be displayed at the top."
        w "Oh, it's getting late, time to go home."
        menu:
            "What to do?"
            
            "Walk a Sabrina home":
                jump sabrina_home
            
            "Hail a taxi (Costs 15$)":
                jump taxi2
            
            "Returned to their homes":
                jump go_home2
        
    else:
        show screen map_button_sabrina
        play sound main
        w "I don't have to go to the park right now."

    return
    

label hobbie:
    w "Listen, do you have a hobby? You know, something that inspires you or you just like."
    show sabrina smile light
    s "I do dance. It helps me feel stronger and more confident."
    show william happy light
    w "Wow, that's cool. {w}How many years have you been doing it?"
    s "For over three years now. Actually, dancing requires a lot of strength and stamina, I myself didn't think I could handle it in the beginning. But it sucked me in."
    w "It's really cool, and I can see why you like it. Does it help your confidence?"
    s "Yes, when I train I forget about all the expectations and what is expected of me. At the dances I am just myself and it gives me a sense of freedom that is sometimes lacking."
    show william smile light
    w "I can see why you have a perfect body. Presumably you're eating properly?"
    show sabrina laught light
    s "Actually, no, I eat what I want, when I want. {w}I'm just lucky with my genetics."
    show william sad light
    w "Lucky, I'm the opposite. I only eat my favourite dessert on holidays."
    show sabrina confused light
    s "Unlucky, but what are your favourite dessert?"
    
    menu:
        "What is your favourite dessert?"
                
        "Cheesecake":
            call cheesecake from _call_cheesecake
                
        "Honey cake":
            call honey_cake from _call_honey_cake

    return
    
    
label cheesecake:
    show william smile light
    w "My favourite dessert is a cheesecake."
    show sabrina happy light
    s "Omg, me too. I like eat it in the morning with coffee."
    play sound plus_point
    $ point_sabrina += 1
    $ girl = point_sabrina
    n "Sabrina is glad that your tastes match +1 point."
    show william happy light
    w "Wow. What a coincidence."
    
    return
    
    
label honey_cake:
    show william smile light
    w "My favourite dessert is a honey cake. What about you?"
    show sabrina smile light
    s "I don't like honey, so I don't like a honey cake, but my favourite is a cheesecake. {w}I like eat it in the morning with coffee."
    w "Cheesecake's good too, but it's not my favourite."
    
    return
    
    
label friends:
    w "Listen, do you have any real friends? The ones you can be totally yourself with?"
    show sabrina sad light
    s "You know... sometimes I think I don't. I have a lot of ‘acquaintances’, but friends... real ones - not so many."
    w "Have you ever thought that maybe they want to get to know the real you too, like I do now?"
    s "Maybe they do. But I'm used to being careful. {w}Even those who call themselves my friends often want something in return - popularity, attention... It's tiring."
    show william sad light
    w "I understand. I think it's really hard to be the centre of attention. People only see what they want to see."
    s "Yeah. Sometimes I think they only see the picture and not me. At first I even liked it, but then it got... hard. It's like someone keeps expecting me to be perfect."
    show william smile light
    w "I don't think that's true. On the contrary, maybe if you let people see the real you, there will be those who will be there for you because they're interested in you, not your image."
    s "Maybe... But it's still scary. {w}I can't even remember the last time I felt like I could just be myself."
    w "Then maybe you should try it now. Well, just for the sake of experimenting."
    show william happy light
    w "I mean, there's no one here but me."
    show sabrina smile light
    s "Okay... I'll give it a try."
    show sabrina confused
    s "You know, to be honest, sometimes I want to leave all this, go somewhere far away and start again. {w}Somewhere where no one will know anything about me. Where I don't have to impress anyone or live up to anyone's expectations."
    show william smile light
    w "That would be brave, Where would you go if you could choose any place?"
    s "Probably somewhere by the sea. Where it's quiet, where you can be alone with yourself."
    show sabrina laught light
    s "That's funny, isn't it? I, accustomed to attention, really just want silence."
    menu:
        "Is it funny?"
            
        "Funny":
            call funny from _call_funny
            
        "Not funny":
            call not_funny from _call_not_funny

    return
    
    
label funny:
    show william happy light
    w "It's funny. {w}You're a little weird."
    show sabrina sad light
    s "See, you judge me by my looks like everyone else."
    show william confused light
    w "No, don't think so, it's just unusual coming from someone who's always at attention."
    s "Well, we'll see."
    play sound minus_point
    $ point_sabrina -= 1
    $ girl = point_sabrina
    n "Your response made it clear to sabrina that you're just like everyone else judging her from a picture -1 point."
    
    return
    
    
label not_funny:
    w "It's not funny at all. Silence is sometimes the only thing that helps you really understand yourself."
    show sabrina smile light
    s "You surprise me. I thought you were one of those people who judged me by my looks. And it turns out you see something more."
    show william happy light
    w "I wanted to see more than that. And, you know... {w}I'm glad you wanted to talk about it."
    s "You know... Thank you for just listening and not expecting me to be perfect. I feel like I can just be me for the first time in a long time."
    w "That's great. Maybe this is the beginning of a real friendship?"
    s "Maybe..."
    play sound plus_point
    $ point_sabrina += 1
    $ girl = point_sabrina
    n "Sabrina likes to have a dialogue with you +1 point."
    
    return
    

label free_time:
    show william smile light
    w "And what do you usually do in your free time?"
    show sabrina smile light
    s "In my free time I like to go shopping, as well as to attend different events, for example, concerts of my favourite artists."
    w "Cool. And what is your favourite artist?"
    s "I listen to Ariana Grande's songs most of all, they are very energetic and uplifting. {w}I also listen to Beyoncé, I like to dance to her tracks."
    w "Yeah, they do have energetic and popular songs."
    
    return
    
    
label sabrina_home:
    w "Let me walk you out."
    s "Let's go"
    play sound plus_point
    $ point_sabrina += 2
    $ girl = point_sabrina
    n "Good decision to walk the girl home at night +2 points."
    show screen map_button_sabrina
    $ current_location = "park2"
    $ next_location = "house_sabrina"
    n "You need to go home to Sabrina."
    
    return
    
label taxi2:
    w "Let me call you a taxi."
    show sabrina happy light
    s "Nice. I wouldn't want to walk home."
    play sound plus_point
    $ point_sabrina += 2
    $ girl = point_sabrina
    n "Good decision +2 points."
    $ money -= 15
    play sound money
    n "You spent $15."
    play sound taxi
    show taxi_icon at Transform(xpos=-200, ypos=286) with moveinleft
    w "A taxi's on its way."
    show sabrina smile light
    s "Thank you."
    show william happy light
    w "You're welcome. I'll see you later."
    s "Okey."
    hide sabrina with moveoutleft
    play sound taxi_drive
    hide taxi_icon
    show screen map_button_sabrina
    $ current_location = "park2"
    $ next_location = "home2"
    n "It's very late, it's time to go home"
    
    return
    
label go_home2:
    w "Well, I'll see you then."
    m "See you."
    hide sabrina with moveoutleft
    play sound minus_point
    $ point_sabrina -= 1
    $ girl = point_sabrina
    n "Sabrina doesn't like to walk alone -1 point."
    show screen map_button_sabrina
    $ current_location = "park2"
    $ next_location = "home2"
    n "It's very late, it's time to go home"
    
    return
    

label house_sabrina:
    stop music fadeout 1
    hide screen map_button_sabrina
    play music night_street
    if next_location == "house_sabrina":
        scene bg sabrina house night with fade
        show sabrina smile light at left2 with moveinleft
        show william smile light at right1 with moveinleft
        s "Here we are."
        show william happy light
        w "All right. Nice walk. I'll see you later."
        s "See you later."
        hide sabrina with moveoutright
        show screen map_button_sabrina
        $ current_location = "house_sabrina"
        $ next_location = "home2"
        show william smile
        n "It's very late, it's time to go home."

    else:
        show screen map_button_sabrina
        w "I don't have to go Sabrina's house right now."
        
    return
    
label home2:
    stop music fadeout 1
    hide screen map_button_sabrina
    play music main
    if next_location == "home2":
        $ home2_visited += 1
        if home2_visited == 1:
            scene bg male bedroom night with fade
            show william smile with dissolve
            w "Here I am at home."
            show william happy
            w "It was an interesting walk, even got Sabrina talking. {w}Maybe even I have a chance!"
            hide william with moveoutright
            show william pijama smile with moveinright
            w "So, it's time to go to bed."
            
            $ days_left -= 1
            scene bg male bedroom day with fade
            show william pijama smile
            w "Good morning, It's such a nice day today."
            show william pijama think
            w "I need to think about where to invite Sabrina next."
            menu:
                "Where to invite Sabrina"
                
                "Beach walk":
                    $ invitation_choice = "invite_beach"
                    call invite_beach from _call_invite_beach
                
                "Go to cafe":
                    $ invitation_choice = "invite_cafe"
                    call invite_cafe from _call_invite_cafe
                    
        elif home2_visited == 2:
            if money >= 40:
                scene bg male bedroom night with fade
                show william smile with dissolve
                w "I'm tired and it's time to go to bed."
                hide william with moveoutright
                show william pijama smile with moveinright
                $ days_left -= 1
                scene bg male bedroom day with fade
                show william pijama smile
                w "Good morning, I have to get ready for school."
                hide william with moveoutright
                show william uniform smile with moveinright
                show screen map_button_sabrina
                $ current_location = "home2"
                $ next_location = "school2"
                n "Go to school."
                
            else:
                $ home2_visited += 1
                scene bg male bedroom day with fade
                play music main
                show william uniform smile with dissolve
                w "I need to get cleaned up and go to the meeting with Sabrina."
                hide william with moveoutright
                show william smile with moveinright
                w "I'm ready."
                if invitation_choice == "invite_beach":
                    show screen map_button_sabrina
                    $ current_location = "home2"
                    $ next_location = "beach"
                    n "Go to the beach."
                elif invitation_choice == "invite_cafe":
                    show screen map_button_sabrina
                    $ current_location = "home2"
                    $ next_location = "cafe"
                    n "Go to the cafe."
                
        elif home2_visited == 3:
            if money >= 40:
                scene bg male bedroom day with fade
                show william uniform smile with dissolve
                w "I need to get cleaned up and go to the meeting with Sabrina."
                hide william with moveoutright
                show william smile with moveinright
                show screen map_button_sabrina
                $ current_location = "home2"
                $ next_location = "cafe"
                n "Go to the cafe."
        
        elif home2_visited == 4:
            scene bg male bedroom night with fade
            if invitation_choice == "invite_beach":
                show william happy with dissolve
                w "Had such a great walk with Sabrina today and I'm glad that she like the photos."
                w "Now I can look at these pictures all day long."
                show william smile
                w "But now I need to go sleep."

            elif invitation_choice == "invite_cafe":
                show william smile with dissolve
                w "I hope Sabrina enjoyed our evening tonight."
                w "I'll have to figure out what to do next. {w}But that's tomorrow."
                w "Now I need to go sleep."
            
            hide william with moveoutright
            show william pijama smile with moveinright
            $ days_left -= 1
            scene bg male bedroom day with fade
            show william pijama smile
            w "Today is another good day."
            w "I need to go to school."
            hide william with moveoutright
            show william uniform smile with moveinright
            show screen map_button_sabrina
            $ current_location = "home2"
            $ next_location = "school2"
            n "Go to school."
        
        elif home2_visited == 5:
            if previous_location == "candy_shop2":
                scene bg male bedroom night with fade
                show william pijama smile with dissolve
                call homework from _call_homework
            
            else:
                scene bg male bedroom day with fade
                show william uniform smile with dissolve
                if action_choiсe == "games":
                    call homework from _call_homework_1

                elif action_choiсe == "homework":
                    call games from _call_games

        elif home2_visited == 6:
            scene bg male bedroom day with fade
            show william uniform smile
            w "I don't have a lot of time, so I have to pack up and get out of the house quickly."
            hide william with moveoutright
            show william smile with moveinright
            w "I'm ready."
            if invitation_choice == "invite_beach":
                show screen map_button_sabrina
                $ current_location = "home2"
                $ next_location = "beach"
                n "Go to the beach."
            elif invitation_choice == "invite_cafe":
                show screen map_button_sabrina
                $ current_location = "home2"
                $ next_location = "cafe"
                n "Go to the cafe."
            elif invitation_choice == "invite_concert":
                show screen map_button_sabrina
                $ current_location = "home2"
                $ next_location = "concert_hall"
                n "Go to the concert hall."
                
        elif home2_visited == 7:
            scene bg male bedroom night with fade
            show william smile
            w "Today was a very good day."
            w "There's hardly any time left to ask Sabrina to prom. {w}So I'll have to get an answer from her tomorrow."
            show william confused
            w "I hope she'll agree."
            show william smile 
            w "But now I need to go sleep."
            hide william with moveoutright
            show william pijama smile with moveinright
            $ days_left -= 1
            scene bg male bedroom day with fade
            show william pijama confused with dissolve
            w "I'm a little afraid to go up to sabrina and ask, but I have to, it's not like I tried for nothing."
            w "Maybe buy some flowers for Sabrina?"
            menu:
                "Buy some flowers for Sabrina?"
            
                "Yes":
                    jump buy_flowers2
            
                "No":
                    jump not_buy_flowers
        
    else:
        show screen map_button_sabrina
        w "I don't have to go home right now."
        
    return
    
label invite_beach:
    show william pijama happy
    w "Sabrina said she likes to sit on the beach in silence. {w}I'll invite her to take a walk there."
    w "I need to call Sabrina to invite her!"
    show william pijama smile at right1 with move
    play sound calling
    show screen phone_call("Sabrina", "images/sms_chat/icon_sabrina2.png", "Calling...") with dissolve
    pause 2
    show screen phone_call("Sabrina", "images/sms_chat/icon_sabrina2.png", "Conversation") with dissolve
    n "[char_name] is talking with Sabrina."
    show screen phone_call("Sabrina", "images/sms_chat/icon_sabrina2.png", "Call ended") with dissolve
    play sound end_call
    hide screen phone_call with dissolve
    show william pijama confused
    w "Eh, Sabrina's busy today."
    w "I need to find something to do."
    menu:
        "What to do?"
                
        "Play computer games":
            $ action_choiсe = "games"
            call games from _call_games_1
                
        "Do homework":
            $ action_choiсe = "homework"
            call homework from _call_homework_2

    return


label invite_cafe:
    show william pijama happy
    w "I think Sabrina likes to go to coffee shops and restaurants. {w}I'll take her out for her favourite drink."
    w "I can call Sabrina to invite her to the cafe!"
    show william pijama smile at right1 with move
    play sound calling
    show screen phone_call("Sabrina", "images/sms_chat/icon_sabrina2.png", "Calling...") with dissolve
    pause 2
    show screen phone_call("Sabrina", "images/sms_chat/icon_sabrina2.png", "Conversation") with dissolve
    n "[char_name] is talking with Sabrina."
    show screen phone_call("Sabrina", "images/sms_chat/icon_sabrina2.png", "Call ended") with dissolve
    play sound end_call
    hide screen phone_call with dissolve
    if money <=20:
        w "Sabrina's busy today."
        show william pijama confused
        w "But I have only $[money]. Maybe I won't have enough."
        show william pijama smile
        w "I should go to my mum's work, she has her own candy shop. I can help her with something and make some money."
        hide william with moveoutright
        show william smile with moveinright
        w "I am ready to go."
        show screen map_button_sabrina
        $ current_location = "home2"
        $ next_location = "candy_shop2"
        n "You need to go to mother work. She is working at candy shop."
    else:
        show william pijama confused
        w "Eh, Sabrina's busy today."
        w "I need to find something to do."
        menu:
            "What to do?"
                
            "Play computer games":
                $ action_choiсe = "games"
                call games from _call_games_2
                
            "Do homework":
                $ action_choiсe = "homework"
                call homework from _call_homework_3
        
    return

label games:
    w "I'm gonna go play my favourite computer game."
    show screen computer_button
    n "Click on the computer to play."
    
    return


label end:
    hide screen computer_button
    scene bg male bedroom night with fade
    show william pijama smile with dissolve
    w "I don't want to play anymore. It's time to go sleep."
    $ days_left -= 1
    scene bg male bedroom day with fade
    show william pijama smile with dissolve
    w "Good morning, I have to get ready for school."
    hide william with moveoutright
    show william uniform smile with moveinright
    show screen map_button_sabrina
    $ current_location = "home2"
    $ next_location = "school2"
    n "Go to school."
    
    return

label homework:
    w "I completely forgot, I have to do my homework."
    hide screen money_display
    hide screen earned_points
    scene homework_table with dissolve
    w "I have to learn a poem."
    n "Try to memorise the poem, after which you will need to put in the missing words."
    
    #Izsaucam ekrānu ar dzejoli
    show screen poem
    n "Read the poem."
    hide screen poem
    call learn_poem from _call_learn_poem
    show screen earned_points
    scene bg male bedroom night with fade
    show screen money_display
    show william pijama happy with dissolve
    w "Nice! I learned a poem."
    w "So, it's time to go sleep."
    $ days_left -= 1
    scene bg male bedroom day with fade
    show william pijama smile
    w "Good morning, I have to get ready for school."
    hide william with moveoutright
    show william uniform smile with moveinright
    show screen map_button_sabrina
    $ current_location = "home2"
    $ next_location = "school2"
    n "Go to school."
    return
    
label learn_poem:
    n "Fill in the blanks: 'Hold fast to dreams. For if ______ die'"
    #Ievaddatu saņemšana no spēlētāja
    $ answer1 = renpy.input("Type in a word:").strip().lower() #Spēlētāja ievadītais teksts pirms pārbaudes tiek pārveidots uz mazajiem burtiem un izdzēš liekas atstarpes
    if answer1 == "dreams":
        n "Correct!"
    else:
        n "Incorrect. Try again."
        jump learn_poem #Uzdevums atkārtojas, ja ir ievadīts nepareizs vārds
        
    n "Fill in the blanks: 'Life is a broken-winged ____, that cannot fly.'"
    $ answer1 = renpy.input("Type in a word:").strip().lower()
    if answer1 == "bird":
        n "Correct!"
    else:
        n "Incorrect. Try again."
        jump learn_poem
    
    n "Fill in the blanks: 'Hold fast to dreams, for when dreams __'"
    $ answer1 = renpy.input("Type in a word:").strip().lower()
    if answer1 == "go":
        n "Correct!"
    else:
        n "Incorrect. Try again."
        jump learn_poem
    
    n "Fill in the blanks: 'Life is a barren field, ______ with snow'"
    $ answer1 = renpy.input("Type in a word:").strip().lower()
    if answer1 == "frozen":
        n "Correct!"
    else:
        n "Incorrect. Try again."
        jump learn_poem

    return
    
label candy_shop2:
    stop music fadeout 1
    hide screen map_button_sabrina
    play music main
    if next_location == "candy_shop2":
        $ candy_shop2_visited += 1
        if candy_shop2_visited == 1:
            scene bg candy shop day with fade
            show mother work smile light at left1 with dissolve
            show william smile light at right1 with moveinright
            mum "Hi, [char_name]! {w}What are you doing here?"
            w "Hi, mum. I need to earn some money. {w}Maybe, I can do something at your work to earn."
            mum "Hmm, We've got a very dirty outside, if you clean it up, you make money."
            w "Nice!"
            hide mother with moveoutleft
            w "I need to go outside"
            hide william with moveoutright
            scene bg candy shop entrance day with fade
            n "Clean rubbish and dirt by pressing on it."
            while rubbish1_visible or rubbish2_visible or rubbish3_visible or rubbish4_visible or rubbish5_visible:
                show screen clean_rubbish
                $ renpy.pause(0.1) 
            hide screen clean_rubbish    
            n "You cleaned up all the rubbish."
            scene bg candy shop day with fade
            show mother work smile light at left1 with dissolve
            show william smile light at right1 with moveinright
            w "I did it."
            mum "Nice! Here is your $30."
            play sound money
            $ money += 30
            n "You have earned $30."
            show william happy light
            w "Thank you!"
            if invitation_choice == "invite_cafe":
                show william sad
                w "Oh. Finally I can go home."
                show screen map_button_sabrina
                $ previous_location = "candy_shop2"
                $ current_location = "candy_shop2"
                $ next_location = "home2"
                n "Go home."
            elif invitation_choice == "invite_concert":
                w "Now I can go to buy a tickets."
                show screen map_button_sabrina
                $ previous_location = "candy_shop2"
                $ current_location = "candy_shop2"
                $ next_location = "concert_hall"
                n "Go to the concert hall."
        
        elif candy_shop2_visited == 2:
            scene bg candy shop day with fade
            show mother work smile light at left1 with dissolve
            show william smile light at right1 with moveinright
            w "Hi, mum."
            mum "Hi, [char_name]! {w}Out of money again?"
            show william sad light
            w "Yes. I really need to make some money."
            mum "All right. {w}You need help sorting out the goods. There's a lot of people today, we can't keep up."
            show william happy
            w "Okey."
            hide william with moveoutright
            n "...[char_name] is sorting out the goods..."
            show william smile light with moveinright
            w "I'm done!"
            m "Thank you. Take your $50."
            $ money += 50
            play sound money
            n "You have earned $50."
            show william happy light
            w "Thanks, Mum!"
            mum "Bye, bye."
            hide mother with moveoutleft
            if invitation_choice == "invite_cafe":
                show william sad
                w "Oh. Finally I can go home."
                show screen map_button_sabrina
                $ previous_location = "candy_shop2"
                $ current_location = "candy_shop2"
                $ next_location = "home2"
                n "Go home."
            elif invitation_choice == "invite_concert":
                w "Now I can go to buy a tickets."
                show screen map_button_sabrina
                $ previous_location = "candy_shop2"
                $ current_location = "candy_shop2"
                $ next_location = "concert_hall"
                n "Go to the concert hall."
            
    else:
        show screen map_button_sabrina
        w "I don't have to go to candy shop right now."
        
    return
    
label cafe:
    hide screen map_button_sabrina
    if next_location == "cafe":
        scene bg bakery entrance afternoon with fade
        show william smile with dissolve
        w "Sabrina's not here yet. {w}I'm gonna go to see what I can buy for her."
        stop music fadeout 1
        scene bg bakery afternoon with fade
        play music cafe
        show william smile with moveinright

        call screen shop_menu
        
    else:
        show screen map_button_sabrina
        w "I don't have to go to the cafe right now."

    return
    

label buy_item1:
    if item == "coffee_with_honeycake":
        if money >= 25:
            n "You bought a two coffee with two honeycakes."
            play sound money
            $ money -= 25
            n "You spent $25"
        else:
            n "You don't have enough money."
    elif item == "coffee_with_cheesecake":
        if money >= 30:
            n "You bought a two coffee with two cheesecakes."
            play sound money
            $ money -= 30
            n "You spent $30"
        else:
            "You don't have enough money."

    jump cafe_after


label cafe_after:
    show william happy
    w "Great, I had enough money. {w}I'm gonna go find an empty table."
    hide william with moveoutleft
    scene bg cafe with fade
    show william happy with moveinright
    w "How lucky I am to be able to choose any table. {w}I'll stay here."
    show sabrina smile light at left3 with moveinright
    show william happy light at right1 with move
    w "Hi!"
    s "Hi."
    show william smile light
    w "I've already placed an order, so we'll just have to wait."
    show sabrina happy light
    s "Nice."
    show salesperson light at left1 with moveinleft
    if item == "coffee_with_honeycake":
        sal "Hello, this is for you. Enjoy."
        show coffee1_icon at Transform(xpos=1071, ypos=619)
        show coffee2_icon at Transform(xpos=954, ypos=619)
        show honeycake1_icon at Transform(xpos=1161, ypos=655)
        show honeycake2_icon at Transform(xpos=855, ypos=645)
        show william happy light
        w "Thank you!"
        hide salesperson with moveoutleft
        w "I hope I ordered what you like."
        s "Yea, I like coffee. {w}But what kind of dessert it is?"
        show william smile light
        w "Honey cake."
        show sabrina sad light
        s "I don't like honey cake, I told you!"
        $ point_sabrina -= 1
        $ girl = point_sabrina
        play sound minus_point
        n "Sabrina is sad, that you don't remember what is her favourite dessert -1 point."
        show william confused light
        w "Omg, I forgot about that, sorry."
        s "I'll have to drink only coffee. {w}You can have my piece too."
        menu:
            "Try to change honeycake?"
                
            "Change":
                call change from _call_change
                
            "Not change":
                call not_change from _call_not_change
                
        show screen map_button_sabrina
        $ current_location = "cafe"
        $ next_location = "home2"
        n "Go home."
        
    elif item == "coffee_with_cheesecake":
        sal "Hello, this is for you. Enjoy."
        show coffee1_icon at Transform(xpos=1071, ypos=619)
        show coffee2_icon at Transform(xpos=954, ypos=619)
        show cheesecake1_icon at Transform(xpos=1161, ypos=655)
        show cheesecake2_icon at Transform(xpos=855, ypos=645)
        show william happy light
        w "Thank you!"
        hide salesperson with moveoutleft
        w "I hope I ordered what you like."
        show sabrina happy light
        s "Oh, you ordered my favourite dessert!"
        w "Yes, I rememered that."
        $ point_sabrina += 2
        $ girl = point_sabrina
        play sound plus_point
        n "Sabrina is happy, that you remember and order her favourite dessert +2 points."
        show william smile light
        show sabrina smile light
        n "...Talk..."
        hide coffee1_icon
        hide coffee2_icon
        hide cheesecake1_icon
        hide cheesecake2_icon
        w "So, it's time to go home."
        show sabrina happy light
        s "Yes. Thank you for the evening."
        show william happy light
        w "Thank you too."
        hide sabrina with moveoutright
        show screen map_button_sabrina
        $ current_location = "cafe"
        $ next_location = "home2"
        n "Go home."
        
    return


label change:
    w "Wait a few minutes."
    hide william with moveoutright
    scene bg bakery afternoon with fade
    show salesperson at left1 with dissolve
    show william smile with moveinleft
    w "Can I have a question?"
    sal "Yes of course."
    w "I ordered a two coffee and two honeycakes. Can I change one honey cake to cheesecake?"
    sal "Yes, but you will have to pay an extra $5."
    if money >= 5:
        show william happy light
        w "Nice."
        play sound money
        $ money -= 5
        "You spend $5 for cheesecake."
        hide william with moveoutleft
        scene bg cafe with fade
        show sabrina sad light at left3 with dissolve
        show coffee1_icon at Transform(xpos=1071, ypos=619)
        show coffee2_icon at Transform(xpos=954, ypos=619)
        show honeycake1_icon at Transform(xpos=1161, ypos=655)
        show honeycake2_icon at Transform(xpos=855, ypos=645)
        show william smile light at right1 with moveinright
        w "I'm here."
        s "I see."
        show salesperson at left1 with moveinleft
        hide honeycake2_icon 
        show cheesecake2_icon at Transform(xpos=855, ypos=645)
        hide salesperson with moveoutleft
        show sabrina happy light
        s "Oh, this is for me?"
        w "Yes."
        s "Thank you, this is my favourite dessert!"
        $ point_sabrina += 1
        $ girl = point_sabrina
        play sound plus_point
        n "Sabrina is happy, that you order her favourite dessert +1 point."
        show william happy light
        w "Nice, that you like it."
        show william smile light
        show sabrina smile light
        n "...Talk..."
        hide coffee1_icon 
        hide coffee2_icon
        hide honeycake1_icon
        hide cheesecake2_icon
        w "So, it's time to go home."
        show sabrina happy light
        s "Yes. Thank you for the evening."
        show william happy light
        w "Thank you too."
        hide sabrina with moveoutright
        
    else:
        show william sad light
        n "You don't have $5."
        w "Sorry, I don't want to change."
        hide william with moveoutleft
        scene bg cafe with fade
        show sabrina sad light at left3 with dissolve
        show coffee1_icon at Transform(xpos=1071, ypos=619)
        show coffee2_icon at Transform(xpos=954, ypos=619)
        show honeycake1_icon at Transform(xpos=1161, ypos=655)
        show honeycake2_icon at Transform(xpos=855, ypos=645)
        show william confused light at right1 with moveinright
        w "I'm here."
        s "I see."
        show william smile light
        show sabrina smile light
        n "...Talk..."
        hide coffee1_icon 
        hide coffee2_icon
        hide honeycake1_icon
        hide honeycake2_icon
        w "So, it's time to go home."
        s "Yes. Thanks for coffee."
        show william happy light
        w "Thanks for evening."
        hide sabrina with moveoutright
    
    return
    
    
label not_change:
    w "I'm so sorry."
    s "It's okay."
    show william smile light
    show sabrina smile light
    n "...Talk..."
    hide coffee1_icon 
    hide coffee2_icon
    hide honeycake1_icon
    hide honeycake2_icon
    w "So, it's time to go home."
    s "Yes. Thanks for coffee."
    show william happy light
    w "Thanks for evening."
    hide sabrina with moveoutright
    
    return
    
label invite_cafe2:
    w "I will invite her to the cafe."
    t "Thank you class. That's all for today."
    w "Nice, lessons is over."
    stop music fadeout 1
    scene bg corridor day with fade
    play music corridor
    show william uniform smile with dissolve
    w "I need to find Sabrina, to invite her."
    hide william with moveoutleft
    stop music fadeout 1
    scene bg courtyard day with fade
    play music courtyard
    show sabrina uniform smile light at left1 with dissolve
    show william uniform smile light with moveinleft
    w "Hi, Sabrina!"
    s "Hi."
    w "Maybe you want to go with me to the cafe?"
    s "Hm, when?"
    w "We can go tomorrow at evening."
    s "Okey, let's go."
    $ point_sabrina += 1
    $ girl = point_sabrina
    play sound plus_point
    n "Sabrina like, that you invited her to the cafe +1 point."
    show william uniform happy light
    w "Cool, see you tomorrow then."
    s "See you tomorrow."
    hide sabrina with moveoutright
    w "I'm happy, that Sabrina agree."
    if money >= 30:
        show william uniform smile
        w "Now I can go home."
        show screen map_button_sabrina
        $ current_location = "school2"
        $ next_location = "home2"
        n "Go home."
    else:
        show william uniform suprized
        w "I don't think there's enough money to go to a cafe."
        show william uniform smile
        w "I've got time to earn."
        show screen map_button_sabrina
        $ current_location = "school2"
        $ next_location = "candy_shop2"
        n "Go to the candy shop, to earn some money."

    return

label beach:
    stop music fadeout 1
    hide screen map_button_sabrina
    play music beach
    if next_location == "beach":
        scene bg beach afternoon with fade
        show william smile light with dissolve
        show sabrina smile light at left1 with moveinleft
        w "Hi."
        s "Hi."
        w "It's very beautiful here today."
        show sabrina happy light
        s "Yes, it's very beautiful."
        w "Come here often?"
        show sabrina smile light
        s "Yeah, I like to come and watch the sunset here."
        show william happy light 
        w "Cool. {w}You know, I brought my camera, let me take some pictures for you."
        show sabrina happy light
        s "Wow, yes. I really want!"
        hide william with moveoutright
        show sabrina smile at center with move
        hide screen earned_points
        
        #Kameras rāmja paradīšana
        show camera_frame at center
        n "Touch the screen to take a picture."
        
        #Izsaucam zibspuldzes efektu
        play sound camera_flash
        show camera_frame with flash
        w "Let's make more."
        show sabrina happy
        play sound camera_flash
        show camera_frame with flash
        w "Wow, the pictures are very beautiful."
        s "Show me."
        hide camera_frame
        hide sabrina with moveoutright
        
        #Izsaucam ekrānu ar foto attēliem
        call screen photos
        
    else:
        show screen map_button_sabrina
        w "I don't have to go to the beach right now."

    return
    

label after_photo:
    show william smile light with dissolve
    show sabrina happy light at left1 with dissolve
    show screen earned_points with dissolve
    s "Very nice photos! I like them."
    $ point_sabrina += 1
    $ girl = point_sabrina
    play sound plus_point
    n "Sabrina liked the pictures +1 point."
    show william happy light
    w "Yeah, I really like it too."
    s "Now I need to go. {w}I have plans."
    menu:
        "Offer to accompany Sabrina?"
                
        "Yes":
            call yes1 from _call_yes1
                
        "No":
            call no1 from _call_no1
    
    w "Okey, see you tommorow then."
    m "Bye."
    hide sabrina with moveoutleft
    show screen map_button_sabrina
    $ current_location = "beach"
    $ next_location = "home2"
    n "Go home."
    
    return


label yes1:
    show william smile light
    w "Can I accompany you?"
    show sabrina smile light
    m "Thanks, but my friend gonna pick me up."
    $ point_sabrina += 1
    $ girl = point_sabrina
    play sound plus_point
    n "+1 point for wanting to accompany Sabrina."

    return
    
    
label no1:
    show william smile light
    show sabrina smile light
    
    return
    
label invite_beach2:
    w "I will invite her to the beach walk."
    t "Thank you class. That's all for today."
    w "Nice, lessons is over."
    stop music fadeout 1
    scene bg corridor day with fade
    play music corridor
    show william uniform smile with dissolve
    w "I need to find Sabrina, to invite her."
    hide william with moveoutleft
    stop music fadeout 1
    scene bg courtyard day with fade
    play music courtyard
    show sabrina uniform smile light at left1 with dissolve
    show william uniform smile light with moveinleft
    w "Hi, Sabrina!"
    s "Hi."
    w "Maybe you want to go with me to the beach?"
    s "Hm, when?"
    w "We can go tomorrow at evening."
    s "Okey, let's go."
    $ point_sabrina += 1
    $ girl = point_sabrina
    play sound plus_point
    n "Sabrina's pleased that you decided to take her to her favourite place +1 point."
    show william uniform happy light
    w "Cool, see you tomorrow then."
    s "See you tomorrow."
    hide sabrina with moveoutright
    w "I'm happy, that Sabrina agree."
    show william uniform smile
    w "Now I can go home."
    show screen map_button_sabrina
    $ current_location = "school2"
    $ next_location = "home2"
    n "Go home."
    
    return

label invite_concert:
    w "I will invite her to the concert."
    t "Thank you class. That's all for today."
    w "Nice, lessons is over."
    stop music fadeout 1
    scene bg corridor day with fade
    play music corridor
    show william uniform smile with dissolve
    w "I need to find Sabrina, to invite her."
    hide william with moveoutleft
    stop music fadeout 1
    scene bg courtyard day with fade
    play music courtyard
    show sabrina uniform smile light at left1 with dissolve
    show william uniform smile light with moveinleft
    w "Hi, Sabrina!"
    s "Hi."
    w "Maybe you want to go with me to the concert?"
    s "Hm, when?"
    w "I'll see what time the concerts are tomorrow."
    s "Okey. {w}I agree."
    show william uniform happy light
    w "Cool, see you tomorrow then."
    s "See you tomorrow."
    hide sabrina with moveoutright
    w "I'm happy, that Sabrina agree."
    if money >= 30:
        show william uniform smile
        w "Now I need to go to buy a concert tickets."
        show screen map_button_sabrina
        $ current_location = "school2"
        $ next_location = "concert_hall"
        n "Go to the concert hall, to buy a tickets."

    else:
        show william uniform suprized
        w "I don't think there's enough money to buy a tickets."
        show william uniform smile
        w "I've got time to earn."
        show screen map_button_sabrina
        $ current_location = "school2"
        $ next_location = "candy_shop2"
        n "Go to the candy shop, to earn some money."

    return


label concert_hall:
    hide screen map_button_sabrina
    if next_location == "concert_hall":
        $ concert_hall_visited += 1
        if concert_hall_visited == 1:
            scene bg concert hall entrance afternoon with fade
            show william smile with dissolve
            n "Choose whose concert you want to attend - Ariana Grande's or Lady Gaga's."
            call screen buy_concert_ticket
            show william happy
            w "Nice, tickets are purchased."
            w "I'll give the ticket to Sabrina at school tomorrow."
            show screen map_button_sabrina
            $ current_location = "concert_hall"
            $ next_location = "home2"
            show william smile
            w "I need to go home."
        elif concert_hall_visited == 2:
            scene bg concert hall entrance afternoon with fade
            show william smile light with dissolve
            show sabrina smile light at left1 with moveinleft
            w "The concert's about to start, come on, let's go."
            show sabrina happy light
            s "Let's go"
            stop music fadeout 1
            scene bg concert hall with fade
            play music concert
            n "...An artiste is performing..."
            stop music fadeout 1
            scene bg concert hall entrance night with fade
            play music main
            show sabrina happy light at left1 with dissolve
            show william smile light with dissolve
            s "Wow, that was exelent. I liked."
            show william happy light 
            w "Me too."
            $ point_sabrina += 1
            $ girl = point_sabrina
            play sound plus_point
            n "Sabrina like the concert +1 point."
            s "Thank you very much! Now I need to go home."
            w "Thank you too. Bye, bye!"
            hide sabrina with moveoutleft
            show screen map_button_sabrina
            $ current_location = "concert_hall"
            $ next_location = "home2"
            n "Go home."

    else:
        show screen map_button_sabrina
        w "I don't have to go to the concert hall right now."
    
    return


label buy_grande:
    $ concert_ticket_choise = "buy_grande"
    n "You bought two tickets to an Ariana Grande concert."
    $ money -= 30
    play sound money
    n "You spent $30 for 2 tickets."

    return
    
    
label buy_gaga:
    $ concert_ticket_choise = "buy_gaga"
    n "You bought two tickets to an Lady Gaga concert."
    $ money -= 30
    play sound money
    n "You spent $30 for 2 tickets."

    return