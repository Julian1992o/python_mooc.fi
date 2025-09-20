# Write your solution here:
class Series:
    def __init__(self, title, seasons, genres):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rating_list = []
        self.avg = 0

    def calc(self):
        if len(self.rating_list) > 0:    
            self.avg = sum(self.rating_list) / len(self.rating_list)
            return self.avg

    def __str__(self):
        if len(self.rating_list) == 0:
            rating_placeholder = "no ratings"
        else:
            rating_placeholder = f"{len(self.rating_list)} ratings, average {self.calc():.1f} points"
        return f"{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\n{rating_placeholder}"
    
    def rate(self, rating: int):
        self.rating_list.append(rating)


def minimum_grade(grade: float, series: list):

    result = []
    for s in series:
        avg = s.calc()  # stellt sicher, dass avg aktuell ist
        if avg >= grade:
            result.append(s)
    return result


def includes_genre(genre: str, series_list: list):

    g = genre.strip().lower()
    return [s for s in series_list if any(g == x.lower() for x in s.genres)]


if __name__ == "__main__":

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