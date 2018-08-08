# WEEB_SHIT

romance = ["Golden Time", "Toradora!","Elfen Lied","Clannad","Danmachi",\
           "Ouran Host Club","Tonari no Kaibatsu-kun","Zero no Tsukaima",\
           "Mahouka Koukou no Rettousei","Ao Haru Ride","Sukitte li na yo",\
           "Campione","Nana","Shuffle","Itazura na Kiss","Skip Beat"]
sus = ["Prison School","Shinmai Maou no Testament","Kiss x Sis",\
       "Sora no Otoshimono","To LOVE-Ru","School Days","Rosario to Vampire",\
       "Girls, Bravo!","Scum's Wish","Highschool of the Dead","Freezing",\
       "B-gata H-kei","Sekirei","Infinite Stratos"]
gory = ["Berserk","Blood-C","Elfen Lied","When They Cry","Corpse Party",\
        "Another","Tokyo Ghoul","Deadman Wonderland","Hellsing Ultimate",\
        "Shiki","Ergo Proxy","Gantz","Samurai Champloo","Black Bullet",\
        "Re-Zero","Darker than Black"]
comedy_sol = ["No Game No Life","Mob Psycho 100","One Punch Man",\
              "Seitokai Yakuindomo","Prison School","Great Teacher Onizuka",\
              "Full Metal Panic!","Amagi Brilliant Park","Is This a Zombie?",\
              "Bokura wa Minna Kawai-sou","School Rumble","Nyan Koi",\
              "Golden Boy","Saiki Kusou no psi-nan"]
that_good_shit = ["Psycho-Pass","Fullmetal Alchemist: Brotherhood",\
                  "Hunter x Hunter (2011)","Shokugeki no Soma","Cowboy Bebop",\
                  "Hajime no Ippo","Code Geass","Monster",\
                  "Neon Genesis Evangelion","Parasyte: The Maxim",\
                  "Paranoia Agent","Black Lagoon"]


file = open("anime_list","w")
    
romance = sorted(romance)
file.write("Romance: ")
file.write("-"*30)
for index,value in enumerate(romance):
    file.write("{:10d}{:>10s}".format(index,value))
    
sus = sorted(sus)
file.write("Sus' Shit: ")
file.write("-"*30)
for index,value in enumerate(sus):
    file.write("{:10d}{:>10s}".format(index,value))
    
gory = sorted(gory)
file.write("Gory: ")
file.write("-"*30)
for index,value in enumerate(gory):
    file.write("{:10d}{:>10s}".format(index,value))
    
comedy_sol = sorted(comedy_sol)
file.write("Comedy/Slice of Life: ")
file.write("-"*30)
for index,value in enumerate(comedy_sol):
    file.write("{:10d}{:>10s}".format(index,value))

that_good_shit = sorted(that_good_shit)
file.write("That good-good: ")
file.write("-"*30)
for index,value in enumerate(that_good_shit):
    file.write("{:10d}{:>10s}".format(index,value))
    
file.close()


    
    
    
    
    
    
    
    