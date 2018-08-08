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



print("List of Good/Trashy Anime: ")
romance = sorted(romance)
print("\nRomance: ")
print("-"*30)
for index,value in enumerate(romance):
    print("{:<10d}{:10s}".format(index+1,value.strip()))
    
sus = sorted(sus)
print("\nSus' Shit: ")
print("-"*30)
for index,value in enumerate(sus):
    print("{:<10d}{:10s}".format(index+1,value.strip()))
    
gory = sorted(gory)
print("\nGory: ")
print("-"*30)
for index,value in enumerate(gory):
    print("{:<10d}{:10s}".format(index+1,value.strip()))
    
comedy_sol = sorted(comedy_sol)
print("\nComedy/Slice of Life: ")
print("-"*30)
for index,value in enumerate(comedy_sol):
    print("{:<10d}{:10s}".format(index+1,value.strip()))

that_good_shit = sorted(that_good_shit)
print("\nThat Good-Good: ")
print("-"*30)
for index,value in enumerate(that_good_shit):
    print("{:<10d}{:10s}".format(index+1,value.strip()))
    



    
    
    
    
    
    
    
    