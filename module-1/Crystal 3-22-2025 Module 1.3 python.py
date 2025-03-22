def beer_wall_song():
    # Step 1: User input for the number of bottles
    N = int(input("Enter the number of bottles: "))

    # Step 2: Countdown loop around the song
    while N > 1:
        print(f"{N} bottles of beer on the wall, {N} bottles of beer.")
        print("Take one down, pass it around,")
        N -= 1  # Decrement the bottle count
        print(f"{N} bottles of beer on the wall.\n")

    # Step 3: When only 1 bottle remains
    if N == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("User buys more beer.")

    # Step 4: End program
    print("End of the song!")

# Run the program
beer_wall_song()