import fresh_tomatoes
import media

# JUMANJI 2 Movie Title, Story lime, Poster Image and Youtube Trailer URL
jumanji_2 = media.Movie(
    "Jumanji 2",
    "JUMANJI 2 - Welcome to the Jungle Trailer",
    "https://upload.wikimedia.org/wikipedia/en/d/dc/Jumanji_Welcome_to_the_Jungle.png",
    "https://www.youtube.com/watch?v=sAWTZVpvPrQ")

# Spiderman Homecoming Movie Title, Story lime, Poster Image and Trailer URL
spiderman_homecoming = media.Movie(
    "Spider-Man Homecoming",
    "Spider Man Homecoming 2017 Trailer!",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
    "https://www.youtube.com/watch?v=DiTECkLZ8HM")

# Dhruva Natchathiram Movie Title, Story lime, Poster Image and Trailer URL
dhruva_natchathiram = media.Movie(
    "Dhruva Natchathiram",
    "The thriller movie by stylish making of Gowtham Menon and Vikram",
    "https://upload.wikimedia.org/wikipedia/en/2/20/Dhruva_Natchathiram_poster.jpg",
    "https://www.youtube.com/watch?v=Jfyjx2rOQWk&t=7s")

# Baahubali 2  Movie Title, Story lime, Poster Image and Trailer URL
baahubali2 = media.Movie(
    "Baahubali 2",
    "Baahubali 2 - The Conculsion ",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
    "https://www.youtube.com/watch?v=G62HrubdD6o")

# Making of 2.0 Movie Title, Story lime, Poster Image and Youtube Trailer URL
making_of_2_0 = media.Movie(
    "Making of 2.0 ",
    "Making of 2.0 - The much expected Rajinikanth Movie Making Video",
    "https://upload.wikimedia.org/wikipedia/en/9/9a/2.0_%28film%29.jpg",
    "https://www.youtube.com/watch?v=nZVno-TGeFI")

# Spider Movie Title, Story lime, Poster Image and Youtube Trailer URL
spider = media.Movie(
    "SPIDER",
    "Spider - The Most expected Tamil and Telugu Bilingual movie",
    "https://upload.wikimedia.org/wikipedia/en/d/de/Spyder_film_poster.jpg",
    "https://www.youtube.com/watch?v=Rt-GWQuys4k")

# Build website - set of movies that passed to media.py file
movies = [
    jumanji_2,
    spiderman_homecoming,
    dhruva_natchathiram,
    baahubali2,
    making_of_2_0,
    spider
    ]

# File creation(fresh_tomatoes.html) and view through browser by fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
