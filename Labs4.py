# Lab 4 Labs
# 150 we covered classes for a long time and I am currently in a data science course at william and mary
# we use classes heavily i didnt have too much trouble within VSC

#Lab 1
class FoodItem:
    def __init__(self, name="Water", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print(f'Nutritional information per serving of {self.name}:')
        print(f'  Fat: {self.fat:.2f} g')
        print(f'  Carbohydrates: {self.carbs:.2f} g')
        print(f'  Protein: {self.protein:.2f} g')


if __name__ == "__main__":

    item_name = input()
    if item_name == 'Water' or item_name == 'water':
        food_item = FoodItem()
        food_item.print_info()
        print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')

    else:
        amount_fat = float(input())
        amount_carbs = float(input())
        amount_protein = float(input())
        num_servings = float(input())

        food_item = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
        food_item.print_info()
        print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')
        print(f'Number of calories for {num_servings:.2f} serving(s): {food_item.get_calories(num_servings):.2f}')


#Lab 2

class Artist:
    def __init__(self, name="unknown", birth_year=-1, death_year=-1):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    def print_info(self):
        if self.birth_year >= 0 and self.death_year >= 0:
            print(f'Artist: {self.name} ({self.birth_year} to {self.death_year})')
        elif self.birth_year >= 0 and self.death_year < 0:
            print(f'Artist: {self.name} ({self.birth_year} to present)')
        else:
            print(f'Artist: {self.name} (unknown)')


class Artwork:
    def __init__(self, title="unknown", year_created=-1, artist=Artist()):
        self.title = title
        self.year_created = year_created
        self.artist = artist

    def print_info(self):
        self.artist.print_info()
        print(f'Title: {self.title}, {self.year_created}')


if __name__ == "__main__":
    user_artist_name = input()
    user_birth_year = int(input())
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)

    new_artwork.print_info()



#Lab 3


class Triangle:
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height

    def get_area(self):
        area = 0.5 * self.base * self.height
        return area

    def print_info(self):
        print(f'Base: {self.base:.2f}')
        print(f'Height: {self.height:.2f}')
        print(f'Area: {self.get_area():.2f}')


if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()

    triangle1.set_base(float(input()))
    triangle1.set_height(float(input()))

    triangle2.set_base(float(input()))
    triangle2.set_height(float(input()))

    print('Triangle with smaller area:')

    if triangle1.get_area() < triangle2.get_area():
        triangle1.print_info()
    else:
        triangle2.print_info()



#Lab 4

class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    def get_win_percentage(self):
        return self.wins / (self.wins + self.losses)

    def print_standing(self):
        win_percentage = self.get_win_percentage()
        print(f'Win percentage: {win_percentage:.2f}')

        if win_percentage >= 0.5:
            print(f'Congratulations, Team {self.name} has a winning average!')
        else:
            print(f'Team {self.name} has a losing average.')

    # TODO: Define get_win_percentage()

    # TODO: Define print_standing()


if __name__ == "__main__":
    team = Team()

    user_name = input()
    user_wins = int(input())
    user_losses = int(input())

    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses

    team.print_standing()


# All these i had within VSC and i just have sent them over

