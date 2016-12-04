import media
import fresh_tomatoes

# class instantiating section:
shawshank = media.Movie("The Shawshank Redemption",
"Two imprisoned men bond over a number of years, finding
"solace and eventual "
"redemption through acts of common decency.",
# noqa
"https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_QL50_SY1000_CR0,0,672,1000_AL_.jpg",
# noqa
"https://www.youtube.com/watch?v=6hB3S9bIaco")

transporter = media.Movie("The Transporter",
"An ex-soldier turned mercenary 'transporter' moves goods, "
"human or otherwise, from one place to another. "
"Complications arise when a job "
"goes astray and he has to save the life of his female cargo.",
# noqa
"http://www.gstatic.com/tv/thumb/movieposters/30543/p30543_p_v8_af.jpg",
# noqa
"https://www.youtube.com/watch?v=0poXFSvX0_4")

bourne = media.Movie("Jason Bourne",
"The next chapter of Universal Pictures' Bourne franchise, "
"which finds the CIA's most lethal former operative "
"drawn out of the shadows.",
# noqa
"http://t3.gstatic.com/images?q=tbn:ANd9GcQ27a64TqUZLOU1QbJiBPhu4mBZMW50wFzR62ob5W9o9Mgx7blK",
# noqa
"https://www.youtube.com/watch?v=v71ce1Dqqns")

# appending movies into a list:
movies = [shawshank,transporter,bourne]

# calling the external rendering function:
fresh_tomatoes.open_movies_page(movies)
