from DBmodules import *
from mongoengine import connect

connect(host="mongodb+srv://kobim:karok12K@kobiscluster.rvdyv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# insert into platforms
win = Platforms(platformName='Windows').save()
osx = Platforms(platformName='OSX').save()
linux = Platforms(platformName='Linux').save()

# insert into genres
action = Genres(genreName='Action').save()
adventure = Genres(genreName='Adventure').save()
indie = Genres(genreName='Indie').save()
rpg = Genres(genreName='RPG').save()
shooters = Genres(genreName='Shooters').save()
simulation = Genres(genreName='Simulation').save()
sports = Genres(genreName='Sports & Racing').save()
strategy = Genres(genreName='Strategy').save()

#  insert into tags
tag1 = Tags(tagName='Fun').save()
tag2 = Tags(tagName='Casual').save()
tag3 = Tags(tagName='Hardcore').save()
tag4 = Tags(tagName='Addicting').save()

# insert into games
req = SystemRequirements(
    system='Windows 7, 8.1, or 10 (64-Bit versions)',
    processor='AMD FX-8350/Ryzen 5 1400 or Intel Core i5-3570/i7-3770',
    memory='16 GB',
    graphics='Nvidia GTX 770 4GB/AMD Radeon R9 290 4GB or better',
    directx='12.b',
    storage='60 GB'
)

req1 = SystemRequirements(
    system='Windows 7, 8.1, or 10 (64-Bit versions)',
    processor='AMD FX-8350/Ryzen 5 1400 or Intel Core i5-3570/i7-3770',
    memory='16 GB',
    graphics='Nvidia GTX 1770 8GB/AMD Radeon R9 290 8GB or better',
    directx='12.b',
    storage='60 GB'
)

game1 = Games(
    gameName='Cyberpunk 2077',
    publisher='CD PROJEKT RED',
    releaseDate='2020-12-10',
    description="Cyberpunk 2077 is an open-world, action-adventure story set in Night City, a megalopolis obsessed "
                "with power, glamour and body modification. You play as V, a mercenary outlaw going after a "
                "one-of-a-kind implant that is the key to immortality. You can customize your character's cyberware, "
                "skillset and playstyle, and explore a vast city where the choices you make shape the story and the "
                "world around you. /n "
                "Become a cyberpunk, an urban mercenary equipped with cybernetic enhancements and build your legend on "
                "the streets of Night City. Create your character from scratch and choose their background out of "
                "three unique Lifepaths. Take the role of a gang-wise Street Kid, freedom-loving Nomad, or a ruthless "
                "Corpo. "
                "Enter the massive open world of Night City, a place that sets new standards in terms of visuals, "
                "complexity and depth. Explore the bustling megalopolis of the future and its extensive districts, "
                "each with exceptional visual flavor, inhabitants and chances to earn cash. Interact with members of "
                "powerful gangs who rule the streets of Night City. "
                "Take the riskiest job of your life and go after a prototype implant that is the key to immortality. "
                "Guided by the legendary Rockerboy, Johnny Silverhand (played by Keanu Reeves), you will change the "
                "course of the corporate-ruled world forever. All this while listening to an intoxicating soundtrack "
                "from artists like Run the Jewels, Refused, Grimes, A$AP Rocky, Gazelle Twin, Ilan Rubin, "
                "Richard Devine, Nina Kraviz, Deadly Hunta, Rat Boy, and Tina Guo.",
    coverImg='http://localhost:3200/Public/Images/1.jpg',
    systemRequirements=req,
    genres=[str(action.id), str(rpg.id)],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/1/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/1/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/1/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/1/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/1/5.jpg',
    },
    platforms=[str(win.id)]
).save()

game2 = Games(
    gameName='The Witcher 3',
    publisher='CD PROJEKT RED',
    releaseDate='2016-8-30',
    description="Become a professional monster slayer and embark on an adventure of epic proportions! Upon its "
                "release, The Witcher 3: Wild Hunt became an instant classic, claiming over 250 Game of the Year "
                "awards. Now you can enjoy this huge, over 100-hour long, open-world adventure along with both its "
                "story-driven expansions worth an extra 50 hours of gameplay. This edition includes all additional "
                "content - new weapons, armor, companion outfits, new game mode and side quests. "

                "Features: /n"

                "Play as a Highly Trained Monster Slayer for Hire"
                "Trained from early childhood and mutated to have superhuman skills, strength, and reflexes, "
                "witchers are a "
                "socially ostracized counterbalance to the monster-infested world in which they live. "
                "- Gruesomely destroy foes as a professional monster hunter armed with a range of upgradeable weapons, "
                "mutating potions, and combat magic. "
                "- Hunt down a wide variety of exotic monsters, from savage beasts prowling mountain passes to cunning "
                "supernatural predators lurking in the shadowy back alleys of densely populated cities. "
                "- Invest your rewards to upgrade your weaponry and buy custom armor, or spend them on horse races, "
                "card games, "
                "fist fighting and other pleasures life brings. "

                "Track Down the Child of Prophecy in a Morally Ambiguous Fantasy Open World"
                "- Built for endless adventure, the massive open world of The Witcher sets new standards in terms of "
                "size, "
                "depth and complexity. "
                "- Traverse a fantastical open world: explore forgotten ruins, caves and shipwrecks, trade with "
                "merchants and "
                "dwarven smiths in cities, and hunt across open plains, amidst mountains and at sea. "
                "- In a time of war, track down the child of prophecy, a living weapon of great power whose coming "
                "was foretold "
                "in ancient elven legends. "
                "Make choices that go beyond good and evil and face their far-reaching consequences.",
    coverImg='http://localhost:3200/Public/Images/2.jpg',
    systemRequirements=req1,
    genres=[
       str(action.id), str(adventure.id), str(adventure.id)],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/2/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/2/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/2/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/2/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/2/5.jpg',
    },
    platforms=[str(win.id), str(osx.id)]
).save()

game3 = Games(
    gameName='Metro Exodus',
    publisher='4A Games',
    releaseDate='2019-8-30',
    description="The year is 2036. A quarter-century after nuclear war devastated the earth, a few thousand survivors "
                "still cling to existence beneath the ruins of Moscow, in the tunnels of the Metro. "
                "They have struggled against the poisoned elements, fought mutated beasts and paranormal horrors, "
                "and suffered the flames of civil war. "
                "But now, as Artyom, you must flee the Metro and lead a band of Spartan Rangers on an incredible, "
                "continent-spanning journey across post-apocalyptic Russia in search of a new life in the East. "
                "Metro Exodus is an epic, story-driven first person shooter from 4A Games that blends deadly combat "
                "and "
                "stealth with exploration and survival horror in one of the most immersive game worlds ever created. "
                "Explore the Russian wilderness across vast, non-linear levels and follow a thrilling story-line that "
                "spans "
                "an entire year through spring, summer and autumn to the depths of nuclear winter. "
                "Inspired by the novels of Dmitry Glukhovsky, Metro Exodus continues Artyom’s story in the greatest "
                "Metro adventure yet.",
    coverImg='http://localhost:3200/Public/Images/3.jpg',
    systemRequirements=req1,
    genres=[str(action.id), str(indie.id), str(shooters.id)],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/3/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/3/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/3/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/3/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/3/5.jpg',
    },
    platforms=[
        str(win.id), str(linux.id)
    ]
).save()

game4 = Games(
    gameName='Hollow Knight',
    publisher='Team Cherry',
    releaseDate='2017-2-24',
    description="Brave the Depths of a Forgotten Kingdom"
                "Beneath the fading town of Dirtmouth sleeps an ancient, ruined kingdom."
                " Many are drawn below the surface, searching for riches, or glory, or answers to old secrets."
                "Hollow Knight is a classically styled 2D action adventure across a vast interconnected world."
                " Explore twisting caverns, ancient cities and deadly wastes; "
                "battle tainted creatures and befriend bizarre bugs; and solve ancient mysteries at the kingdom's "
                "heart.",
    coverImg='http://localhost:3200/Public/Images/4.jpg',
    systemRequirements=req1,
    genres=[
        str(action.id),
        str(indie.id),
        str(rpg.id),],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/4/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/4/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/4/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/4/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/4/5.jpg',
    },
    platforms=[
        str(win.id),
        str(osx.id),
        str(linux.id),
    ]
).save()

game5 = Games(
    gameName="Baldur's Gate 3",
    publisher='Larian Studios',
    releaseDate='2021-10-6',
    description="Gather your party, and return to the Forgotten Realms in a tale of fellowship and betrayal, "
                "sacrifice and survival, and the lure of absolute power. "

                "Mysterious abilities are awakening inside you, drawn from a Mind Flayer parasite planted in your "
                "brain. Resist, and turn darkness against itself. Or embrace corruption, and become ultimate evil. "

                "From the creators of Divinity: Original Sin 2 comes a next-generation RPG, set in the world of "
                "Dungeons and Dragons. "
                "Choose from a wide selection of D&D races and classes, or play as an origin character with a "
                "hand-crafted background. Adventure, loot, battle and romance as you journey through the Forgotten "
                "Realms and beyond. Play alone, and select your companions carefully, or as a party of up to four in "
                "multiplayer.",
    coverImg='http://localhost:3200/Public/Images/5.jpg',
    systemRequirements=req,
    genres=[
        str(adventure.id),
        str(indie.id),
        str(rpg.id)],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/5/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/5/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/5/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/5/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/5/5.jpg',
    },
    platforms=[
        str(win.id),
        str(osx.id)
    ]
).save()

game6 = Games(
    gameName="Sleeping Dogs",
    publisher='Square Enix',
    releaseDate='2014-8-8',
    description="The Definitive Edition of the critically acclaimed, award winning open-world action adventure, "
                "reworked, rebuilt and re-mastered for the new generation. "
                "All 24 previously available DLC extensions have been integrated into the game, including the "
                "story-extending episode Year of the Snake and the horror-themed Nightmare in North Point. Alongside "
                "a wealth of new technological, audio and visual improvements, Hong Kong has never felt so alive. "

                "A vibrant, neon city teaming with life, Hong Kong’s exotic locations and busy streets and markets "
                "hide one of the most powerful and dangerous criminal organizations in the world: the notorious "
                "Triads. Play as Wei Shen – the highly skilled undercover cop trying to take down the Triads from the "
                "inside out. You'll have to prove yourself worthy as you fight your way up the organization, "
                "taking part in brutal criminal activities without blowing your cover. "

                "Destroy your opponents in brutal hand-to-hand combat using an unmatched martial arts system. "
                "Dominate Hong Kong’s buzzing streets in thrilling illegal street races and tear it up in explosive "
                "firearms action. Sleeping Dogs’ Hong Kong is the ultimate playground. "
                "Undercover, the rules are different.",
    coverImg='http://localhost:3200/Public/Images/6.jpg',
    systemRequirements=req,
    genres=[
        str(action.id),
        str(adventure.id)
    ],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/6/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/6/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/6/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/6/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/6/5.jpg',
    },
    platforms=[
        str(win.id),
        str(osx.id)
    ]
).save()

game7 = Games(
    gameName="METAL GEAR SOLID",
    publisher='KONAMI',
    releaseDate='2000-8-8',
    description="You are Snake, a government agent on a mission to regain control of a secret nuclear weapons base "
                "from terrorist hands. "

                "Now the international best-selling PlayStation game comes to the PC with better graphics, "
                "added features, "
                "and new gameplay modes! Unlike anything you've played before, Metal Gear Solid introduces a new "
                "genre of gaming where ninja-like stealth and cool head are your best weapons for survival.",
    coverImg='http://localhost:3200/Public/Images/7.jpg',
    systemRequirements=req,
    genres=[
        str(action.id),
        str(adventure.id),
    ],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/7/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/7/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/7/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/7/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/7/5.jpg',
    },
    platforms=[
        str(win.id)
    ]
).save()

game9 = Games(
    gameName="GRIP",
    publisher='Wired Productions',
    releaseDate='2018-5-27',
    description="Harness the power of gravity-defying wheeled or airborne vehicles, and smash your way through "
                "opponents with a bristling arsenal of outlandish weapons. GRIP delivers one of the fastest and most "
                "unique racing experiences ever as you scale walls, ceilings and anything else you can get your ride "
                "onto. Master twisting tracks, tricks and perform ridiculous stunts, fighting your way across alien "
                "planets to become the ultimate vehicular assailant.",
    coverImg='http://localhost:3200/Public/Images/9.jpg',
    systemRequirements=req1,
    genres=[
        str(action.id),
        str(strategy.id),
    ],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/9/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/9/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/9/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/9/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/9/5.jpg',
    },
    platforms=[
        str(win.id),
        str(linux.id),
    ]
).save()

game8 = Games(
    gameName="Carmageddon",
    publisher='THQ Nordic GmbH',
    releaseDate='2016-8-27',
    description="Play an adrenaline pumping bunch of game modes against AI opponents, or online against the rest of "
                "the Carmafan masses! Progress your Career through the Carma ranks or have a MultiPlayer romp in a "
                "Car Crusher, "
                "Fox 'n' Hounds (always been Stainless MP game session favourite!), Death Race or Checkpoint Stampede "
                "event - all frenetic fun, featuring Carmageddon’s trademark over-the-top violence, crazy PowerUps "
                "and non-stop laughs… "

                "PLUS! You can relive all the mangling mayhem with the built-in Action Replay System. Featuring "
                "multiple choice of cameras and replay options – it’ll mean you never miss a pile-up again! Get your "
                "movies online and brag about your ped culling achievements. "
                "And there will be plenty of THOSE too – Achievements, Challenges and Collectables to hunt down, "
                "that’ll keep the whole family entertained for hour upon happy blood and oil splattered hour.",
    coverImg='http://localhost:3200/Public/Images/8.jpg',
    systemRequirements=req,
    genres=[
        str(sports.id)
    ],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/8/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/8/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/8/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/8/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/8/5.jpg',
    },
    platforms=[
        str(win.id)
    ]
).save()


game10 = Games(
    gameName="Into the Breach",
    publisher='Subset Games',
    releaseDate='2018-2-27',
    description="he remnants of human civilization are threatened by gigantic creatures breeding beneath the earth."
                "You must control powerful mechs from the future to hold off this alien threat. Each attempt to save "
                "the world presents a new randomly generated challenge in this turn-based strategy game from the "
                "makers of FTL. "
                "Defend the Cities: Civilian buildings power your mechs. Defend them from the Vek and watch your fire!"
                "Perfect Your Strategy: All enemy attacks are telegraphed in minimalistic, turn-based combat. Analyze "
                "your "
                "opponent's attack and come up with the perfect counter every turn. "
                "Build the Ultimate Mech: Find powerful new weapons and unique pilots as you battle the Vek "
                "infestation across "
                "Corporate-Nation islands. "
                "Another Chance: Failure is not an option. When you are defeated, send help back through time to save "
                "another "
                "timeline!",
    coverImg='http://localhost:3200/Public/Images/10.jpg',
    systemRequirements=req,
    genres=[
        str(simulation.id),
        str(strategy.id)
    ],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/10/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/10/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/10/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/10/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/10/5.jpg',
    },
    platforms=[
        str(win.id),
        str(osx.id),
        str(linux.id)
    ]
).save()


game11 = Games(
    gameName="Slay the Spire",
    publisher='Mega Crit Games',
    releaseDate='2019-1-23',
    description="""We fused card games and roguelikes together to make the best single player deckbuilder we could. 
                "Craft a unique deck, encounter bizarre creatures, discover relics of immense power, and Slay the Spire!


                Features:

            Dynamic Deck Building: Choose your cards wisely! Discover hundreds of cards to add to your deck with each 
            attempt at climbing the Spire. Select cards that work together to efficiently dispatch foes and reach the 
            top. An Ever-changing Spire: Whenever you embark on a journey up the Spire, the layout differs each time. 
            Choose a risky or safe path, face different enemies, choose different cards, discover different relics, 
            and even fight different bosses! Powerful Relics to Discover: Powerful items known as relics can be found 
            throughout the Spire. The effects of these relics can greatly enhance your deck through powerful 
            interactions. But beware, obtaining a relic may cost you more than just gold... 



            Four characters that each have their own unique set of cards.
            350+ fully implemented cards.
            200+ different items to be found.
            50+ unique combat encounters.
            50+ mysterious events that can help or harm you.
            Daily Climbs allow you to compare yourself with every other player in the world.
            Custom mode that allows mixing and matching various crazy run modifiers.""",
    coverImg='http://localhost:3200/Public/Images/11.jpg',
    systemRequirements=req,
    genres=[
        str(rpg.id),
        str(strategy.id)
    ],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/11/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/11/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/11/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/11/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/11/5.jpg',
    },
    platforms=[
        str(win.id),
        str(osx.id),
        str(linux.id)
    ]
).save()


game12 = Games(
    gameName="Heroes 3",
    publisher='Ubisoft',
    releaseDate='1999-6-1',
    description="""Murder, treachery, resurrection, savage battles and ultimately-freedom!

When Erathia's King Gryphonheart is murdered by traitors he is resurrected as an undead warlord who leads a ruthless 
invasion of his former Kingdom. Little resistance is met until his daughter Catherine, Queen of Enroth, returns to 
her homeland commanding an army of elite Enrothian warriors. Meanwhile the Necromancers raise large hordes of undead 
and advance towards the Erathian capitol. Queen Catherine receives the aid of her father's survived generals and 
embarks on a crusade to reclaim her lost land. 

You control the greatest heroes and fiercest creatures in a conflict of epic proportions, as Cathereine fights to 
restore her family's rightful reign, uncover her father's killers and free him from the dark prison of his undead body! 

This is a must have for every Might and Magic series fan!

    Insanely addictive gameplay that will make you want to play “just one more turn” over and over again
    Great multiplayer, especially when playing in hot seat mode on one PC""",
    coverImg='http://localhost:3200/Public/Images/12.jpg',
    systemRequirements=req,
    genres=[
        str(strategy.id)
    ],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/12/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/12/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/12/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/12/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/12/5.jpg',
    },
    platforms=[
        str(win.id)
    ]
).save()


game13 = Games(
    gameName="Evil Genius",
    publisher='Rebellion',
    releaseDate='2004-10-15',
    description="""Build a secret base, gain notoriety by completing daring missions, repel the forces of justice in 
    real-time combat, and develop evil super-weapons to complete your nefarious master plan. As a malevolent 
    mastermind bent on achieving global domination, through the construction of the ultimate doomsday device, 
    Evil Genius gives you all the dastardly with none of the muttley. A tongue-in-cheek take on the spy thrillers of 
    the '60s, offering you the unique opportunity to play the villain as you control a secret island fortress 
    complete with powerful henchmen, loyal minions, ice-cold beauty queens, and a host of hilarious gizmos. 

Will you dare to try how evil you are? In this real-time mad scientist lair management strategic simulation, you can!

    Become the ultimate villain and take over the world!
    Fun-packed gameplay with humor and cliché lurking around every corner
    Unique, memorable characters and stylish, cartoonish visuals""",

    coverImg='http://localhost:3200/Public/Images/13.jpg',
    systemRequirements=req1,
    genres=[
        str(strategy.id)
    ],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/13/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/13/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/13/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/13/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/13/5.jpg',
    },
    platforms=[
        str(win.id)
    ]
).save()


game14 = Games(
    gameName="Banner Saga 3",
    publisher='Versus Evil',
    releaseDate='2018-10-15',
    description="""Banner Saga 3 is the final dramatic chapter in the mature, story driven Viking RPG series which 
    has won over 20 awards and has been nominated for 4 BAFTA awards. As the world continues to crumble around you, 
    who can you trust, how will you protect your allies and what choices will you make as the Darkness draws near? 

    Witness the Banner Saga as you’ve never seen it before as a dark force takes over and effects everything you’ve 
    come to know in the beautifully hand-painted finale of the trilogy. Choose new playable characters to join your 
    party, including dredge heroes! Take advantage of new upgrade options as they progress in battle. Deeper 
    strategic combat with the new battle waves system against a myriad of new enemies.The valka spear and heroic 
    titles let players customize their playstyle even further. Drive your own narrative as you carry over your 
    choices from both Banner Sagas 1 & 2, leading to different climatic endings in this final chapter. No hero is 
    safe. An all-new original score from Grammy-nominated composer Austin Wintory.""",

    coverImg='http://localhost:3200/Public/Images/14.jpg',
    systemRequirements=req1,
    genres=[
        str(rpg.id),
        str(strategy.id)
    ],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/14/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/14/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/14/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/14/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/14/5.jpg',
    },
    platforms=[
        str(win.id),
        str(osx.id)
    ]
).save()


game15 = Games(
    gameName="RimWorld",
    publisher='Ludeon Studios',
    releaseDate='2018-11-17',
    description="""RimWorld is a sci-fi colony sim driven by an intelligent AI storyteller. Inspired by Dwarf 
    Fortress, Firefly, and Dune. 

    You begin with three survivors of a shipwreck on a distant world.

    Manage colonists' moods, needs, wounds, illnesses and addictions.
    Build in the forest, desert, jungle, tundra, and more.
    Watch colonists develop and break relationships with family members, lovers, and spouses.
    Replace wounded limbs and organs with prosthetics, bionics, or biological parts harvested from others.
    Fight pirates, tribes, mad animals, giant insects and ancient killing machines.
    Craft structures, weapons, and apparel from metal, wood, stone, cloth, and futuristic materials.
    Tame and train cute pets, productive farm animals, and deadly attack beasts.
    Trade with passing ships and caravans.
    Form caravans to complete quests, trade, attack other factions, or migrate your whole colony.
    Dig through snow, weather storms, and fight fires.
    Capture refugees or prisoners and turn them to your side or sell them into slavery.
    Discover a new generated world each time you play.
    Explore hundreds of wild and interesting mods.
    Learn to play easily with the help of an intelligent and unobtrusive AI tutor.""",

    coverImg='http://localhost:3200/Public/Images/15.jpg',
    systemRequirements=req1,
    genres=[
        str(simulation.id),
        str(strategy.id)
    ],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/15/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/15/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/15/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/15/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/15/5.jpg',
    },
    platforms=[
        str(win.id),
        str(osx.id),
        str(linux.id)
    ]
).save()


game16 = Games(
    gameName="Stardew Valley",
    publisher='ConcernedApe',
    releaseDate='2016-11-17',
    description="""You've inherited your grandfather's old farm plot in Stardew Valley. Armed with hand-me-down tools 
    and a few coins, you set out to begin your new life. Can you learn to live off the land and turn these overgrown 
    fields into a thriving home? It won't be easy. Ever since Joja Corporation came to town, the old ways of life 
    have all but disappeared. The community center, once the town's most vibrant hub of activity, now lies in 
    shambles. But the valley seems full of opportunity. With a little dedication, you might just be the one to 
    restore Stardew Valley to greatness! 

Features

    Turn your overgrown field into a lively farm! Raise animals, grow crops, start an orchard, craft useful machines, 
    and more! You'll have plenty of space to create the farm of your dreams. 

    4 Player Farming! Invite 1-3 players to join you in the valley online! Players can work together to build a 
    thriving farm, share resources, and improve the local community. As more hands are better than one, players have 
    the option to scale profit margin on produce sold for a more challenging experience. 

    Improve your skills over time. As you make your way from a struggling greenhorn to a master farmer, you'll level 
    up in 5 different areas: farming, mining, combat, fishing, and foraging. As you progress, you'll learn new 
    cooking and crafting recipes, unlock new areas to explore, and customize your skills by choosing from a variety 
    of professions.""" ,

    coverImg='http://localhost:3200/Public/Images/16.jpg',
    systemRequirements=req1,
    genres=[
        str(simulation.id),
        str(rpg.id)
    ],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/16/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/16/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/16/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/16/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/16/5.jpg',
    },
    platforms=[
        str(win.id),
        str(osx.id),
        str(linux.id)
    ]
).save()


game17 = Games(
    gameName="SimCity 4",
    publisher='Electronic Arts',
    releaseDate='2003-10-17',
    description="""SimCity 4, you don't just build your city, you breathe life into it. Create a megalopolis by 
    weaving together a tapestry of cities ranging from a bedroom community to a high tech urban center or a vacation 
    destination to a farming village. You can create a region of interconnected cities sharing and competing for 
    resources that are linked by a fully integrated transportation network. Use god-like powers to create mountain 
    ranges, carve valleys, and lay rivers to construct the most realistic metropolis imaginable. The new simulation 
    engine offers immediate feedback so you can react to the needs of an expanding metropolis. Now individual 
    buildings and their lots provide you with feedback. Use the My Sim features to personalize your Sim and 
    immediately move him or her into any area and watch them experience life around town and get instant feedback on 
    the city's progress. Each decision has a greater impact and gives you the ability to respond more effectively.""" ,

    coverImg='http://localhost:3200/Public/Images/17.jpg',
    systemRequirements=req1,
    genres=[
        str(simulation.id)
    ],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/17/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/17/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/17/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/17/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/17/5.jpg',
    },
    platforms=[
        str(win.id)
    ]
).save()


game18 = Games(
    gameName="No Man's Sky",
    publisher='Hello Games',
    releaseDate='2016-8-12',
    description="""Inspired by the adventure and imagination that we love from classic science-fiction, No Man's Sky 
    presents you with a galaxy to explore, filled with unique planets and lifeforms, and constant danger and action. 

In No Man's Sky, every star is the light of a distant sun, each orbited by planets filled with life, and you can go 
to any of them you choose. Fly smoothly from deep space to planetary surfaces, with no loading screens, 
and no limits. In this infinite procedurally generated universe, you'll discover places and creatures that no other 
players have seen before - and perhaps never will again. 

Now including... Play with all major updates since launch: Foundation, Pathfinder, Atlas Rises, NEXT, The Abyss, 
Visions, the 2.0 BEYOND update, Synthesis, Living Ship, Exo Mech, Desolation and the 3.0 update, ORIGINS, 
Next Generation, Companions and Expeditions. 

An epic voyage to the centre of a shared universe awaits, allowing you to explore, trade, fight and survive alone or 
with friends.""",

    coverImg='http://localhost:3200/Public/Images/18.jpg',
    systemRequirements=req,
    genres=[
        str(action.id)
    ],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/18/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/18/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/18/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/18/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/18/5.jpg',
    },
    platforms=[
        str(win.id),
        str(osx.id),
        str(linux.id)
    ]
).save()


game19 = Games(
    gameName="Pyre",
    publisher='Supergiant Games',
    releaseDate='2017-7-25',
    description="""Pyre is a party-based RPG in which you lead a band of exiles to freedom through ancient 
    competitions spread across a vast, mystical purgatory. Who shall return to glory, and who shall remain in exile 
    to the end of their days? Experience the biggest and most imaginative world yet from Supergiant! Get to know an 
    ensemble cast of characters struggling to earn back their freedom as you make your way across the forsaken land 
    called the Downside. Battle against a colorful cast of adversaries in pitched, high-stakes confrontations where 
    each victory (or defeat!) brings your exiles closer to enlightenment. Choose three from your party for each Rite, 
    and outfit them with mystic Talismans and powerful Masteries.""",

    coverImg='http://localhost:3200/Public/Images/19.jpg',
    systemRequirements=req,
    genres=[
        str(action.id),
        str(rpg.id),
        str(indie.id)
    ],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/19/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/19/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/19/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/19/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/19/5.jpg',
    },
    platforms=[
        str(win.id),
        str(osx.id),
        str(linux.id)
    ]
).save()


game20 = Games(
    gameName="Wolfenstein II",
    publisher='Bethesda Softworks',
    releaseDate='2017-10-26',
    description="""Wolfenstein II: The New Colossus™ is the highly anticipated sequel to the critically acclaimed, 
    Wolfenstein®: The New Order™ developed by the award-winning studio MachineGames. 

An exhilarating adventure brought to life by the industry-leading id Tech® 6, Wolfenstein® II sends players to 
Nazi-controlled America on a mission to recruit the boldest resistance leaders left. Fight the Nazis in iconic 
American locations, equip an arsenal of badass guns, and unleash new abilities to blast your way through legions of 
Nazi soldiers in this definitive first-person shooter. STORY: America, 1961. Your assassination of Nazi General 
Deathshead was a short-lived victory. Despite the setback, the Nazis maintain their stranglehold on the world. You 
are BJ Blazkowicz, aka “Terror-Billy,” member of the Resistance, scourge of the Nazi empire, and humanity’s last hope 
for liberty. Only you have the guts, guns, and gumption to return stateside, kill every Nazi in sight, and spark the 
second American Revolution. .""",

    coverImg='http://localhost:3200/Public/Images/20.jpg',
    systemRequirements=req,
    genres=[
        str(shooters.id)
    ],
    screenshots={
        'screenshot1': 'http://localhost:3200/Public/Images/20/1.jpg',
        'screenshot2': 'http://localhost:3200/Public/Images/20/2.jpg',
        'screenshot3': 'http://localhost:3200/Public/Images/20/3.jpg',
        'screenshot4': 'http://localhost:3200/Public/Images/20/4.jpg',
        'screenshot5': 'http://localhost:3200/Public/Images/20/5.jpg',
    },
    platforms=[
        str(win.id)
    ]
).save()


# insert Users
user1 = Users(
    username="kobim1",
    password="karok12KL",
    email="kobim1@gmail.com",
    img="http://localhost:3200/Public/Images/avatar.png",
    favorite_genres=[str(action.id), str(rpg.id), str(strategy.id)],
    favorite_games=[str(game1.id), str(game2.id), str(game5.id), str(game10.id)],
    isAdmin=True
).save()

user2 = Users(
    username="kobim2",
    password="karok12KL",
    email="kobim2@gmail.com",
    img="http://localhost:3200/Public/Images/avatar.png",
    favorite_genres=[str(adventure.id), str(action.id), str(rpg.id)],
    favorite_games=[str(game1.id), str(game3.id), str(game5.id), str(game7.id), str(game9.id)],
    isAdmin=False
).save()

user3 = Users(
    username="kobim3",
    password="karok12KL",
    email="kobim3@gmail.com",
    img="http://localhost:3200/Public/Images/avatar.png",
    favorite_genres=[str(action.id), str(rpg.id), str(strategy.id)],
    favorite_games=[str(game12.id), str(game13.id)],
    isAdmin=False
).save()


user4 = Users(
    username="kobim4",
    password="karok12KL",
    email="kobim4@gmail.com",
    img="http://localhost:3200/Public/Images/avatar.png",
    favorite_genres=[str(action.id), str(simulation.id), str(strategy.id)],
    favorite_games=[str(game11.id), str(game9.id), str(game19.id), str(game15.id)],
    isAdmin=False
).save()


user5 = Users(
    username="kobim5",
    password="karok12KL",
    email="kobim5@gmail.com",
    img="http://localhost:3200/Public/Images/avatar.png",
    favorite_genres=[str(action.id), str(indie.id), str(shooters.id)],
    favorite_games=[str(game1.id), str(game2.id), str(game3.id), str(game10.id)],
    isAdmin=False
).save()


user6 = Users(
    username="kobim6",
    password="karok12KL",
    email="kobim6@gmail.com",
    img="http://localhost:3200/Public/Images/avatar.png",
    favorite_genres=[str(shooters.id), str(sports.id), str(adventure.id)],
    favorite_games=[str(game7.id), str(game8.id), str(game9.id), str(game18.id)],
    isAdmin=False
).save()


user7 = Users(
    username="kobim7",
    password="karok12KL",
    email="kobim7@gmail.com",
    img="http://localhost:3200/Public/Images/avatar.png",
    favorite_genres=[str(action.id), str(adventure.id), str(simulation.id)],
    favorite_games=[str(game7.id), str(game16.id), str(game14.id), str(game19.id)],
    isAdmin=False
).save()


user8 = Users(
    username="kobim8",
    password="karok12KL",
    email="kobim8@gmail.com",
    img="http://localhost:3200/Public/Images/avatar.png",
    favorite_genres=[str(strategy.id), str(indie.id), str(sports.id)],
    favorite_games=[str(game7.id), str(game2.id), str(game13.id), str(game17.id)],
    isAdmin=False
).save()


user9 = Users(
    username="kobim9",
    password="karok12KL",
    email="kobim9@gmail.com",
    img="http://localhost:3200/Public/Images/avatar.png",
    favorite_genres=[str(shooters.id), str(rpg.id), str(strategy.id)],
    favorite_games=[str(game20.id), str(game7.id), str(game2.id), str(game10.id)],
    isAdmin=False
).save()


user10 = Users(
    username="kobim10",
    password="karok12KL",
    email="kobim10@gmail.com",
    img="http://localhost:3200/Public/Images/avatar.png",
    favorite_genres=[str(action.id), str(shooters.id), str(indie.id)],
    favorite_games=[str(game6.id), str(game8.id), str(game5.id), str(game11.id)],
    isAdmin=False
).save()

# insert reviews
# user1
review1 = Reviews(
    userId=str(user1.id),
    gameId=str(game1.id),
    visability=True,
    title="""ever trust the hype""",
    body="""Cyberpunk 2077 failed to deliver the experiance that CDPR was advertising up until the release of the game. They promised an RPG that will redefine the genre, but instead we got a middling Action-RPG experiance that feels more like FarCry rather than the pen and paper game the game is based on. 

All troughout the development of the game we were promised a experiance unlike any other and I must admit that I actually believed that CDPR could pull it off. 

But they didn't...""",
    conclusion="""The buggs and horrible optimization are the least of the games problems, they are just convinient 
    issues that CDPR is happy about. Since the bugs distract people from the real issues of the game. """,
    score=7,
    tags=[str(tag1.id), str(tag2.id)]
).save()

review2 = Reviews(
    userId=str(user1.id),
    gameId=str(game2.id),
    visability=True,
    title="""A Masterpiece!""",
    body="""I've always been an RPG lover. But did not enjoy any third person perspective ones. So, obviously, 
    I had never played this. A friend of my recently learned of this fact and for months pestered me to play this 
    game. I eventually gave in, and bought the game early 2021. And I must say, putting my bias aside, this game is 
    nothing short of phenomenal. I trully love the quests. The writing is top tier, as I had heard from CDPR. I had 
    quests where I ended tearing up. I felt some strong emotions. Not only that, Geralt's relatioship with Triss, 
    whose romance I enjoyed the most, really felt familiar to my very own. And not to mention that in 2021, 
    the graphical aspect of the game is yet amazing. It just looks beautiful. The controls sure feel weird to me, 
    although I will credit that to my lack of joy for the perspective and as such will not hold it agains the game 
    itself. The game spoke to my in a way so particular, I placed aside my hatred for third person just for this 
    sage. I  ended up getting the previous two games because of this one.""",
    conclusion="""Amazing in every single way! You will remember this game like a fine fine book! 10/10""",
    score=10,
    tags=[str(tag2.id), str(tag3.id)]
).save()


review3 = Reviews(
    userId=str(user1.id),
    gameId=str(game5.id),
    visability=True,
    title="""Worth it""",
    body="""if you expect a perfect gem, hyper-polished with zero bugs and amazing stability. Go away, this is an 
    Early Access game. Not all early access games are stable. 

If you want an authentic 5e simulator for the Forgotten Realms DnD campaign - just get RollD20 and write your own one. 

We all know what happens when you are hyper-tied to your setting or system, you get Temple of Elemental Evil. A game 
so mindbogglingly complex only three DMs that have read and memorized the books can figure out how to actually play it. 

No, this game is made by Larian, but the setting, the lore, and systems are in service of the game, not the other way around.

And while it's a buggy, glitchy and sometimes crash-prone mess. It's a gem and I'd honestly buy it again""",
    conclusion="""Then BG3 is the game from you. I played this game for 20hrs, only to realize, I didn't scratch the 
    surface of what it's story brings.""",
    score=8,
    tags=[str(tag1.id), str(tag2.id), str(tag3.id)]
).save()


review4 = Reviews(
    userId=str(user1.id),
    gameId=str(game10.id),
    visability=True,
    title="""What a game!""",
    body="""What can I say? This is turn based at its best and somewhat weirdest. I've put ~40 hours into this, 
    but that's just scratching the surface. This is challenging, sometimes frustrating (because the odds are stacked 
    against you), but oh so rewarding.""",
    conclusion="""Please do yourself a favor and buy this game.""",
    score=9,
    tags=[str(tag1.id), str(tag4.id)]
).save()


# user2
review5 = Reviews(
    userId=str(user2.id),
    gameId=str(game1.id),
    visability=True,
    title="""Major disappointment""",
    body="""Major disappointment

June 20, 2021 Verified owner

Graphically, the game is stunning and CDPR have done a great job of creating a city. That's where the praise ends.

Character creation is incredibly limited for such a contemporary game. There are MMOs with much richer character 
creation than CP2077 offered. This is a massive let down! -1 Star 

The story is actually really good. Insanely good and like CDPR's marketing campaign, the promise at the start is 
palpable. However, then they throw the classic sense of urgency at you. In the Witcher III, we were given a mission 
but there was no hurry, so we were given a legitimate chance to explore the world and experience the wonderful side 
quests on offer. CP2077 makes you feel as though you're supposed to rush through to the end or else... stupid. -1 Star 

Glitches Galore. So many times main characters just got into my car... while I was driving at 200km/h... A lot of 
other glitches but there are forums describing these so I need not. I've played enough Bethesda games to appreciate 
bugs are a thing but CDPR always say when it's ready and this clearly was not. -1 Star 

Graphically, the world was amazing. Rich and varied and the places all seemed to make sense. I loved driving through NC with raytracing on and watching the skyscrapers glisten off my car. +1 star

A large portion of the game is spent driving... ugh wow. -1 Star.""",
    conclusion="""I could never ever recommend this game. This also from someone desperate to love it. Shame it 
    didn't work out.""",
    score=5,
    tags=[str(tag1.id), str(tag2.id)]
).save()


review6 = Reviews(
    userId=str(user2.id),
    gameId=str(game3.id),
    visability=True,
    title="""Emotional Story""",
    body="""First off, the presentation of the game, especially the Enhanced Edition is unrivalled. Lighting looks 
    amazing. The game looks amazing. 

The gameplay is varied and interesting. You can go in guns blazing or sneak around and kill nobody. Do note that the 
game pushes you to the latter to get a good ending. 

The story is pretty personal to Artyom. You're not really saving the world or anything. You're saving your friends.""",
    conclusion="""Highly recommended.""",
    score=9,
    tags=[str(tag1.id), str(tag2.id)]
).save()


review7 = Reviews(
    userId=str(user2.id),
    gameId=str(game5.id),
    visability=True,
    title="""I liked it""",
    body="""I'd give this game a solid 4 out of 5 stars if it weren't for the slow combat.  Whoever the genius is who 
    thought watching 15 trash mobs move a few inches across your screen is fun really needs to rethink what fun 
    actually is. 

Larian should have implemented BOTH turn based comabt and real time with pause, or at the very least speed the combat 
up.  There are several RPGs out there with both options available.  I didn't find the combat all that challenging.  
It was just so long and drawn out that I nearly fell asleep.  I get that they like turn based, that they're trying to 
recreate a table top experience, but I feel that in this day and age it doesn't translate well in a single player 
computer game.  I think it would be a boon to the game and it's player base to inculde both, IMO. 

However, even though the combat was a bore, I still enjoyed what the game has to offer.  It looks great, 
employs a cast of amazing voice actors and the writing isn't bad.  I especially loved the characters.  It was 
surprisingly not as buggy as I thought it would be.  The only thing major that I came across was a lot of crashing 
when loading a quicksave. 

Another thing - this game doesn't have anything in common with the Baldur's Gate games that came before it, 
its very much Divinity vaguely based in the Forgotten Realms.  It even started similiar to the last Divinity game.  
Captive in a ship and it crashes on a beach!""",
    conclusion="""I still think it has a ton of potential and I'm looking forward to the final product.  Here's 
    hoping they iron out that sloooooooow combat problem.   """,
    score=7,
    tags=[str(tag1.id)]
).save()


review8 = Reviews(
    userId=str(user2.id),
    gameId=str(game7.id),
    visability=True,
    title="""Recommendations, flaws personal opinions""",
    body="""Games: 19 Reviews: 1

Recommendations, flaws personal opinions

June 16, 2021 Verified owner

This game is an absolute classic, granted it's unlike the PS1 port, which I played when I was a kid who always liked 
the scenes that made the controller vibrate that always created more immersion, which is something the PC port 
doesn't have, sadly. But that's not to say that the game is bad in any way. You're still playing as the iconic Solid 
Snake, the story isn't tempered with in any way and the gameplay is just how I remembered it. I would recommend you 
to play this on a controller though and change the keybindings in-game, then you'd get to have a nice and (for some) 
a nostalgic experience. 

Playing with the keyboard is a bit tricky but managable, it doesn't include the entire Alert soundtrack but it's 
still good, for graphics the PC port uses texture smoothing which removes this blocky-pixelated look of the original 
PS1 port which is supposed to be part of the game's appeal. 

With these flaws the PC port is still perfectly playable and enjoyable, but that's just my opinion.""",
    conclusion="""This game is one of my favorite games and was the first one that put me into the world of gaming, 
    thus I have so much respect for the game. """,
    score=9,
    tags=[str(tag2.id), str(tag3.id)]
).save()


review9 = Reviews(
    userId=str(user2.id),
    gameId=str(game7.id),
    visability=True,
    title="""Still in love after +650hours""",
    body="""This GoG version is a really good deal if you want to play in Singleplayer, it contains almost all DLCs, 
    it just lacks one map and one free car (which might come later into an update). Only lacking things are the 
    Delorean, the VR and MP features, but you can still play split-screen! 

Now for all the new players, the game itself is a really great and wonderful game, a lot of maps, a lot of variety in 
cars, you can spend a lot of great time just trying to beat the best times on the speedrun.com page. If you want a 
Rollcage spiritual successor, this is the one. If you want to experience great great speed, this is the one. If you 
want to witness mayhem and chaos, this is the one.""",
    conclusion="""The GoG version is really a great deal and if you want a great racing game, just go for it. """,
    score=10,
    tags=[str(tag2.id), str(tag3.id)]
).save()


# user3
review10 = Reviews(
    userId=str(user3.id),
    gameId=str(game12.id),
    visability=True,
    title="""Favorite Turn-based Fantasy Game""",
    body="""After the older Heroes of Might and Magic 2, this is my next favorite turn-based fantasy strategy game.  
    Like the previous game, this game has fantastic music and aesthetics, and incorporates a variety of magical 
    creatures from different myths and religions of the world such as Greek Titans and Minotaurs, to Genies and other 
    creatures from middle eastern cultures, as well as other magical and medieval creatures like wizards, druids, 
    crusaders, etc.  This game also seems to bring in creatures from the Christian religion like Angels and Devils as 
    well. 

I would recommend playing Heroes of Might and Magic 2 first if you are new to the series because it's the best and 
will familiarize yourself with the game world before moving on to the newer game, particularly if you're playing the 
single player campaign (which isn't that great imo). 

The way I most enjoy playing this are the single player skirmish scenarios vs the AI.

This is old, but it's a classic.  This is the sort of game I still play with friends who used to play this with me in 
decades past because it's still quite fun even decades later. 

People will argue over which is the best in the series, but I think the general consensus in my experience is that 
Heroes 2 and Heroes 3 are the best (by far).""",
    conclusion="""gIf you like medieval fantasy and turn-based strategy games like Civilization 5 or something like 
    that, don't hesitate to buy this! I strongly recommend it. """,
    score=9,
    tags=[str(tag4.id), str(tag3.id)]
).save()


review11 = Reviews(
    userId=str(user3.id),
    gameId=str(game13.id),
    visability=True,
    title="""Meh; this game's nothing special.""",
    body="""Among strategy games, where you get to BE THE BAD GUY, and DEFEND YOUR DOMAIN, it COULD have been that 
    great, but honestly? Compared to the Dungeon Keeper games that were released for PC, it's FAR too slow-paced.""" ,
    conclusion="""What a shame; it COULD have been a MASTERPIECE! But instead, I've been playing it and, it's just 
    not very good.""",
    score=5,
    tags=[str(tag1.id), str(tag4.id)]
).save()


# user4
review12 = Reviews(
    userId=str(user4.id),
    gameId=str(game11.id),
    visability=True,
    title="""Beautiful pearl within an ugly shell""",
    body="""it's a very engaging, well - balanced deckbuilder, with 4 very distinct characters, tons of different 
    card combinations, enough randomness to keep things fresh and enough strategy to always be fair with your chances 
    to beat it. Building your deck from what you can get in any given game is a great way to force you to constantly 
    rethink and optimize your options and prevents you from keeping a predetermined strategy in mind. It feels a 
    little bit like a rougelike, and is equally engaging. 

On the other hand the graphics are pretty ugly and animations are almost non - existent in this game. But if you can 
look past its ugly shell, you will fond a real pearl inside.""",
    conclusion="""I, personally, love it, and despite its ugliness I'm rating it 10/10.""",
    score=10,
    tags=[str(tag1.id), str(tag2.id)]
).save()


review13 = Reviews(
    userId=str(user4.id),
    gameId=str(game9.id),
    visability=True,
    title=""""Great game, just no multiplayer""",
    body="""This is pretty much the Steam version just missing multiplayer.  Dunno what that other guy is so angry 
    about DLC because most of the paid stuff on Steam is included for free here 

            Game is fast and fun but kinda hard so be prepared to put some time in.  I like the wheeled cars better 
            but the hovers are fun too.  Some tracks are better than others.""" ,
    conclusion="""Solid 8/10""",
    score=8,
    tags=[str(tag1.id), str(tag2.id)]
).save()


review14 = Reviews(
    userId=str(user4.id),
    gameId=str(game19.id),
    visability=True,
    title=""""Like a good fantasy book or series""",
    body="""I don't always finish my games. Even more so when the gameplay doesn't catch me. But this jewel just has 
    one of the best settings and story of everything I played in recent years. Combined with a fantastic soundtrack, 
    I just couldn't stop returning every night. 

Somehow it felt like a novel of Neil Gaiman. And after finishing it, I feel the same nostalgic satisfaction a good 
book leaves me with.""",
    conclusion="""If you like the action matches, this could easily be ten for you. If not so much, just tune down 
    the difficulty and enjoy the world. """,
    score=9,
    tags=[str(tag1.id), str(tag4.id)]
).save()


# user5
review15 = Reviews(
    userId=str(user5.id),
    gameId=str(game1.id),
    visability=True,
    title=""""A gem tarnished by undelivered promises""",
    body="""The Good
-Story overall neatly excetued personal story about trying to save yourself wish only the subplot with AI's and black wall had more to it.
-Johhny Silverhand(Good character impression of John Prick by Keeanu) 
-The Characters controls are really slick and responsive and running around the city jumping and sliding are really cool and make you feel like parkour master.
-The stealth mingame  Hiding from enemies and man aging their lines of sight with elemnts of enviorment gives a really great immersive feel of baing cyber ninja on the prowl.

The Bad
-Combat system (despite stamina mechanic for mele) and ability to shoot from behind the cover you can see that there were preparations for deeper system coupled with ingame physics however it was abandonded for some reason undisclosed(propably time) This is especially sad as for instance the destructible envioremnt would give the combat mechanics the so much neede feeling of being powerfull and interesting. But it has been scaled back to occasional destructible sign or two 
-Cops Who made the decision to make them unhackable and for what reason? Also the saddest part is that NC Cops will never chase with the player with their cars which kills the immersion 
-Hacking minigame By the end this minigame becomes tedious and annoying, Nothing on the level of Gwent which was one of the best minigames made apart from Cooking mechanic in Dragons Crown.", "Overall this game gives me early Vampire the Masquarade Bloodlines impression a great gem but unpolished and tarnished by wierd design decisions.
Wish it weren't so and hope reds will go No mans sky way out of it but as for now if I could decide to buy this game again I simply wouldn't do so.""",
    conclusion=""""Overall this game gives me early Vampire the Masquarade Bloodlines impression a great gem but unpolished and tarnished by wierd design decisions.
Wish it weren't so and hope reds will go No mans sky way out of it but as for now if I could decide to buy this game again I simply wouldn't do so.""",
    score=6,
    tags=[str(tag3.id), str(tag4.id)]
).save()


review16 = Reviews(
    userId=str(user5.id),
    gameId=str(game3.id),
    visability=True,
    title=""""Highly Overlooked""",
    body=""""Weapons for all cases, circumstances and scenarios? Yep
Good AI that calls our your position depending on what type of object or landmark you are by? Yep
Satisfying sound design for guns and other interactions? Yep
Well written story that keeps you constantly engaged with a range of emotions and good characters? Yep""",
    conclusion="""No idea why people love to crap on thid title so much. I guess thats what years of constant COD and 
    BF releases does to people. """,
    score=9,
    tags=[str(tag1.id), str(tag2.id)]
).save()


review17 = Reviews(
    userId=str(user5.id),
    gameId=str(game2.id),
    visability=True,
    title=""""Sharing my journey with this epic game""",
    body="""I pirated it, tested it, and wasn't hooked up, and gave up.

Several years later, we're in 2020, trying it again, played it a little bit more, and discovered all the beauty: the writing, the acting, the atmosphere, the characters.
Suddenly, I was ready to contemplate what a masterpiece was like.

I of course bought it immediately, as I promised myself I would when I would have grown up.""",
    conclusion="""I can understand why some might not like it, but it doesn't make it less of a masterpiece""",
    score=10,
    tags=[str(tag1.id), str(tag2.id)]
).save()


# user6
review18 = Reviews(
    userId=str(user6.id),
    gameId=str(game7.id),
    visability=True,
    title=""""Shabby, barebones port""",
    body="""A disappointing port of a great game. The main issue for me is the control scheme, which is shockingly 
    clumsy and frustratingly limited. Just maneuvering out of the first cargo dock area was incredibly difficult, 
    and that's not even attempting CQC or firing a weapon. An extremely patient and forgiving person might be able to 
    slog through it, but I can't imagine playing the full game this way. 

If you've played MGS on a console and are looking to revisit it on PC, let me assure you that this does not live up 
to the original experience. If you've never played MGS before, I'd hate to think that this is how someone might 
experience one of the best games ever for the first time. Even on deep discount I'd be hesitant to recommend this to 
anyone.""",
    conclusion="""Thankfully I'm only out a few bucks for my trouble, but rather than force myself to endure this, 
    I'm just going to hang tight for the rumored PS5 / PC remake. """,
    score=5,
    tags=[str(tag4.id), str(tag2.id)]
).save()


review19 = Reviews(
    userId=str(user6.id),
    gameId=str(game9.id),
    visability=True,
    title=""""Grip Lite edition""",
    body="""The game features different game modes like the standard vanilla race and campaign with preset events, 
    or the speed demon race with only booster powerups to name a few, and if you ever feel like spicing things up, 
    there are modificators such as insta-kill or hyperdrive as well to create your own custom races and events. 

The tracks are divided in four main themes that could be summarized as: Desert, Snow, Artificial, and Seaside Woods. 
While it might look like there is a lack of variety, the tracks themselves all have a different take on the formula, 
sometimes being on a plain field, sometimes twisting and spinning around with loops and upside-down paths, 
and sometimes even shifting from a snowy road to the inside of a volcano, or from a seaside to an underwater tunnel. 

The only two issues with the game are the janky physics and cheatsy AI. To put it simple, the physics in this game 
are unpredictable, the kind that you can hit a barrel and have a chance to either send it to the moon or have your 
car trip over it (I'm not kidding). As for the AI, raising the difficulty turns the races from a 10 Vs 10 into a 1 Vs 
10, because the opponent cars will all focus their attacks on you regardless of how many other racers might be on 
their sight.""",
    conclusion="""Overall, this is one of the most fun Sci-Fi racers out there. The races are intense, the tracks are 
    fun to drive thorough, the vehicles are powerful monsters, and hitting enemies with missiles always feels 
    great.""",
    score=7,
    tags=[str(tag4.id), str(tag1.id)]
).save()


review20 = Reviews(
    userId=str(user6.id),
    gameId=str(game8.id),
    visability=True,
    title=""""Can't believe the harsh reviews""",
    body="""The only reason i'm not giving it 5 stars is because the loading times are pretty brutal... although, the maps are huge, and packed with powerups, pedestrians, tokens, secrets, ramps and loop dee loops..etc etc... One could spend hours just exploring. So perhaps this is why.

As for the driving mechanics., I think it's even better than previous Carmageddons. Yep, i said that. And i've been playing Carmageddon allll my life, still play the old ones today too. It's NOT a racing game. The handling is supposed to feel like that. Believe it or not, this is realistic.. for suped up tank cars flying down city streets at breakneck speeds running over curbs, car parts and pedestrians.. what did you expect? I find the driving perfect. It is so much easier than the previous games. What is the problem here? No idea. I can drive the crap out of this game with near perfect handling.
I stress again. NOT a racing game. Think more like a demolition derby game.
Drive it like a real car. If you start going into a skid... take your foot off the pedal. Easy.

The graphics look beautiful on my 3000whatever resolution, 4k screen. Even at low settings.""",
    conclusion="""I'm kind of baffled why everyone seems to hate this game. I adore it. A fine successor to the franchise.
The only bad point i can make is the loading times. A bit long, but whatever. I have so much fun with this. And at reg. 18bucks or whatever, (i got it on sale for like 4bucks) how can you go wrong? """,
    score=8,
    tags=[str(tag1.id)]
).save()


# user7
review21 = Reviews(
    userId=str(user7.id),
    gameId=str(game7.id),
    visability=True,
    title=""""I am satisfied""",
    body="""Of course the game is rich in story. This game has some moral values and has also affected my character 
    and thoughts in a positive way. Soundtrack is amazing, different music are played according to the situation 
    which elevates the player's mood all the time. The boss battles are really tough and puts our skills to test. """,
    conclusion="""The game doesn't feel boring at all, vibe is always taken care of from starting to end.""",
    score=9,
    tags=[str(tag4.id), str(tag1.id)]
).save()


review22 = Reviews(
    userId=str(user7.id),
    gameId=str(game16.id),
    visability=True,
    title=""""Nice wholesome game""",
    body="""This is nice, wholesome game I lie to play to get my spirit up. It's like listening to Bob Ross saying nice thing to make you feel good.

Game as challenging as you want it to be.""",
    conclusion="""Really, dev made a wonderful job. I return to valley every now and then.""",
    score=9,
    tags=[str(tag2.id), str(tag1.id)]
).save()


review23 = Reviews(
    userId=str(user7.id),
    gameId=str(game14.id),
    visability=True,
    title=""""3 times is the charm?""",
    body="""If you played the first two games you'd probably wondered what the hell was going on, as not much 
    explanation was given. Fear not, the conclusion to the whole story comes with this one and it isn't even that 
    bad. it's particularly that great either, though, as two main narrative threads seem quite disconnected. Well, 
    storytelling wasn't really the strong point of the saga anyway, if you ask me, and the tactical battles still 
    deliver.""",
    conclusion="""If you are like me, you'd probably like the survial mode more than the actual campaign so I'd 
    recommend getting it. It's quite tough but allows for some really, really broken combos and no narrator is taking 
    your heroes away dramatic reasons just after you invested a ton of money in them... """,
    score=8,
    tags=[str(tag2.id), str(tag3.id)]
).save()


# user8
review24 = Reviews(
    userId=str(user8.id),
    gameId=str(game2.id),
    visability=True,
    title=""""Game Changer!""",
    body="""This Game is one of the best things that has happened in my life. regardless of this i'd say that after 
    finishing the game there are no relevent things to see in your life as Geralt because everyone is simply gone! I 
    mean all the actions that i took meant a lot to me but after the game is finished it feels like i have done 
    nothing at all! Plus the game doesn't make a good connection with Assassin Of Kings but that's not that big of a 
    deal to me""",
    conclusion="""So after considering all that I'm still and forever grateful to CDPR for taking me to this 
    beautiful unique journey.""",
    score=9,
    tags=[str(tag2.id), str(tag4.id)]
).save()


review24 = Reviews(
    userId=str(user8.id),
    gameId=str(game7.id),
    visability=True,
    title=""""Pretty Good""",
    body="""its pretty good i do have some issues like i use a xbox one controller and rebinding is kind of a pain 
    trying to get the exact ps1 controls from the og on the ps1  """,
    conclusion="""its the shit!""",
    score=8,
    tags=[str(tag2.id), str(tag3.id)]
).save()


review24 = Reviews(
    userId=str(user8.id),
    gameId=str(game13.id),
    visability=True,
    title=""""less Genius and more super-talented""",
    body="""This is a game I missed when it first came out. Something just didn't charm me into buying it. Thanks to 
    GOG I got that second chance. I don't regret buying it now, just maybe more that I never back then. As good as it 
    is, and it's addictive and quirky, it feels lacking in something, some magic, and maybe that is more about it 
    belonging to a previous generation of games more than it not being exceptional. 

The music is good, graphics look dated but still playable. Animations are surprisingly as good as we get nowadays, 
and in the case of Mass Effect Andremda, far better! It's simple to pick up, easy to play, and a fantastic game. I 
don't however find it funny, that was a selling point, people found it funny. Maybe I'll get my funny bone checked 
out at Two Point Hospital when that comes out... 

I just feel like It's missing some gameplay, or time has caught up with it. I've spent many an hour on the world map 
wondering if that is all there is to the game once your base has max occupants and you're waiting for the challenge 
bits to be accessible, moving the sttory/events on requiring hitting certain infamy levels and due to this it feels a 
bit grindy.""",
    conclusion="""I'd recomend it to anyone that had it back in the day as it's still addictive and as good as most 
    games out there, I feel that my review is scored on the fact that after 2 decades of hearing how awesome it is, 
    I still don't see it maybe for what others do, a classic. """,
    score=8,
    tags=[str(tag1.id), str(tag3.id)]
).save()


review25 = Reviews(
    userId=str(user8.id),
    gameId=str(game17.id),
    visability=True,
    title=""""A bit too much""",
    body="""If you wanted even more complexity to your Simcity experiance, disregard my score and pick this one up.

In my experiance, the other titles give you a complex task of running a city and makes it fun and engaging. 
Up until 4, I've had a good time with the series.

It's still all there, looks better, adds more... way more. Too much more, in my opinion. 

I figured out from watching videos how the new growth system works [different class levels of Sims will want to move 
into different areas, industry levels change in a similar way, they all tie together, ect] You can micro manage the 
budget for Powerplants, Shools, Hostipals, ect, to shave off costs You have like... 5 different types of roads now. 
And highways... It becomes a mess at this point, and a turn off to me. 

The new graphics are awesome, but then you have trouble finding things like busstops and hostipals, key locations get 
lost in the density. The underground scene is way more easier to read at first, until you start running into hills, 
with your waterpipes being lost in deep silly looking canyons that require you to mash the rotation keys to even 
understand what you're looking for.""",
    conclusion="""I feel like I have a LOT more research to do before I can get into this one.
Or, I'ma just go back to one of the earlier enteries in the series until I'm ready.""",
    score=7,
    tags=[str(tag1.id), str(tag2.id)]
).save()


# user9
review26 = Reviews(
    userId=str(user9.id),
    gameId=str(game7.id),
    visability=True,
    title=""""Bucket Listers Rejoice""",
    body="""For anyone wanting to start this series the right way, look no further. This is the cheapest, easiest, 
    most user-friendly way to get your feet wet and start your path in this amazing game franchise TODAY. Sure, 
    you could also buy the original Metal Gear (also on this site for cheap) and start at the VERY beginning, 
    but it's not really necessary in my opinion. 

Okay so to anyone who hasn't figured this out already: THE BLACK BAR IS NOT A GLITCH, read that again. Also, 
reviews that talk about how crappy the graphics look on the PC version aren't lying, it's just something you have to 
accept about the era this game was made in. It's not as bad as the sprites from FFVII, but it sometimes is difficult 
to feel the full emotional impact of a tear-jerking scene when you're watching a non-expressive, emotionless, 
eyeless mask of a face bob up-and-down for five minutes straight. 

Otherwise this game just blows me away even this many years later. Having owned and played the original Playstation 1 
console as a kid I just can't get over how well designed and developed this game is in almost every aspect. The voice 
acting is phenomenal, it plays like a cheesy thriller action movie with all the whirlwind emotional twists and turns 
and I love every minute of it. The gameplay is a little tanky, kind of like playing old Resident Evil games, 
but it's very innovative for the time with a huge arsenal of weapons and items being at your disposal. The story is 
much like the voice acting and is very over-the-top and dramatic with a spy element that is hard not to love. """,
    conclusion="""Buy it play it right NOW""",
    score=9,
    tags=[str(tag1.id)]
).save()


review27 = Reviews(
    userId=str(user9.id),
    gameId=str(game7.id),
    visability=True,
    title=""""Bucket Listers Rejoice""",
    body="""For anyone wanting to start this series the right way, look no further. This is the cheapest, easiest, 
    most user-friendly way to get your feet wet and start your path in this amazing game franchise TODAY. Sure, 
    you could also buy the original Metal Gear (also on this site for cheap) and start at the VERY beginning, 
    but it's not really necessary in my opinion. 

Okay so to anyone who hasn't figured this out already: THE BLACK BAR IS NOT A GLITCH, read that again. Also, 
reviews that talk about how crappy the graphics look on the PC version aren't lying, it's just something you have to 
accept about the era this game was made in. It's not as bad as the sprites from FFVII, but it sometimes is difficult 
to feel the full emotional impact of a tear-jerking scene when you're watching a non-expressive, emotionless, 
eyeless mask of a face bob up-and-down for five minutes straight. 

Otherwise this game just blows me away even this many years later. Having owned and played the original Playstation 1 
console as a kid I just can't get over how well designed and developed this game is in almost every aspect. The voice 
acting is phenomenal, it plays like a cheesy thriller action movie with all the whirlwind emotional twists and turns 
and I love every minute of it. The gameplay is a little tanky, kind of like playing old Resident Evil games, 
but it's very innovative for the time with a huge arsenal of weapons and items being at your disposal. The story is 
much like the voice acting and is very over-the-top and dramatic with a spy element that is hard not to love. """,
    conclusion="""So what's in the box? Well since this is Integral you get a more finished version of the original 
    game, with all of the VR missions and whatnot. You could also consider this a director's cut because the game is 
    altered slightly to accommodate the PC (mostly in the Psycho Mantis fight). You can easily plug in a PS4 
    controller to play it. """,
    score=9,
    tags=[str(tag1.id)]
).save()


review28 = Reviews(
    userId=str(user9.id),
    gameId=str(game10.id),
    visability=True,
    title=""""A gem you may need to polish to get into""",
    body="""It's a really fun game with lots of unlockable variability you may miss in the beginning when you're 
    still bad at it. Be patient, learn the ropes, and it's basically an endless puzzle game of good quality. When 
    things go well, you feel competent and like you've earned the right to feel that. When things go badly, 
    it's the most infuriating thing you can imagine, because it's largely your own fault for positioning yourself 
    without thinking about the next round. """,
    conclusion="""Buy it play it right NOW""",
    score=9,
    tags=[str(tag3.id)]
).save()


# user10
review29 = Reviews(
    userId=str(user10.id),
    gameId=str(game4.id),
    visability=True,
    title=""""Flawed masterpiece, QoL issues""",
    body="""PROs: Hollow Knight is a masterpiece in so many ways. Rarely has a game's atmosphere so captivated me, 
    or the feeling of exploration been so real and wonderful. Almost everything about the game is such a polished 
    masterpiece, feeling amazingly unique among the hundreds or thousands of games I've tried. 

CONs: What got me to abandon the game was something absolutely ludicrous: checkpoints are far from boss fights.

When you lose to a boss, you have to re-travel through up to a dozen screens full of enemies, battling and dodging 
through them in a desperate attempt to avoid losing any hitpoints before getting your next shot at the boss. This is 
the opposite of fun and felt like a colossal waste of time to me. 

There are a few smaller QoL issues in the game, like having to spend one of your limited equipment slots if you want 
to be able to see where you are on the map, and losing all of your money every time you die in a hard-to-reach place 
(your ghost keeps it until your next death, but getting there could be deadly, and if you manage, your ghost might 
kill you). 

Everything else about this game is an absolute masterpiece and kept me playing for hours despite the frustrations, 
but somewhere around the midway through the game I noticed I had spent more than half the time of the last few hours 
re-fighting the same waves of enemies to re-reach the easiest remaining boss. I'd rather watch a movie than continue 
that loop.""",
    conclusion="""The first third or so of Hollow Knight felt like a true wonder of the gaming world, 
    but the frustrating combination of difficulty and low QoL left a bad taste in my mouth.""",
    score=9,
    tags=[str(tag1.id)]
).save()


review30 = Reviews(
    userId=str(user10.id),
    gameId=str(game13.id),
    visability=True,
    title=""""Throw me a bone, people!""",
    body="""There's a lot to like here, and some very clever in-jokes for fans of Bond films and classic spy shows of yore.

That said, a few notable whinges:

1.  The Acts of Infamy (AoI) that should be the heart of the tactical game are abstracted to the point of being as 
exciting as watching a download.  I'd like to see a revision of the game that makes the AoI missions the heart of 
gameplay using an engine like Silent Storm or Invisible Inc. 

2.  The lack of scenarios or random starts, and the fact that any restart takes you all the way back to square 1 
having to reinvent every room from scratch - these things hurt replay (at least for me) since it feels like I have a 
long slog just to get up to the interesting part. 

3.  You absolutely need to follow a walkthru to prevent making a critical error that will screw up your end game because...

4.  The game plays out in a stuck script with only a few digressions or options along the way.  The side quests are 
minimal and really just add more loot, the variation in henchmen is fixed (can't create your own or even name them), 
and the objectives are linear with no branching.""",
    conclusion="""All in, it's definitely worth the price here on GOG, but you will get bored sooner than with 
    comparable games like Dungeon Keeper - and that's too bad.  There is an opportunity here for a truly great game 
    and maybe someone will pick that up and give us Evil Genius 2.  If so, I'd want to see it focused more on the AoI 
    missions, allow for more user customization and branching plots/objectives.""",
    score=8,
    tags=[str(tag2.id)]
).save()



review31 = Reviews(
    userId=str(user4.id),
    gameId=str(game6.id),
    visability=True,
    title=""""7th Generation Gem""",
    body="""This game is one of my favourite new IPs from its generation. To explain it in short, it's a GTA clone 
    set in Hong Kong with an emphasis on Batman-esque hand to hand fighting and limited gunplay. 

The story is a short and sweet 15 hour campaign revolving around Wei Shen, a Hong Kong-American repat undercover with 
the HKPD tasked to infiltrate and take down the triad. While a simple setup there's well written characters (with 
some surprisingly big name voice actors) and a greyness to Wei's character as his loyalty to the police, the triads 
and his own personal motivations all come into play throughout the story. 

The combat is fun and satisfying with unlockable moves gained from statues hidden around the map and character 
upgrades tied to Triad and Police XP gained through missions depending on how much illegal stuff you do over the 
mission vs how by the books you were. It is rather easy though and doesn't have the depth of a Yakuza title for 
example. You can also impale guys on swordfish. 

Side content of favours, racing and rooster fights are pretty fun and a nice way to explore United Front's version of 
Hong Kong (which has an unmatched atmosphere when rainy and paired with the absolutely killer radio soundtrack). The 
dating side missions are hilarious because you will meet a girl, go out once and she will then disappear from your 
phone and the game, very obviously something that had to be cut during development. 

Included are also the two DLC expansions. These weren't amazingly well received when this game was new but as a pack 
in they're both fun 1-2 hour romps each. One is an MJ Thriller homage with hopping ghosts and the other is Wei back 
on beat cop duty beating down a cult.""",
    conclusion="""All in all, this is my favourite AA game which is sadly a category you don't see too much these 
    days.""",
    score=8,
    tags=[str(tag2.id)]
).save()




