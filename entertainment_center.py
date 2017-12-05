import media
import fresh_tomatoes

inception = media.Movie('Inception',
                       'A dream within a dream',
                       'http://i.dailymail.co.uk/i/pix/2012/01/21/article-0-11644C10000005DC-276_634x463.jpg',
                       'https://www.youtube.com/watch?v=66TuSJo4dZM')

avengers = media.Movie('Avengers',
                     'A story of a Marine on an alien planet',
                     'https://orig00.deviantart.net/6be0/f/2011/004/6/f/__the_avengers___poster_2_by_themadbutcher-d36eop9.jpg',
                     'https://www.youtube.com/watch?v=eOrNdBpGMv8')

die_hard = media.Movie('Die Hard',
                      'The story of John Mcclain chasing down bad guys',
                      'https://images-na.ssl-images-amazon.com/images/I/51l7e1ENZvL._SY300_.jpg',
                      'http://c8.alamy.com/comp/EFAW6Y/bruce-willis-poster-die-hard-with-a-vengeance-die-hard-3-1995-EFAW6Y.jpg')

phonebooth = media.Movie('Phonebooth',
                      'The story of a guy in a phonebooth',
                      'http://www.media4.hw-static.com/wp-content/uploads/phone-booth-movie-still-movie-poster_1711570-304x400.jpeg',
                      'https://www.youtube.com/watch?v=p07lBCfC2q8')

narnia = media.Movie('The Chronicles of Narnia: The Lion, the Witch and the Wardrobe',
                     'A story of four kids who adventure in a mystical world',
                     'https://images-na.ssl-images-amazon.com/images/M/MV5BMTc0NTUwMTU5OV5BMl5BanBnXkFtZTcwNjAwNzQzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                     'https://www.youtube.com/watch?v=pYcGFLgJ8Uo')

harry_potter = media.Movie('Harry Potter and the Deathly Hallows',
                          'The start of the end',
                          'https://images-na.ssl-images-amazon.com/images/I/51lbV87oWwL._SY300_.jpg',
                          'https://www.youtube.com/watch?v=9hXH0Ackz6w')

movies = [inception,avengers,die_hard,phonebooth,narnia,harry_potter]
fresh_tomatoes.open_movies_page(movies)
