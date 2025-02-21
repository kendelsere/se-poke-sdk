from poke_sdk import PokeClient

def main():
    # Create a Pokemon instance
    pokemon_client = PokeClient()
    
    # Get Pikachu by ID (25)
    pikachu = pokemon_client.get_pokemon(25)
    
    print(f"\nPokemon Information:")
    print(f"Name: {pikachu.name.title()}")
    print(f"ID: {pikachu.id}")
    print(f"Height: {pikachu.height} decimetres")
    print(f"Weight: {pikachu.weight} hectograms")
    print(f"Types: {', '.join(t['type']['name'] for t in pikachu.types)}")
    print(f"Base Experience: {pikachu.base_experience}")
    
    # Example of listing Pokemon (paginated)
    print("\nFirst page of Pokemon (limit 5):")
    pokemon_list = pokemon_client.list_pokemon(page=1, limit=5)
    for pokemon in pokemon_list.results:
        print(f"- {pokemon.name}")
    # List generations
    print("\nFirst page of Generations (limit 5):")
    gen_list = pokemon_client.list_generations(page=1, limit=5)
    for gen in gen_list.results:
        print(f"- {gen.name}")

    # Get specific generation
    gen1 = pokemon_client.get_generation(1)
    print("\nGeneration Information:")
    print(f"Name: {gen1.name}")
    print(f"Region: {gen1.main_region.name}")

    

if __name__ == "__main__":
    main()
