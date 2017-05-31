import media
import fresh_tomatoes

movies = [
    media.Movie("Toy Story",
                "A story of a boy and his toys, who come to life",
                "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                "https://www.youtube.com/watch?v=KYz2wyBy3kc"),

    media.Movie("Avatar",
                "A marine on an alien planet",
                "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                "https://www.youtube.com/watch?v=5PSNL1qE6VY"),

    media.Movie("Moana",
                "A girl sets off on an adventure to save her people",
                "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
                "https://www.youtube.com/watch?v=LKFuXETZUsI"),

    media.Movie("Deadpool",
                "A fast-talking mercenary undergoes an experiment that give him super powers",
                "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_SY1000_SX686_AL_.jpg",
                "http://www.youtube.com/watch?v=gtTfd6tISfw"),

    media.Movie("The Dark Tower(Upcoming)",
                "The gunslinger pursues the man in black and the dark tower in order to save the world",
                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU3MjUwMzQ3MF5BMl5BanBnXkFtZTgwMjcwNjkxMjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                "https://www.youtube.com/watch?v=GjwfqXTebIY")
]

fresh_tomatoes.open_movies_page(movies)
