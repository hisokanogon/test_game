# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#252121", who_outlines=[(4, "#fff", 0, 0)])



init python:
    import datetime

# Initialize the persistent variables if they don't exist
default persistent.login_count = 0
default persistent.consecutive_login_count = 0
default persistent.last_login_day = None


init python:
    def open_renpyorg():
        import webbrowser
        webbrowser.open_new('https://ningning.netlify.app')

default v1 = ""
default v2 = ""
default v3 = ""
default v4 = ""

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
   # $ persistent.login_count += 1

    scene bg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show girl1 at top

    menu:
        "你在下列哪種情況比較能獲得能量？"
        "獨處，一個人追劇打電動":
            $ v1 = "i"
        "出去玩，或和朋友或家人相聚":
            $ v1 = "e"
        
    menu:
        "當你學習新事物時，你傾向？"
        "天馬行空，喜歡開放性思考":
            $ v2 = "n"
        "依照經驗，需要明確方向":
            $ v2 = "s"

    menu:
        "當你在溝通時，你傾向？"
        "先看這件事有沒有合乎邏輯或公平性":
            $ v3 = "t"
        "先確認對方感受，希望和諧相處":
            $ v3 = "f"

    menu:
        "出國旅遊之前，你通常會？"
        "列好每個行程，並按照計畫進行":
            $ v4 = "j"
        "去到那裡再說，當天看心情決定":
            $ v4 = "p"

    jump 結局


label start2:
    e "記得關注我們的 {a=https://www.youtube.com/channel/UCjG_c3oED79Gx4i08JfkSWg}Youtube{/a} 和 {a=https://ningning.netlify.app/}官網{/a} "

    

    # These display lines of dialogue.
    $ current_day = datetime.date.today()

    # Check if the player has logged in today
    if persistent.last_login_day != current_day:
        $ persistent.login_count += 1
 
    # Check if the player has logged in consecutively
    if persistent.last_login_day == current_day - datetime.timedelta(days=1):
        $ persistent.consecutive_login_count += 1
    else:
        $ persistent.consecutive_login_count = 1

    $ persistent.last_login_day = current_day       

    "You have logged to the game "
    "You have logged in for a total of [persistent.login_count] days."

    e "Login Count: [persistent.login_count]"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
        "Choice 1":
            "123"
        "Choice 2":
            "456"
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat." 
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."     

    return
