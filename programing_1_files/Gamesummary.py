def showsummary(title, date, player, score_home, score_away):
    wasawin=score_home >score_away
    wasatie=score_home==score_away
    print(f"game: {title} ({date})")
    print("--------------------------")
    print(f"final score: {score_home}-{score_away}")
    if wasawin:
      print(f"{player} Won!!")
    elif wasatie:
      print(f"{player} Tie!")
    else:
      print(f"{player} lose.")
    print("")
    


def playernames(player):
    playernames = [player]
    if player not in playernames:
      playernames=[player]+player
      print(playernames)
    elif player in playernames:
      print(playernames)
dict()

file = open("games.txt", "r")
line1 = file.readline()
lp1=line1.strip().split(",")
showsummary(lp1[0],lp1[1],lp1[2],lp1[3],lp1[4])
playernames(lp1[2])

line2 = file.readline()
pl2=line2.strip().split(",")
showsummary(pl2[0],pl2[1],pl2[2],pl2[3],pl2[4])
playernames(pl2[2])

line3 = file.readline()
pl3=line3.strip().split(",")
showsummary(pl3[0],pl3[1],pl3[2],pl3[3],pl3[4])

line4 = file.readline()
pl4=line4.strip().split(",")
showsummary(pl4[0],pl4[1],pl4[2],pl4[3],pl4[4])

line5 = file.readline()
pl5=line5.strip().split(",")
showsummary(pl5[0],pl5[1],pl5[2],pl5[3],pl5[4])

line6 = file.readline()
pl6=line6.strip().split(",")
showsummary(pl6[0],pl6[1],pl6[2],pl6[3],pl6[4])

line7 = file.readline()
pl7=line7.strip().split(",")
showsummary(pl7[0],pl7[1],pl7[2],pl7[3],pl7[4])

line8 = file.readline()
pl8=line8.strip().split(",")
showsummary(pl8[0],pl8[1],pl8[2],pl8[3],pl8[4])

line9 = file.readline()
pl9=line9.strip().split(",")
showsummary(pl9[0],pl9[1],pl9[2],pl9[3],pl9[4])

line10 = file.readline()
pl10=line10.strip().split(",")
showsummary(pl10[0],pl10[1],pl10[2],pl10[3],pl10[4])

line11 = file.readline()
pl11=line11.strip().split(",")
showsummary(pl11[0],pl11[1],pl11[2],pl11[3],pl11[4])

line12 = file.readline()
pl12=line12.strip().split(",")
showsummary(pl12[0],pl12[1],pl12[2],pl12[3],pl12[4])