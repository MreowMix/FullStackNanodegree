import media
import fresh_tomatoes

# movie data for Toy Story containing name, info, image, and trailer link
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia"
                        "/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# movie data for Avatar containing name, info, image, and trailer link
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia"
                     "/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")

# movie data for Incredibles containing name, info, image, and trailer link
incredibles = media.Movie("The Incredibles",
                          "The life of a superhero dad and his family",
                          "https://upload.wikimedia.org/wikipedia"
                          "/en/e/ec/The_Incredibles.jpg",
                          "https://www.youtube.com/watch?v=-UaGUdNJdRQ")

# movie data for Incredibles 2 containing name, info, image, and trailer link
incredibles2 = media.Movie("The Incredibles 2",
                           "A sequel and the life of a superhero mom",
                           "https://upload.wikimedia.org/wikipedia"
                           "/en/2/27/The_Incredibles_2.jpg",
                           "https://www.youtube.com/watch?v=i5qOzqD9Rms")

# movie data for Finding Nemo containing name, info, image, and trailer link
finding_nemo = media.Movie("Finding Nemo",
                           "A lost fish in a big vast ocean",
                           "https://upload.wikimedia.org/wikipedia"
                           "/en/2/29/Finding_Nemo.jpg",
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")

# movie data for Finding Dory containing name, info, image, and trailer link
finding_dory = media.Movie("Finding Dory",
                           "Another lost fish in a big vast ocean",
                           "https://upload.wikimedia.org/wikipedia"
                           "/en/3/3e/Finding_Dory.jpg",
                           "https://www.youtube.com/watch?v=0tkLUap7oGQ")

movies = [toy_story, avatar, incredibles,
          incredibles2, finding_nemo, finding_dory]

fresh_tomatoes.open_movies_page(movies)
