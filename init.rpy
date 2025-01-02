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

#Dienu skaitītājs
default days_left = 7
screen days_left_display:
    text "{b}Days left: [days_left]{/b}" xpos 0.89 ypos 0.01 color "#FFFFFF" size 30

#Mainīgais, kas seko nākamajai lokācijai
default next_location = "none"

#Mainīgais, kas glabā pašreizējo lokāciju
default current_location = "none"

#Mainīgais, kas glabā iepriekšējo lokāciju
default previous_location = "none"

#Mainīgie, kas uzskaita, cik reizes spēlētājs ir “apmeklējis” noteikto vietu
default home_visited = 0
default cinema_visited = 0
default gallery_visited = 0
default school_visited = 0
default candy_shop_visited = 0

#Kartes ekrāns, izvēloties Mīju
screen map:
    modal True
    #Ekrāns tiks parādīts virs visiem pārējiem ekrāniem. Numurs norāda, kādā secībā ekrāns tiek parādīts (zorder 0 ir vistālākais ekrāns)
    zorder 100
    fixed:
        xsize 1920 ysize 1119
        add "images/map/map.gif" align(0.5,0.5) #Centrēšana
    fixed:
        xsize 1920 ysize 1119
        #Lokāciju definēšana
        button:
            xpos 634 ypos 348
            xsize 90 ysize 90
            idle_background "images/map/house.png"
            hover_foreground "images/map/house_hover.png"    
            tooltip "{b}Home{/b}{p}{i}{size=20}Click to go home{/i}"
            action Hide("map"), Jump("home")
            #Poga nav aktīva, ja spēlētājs atrodas tajā vietā
            sensitive current_location != "home"
        
        button:
            xpos 798 ypos 528
            xsize 80 ysize 80
            idle_background "images/map/school.png"
            hover_foreground "images/map/school_hover.png"
            tooltip "{b}School{/b}{p}{i}{size=20}Click to go to school{/i}"
            action Hide("map"), Jump("school")
            sensitive current_location != "school"
            
        button:
            xpos 646 ypos 675
            xsize 80 ysize 80
            idle_background "images/map/park.png"
            hover_foreground "images/map/park_hover.png"
            tooltip "{b}Park{/b}{p}{i}{size=20}Click to go to the park{/i}"
            action Hide("map"), Jump("park")
            sensitive current_location != "park"
            
        button:
            xpos 1231 ypos 513
            xsize 80 ysize 80
            idle_background "images/map/cinema.png"
            hover_foreground "images/map/cinema_hover.png"
            tooltip "{b}Cinema{/b}{p}{i}{size=20}Click to go to the cinema{/i}"
            action Hide("map"), Jump("cinema")
            sensitive current_location != "cinema"
        
        button:
            xpos 765 ypos 649
            xsize 80 ysize 80
            idle_background "images/map/bakery.png"
            hover_foreground "images/map/bakery_hover.png"
            tooltip "{b}Bakery{/b}{p}{i}{size=20}Click to go to the bakery{/i}"
            action Hide("map"), Jump("bakery")
            sensitive current_location != "bakery"
        
        button:
            xpos 480 ypos 552
            xsize 80 ysize 80
            idle_background "images/map/house_mia.png"
            hover_foreground "images/map/house_mia_hover.png"
            tooltip "{b}Mia's house{/b}{p}{i}{size=20}Click to go to Mia's house{/i}"
            action Hide("map"), Jump("house_mia")
            sensitive current_location != "house_mia"
        
        button:
            xpos 1266 ypos 297
            xsize 80 ysize 80
            idle_background "images/map/candy_shop.png"
            hover_foreground "images/map/candy_shop_hover.png"
            tooltip "{b}Candy shop{/b}{p}{i}{size=20}Click to go there{/i}"
            action Hide("map"), Jump("candy_shop")
            sensitive current_location != "candy_shop"
            
        button:
            xpos 1531 ypos 526
            xsize 80 ysize 80
            idle_background "images/map/art_gallery.png"
            hover_foreground "images/map/art_gallery_hover.png"
            tooltip "{b}Art Gallery{/b}{p}{i}{size=20}Click to go there{/i}"
            action Hide("map"), Jump("art_gallery")
            sensitive current_location != "art_gallery"
            
        button:
            xpos 928 ypos 400
            xsize 80 ysize 80
            idle_background "images/map/city_centre.png"
            hover_foreground "images/map/city_centre_hover.png"
            tooltip "{b}City Centre{/b}{p}{i}{size=20}Click to go there{/i}"
            action Hide("map"), Jump("city_centre")
            sensitive current_location != "city_centre"
            
    #RenPy iebūvētā funkcija tooltip. Uznirstošais logs ar informāju par vietu  
    $ tooltip = GetTooltip()
    if tooltip:
        fixed:
            xpos 21 ypos 732
            xsize 300 ysize 202
            add "images/map/textbox1.png"
            #align(0,5,0,5) teksts tiek centrēts uz fona attēla
            text "{color=#000000}[tooltip]{/color}" align(0.5,0.5) text_align 0.5

#Poga, kartes atvēršanai
screen map_button:
    modal True
    imagebutton:
        xpos 210 ypos 0
        idle "images/map/map_icon.png"
        hover "images/map/map_icon_hover.png"
        action Show("map")