import pytest
from poke_sdk import PokeClient

@pytest.fixture
def client():
    return PokeClient()

def test_get_generation_by_id(client):
    # Test getting Generation I by ID
    gen = client.get_generation(1)
    assert gen.id == 1
    assert gen.name == "generation-i"
    assert gen.main_region.name == "kanto"
    assert len(gen.pokemon_species) > 0
    assert len(gen.types) > 0
    assert len(gen.version_groups) > 0

def test_get_generation_by_name(client):
    # Test getting Generation II by name
    gen = client.get_generation("generation-ii")
    assert gen.id == 2
    assert gen.name == "generation-ii"
    assert gen.main_region.name == "johto"
    assert len(gen.abilities) == 0  # Gen II didn't introduce new abilities
    assert len(gen.moves) > 0
    assert len(gen.names) > 0

def test_list_generations(client):
    # Test listing all generations
    collection = client.list_generations(page=0, limit=10)
    assert len(collection.results) > 0
    # There should be 9 generations as of 2024
    assert len(collection.results) <= 9
    assert collection.results[0].name is not None
    assert collection.results[0].url is not None

def test_generation_fetchable_relations(client):
    # Test that we can fetch related data using Fetchable
    gen = client.get_generation(3)
    
    # Test main_region fetchable
    region_data = gen.main_region.get_json()
    assert region_data["name"] == "hoenn"
    
    # Test moves fetchable
    if len(gen.moves) > 0:
        move_data = gen.moves[0].get_json()
        assert "name" in move_data
        assert "power" in move_data
    
    # Test types fetchable
    if len(gen.types) > 0:
        type_data = gen.types[0].get_json()
        assert "name" in type_data
        assert "damage_relations" in type_data

def test_generation_names(client):
    # Test that generation names are properly localized
    gen = client.get_generation(1)
    
    # Find English name
    english_name = next(
        (name for name in gen.names if name.language.name == "en"),
        None
    )
    assert english_name is not None
    assert english_name.name == "Generation I" 