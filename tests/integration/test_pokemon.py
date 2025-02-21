import pytest
from poke_sdk import PokeClient

@pytest.fixture
def client():
    return PokeClient()

def test_get_pokemon_by_id(client):
    # Test getting Bulbasaur by ID
    pokemon = client.get_pokemon(1)
    assert pokemon.id == 1
    assert pokemon.name == "bulbasaur"
    assert pokemon.height == 7
    assert pokemon.weight == 69
    assert len(pokemon.abilities) > 0
    assert len(pokemon.forms) > 0

def test_get_pokemon_by_name(client):
    # Test getting Charizard by name
    pokemon = client.get_pokemon("charizard")
    assert pokemon.id == 6
    assert pokemon.name == "charizard"
    assert pokemon.height == 17
    assert pokemon.weight == 905
    assert len(pokemon.abilities) > 0
    assert len(pokemon.forms) > 0

def test_list_pokemon(client):
    # Test pagination of pokemon list
    collection = client.list_pokemon(page=1, limit=20)
    assert len(collection.results) == 20
    assert collection.results[0].name is not None
    assert collection.results[0].url is not None

def test_pokemon_forms_fetchable(client):
    # Test that we can fetch related forms
    pokemon = client.get_pokemon("mewtwo")
    assert len(pokemon.forms) > 0
    
    # Get the first form details
    form = pokemon.forms[0]
    form_details = form.get_json()
    assert form_details is not None
    assert "name" in form_details
    assert "form_name" in form_details 