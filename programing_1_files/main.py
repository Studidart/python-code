
"""
madlib v1
for i in range(3):
  place=input("Pick a place: ")
  verb1=input("Pick a verb: ")
  feeling=input("Pick a feeling: ")
  verb2=input("Pick a diffrent verb: ")
  print("At",place,"in the sun. We'll be",verb1,"And it makes me feel so", feeling, "I tried",verb2)

game summary display 6 paramitors.
def showsummary(title, date, player, score_home, score_away,winrate):
    wasawin=score_home >score_away
    print(f"game: {title} ({date})")
    print("--------------------------")
    print(f"final score: {score_home}-{score_away}")
    if (wasawin):
      print(f"{player} Won!!")
    else:
      print(f"{player} Lost")
    print(f"Win rate {winrate}%")
    print("")

showsummary("Homecoming",2000,"job",140,200,50)


madlib v2
def thefunnystory():
    adjective1=input("adjective: ")
    adjective2=input("adjective: ")
    bird=input("type of bird: ")
    room1=input("room in a house: ")
    verbpast=input("past tense verb: ")
    verb=input("verb: ")
    relativesname=input("relatives name: ")
    noun1=input("noun: ")
    liquid=input("a liquid pls: ")
    verbing1=input("a verb ending with 'ing': ")
    bodypart=input("part of the body 'plural': ")
    pluralnoun=input("a plural noun: ")
    verbing2=input("verb ending with 'ing': ")
    noun2=input("another noun pls: ")


    print("It was a "+adjective1+", cold november day. I woke up to the "+adjective2+" smell of "+bird+" roasting in the "+room1+" downstairs. I "+verbpast+" down the stairs to see if i could help "+verb+" the dinner. My mom said, 'See if "+relativesname+" needs a fresh "+noun1+".' So I carried a tray of glasses of "+liquid+" into the "+verbing1+" room. When I got there, I couldn't belive my "+ bodypart+"! There were "+pluralnoun+" "+verbing2+" on the "+noun2+"!")

thefunnystory()
thefunnystory()
thefunnystory()
thefunnystory()
thefunnystory()


"""