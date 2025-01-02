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
    #Sakrāto punktu paradīšana
    $ girl = point_mia #Mainīgā point_mia vērtība tiek piešķirta mainīgajam girl
    show screen earned_points
    n "The points scored will be displayed on the right hand side"
    play sound plus_point
    #Palielina mainīgā point_mia vērtību par 1.
    $ point_mia += 1
    
    #Atjaunina mainīgo girl vērtību
    $ girl = point_mia
    n "Congratulations! You've earned + 1 point for the invitation."
    #Jauna diena
    $ days_left -= 1
    
    scene bg male bedroom day with fade
    show william pijama smile with dissolve
    w "Oh, morning... Well, the day has finally arrived!"
    show william pijama confused
    w "Today is the meeting with Mia, and I think I'm a little nervous. {w}But why worry?"
    show william pijama smile 
    w "It's gonna be great. It's all about being yourself! {w}I've got to go get ready."
    hide william with moveoutright
    show william smile with moveinright
    w "I'm ready!"
    show william confused
    w "I've got to think of something to talk about. {w}But we've been texting pretty well, so it should be easy."
    w "Okay, just don't be shy and everything will be fine."
    show screen map_button
    
    #Noslēpt māju mapē, jo spēlētājs atrodas mājā
    $ current_location = "home"
    
    #Jādodas uz parku
    $ next_location = "park"
    n "To go to the meeting, open the map and find the park."
    
    return
    

label park:
    stop music fadeout 1
    hide screen map_button
    play music park
    if next_location == "park":
        scene bg park day with fade
        show william smile light at right1 with moveinright
        show mia smile light at left2 with moveinleft
        
        #Sakrāto punktu paradīšana
        $ girl = point_mia
        show screen earned_points
        w "Hi, Mia!"
        m "Hi, [char_name]!"

#Informācijas loga paradīšana
        show screen information
        w "It's a beautiful park, isn't it? Do you come here often?"
        m "Yeah, sometimes. I like to hang out here after school when I have some free time."
        show william happy light
        w "Great, good for the brain, huh? It's hard to switch off after studying. {w}By the way, I hear you're doing well in your studies, you probably have an ‘A’ in all your subjects, right?"
        show mia confused light
        m "Well, yeah, I try. It's just that I'm used to always learning, I guess it's part of who I am."
        w "Wow, cool! What's your favourite subject? Maybe I can understand something and tighten up my knowledge too, to be honest, I'm not the most diligent student."
        show mia shy light
        m "My favourite? Probably maths... Or chemistry. I like everything to be logical and have answers to questions. How about you?"
        show william smile light
        w "Maths, you say... well, it doesn't come to me straight away, but you've almost inspired me to try and understand it better!"
        menu:
            "What's your favourite subject?"
            
            "History":
                call history from _call_history
            
            "Sport":
                call sport from _call_sport
            
            "None":
                call none from _call_none
        
        show william smile light
        w "All right, well, school's out of the way. {w}Listen, what do you usually do in your free time?"
        show mia smile light
        m "Um, I like to read. I like to escape into another world for a while. Do you?"
        w "I don't read books, I like watching films better. {w} Do you have a favourite book? "
        m "Yes, have one favorite book ‘Romeo and Juliet by William Shakespeare. We had to read it as part of our school curriculum and I just loved it so much."
        m "But films are interesting too, sometimes I watch films, but I feel I get more emotion when I read books."
        
        menu:
            "Continue the dialogue"
            
            "What genres of films do you like?":
                call genres_of_films from _call_genres_of_films
            
            "Maybe, but you can get a lot of emotion from the film as well.":
                call emotion from _call_emotion
            
        w "Besides reading books, what else do you like to do?"
        m "I'm also into drawing and cooking. It helps me to relax after studying."
        show william confused light
        w "That's awesome! I can't cook at all."
        show william smile light
        m "It's just that I've been helping my mum since I was a kid and that's how I learned to cook."
        w "And what's your favourite thing to cook?"
        show mia happy light
        m "I like to cook pasta as a staple food, it doesn't take long and it's very tasty, and in the morning I like to drink green tea with pancakes."
        show william happy light
        w "Pasta is very tasty! You told, that you like to drawing too. What do you like to draw the most?"
        show mia smile light
        m "Landscapes. Especially nature"
        show william smile light
        w "Interesting! I'll have to see your work sometime."
        w "If you like to paint, you probably like to visit art galleries?"
        show mia sad light
        m "I would really like to go to different galleries, but alone is not so interesting, I want to discuss each picture with someone, and my parents do not understand anything about it."
        show william sad light
        w "I don't know anything about it either."
        m "Well, you have to be interested in it to understand it."
        w "Maybe."
        
        menu:
            "What suggest?"
            
            "Drink coffee":
                call coffee from _call_coffee
            
            "Drink tea":
                call tea from _call_tea
        
        #Ja spēlētājs nav aizvēris informācijas logu, tas paslēpjas šajā vietā
        hide screen information
        
        #Kartes pogas paradīšana
        show screen map_button
        $ current_location = "park"
        $ next_location = "bakery"
        n "You need to go to the bakery"
    
    else:
        show screen map_button
        w "I don't have to go to the park right now."
        
        return

        
label history:
    w "And I guess I've got history. There are so many interesting stories and events, it's like time travelling."
    show mia smile light
    m "Oh, the story is interesting too! I like how everything is connected: one event influences another. I don't have a very good memory for dates, though."
    show william happy light
    w "Yeah, that's for sure. I usually remember through some fun facts. Like how one emperor ate so many cakes that he was nicknamed ‘The Cake Emperor’... not sure if that's a real story though."
    show mia happy light
    m "Sounds... not believable, but fun! You clearly need to teach history that way."
    w "Yeah, I'll tell it through jokes, maybe at least I'd do better that way."
    
    return


label sport:
    w "I'm probably into sports. There is so much adrenaline and emotion there, as if it were a real battle, only without the wars."
    show mia smile light
    m "Sport? Really? What's your favourite?"
    w "Football, definitely! It's all about teamwork, strategy and action. You stand on the pitch and every moment decides something. {w}Do you play sports yourself?"
    show mia confused light
    m "Um. to be honest, I'm not really into sports. It's not really my thing. I'm more of a relaxed kind of guy - books, learning new things... I know it sounds boring."
    menu:
        "Sound really boring?"
        
        "Boring":
            call boring from _call_boring
        
        "Not boring":
            call not_boring from _call_not_boring
    
    return


label none:
    show william confused light
    w "I don't even know... To be honest, I don't have any. I don't like any of them, I study just because I have to."
    show mia confused light
    m "Really? None at all? Or maybe you just haven't found something of your own?"
    w "Maybe... I just don't feel passionate about anything in particular. Sometimes I think that if I didn't have to study, I probably wouldn't be doing it."
    m "I understand. A lot of people have that."
    
    return


label boring:
    show william sad light
    w "Well. yeah, it sounds kind of boring. It's hard for me to sit still or read for long periods of time. I want to move all the time."
    show mia sad light
    m "Yeah, I understand."
    play sound minus_point
    $ point_mia -= 1
    $ girl = point_mia
    "Mia got sad! You lose 1 point."
    
    return

    
label not_boring:
    w "No, it's not boring! At least you know a lot of things and can easily understand any complicated topic. And sport is not for everyone, that's okay."
    show mia happy light
    m "I'm attracted to the fact that you feel that way."
    play sound plus_point
    $ point_mia += 1
    $ girl = point_mia
    "Mia likes your answer! You get 1 point."
    
    return


label genres_of_films:
    w "What genres of films do you like?"
    m "I mostly watch dramas and melodramas. I like it when there are interesting characters and emotional moments. {w}But I don't like sci-fi or horror at all."
    show william sad light
    w "I see. I'm the opposite! I love horror and sci-fi. Those genres are my thing. When you watch horror, everything inside is so tense, but then you feel so relieved, as if you had experienced something terrible."
    w "And sci-fi is another world where everything is possible. I especially like it when it's about inventions or space."
    show mia sad light
    m "I find horror too scary. I don't know if I could sit through a film like that."
    show william smile light
    w "Yeah, a lot of people don't like them. But I like the adrenaline. And then, most horror films aren't that scary, they just create tension."
    show mia smile light
    m "Probably"
    
    return


label emotion:
    w "Maybe, but you can get a lot of emotion from the film as well"
    m "Yes, of course. I'm not arguing, films can be very emotional too. It's just that in books you imagine everything the way you want it to be, while a film gives you a ready-made picture."
    w "It's true, but sometimes it's the finished picture that strikes you. The way the directors convey the atmosphere, the music they choose - it all creates a special mood."
    m "Yeah, I agree. The soundtrack in a film can sometimes do half the work. Without the right music, even the strongest scenes can seem boring."
    w "I agree."
    
    return


label coffee:
    show william happy light
    w "Maybe we could go for a coffee?"
    m "It's a good idea, but I don't drink coffee. Like I said, I like green tea."
    play sound minus_point
    $ point_mia -= 1
    $ girl = point_mia
    n "Mia thought you were paying attention -1 point."
    show william smile light
    w "Then let's go and get some tea."
    show mia smile light
    m "Let's go!"
    
    return
    
    
label tea:
    show william happy light
    w "Maybe we could go for a tea?"
    show mia smile light
    m "It's a good idea"
    play sound plus_point
    $ point_mia += 1
    $ girl = point_mia
    n "Mia is glad that you remembered that she likes to drink green tea +1 point."
    w "Then let's go and get some tea."
    m "Let's go!"
    
    return 
    
    label bakery:
    stop music fadeout 1
    hide screen map_button
    play music main
    if next_location == "bakery":
        scene bg bakery entrance afternoon with fade
        show william smile light at right1 with moveinright
        show mia smile light at left2 with moveinright
        w "Wait here then, I'll just go and get some and then we'll go for a walk."
        m "Okey."
        scene bg bakery afternoon with fade
        n "Welcome to the bakery."
        show screen money_display
        n "Now your money will be displayed at the top."
        show william smile with moveinright
        
        define tea = 0
        define coffee = 0 
        define item = ""
        
        #Ekrāns ar precēm
        call screen shop_menu_drink
        
    else:
        show screen map_button
        w "I don't have to go to the bakery right now."

    return
    
    
label buy_item:
    if item == "tea":
        if money >= 5:
            n "You bought a tea."
            play sound money
            $ money -= 5
            n "You spent $5"
        else:
            n "Tea costs $5. You don't have enough."
    elif item == "coffee":
        if money >= 10:
            n "You bought a coffee."
            play sound money
            $ money -= 10
            n "You spent $20"
        else:
            "Coffee costs $10. You don't have enough."

    jump bakery_after

label bakery_after:
    hide william with moveoutright
    scene bg bakery entrance afternoon with fade
    show mia smile light at left2
    show william smile light at right1 with moveinright
    if item == "tea":
        show tea1_icon at Transform(xpos=1227, ypos=931)
        show tea2_icon at Transform(xpos=1330, ypos=678)
        w "This is for you."
        show tea2_icon at Transform(xpos=565, ypos=757)
        show mia happy light
        m "Thank you"
        $ point_mia += 1
        $ girl = point_mia
        play sound plus_point
        n "Mia is pleased that you bought her favourite drink +1 point."
    elif item == "coffee":
        show coffee1_icon at Transform(xpos=1227, ypos=931)
        show coffee2_icon at Transform(xpos=1330, ypos=678)
        w "This is for you."
        show coffee2_icon at Transform(xpos=565, ypos=757)
        show mia sad light
        m "I told you I don't like coffee."
        $ point_mia -= 1
        $ girl = point_mia
        play sound minus_point
        n "Mia's upset that you didn't remember the second time she didn't like coffee -1 point."
        show william confused light
        w "Oh, sorry. I can went to buy a tea."
        m "No, thank you."
    stop music fadeout 1
    scene bg bakery entrance night with fade
    play music night_street
    show mia smile light at left2
    show william smile light at right1
    w "It's really late, it's time to go home."
    m "Yes."
        
    menu:
        "What to do?"
            
        "Walk a Mia home":
            jump mia_home
            
        "Hail a taxi (Costs 15$)":
            jump taxi
            
        "Returned to their homes":
            jump go_home
            
    return
    
    