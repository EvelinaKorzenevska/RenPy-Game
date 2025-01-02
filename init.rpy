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
