import media
import fresh_tomatoes



toy_story = media.Movies("Toy story",
	"these story of the fictional toys",
	"http://media.comicbook.com/uploads1/2015/03/group-disney-announces-toy-story-4-is-happening-126226.jpeg",
	"https://www.youtube.com/watch?v=LJnlmJ4lqik")
print(toy_story.storyline)


christ_passion = media.Movies("Passion of The Christ",
	"how jesus the savour of man died for our sins",
	"https://upload.wikimedia.org/wikipedia/en/6/61/Thepassionposterface-1-.jpg",
	"https://www.youtube.com/watch?v=4Aif1qEB_JU")

the_wedding_party = media.Movies("The wedding party",
	"trying hard to maintain a good relationship",
	"https://www.bellanaija.com/wp-content/uploads/2016/08/Dozie-Dunni-AY-in-THE-WEDDING-PARTY-600x400.jpg",
	"https://www.youtube.com/watch?v=zbnXd-zCD6I")

The_boss_baby = media.Movies("The boss baby",
	"the story about the boss baby",
	"https://statcdn.fandango.com/MPX/image/NBCU_Fandango/87/782/thebossbaby_clip_imtheboss.jpg",
	"https://youtu.be/r8kE7rSzfQs")

logan = media.Movies("logan",
	"an epic marvel movie",
	"https://i.ytimg.com/vi/tuxtrmSjzIY/maxresdefault.jpg",
	"https://www.youtube.com/watch?v=Div0iP65aZo",)

dunkirk = media.Movies("dunkirk",
	"a war zone named dunkirk",
	"https://i2.wp.com/www.badchix.com/wp-content/uploads/2017/05/seen-on-badchix-dunkirk-official-trailer-02.jpg",
	"https://www.youtube.com/watch?v=F-eMt3SrfFU")

movies = [toy_story, christ_passion, the_wedding_party, The_boss_baby,logan,dunkirk]
fresh_tomatoes.open_movies_page(movies)
