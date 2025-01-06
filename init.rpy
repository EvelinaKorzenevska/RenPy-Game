#Spēles varoņu deklarēšana
define w = Character("[char_name]", color="#80b3ff", callback=name_callback, cb_name="william") #cb_name="william" - pirmais vārds attēla nosaukumam
define t = Character("Teacher", color="#ff0000", callback=name_callback, cb_name="teacher")
define m = Character("Mia", color="#ff99dd", callback=name_callback, cb_name="mia")
define s = Character("Sabrina", color="#ff99dd", callback=name_callback, cb_name="sabrina")
define sal = Character("Salesperson", color="#ff0000", callback=name_callback, cb_name="salesperson")
define mum = Character("Mum", color="#ff0000", callback=name_callback, cb_name="mother")

#Autora vārdi režīmā nvl - dialoglodziņš parādās pa visu ekrānu
define a = Character(None, kind=nvl)

#Autora vārdu definēšana ar slīprakstu un pelēko krāsu. Autoram runājot, nerunājošie varoņi neizcēlās
define n = Character(callback=name_callback, cb_name=None, what_italic=True, what_color="#888888")

#Varoņa attēla deklarēšana, lai runājošs varonis izceltos
image william uniform confused light = At('william uniform confused', sprite_highlight('william'))
image william uniform confused2 light = At('william uniform confused2', sprite_highlight('william'))
image william uniform smile light = At('william uniform smile', sprite_highlight('william'))
image william uniform happy light = At('william uniform happy', sprite_highlight('william'))
image william uniform suprized light = At('william uniform suprized', sprite_highlight('william'))
image william uniform sad light = At('william uniform sad', sprite_highlight('william'))
image william smile light = At('william smile', sprite_highlight('william'))
image william happy light = At('william happy', sprite_highlight('william'))
image william sad light = At('william sad', sprite_highlight('william'))
image william confused light = At('william confused', sprite_highlight('william'))

image teacher sad light = At('teacher sad', sprite_highlight('teacher'))
image teacher smile light = At('teacher smile', sprite_highlight('teacher'))

image mia uniform smile light = At('mia uniform smile', sprite_highlight('mia'))
image mia uniform suprized light = At('mia uniform suprized', sprite_highlight('mia'))
image mia uniform sad light = At('mia uniform sad', sprite_highlight('mia'))
image mia uniform happy light = At('mia uniform happy', sprite_highlight('mia'))
image mia smile light = At('mia smile', sprite_highlight('mia'))
image mia happy light = At('mia happy', sprite_highlight('mia'))
image mia confused light = At('mia confused', sprite_highlight('mia'))
image mia shy light = At('mia shy', sprite_highlight('mia'))
image mia sad light = At('mia sad', sprite_highlight('mia'))
image mia smile p2 light = At('mia smile p2', sprite_highlight('mia'))

image sabrina uniform sad light = At('sabrina uniform sad', sprite_highlight('sabrina'))
image sabrina uniform suprized light = At('sabrina uniform suprized', sprite_highlight('sabrina'))
image sabrina uniform smile light = At('sabrina uniform smile', sprite_highlight('sabrina'))
image sabrina unhappy light = At('sabrina unhappy', sprite_highlight('sabrina'))
image sabrina sad light = At('sabrina sad', sprite_highlight('sabrina'))
image sabrina laught light = At('sabrina laught', sprite_highlight('sabrina'))
image sabrina smile light = At('sabrina smile', sprite_highlight('sabrina'))
image sabrina confused light = At('sabrina confused', sprite_highlight('sabrina'))
image sabrina happy light = At('sabrina happy', sprite_highlight('sabrina'))

image salesperson light = At('salesperson', sprite_highlight('salesperson'))
image salesperson form light = At('salesperson form', sprite_highlight('salesperson'))

image mother work smile light = At('mother work smile', sprite_highlight('mother'))

#Mūzika un skaņas efekti
define audio.start = "music/start_music.mp3"
define audio.main = "music/main_music.mp3"
define audio.classroom = "music/classroom_music.mp3"
define audio.corridor = "music/school_corridor_music.mp3"
define audio.courtyard = "music/school_courtyard.mp3"
define audio.park = "music/park.mp3"
define audio.night_street = "music/night_street.mp3"
define audio.city_center = "music/city_center.mp3"
define audio.shopping_center = "music/shopping_center.mp3"
define audio.cafe = "music/cafe_music.mp3"
define audio.beach = "music/beach.mp3"
define audio.concert = "music/concert.mp3"

define audio.knock = "sounds/knocking.mp3"
define audio.door = "sounds/door_open.mp3"
define audio.bell = "sounds/school_bell.mp3"
define audio.plus_point = "sounds/plus_point.mp3"
define audio.minus_point = "sounds/minus_point.mp3"
define audio.money = "sounds/money.mp3"
define audio.taxi = "sounds/taxi.mp3"
define audio.taxi_drive = "sounds/taxi_drive.mp3"
define audio.victory = "sounds/victory.mp3"
define audio.loss = "sounds/loss.mp3"
define audio.calling = "sounds/phone_call.mp3"
define audio.end_call = "sounds/end_of_call.mp3"
define audio.camera_flash = "sounds/camera_flash.mp3"

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
#Pogas veidošana. Noklikškinot uz meiteni, parādas informācijas logs par viņu
screen mia_button:
    imagebutton:
        xalign 0.05
        yalign 1.1
        idle "images/button/mia_idle.png"
        hover "images/button/mia_hover.png"
        action Show("info_panel_mia")             

screen sabrina_button:
    imagebutton:
        xalign 0.4
        yalign 1.1
        idle "images/button/sabrina_idle.png"
        hover "images/button/sabrina_hover.png"
        action Show("info_panel_sabrina")

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
            
#Informācijas logs
screen information:
        frame:
            padding(10,10)
            xalign 0.1
            yalign 0.05
            xsize 400
            vbox:
                xsize 380
                text "{color=#80b3ff}HINT{/color}" xalign 0.5
                null height 15
                text "Read the dialogue carefully, it can help you score more points for further action." size 30
                null height 10
                text "Focus on the answers, there is a hidden logic that you need to grasp." size 30
                null height 15
                textbutton "CLOSE" action Hide("information") xalign 0.5

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
        
#Mainīgie, kas uzskaita, cik reizes spēlētājs ir “apmeklējis” noteikto vietu
default home2_visited = 0
default school2_visited = 0
default candy_shop2_visited = 0
default concert_hall_visited = 0

#Kartes ekrāns, izvēloties Sabrinu
screen map2:
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
            action Hide("map2"), Jump("home2")
            #Poga nav aktīva, ja spēlētājs atrodas tajā vietā
            sensitive current_location != "home2"
        
        button:
            xpos 798 ypos 528
            xsize 80 ysize 80
            idle_background "images/map/school.png"
            hover_foreground "images/map/school_hover.png"
            tooltip "{b}School{/b}{p}{i}{size=20}Click to go to school{/i}"
            action Hide("map2"), Jump("school2")
            sensitive current_location != "school2"
            
        button:
            xpos 646 ypos 675
            xsize 80 ysize 80
            idle_background "images/map/park.png"
            hover_foreground "images/map/park_hover.png"
            tooltip "{b}Park{/b}{p}{i}{size=20}Click to go to the park{/i}"
            action Hide("map2"), Jump("park2")
            sensitive current_location != "park2"
            
        button:
            xpos 480 ypos 552
            xsize 80 ysize 80
            idle_background "images/map/house_mia.png"
            hover_foreground "images/map/house_mia_hover.png"
            tooltip "{b}Sabrina's house{/b}{p}{i}{size=20}Click to go to Sabrina's house{/i}"
            action Hide("map2"), Jump("house_sabrina")
            sensitive current_location != "house_sabrina"
        
        button:
            xpos 1266 ypos 297
            xsize 80 ysize 80
            idle_background "images/map/candy_shop.png"
            hover_foreground "images/map/candy_shop_hover.png"
            tooltip "{b}Candy shop{/b}{p}{i}{size=20}Click to go the candy shop{/i}"
            action Hide("map2"), Jump("candy_shop2")
            sensitive current_location != "candy_shop2"
        
        button:
            xpos 829 ypos 297
            xsize 80 ysize 80
            idle_background "images/map/cafe.png"
            hover_foreground "images/map/cafe_hover.png"
            tooltip "{b}Cafe{/b}{p}{i}{size=20}Click to go to the cafe{/i}"
            action Hide("map2"), Jump("cafe")
            sensitive current_location != "cafe"
        
        button:
            xpos 411 ypos 255
            xsize 80 ysize 80
            idle_background "images/map/beach.png"
            hover_foreground "images/map/beach_hover.png"
            tooltip "{b}Beach{/b}{p}{i}{size=20}Click to go to the beach{/i}"
            action Hide("map2"), Jump("beach")
            sensitive current_location != "beach"
            
        button:
            xpos 1231 ypos 531
            xsize 80 ysize 80
            idle_background "images/map/concert_hall.png"
            hover_foreground "images/map/concert_hall_hover.png"
            tooltip "{b}Concert hall{/b}{p}{i}{size=20}Click to go to the concert hall{/i}"
            action Hide("map2"), Jump("concert_hall")
            sensitive current_location != "concert_hall"
        
        button:
            xpos 928 ypos 400
            xsize 80 ysize 80
            idle_background "images/map/city_centre.png"
            hover_foreground "images/map/city_centre_hover.png"
            tooltip "{b}City Centre{/b}{p}{i}{size=20}Click to go there{/i}"
            action Hide("map2"), Jump("city_centre2")
            sensitive current_location != "city_centre2"
            
    $ tooltip = GetTooltip()
    if tooltip:
        fixed:
            xpos 30 ypos 732
            xsize 350 ysize 236
            add "images/map/textbox.png"
            text "{color=#000000}[tooltip]{/color}" align(0.5,0.5) text_align 0.5

#Poga, kartes atvēršanai
screen map_button_sabrina:
    modal True
    imagebutton:
        xpos 210 ypos 0
        idle "images/map/map_icon.png"
        hover "images/map/map_icon_hover.png"
        action Show("map2")

#Ekrāns telefona zvanam
screen phone_call(caller_name, caller_image, call_status):
    #Telefona fons un izvietojums
    frame:
        xalign 0.3
        yalign 0.3
        xsize 400
        ysize 850
        background "images/sms_chat/phone_background.png"
        foreground "images/sms_chat/phone_foreground.png"

    #Abonenta vārda parādīšana
    vbox:
        xpos 0.30
        ypos 0.15
        text "[caller_name]" size 40 color "#FFFFFF" xmaximum 250

    #Abonenta attēls
    add caller_image xpos 0.29 ypos 0.25

    #Pašreizeja zvana statuss
    vbox:
        xalign 0.33
        yalign 0.6
        text "[call_status]" size 30 color "#FFFFFF" xmaximum 250

#Spēlētāja nauda
default money = 30
screen money_display:
    image "images/icons/money.png" xpos 55 ypos 24
    text "{b}[money]{/b}" xpos 115 ypos 24 color "#FFFFFF" size 40

#Pieejamas precces deklarēšana
define tea = 0
define coffee = 0 
define coffee_with_honeycake = 0
define coffee_with_cheesecake = 0
define item = ""

#Ekrāns ar precēm
screen shop_menu_drink:
    image "images/shop/MENU.png" xpos 354 ypos 292
    imagebutton:
        xpos 361
        ypos 486
        idle "images/shop/tea.png"
        hover "images/shop/tea_hover.png"
        #SetVariable nosaka jaunu vērtību mainīgajam
        action [SetVariable("tea", tea + 1), SetVariable("item", "tea"), Jump("buy_item")]

    imagebutton:
        xpos 546
        ypos 486
        idle "images/shop/coffee.png"
        hover "images/shop/coffee_hover.png"
        action [SetVariable("coffee", coffee + 1), SetVariable("item", "coffee"), Jump("buy_item")]

#Ekrāns ar precēm
screen shop_menu:
    image "images/shop/MENU.png" xpos 354 ypos 292
    imagebutton:
        xpos 320
        ypos 486
        idle "images/shop/coffee_honeycake.png"
        hover "images/shop/coffee_honeycake_hover.png"
        action [SetVariable("coffee_with_honeycake", coffee_with_honeycake + 1), SetVariable("item", "coffee_with_honeycake"), Jump("buy_item1")]

    imagebutton:
        xpos 540
        ypos 486
        idle "images/shop/coffee_cheesecake.png"
        hover "images/shop/coffee_cheesecake_hover.png"
        action [SetVariable("coffee_with_cheesecake", coffee_with_cheesecake + 1), SetVariable("item", "coffee_with_cheesecake"), Jump("buy_item1")]
        
#Ikonas
image tea1_icon = "images/icons/tea1.png"
image tea2_icon = "images/icons/tea2.png"
image coffee1_icon = "images/icons/coffee1.png"
image coffee2_icon = "images/icons/coffee2.png"
image honeycake1_icon = "images/icons/cake1.png"
image honeycake2_icon = "images/icons/cake2.png"
image cheesecake1_icon = "images/icons/cheesecake1.png"
image cheesecake2_icon = "images/icons/cheesecake2.png"
image taxi_icon = "images/icons/taxi.png"
image popcorn = "images/icons/popcorn.png"
image book = "images/icons/book.png"
image flowers = "images/icons/flowers.png"
image chamomile = "images/icons/chamomile.png"

#Naudas pelnīšana, mazgājot grīdu
default william_pos = 1000  #Sākum pozīcija pa x asi
default time_passed = 0     #Laiks, kas pagājis kopš mijiedarbības sākuma

screen william_move():
    add "images/icons/william_with_mop.png" xpos william_pos ypos 150

#Ekrāns ar pārvietošanas pogām
screen move_button():
    imagebutton:
        idle "images/icons/left.png"
        xpos 706
        ypos 10
        action SetVariable("william_pos", william_pos - 50)

    imagebutton:
        idle "images/icons/right.png"
        xpos 1009
        ypos 10
        action SetVariable("william_pos", william_pos + 50)

#Nopirkt kino biļeti
default ticket_choise = "none" #Mainīgais, kas glābā nopirkto kino biļetes žanru
screen buy_ticket():
        imagebutton:
            xpos 153 ypos 84
            idle "images/icons/ticket_horror.png"
            hover "images/icons/ticket_horror_hover.png"
            action Call("buy_horror")

        imagebutton:
            xpos 153 ypos 385
            idle "images/icons/ticket_scifi.png"
            hover "images/icons/ticket_scifi_hover.png"
            action Call("buy_scifi")

        imagebutton:
            xpos 153 ypos 684
            idle "images/icons/ticket_melodrama.png"
            hover "images/icons/ticket_melodrama_hover.png"
            action Call("buy_melodrama")

#Nopirkt biļeti uz galeriju
screen buy_gallery_ticket():
        imagebutton:
            xpos 187 ypos 151
            idle "images/icons/gallery_ticket.png"
            hover "images/icons/gallery_ticket_hover.png"
            action Call("gallery_ticket")
            
#Mainīgais, kas glabā informāciju par spēlētāja izdarīto lēmumu - kur uzaicināt meiteni
default invitation_choice = "none"

#Mainīgais, kas glabā informāciju par spēlētāja izdarīto lēmumu - kādu jautājumu uzdot
default question_choice = "none"

#Mainīgais, kas glabā informāciju par spēlētāja izdarīto lēmumu - kādu darbību veikt
default action_choiсe = "none"

#Dzejoļa paradīšana
screen poem:
    text "{i}Hold fast to dreams, for if dreams die\nLife is a broken-winged bird, that cannot fly.\nHold fast to dreams, for when dreams go\nLife is a barren field, frozen with snow.{/i}":
        xalign 0.5
        yalign 0.25
        size 30

#Datora poga, lai sākt spēlēt spēli
screen computer_button:
    modal True
    imagebutton:
        xpos 396 ypos 499
        idle "images/icons/computer.png"
        hover "images/icons/computer_hover.png"
        action Show("choice_menu")

#Ekrāns ar spēles sākumu
screen choice_menu:
    add "images/bg/computer.png"
    modal True
    text "Rock-paper-scissors game, make a choice." align .5, .6
    imagebutton:
        xalign 0.35
        yalign 0.4
        idle "images/icons/rock_idle.png"
        hover "images/icons/rock_hover.png"
        action [SetVariable("player_choice", "rock"), Hide("choice_menu"), Show("result")]

    imagebutton:
        xalign 0.5
        yalign 0.4
        idle "images/icons/scissors_idle.png"
        hover "images/icons/scissors_hover.png"
        action [SetVariable("player_choice", "scissors"), Hide("choice_menu"), Show("result")]

    imagebutton:
        xalign 0.65
        yalign 0.4
        idle "images/icons/paper_idle.png"
        hover "images/icons/paper_hover.png"
        action [SetVariable("player_choice", "paper"), Hide("choice_menu"), Show("result")]

#Ekrāns ar spēles rezultātu
screen result:
    add "images/bg/computer.png"
    modal True
    python:
        computer_choice = renpy.random.choice(["rock", "scissors", "paper"])
    
    if player_choice == computer_choice:
        text "It's a tie!" align .5, .45
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
        text "You win!" align .5, .45
    else:
        text "You lose!" align .5, .45

    add "/images/icons/" + player_choice + "_idle.png" align .5, .3
    add "/images/icons/" + computer_choice + "_idle.png" align .5, .6
    
    text "Play it again?" align .7, .45
    hbox:
        align .68, .5
        textbutton "Yes" action[Hide("result"), Show("choice_menu")]
        textbutton "No" action[Hide("result"), Jump("end")]
        
#Sakopt visus atkritumus
#Atkritumu definēšana
image rubbish1 = "images/rubbish/apple.png"
image rubbish2 = "images/rubbish/bottle.png"
image rubbish3 = "images/rubbish/candy.png"
image rubbish4 = "images/rubbish/mud.png"
image rubbish5 = "images/rubbish/paper.png"

#Atkritumu redzamība
default rubbish1_visible = True
default rubbish2_visible = True
default rubbish3_visible = True
default rubbish4_visible = True
default rubbish5_visible = True

#Ekrāns ar atkritumiem
screen clean_rubbish:
    if rubbish1_visible:
        imagebutton:
            xpos 1578 ypos 829
            idle "images/rubbish/apple.png"
            action [SetVariable("rubbish1_visible", False), Hide("rubbish1")]  #elementa slēpšana

    if rubbish2_visible:
        imagebutton:
            xpos 849 ypos 877
            idle "images/rubbish/bottle.png"
            action [SetVariable("rubbish2_visible", False), Hide("rubbish2")]
    
    if rubbish3_visible:
        imagebutton:
            xpos 1219 ypos 886
            idle "images/rubbish/candy.png"
            action [SetVariable("rubbish3_visible", False), Hide("rubbish3")]
    
    if rubbish4_visible:
        imagebutton:
            xpos 522 ypos 469
            idle "images/rubbish/mud.png"
            action [SetVariable("rubbish4_visible", False), Hide("rubbish4")]
    
    if rubbish5_visible:
        imagebutton:
            xpos 78 ypos 732
            idle "images/rubbish/paper.png"
            action [SetVariable("rubbish5_visible", False), Hide("rubbish5")]
            
#Foto efekts
image camera_frame = "images/icons/camera_frame.png"  #Kameras rāmis

#Zibspuldzes efekts (Parametri - zibspuldzes vienmērīgas pārejas laiks, pēc cik sekundēm tiek parādīta vienkrāsa, pēc cik sekundēm tiek parādīts dialoga teksts.)
define flash = Fade(.25, 0, .75, color="#ffffff") 

#Ekrāns ar bildēm
init python:
    photos = ["images/icons/foto1.png", "images/icons/foto2.png"] #Fotoattēlu saraksts
    current_photo_index = 0 #Mainīgais pašreizējam fotoattēla indeksam

screen photos():
    modal True
    add photos[current_photo_index] align .5, .2 #Parādīt pašreizējo fotoattēlu ar indeksu 0
    
    #Pogas veidošana
    vbox:
        align (0.5, 0.75)
        hbox:
            #Pāriet pie iepriekšējas bildes
            if current_photo_index > 0:
                textbutton "Previous" action[SetVariable("current_photo_index", current_photo_index - 1), Function(renpy.restart_interaction)] #Funkcija, kas ļauj restartēt pašreizējo ekrānu, liekot to pārzīmēt no jauna
            
            #Pāriet pie nākamās bildes
            if current_photo_index < len(photos) - 1: #Pārbauda, vai pašreizējais fotoattēla indekss ir pēdējais sarakstā
                textbutton "Next" action [SetVariable("current_photo_index", current_photo_index + 1), Function(renpy.restart_interaction)]
            
            textbutton "Close" action Hide("photos"), Jump("after_photo")

#Nopirkt koncerta biļeti
default concert_ticket_choise = "none"

#Ekrāns ar piedavātajām biļetēm
screen buy_concert_ticket():
        imagebutton:
            xpos 153 ypos 84
            idle "images/icons/ticket_grande.png"
            hover "images/icons/ticket_grande_hover.png"
            action Call("buy_grande")

        imagebutton:
            xpos 153 ypos 385
            idle "images/icons/ticket_gaga.png"
            hover "images/icons/ticket_gaga_hover.png"
            action Call("buy_gaga")