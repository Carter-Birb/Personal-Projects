# As a little project, I may host a github repository to allow friends to add dex entries

"""
DEXENTRIES are of the form:

region: {
    pokemon name: {
        "name": "Name",
        "type": "Type",
        "weakness": "Weakness(s)",
        "evolves" : lvl the pokemon evolves at (int)
        "description": "Pokedex description of Pokemon"
    }
}
"""

DEXENTRIES = {
    "kanto": {
        "bulbasaur": {
            "name": "Bulbasaur",
            "type": "grass/poison",
            "weakness": "fire/psychic/flying/ice",
            "evolves": 16,
            "description": "A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.",
            "number": 1
        },
        "charmander": {
            "name": "Charmander",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 16,
            "description": "Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail.",
            "number": 4
        },
        "squirtle": {
            "name": "Squirtle",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 16,
            "description": "After birth, its back swells and hardens into a shell. It powerfully sprays foam from its mouth.",
            "number": 7
        }
    },
    
    "johto": {
        "chikorita": {
            "name": "Chikorita",
            "type": "grass",
            "weakness": "fire/ice/poison/flying/bug",
            "evolves": 16,
            "description": "A sweet aroma gently wafts from the leaf on its head. It is docile and loves to soak up the sun's rays.",
            "number": 152
        },
        "cyndaquil": {
            "name": "Cyndaquil",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 14,
            "description": "It usually stays hunched over. If it is angry or surprised, it shoots flames out of its back.",
            "number": 155
        },
        "totodile": {
            "name": "Totodile",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 18,
            "description": "It is small but rough and tough. It won't hesitate to take a bite out of anything that moves.",
            "number": 158
        }
    },
    
    "hoenn": {
        "treecko": {
            "name": "Treecko",
            "type": "grass",
            "weakness": "fire/ice/poison/flying/bug",
            "evolves": 16,
            "description": "It quickly scales even vertical walls. It senses humidity with its tail to predict the next day's weather.",
            "number": 252
        },
        "torchic": {
            "name": "Torchic",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 16,
            "description": "Inside its body is a place where it keeps its flame. Give it a hug—it will be glowing with warmth.",
            "number": 255
        },
        "mudkip": {
            "name": "Mudkip",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 16,
            "description": "To alert it, the fin on its head senses the flow of water. It has the strength to hurl boulders.",
            "number": 258
        }
    },
    
    "sinnoh": {
        "turtwig": {
            "name": "Turtwig",
            "type": "grass",
            "weakness": "fire/ice/poison/flying/bug",
            "evolves": 18,
            "description": "It is weak to the cold. In the winter, the leaves on its head wilt and it becomes listless.",
            "number": 387
        },
        "chimchar": {
            "name": "Chimchar",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 14,
            "description": "It is very energetic, and its fiery tail will burn you if you try to touch it.",
            "number": 390
        },
        "piplup": {
            "name": "Piplup",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 16,
            "description": "It is highly prideful and dislikes being treated like a baby. It is a great swimmer.",
            "number": 393
        }
    },
    
    "unova": {
        "snivy": {
            "name": "Snivy",
            "type": "grass",
            "weakness": "fire/ice/poison/flying/bug",
            "evolves": 17,
            "description": "It is very proud and calm, with a demeanor as graceful as it is intelligent.",
            "number": 495
        },
        "tepig": {
            "name": "Tepig",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 17,
            "description": "It is a hot-headed Pokémon that constantly seeks to prove itself.",
            "number": 498
        },
        "oshawott": {
            "name": "Oshawott",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 17,
            "description": "It is an easygoing Pokémon, often seen playing with its water gun.",
            "number": 501
        }
    },
    
    "kalos": {
        "chespin": {
            "name": "Chespin",
            "type": "grass",
            "weakness": "fire/ice/poison/flying/bug",
            "evolves": 16,
            "description": "It is very lively and loves to eat. It is also quick to defend itself with its spiky quills.",
            "number": 650
        },
        "fennekin": {
            "name": "Fennekin",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 16,
            "description": "It has a calm and curious nature, often using its long ears to sense the environment.",
            "number": 653
        },
        "froakie": {
            "name": "Froakie",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 16,
            "description": "It is very agile and able to move silently, blending in with its surroundings.",
            "number": 656
        }
    },
    
    "alola": {
        "rowlet": {
            "name": "Rowlet",
            "type": "grass/flying",
            "weakness": "fire/ice/poison/rock",
            "evolves": 17,
            "description": "It can silently blend into its surroundings. It attacks by shooting razor-sharp leaves.",
            "number": 722
        },
        "litten": {
            "name": "Litten",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 17,
            "description": "It is a fierce and independent Pokémon. It doesn’t show much emotion but is a powerful fighter.",
            "number": 724
        },
        "popplio": {
            "name": "Popplio",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 17,
            "description": "It is a playful and graceful Pokémon, often using its water balloons to entertain itself.",
            "number": 726
        }
    },
    
    "galar": {
        "grookey": {
            "name": "Grookey",
            "type": "grass",
            "weakness": "fire/ice/poison/flying/bug",
            "evolves": 16,
            "description": "It loves to play around and can often be found tapping sticks to make rhythms.",
            "number": 810
        },
        "scorbunny": {
            "name": "Scorbunny",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 16,
            "description": "It is quick and full of energy, often seen bouncing around with excitement.",
            "number": 813
        },
        "sobble": {
            "name": "Sobble",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 16,
            "description": "It is a shy and anxious Pokémon, often hiding when it feels threatened.",
            "number": 816
        }
    },
    
    "paldea": {
        "sprigatito": {
            "name": "Sprigatito",
            "type": "grass",
            "weakness": "fire/ice/poison/flying/bug",
            "evolves": 16,
            "description": "It is a lively and curious Pokémon. It is often seen playing in the fields of Paldea.",
            "number": 906
        },
        "fuecoco": {
            "name": "Fuecoco",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 16,
            "description": "It is a laid-back Pokémon, often seen taking naps under the sun, with a fiery spirit when awake.",
            "number": 907
        },
        "quaxly": {
            "name": "Quaxly",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 16,
            "description": "It is a calm and elegant Pokémon, often gliding gracefully on the water.",
            "number": 908
        }
    },
}