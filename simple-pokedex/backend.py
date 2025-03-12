##########################################
# Carter Landry
# 2/24/25
# This is a Flask Project that uses pokedex entries as endpoints.
##########################################


from flask import Flask, jsonify, request
from pokedexentries import DEXENTRIES

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"success": True, "me": "Carter"})


# Returns the regions contained within opkedexentries.py. This will update dynamically as regions are added
@app.route("/listregions", methods=["GET"])
def pokedexlist():
    """
    returns the regions currently supported by the Pokedex.
    """
    return jsonify(DEXENTRIES)


# This creates a dynamic endpoint system that will update with regions added to the DEXENTRIES dictionary.
@app.route("/<region>", methods=["GET"])
def getregion(region:str):
    """
    returns the region.
    """
    if region in DEXENTRIES:
        return jsonify(DEXENTRIES[region])


# This creates a dynamic endpoint system that will update the regions and pokemon as they are added to DEXENTIRES
@app.route("/<region>/<pokemon>", methods=["GET"])
def getpokemon(region:str, pokemon:str):
    """
    returns the pokemon contained within a region.
    """
    return jsonify(DEXENTRIES[region][pokemon])


# This creates an endpoint directed to a pokemon's name
@app.route("/<region>/<pokemon>/name", methods=["GET"])
def getname(region, pokemon):
    """
    returns the name of a Pokemon
    """
    return jsonify(DEXENTRIES[region][pokemon]['name'])


# This creates an endpoint directed to a pokemon's type
@app.route("/<region>/<pokemon>/type", methods=["GET"])
def gettype(region, pokemon):
    """
    returns the Pokemon's type
    """
    return jsonify(DEXENTRIES[region][pokemon]['type'])


# This creates an endpoint directed to a pokemon's weakness
@app.route("/<region>/<pokemon>/weakness", methods=["GET"])
def getweakness(region, pokemon):
    """
    returns the Pokemon's weakness
    """
    return jsonify(DEXENTRIES[region][pokemon]['weakness'])


# This creates an endpoint directed to a pokemon's evolution level
@app.route("/<region>/<pokemon>/evolves", methods=["GET"])
def getevolves(region, pokemon):
    """
    returns the level at which a Pokemon will evolve
    """
    return jsonify(DEXENTRIES[region][pokemon]['evolves'])


# This creates an endpoint directed to a pokemon's description
@app.route("/<region>/<pokemon>/description", methods=["GET"])
def getdescription(region, pokemon):
    """
    returns the description of a pokemon
    """
    return jsonify(DEXENTRIES[region][pokemon]['description'])


# This creates an endpoint directed to a pokemon's pokedex number
@app.route("/<region>/<pokemon>/number", methods=["GET"])
def getnumber(region, pokemon):
    """
    returns the pokemon's pokedex number
    """
    return jsonify(DEXENTRIES[region][pokemon]['number'])



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8000")