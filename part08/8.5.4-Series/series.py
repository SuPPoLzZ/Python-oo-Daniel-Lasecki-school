class Series:
    def __init__(self, title, seasons, genres):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def rate(self, rating):
        if 0 <= rating <= 5:
            self.ratings.append(rating)

    def average_rating(self):
        if not self.ratings:
            return None
        return round(sum(self.ratings) / len(self.ratings), 1)

    def __str__(self):
        rating_str = f"{len(self.ratings)} ratings, average {self.average_rating()} points" if self.ratings else "no ratings"
        genres_str = ", ".join(self.genres)
        return f"{self.title} ({self.seasons} seasons)\ngenres: {genres_str}\n{rating_str}"

def minimum_grade(rating, series_list):
    return [series for series in series_list if series.average_rating() and series.average_rating() >= rating]

def includes_genre(genre, series_list):
    return [series for series in series_list if genre in series.genres]


dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
print(dexter)

dexter.rate(4)
dexter.rate(5)
dexter.rate(5)
dexter.rate(3)
dexter.rate(0)
print(dexter)

s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)

s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)

s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)

series_list = [s1, s2, s3]

print("a minimum grade of 4.5:")
for series in minimum_grade(4.5, series_list):
    print(series.title)

print("genre Comedy:")
for series in includes_genre("Comedy", series_list):
    print(series.title)
