movies = (input("Enter a list of movies released in 2025 ="))
watched_movies = input("Enter the name of movies that you have watched =")

movies_set = set(movies.split())
watched_movies_set = set(watched_movies.split())

print(movies_set)
print(watched_movies_set)


common_movies = movies_set.intersection(watched_movies_set)
print(common_movies)

movies_not_watched = movies_set.difference(watched_movies_set)
print(movies_not_watched)

movies_set.union(watched_movies_set)
print(movies_set)