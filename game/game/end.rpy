

label 結局1:
    "你的性格是"
    $ renpy.run(OpenURL('https://www.16personalities.com/intj-personality'))
    return

label 結局2:
    "你的性格是"
    $ renpy.run(OpenURL('https://www.16personalities.com/isfj-personality'))
    return


label 結局:
    $ url = "https://www.16personalities.com/{}{}{}{}-personality".format(v1, v2, v3, v4)
    $ renpy.run(OpenURL(url))
    return