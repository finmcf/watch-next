# import the spacy module

import spacy

# en_core_web_md model with spacy and define as nlp

nlp = spacy.load('en_core_web_md')

# open the movies text file in read mode

with open("movies.txt", "r") as movies:

    # define a variable that stores a string of the description of planet hulk

    planet_hulk = """Will he save their world or destroy it? When the
     Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk
      into a shuttle and launch him into space to a planet where the Hulk
       can live in peace. Unfortunately, Hulk land on the planet Sakaar 
       where he is sold into slavery and trained as a gladiator."""

    # initialise the highest similarity to initially be 0

    highest_similarity = 0

    # initialise the next movie to initially be an empty string

    next_movie = ""

    # initialise a list storing each movie description from the movies text file, each line on the movies text file is
    # store as a seperate string in the list

    movies_descriptions = movies.read().splitlines()

    # loop through each movie description

    for movie_description in movies_descriptions:

        # calculate the similarity between the planet_hulk string and the description of each (removing the movie number letter
        # beforehand)

        similarity = nlp(planet_hulk).similarity(nlp(movie_description[9:]))

        # if similarity is higher than the current highest similarity

        if similarity > highest_similarity:

            # set highest_similarity to this similarity value

            highest_similarity = similarity

            # and also set next movie to the movie which gave this higher similarity value

            next_movie = movie_description

    # print the next movie which will be the one with the greatest similarity

    print(f"This next movie is {next_movie}")

    # close the movies text file

    movies.close()
