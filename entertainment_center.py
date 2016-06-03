import media
import fresh_tomatoes
baahubali = media.Movie("Baahubali","Indian epic historical fiction film directed by S. S. Rajamouli",
                        "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",
                        "https://www.youtube.com/watch?v=3NQRhE772b0")

twentyfour = media.Movie("24","Indian Science fiction action adventure film written and directed by Vikram Kumar",
                         "https://upload.wikimedia.org/wikipedia/en/7/79/24_%282016_film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=X2eQqOAiEok")

kabali = media.Movie("Kabali","Rajinikanth super star mafia background",
                     "https://upload.wikimedia.org/wikipedia/en/9/9e/Rajinikanth_in_Kabali.jpg",
                     "https://www.youtube.com/watch?v=9mdJV5-eias")

racegurram = media.Movie("Race Gurram","Story between two brothers ",
                         "https://upload.wikimedia.org/wikipedia/en/8/8a/Race_Gurram_poster.jpg",
                         "https://www.youtube.com/watch?v=nda6eGtu8DI")

ipman = media.Movie("Ip Man","Real life story of Ip man",
                        "https://upload.wikimedia.org/wikipedia/en/2/2f/Ipmanposter02.jpg",
                        "https://www.youtube.com/watch?v=nhz4Jl6nf58")

nani = media.Movie("Nani Gentleman","Nani playing two different shades ",
                   "https://upload.wikimedia.org/wikipedia/commons/6/6a/Gentle_man.jpg",
                   "https://www.youtube.com/watch?v=E7lAZhIBOlU")

xmen = media.Movie("X-Men","Super hero movie",
                    "https://upload.wikimedia.org/wikipedia/en/8/8c/XMen1poster.jpg",
                    "https://www.youtube.com/watch?v=Jer8XjMrUB4")

aagadu = media.Movie("Aagadu","UnStoppable Cop story ",
                     "https://upload.wikimedia.org/wikipedia/en/f/fc/Aagadu_poster.jpg",
                     "https://www.youtube.com/watch?v=r1Ct9zYinPw&feature=player_embedded")



movies = [baahubali, twentyfour, kabali, racegurram, ipman, nani, xmen, aagadu]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
