#Spēles varoņu deklarēšana
define w = Character("[char_name]", color="#80b3ff", callback=name_callback, cb_name="william") #cb_name="william" - pirmais vārds attēla nosaukumam
define t = Character("Teacher", color="#ff0000", callback=name_callback, cb_name="teacher")
define m = Character("Mia", color="#ff99dd", callback=name_callback, cb_name="mia")
define s = Character("Sabrina", color="#ff99dd", callback=name_callback, cb_name="sabrina")

#Varoņu pozīciju definēšana
init:
    $ right1 = Position(xalign=0.8, yalign=1.1)
    $ left1 = Position(xalign=0.1, yalign=1.1)
    $ left2 = Position(xalign=0.4, yalign=1.1)
    $ right2 = Position(xalign=0.9, yalign=1.1)
    $ left3 = Position(xalign=0.3, yalign=1.1)
    
#Tabulas ar meiteņu personīgo informāciju    
screen info_panel_mia:
        #Spēle neturpinās, kamēr nav aizvērts ekrāns
        modal True
        frame:
            #Blokā teksta attālums no sāniem, augšas un apakšas
            padding(10,10)
            xalign 0.75
            yalign 0.3
            xsize 400
            
            #Vertikālā kaste
            vbox:
                xsize 380
                text "{color=#80b3ff}INFORMATION" xalign 0.5 #Centrēt tekstu
                null height 15
                text "{color=#80b3ff}NAME{/color}: {size=30}Mia"
                text "{color=#80b3ff}AGE{/color}: {size=30}18"
                text "{color=#80b3ff}HOBBIE{/color}: {size=30}Reading and creativity"
                text "{color=#80b3ff}BRIEF DESCRIPTION{/color}: {size=30}Shy, intelligent, clever, loves literature, passionate about writing short stories."
                #Atstarpe starp tekstu un pogu aizvērt 15px
                null height 15
                textbutton "CLOSE" action Hide("info_panel_mia") xalign 0.5

screen info_panel_sabrina:
        modal True
        frame:
            padding(10,10)
            xalign 0.75
            yalign 0.3
            xsize 400
            
            vbox:
                xsize 380
                text "{color=#80b3ff}INFORMATION" xalign 0.5
                null height 15
                text "{color=#80b3ff}NAME{/color}: {size=30}Sabrina"
                text "{color=#80b3ff}AGE{/color}: {size=30}19"
                text "{color=#80b3ff}HOBBIE{/color}: {size=30}Style and Fashion"
                text "{color=#80b3ff}BRIEF DESCRIPTION{/color}: {size=30}Style icon, follows fashion trends, always looks flawless, self-loved."
                null height 15
                textbutton "CLOSE" action Hide("info_panel_sabrina") xalign 0.5

#SMS tērzētava
default messages = [] #Saraksts ziņu glabāšanai
define message_sound = "sounds/message_sound.mp3" #skaņas efektu definēšana
#SMS tērzētavas ekrāns
screen sms_chat:
    frame:
        xalign 0.3
        yalign 0.3
        xsize 400
        ysize 850
        background "images/sms_chat/phone_background.png"
        foreground "images/sms_chat/phone_foreground.png"

        #Teksta bloks ar sarunas varoņa vārdu
        frame:
            xalign 0.5
            yalign 0.06
            xsize 300
            vbox:
                xalign 0.5
                yalign 0.06
                text contact_name size 30 color "#FFFFFF"

        #Ziņojumu rādīšanas lauks
        vbox:
            xalign 0.2
            yalign 0.4
            spacing 10

            #Visu ziņojumu rādīšana
            for message in messages:
                hbox:
                    if message[0] == "w":
                        spacing 10
                        add "images/sms_chat/icon_william.png" xsize 40 ysize 40
                        text message[1] size 20 color "#FFFFFF" xmaximum 250 #Teksta bloka maksimālais platums
                    else:
                        spacing 10
                        add contact_icon xsize 40 ysize 40 
                        text message[1] size 20 color "#FFFFFF" xmaximum 250

init python:
    #Ziņu pievienošana
    def display_message(character, text):
        messages.append((character, text))
    
    #Skaņas efektu pievienošana
    def play_message_sound():
        renpy.sound.play(message_sound)

#Ziņojumi ar katru meiteni
default messages_list_mia = [
    ("w", "Hey, did you finish the project?"),
    ("m", "Hi, yes, almost done. Just need a few tweaks."),
    ("w", "That's awesome! How about a walk in the park tomorrow?"),
    ("m", "That's a good idea, what time?"),
    ("w", "Let's go at 3pm"),
    ("m", "Great")
]

default messages_list_sabrina = [
    ("w", "Hey, How are you?"),
    ("s", "Hi! Good, what about you?"),
    ("w", "Also good. How about a walk in the park tomorrow?"),
    ("s", "Where do we go out?"),
    ("w", "We can go to the park first to socialise."),
    ("s", "I have plans for tomorrow "),
    ("w", "But maybe you have time tomorrow in the evening, about 8pm?"),
    ("s", "I think so."),
    ("w", "Great, see you tomorrow!")
]

#Sakrāšanas punktu sistēma
default maxpoint = 10
default minpoint = 0

default point_mia = 0
default point_sabrina = 0

default girl = 0

#Attiecību ekrāna josla
screen earned_points:
    vbox:
        align (0.95, 0.5)
        #Sakrāto punktu paradīšana
        text "{b}[girl]/[maxpoint]{/b}" size 25 color "#ff80b3" xalign 0.45
        vbar:
            xsize 200
            ysize 400
            #Vērtības piesaistīšana mainīgajam
            value AnimatedValue(value=girl, range=maxpoint, delay=1.0) #1 sekundes aizkave
            #Attēli pilnai un tukšai joslai
            bottom_bar Frame("gui/bar/bottom1.png", 10, 10)
            top_bar Frame("gui/bar/top1.png", 10, 10)