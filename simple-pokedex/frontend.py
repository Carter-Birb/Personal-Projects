##########################################
# Carter Landry
# 2/24/25
# This is a Flask Project that uses pokedex entries as endpoints.
##########################################


from time import sleep
import requests
import backend

class Pokedex:

    IP_ADDR = "127.0.0.1"
    API_URL = f"http://{IP_ADDR}:8000"

    def __init__(self):
        self.availableregions = self.availableregions()
        self.currentregion = None
        self.currentpokemon = None


    def availableregions(self) -> dict:
        """
        accesses the regions that are available.
        contains: regions
        returns a dictionary.
        """
        regionsdata = requests.get(url=f"{Pokedex.API_URL}/listregions")
        regionsdata_ = regionsdata.json()
        return regionsdata_
    
    def accessregion(self, region:str) -> dict:
        """
        accesses the data contained within a region.
        contains: pokemon
        returns a dictionary.
        """
        regiondata = requests.get(url=f"{Pokedex.API_URL}/{region}")
        regiondata_ = regiondata.json()
        return regiondata_
    
    def accesspokemon(self, region:str, pokemon:str) -> dict:
        """
        accesses the data contained within a pokemon.
        contains: pokemon info
        returns a dictionary.
        """
        pokemondata = requests.get(url=f"{Pokedex.API_URL}/{region}/{pokemon}")
        pokemondata_ = pokemondata.json()
        return pokemondata_
    
    def accessdata(self, region:str, pokemon:str, datatype:str) -> str:
        """
        accesses the datatype specified by the user.
        contains: str linked to datatype
        returns a string.
        """
        dexdata = requests.get(url=f"{Pokedex.API_URL}/{region}/{pokemon}/{datatype}")
        dexdata_ = dexdata.json()
        return dexdata_
    
    
    def regiondir(self, userinput:str) -> dict:
        """
        marks the user's current region location.
        """
        self.currentregion = userinput
    
    def pokemondir(self, userinput:str) -> dict:
        """
        marks the user's current pokemon location.
        """
        self.currentpokemon = userinput
    
    
    def startdex(self):
        """
        begins the Pokedex.
        This is only run once when the program starts.
        """
        print("Welcome to The Pokedex!")
        sleep(0.5)
        print("Valid commands are: \"<region>\" \"regions\" \"<pokemon>\" \"pokemon\" \"<data>\" \"back\" \"help\" \"quit\"")
        sleep(0.5)
        print("The regions this Pokedex support are:")
        sleep(0.5)
        print(", ".join(self.availableregions.keys()))
        sleep(0.5)
        print("Which region would you like to explore?")
        self.runPokedex()
    
    def displayhelp(self):
        """
        Displays a list of the available commands.
        """
        print("Valid commands are: \"<region>\" \"regions\" \"<pokemon>\" \"pokemon\" \"<data>\" \"data\" \"back\" \"help\" \"quit\"")
        sleep(0.5)
    
    def displayregions(self):
        """
        Displays the regions available.
        """
        print("The regions this Pokedex support are:")
        sleep(0.5)
        print(", ".join(self.availableregions.keys()))
        sleep(0.5)
    
    def displaypokemon(self, region:str):
        """
        Displays the pokemon available.
        """
        print(f"The Pokemon currently in the {region.title()} region are:")
        sleep(0.5)
        print(", ".join(self.accessregion(region).keys()))
        sleep(0.5)
    
    def displaydata(self):
        """
        Displays the data available.
        """
        print(f"The current data available for {self.currentpokemon} is:")
        sleep(0.5)
        print(", ".join(self.accesspokemon(self.currentregion, self.currentpokemon).keys()))
        sleep(0.5)
    
    def quit(self):
        print("Now exiting the Pokedex... Goodbye!")
        sleep(1)
        exit()
    
    def enterregion(self, userinput):
        """
        Executed when the user enters the region level of the program.
        """
        self.regiondir(userinput)
        region = self.accessregion(userinput)
        print(f"Now entering the {userinput.title()} region!")
        sleep(0.5)
        print(f"The Pokemon currently in this region are:")
        sleep(0.5)
        print(", ".join(region.keys()))
        sleep(0.5)
        print("Which Pokemon would you like to know more about?")
    
    def enterpokemondata(self, userinput):
        """
        Executed when the user enters the pokemondata level of the program.
        """
        self.pokemondir(userinput)
        pokemon = self.accesspokemon(self.currentregion, userinput)
        print(f"Getting data for {userinput}...")
        sleep(0.5)
        print(f"The current data available for {self.currentpokemon} is:")
        sleep(0.5)
        print(", ".join(pokemon.keys()))
        sleep(0.5)
        print(f"What would you like to know about {self.currentpokemon}?")
    
    def runPokedex(self):
        """
        runs the Pokedex
        """
        # Everything below this while True loop is contained within the / (home) directory
        while True:
            userinput = input("").lower().strip()
            
            if userinput == "back":
                print("That command cannot be executed at this time!")
                sleep(0.5)
            
            elif userinput == "quit":
                self.quit()
            
            elif userinput == "help":
                self.displayhelp()
            
            elif userinput == "regions":
                self.displayregions()
            
            elif userinput == "pokemon":
                print("Please enter a region first!")
                sleep(0.5)
            
            elif userinput == "data":
                print("Please enter a region first!")
                sleep(0.5)
            
            elif userinput in self.availableregions:
                self.enterregion(userinput)


                # Everything below this while True loop is contained within the /<region> directory
                while True:
                    userinput = input("").lower().strip()
                    
                    if userinput == "back":
                        self.currentregion = None
                        break
                    
                    elif userinput == "quit":
                        self.quit()
                    
                    elif userinput == "help":
                        self.displayhelp()
                    
                    elif userinput == "regions":
                        self.displayregions()
                    
                    elif userinput == "pokemon":
                        self.displaypokemon(self.currentregion)
                    
                    elif userinput == "data":
                        print("Please select a Pokemon first!")
                        sleep(0.5)
                    
                    elif self.currentregion and userinput in self.availableregions[self.currentregion]:
                        self.enterpokemondata(userinput)


                        # Everything below this while True loop is contained within the /<region>/<pokemon> directory
                        while True:
                            userinput = input("").lower().strip()
                            
                            if userinput == "back":
                                self.currentpokemon = None
                                break
                            
                            elif userinput == "quit":
                                self.quit()
                            
                            elif userinput == "help":
                                self.displayhelp()
                            
                            elif userinput == "regions":
                                self.displayregions()
                            
                            elif userinput == "pokemon":
                                self.displaypokemon(self.currentregion)
                            
                            elif userinput == "data":
                                self.displaydata()
                            
                            elif userinput == "name" and userinput in self.accesspokemon(self.currentregion, self.currentpokemon):
                                print("Fetching name...")
                                sleep(0.5)
                                print(f"{self.currentpokemon}'s name is {self.accessdata(self.currentregion, self.currentpokemon, userinput)}")
                                sleep(0.5)
                                print(f"What else would you like to know about {self.currentpokemon}?")
                            
                            elif userinput == "type" and userinput in self.accesspokemon(self.currentregion, self.currentpokemon):
                                print("Fetching type...")
                                sleep(0.5)
                                print(f"{self.currentpokemon}'s type is {self.accessdata(self.currentregion, self.currentpokemon, userinput)}")
                                sleep(0.5)
                                print(f"What else would you like to know about {self.currentpokemon}?")
                            
                            elif userinput == "weakness" and userinput in self.accesspokemon(self.currentregion, self.currentpokemon):
                                print("Fetching weakness...")
                                sleep(0.5)
                                print(f"{self.currentpokemon}'s weakness is {self.accessdata(self.currentregion, self.currentpokemon, userinput)}")
                                sleep(0.5)
                                print(f"What else would you like to know about {self.currentpokemon}?")
                            
                            elif userinput == "evolves" and userinput in self.accesspokemon(self.currentregion, self.currentpokemon):
                                print("Fetching evolution level...")
                                sleep(0.5)
                                print(f"{self.currentpokemon} evolves at level {self.accessdata(self.currentregion, self.currentpokemon, userinput)}")
                                sleep(0.5)
                                print(f"What else would you like to know about {self.currentpokemon}?")
                            
                            elif userinput == "description" and userinput in self.accesspokemon(self.currentregion, self.currentpokemon):
                                print("Fetching description...")
                                sleep(0.5)
                                print(self.accessdata(self.currentregion, self.currentpokemon, userinput))
                                sleep(0.5)
                                print(f"What else would you like to know about {self.currentpokemon}?")
                            
                            elif userinput == "number" and userinput in self.accesspokemon(self.currentregion, self.currentpokemon):
                                print("Fetching pokedex number...")
                                sleep(0.5)
                                print(f"{self.currentpokemon.title()}'s pokedex number is #{self.accessdata(self.currentregion, self.currentpokemon, userinput)}")
                                sleep(0.5)
                                print(f"What else would you like to know about {self.currentpokemon}?")


                            else:
                                print("The Pokedex does not contain that data!")


                    else:
                        print("That Pokemon is not in this Pokedex/region!")
                        sleep(0.5)

                    print("Which Pokemon would you like to know more about?")


            print("Which region would you like to explore?")



if __name__ == "__main__":
    p = Pokedex()
    p.startdex()