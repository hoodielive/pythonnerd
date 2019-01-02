"""
- Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, & 'q' to quit:
- Add movies
- See movies
- find movies
- stop running the program

Tasks:
[]: Decide where to store movies
[]: Show the user the main interface and get their input
[]: Allow users to add movies
[]: Show all their movies
[]: Find a movie
[]: Stop running the program when they type 'q'
"""


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, & 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print("Unknown command-please try again.")

        user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, & 'q' to quit: ")


menu()
