










### Lab 5 Labs


#Pet info
class Pet:
    def __init__(self):
        self.name = ''
        self.age = 0

    def print_info(self):
        print(f'Pet Information:')
        print(f'   Name: {self.name}')
        print(f'   Age: {self.age}')


class Cat(Pet):
    def __init__(self):
        Pet.__init__(self)
        self.breed = ''


my_pet = Pet()
my_cat = Cat()

pet_name = input()
pet_age = int(input())
cat_name = input()
cat_age = int(input())
cat_breed = input()

# TODO: Create generic pet (using pet_name, pet_age) and then call print_info()


my_pet.name = pet_name
my_pet.age = pet_age

my_cat.name = cat_name
my_cat.age = cat_age
my_cat.breed = cat_breed

my_pet.print_info()

my_cat.print_info()

# TODO: Create cat pet (using cat_name, cat_age, cat_breed) and then call print_info()


print(f'   Breed: {my_cat.breed}')


# the "my_pet thing was really throwing me off at first, i didnt reallyy understand what they meant exactly for a good bit)


# 2 instruments

class Instrument:
    def __init__(self, name, manufacturer, year_built, cost):
        self.name = name
        self.manufacturer = manufacturer
        self.year_built = year_built
        self.cost = cost

    def print_info(self):
        print(f'Instrument Information:')
        print(f'   Name: {self.name}')
        print(f'   Manufacturer: {self.manufacturer}')
        print(f'   Year built: {self.year_built}')
        print(f'   Cost: {self.cost}')


class StringInstrument(Instrument):
    def __init__(self, name, manufacturer, year_built, cost, num_strings, num_frets, is_bowed):
        Instrument.__init__(self, name, manufacturer, year_built, cost)
        self.num_strings = num_strings
        self.num_frets = num_frets
        self.is_bowed = is_bowed
    # TODO: Define constructor with attributes:
    #       name, manufacturer, year_built, cost, num_strings, num_frets, is_bowed


if __name__ == "__main__":
    instrument_name = input()
    manufacturer_name = input()
    year_built = int(input())
    cost = int(input())
    string_instrument_name = input()
    string_manufacturer = input()
    string_year_built = int(input())
    string_cost = int(input())
    num_strings = int(input())
    num_frets = int(input())
    is_bowed = input() == 'True'

    my_instrument = Instrument(instrument_name, manufacturer_name, year_built, cost)
    my_string_instrument = StringInstrument(string_instrument_name, string_manufacturer, string_year_built, string_cost,
                                            num_strings, num_frets, is_bowed)

    my_instrument.print_info()
    my_string_instrument.print_info()

    print(f'   Number of strings: {my_string_instrument.num_strings}')
    print(f'   Number of frets: {my_string_instrument.num_frets}')
    print(f'   Is bowed: {my_string_instrument.is_bowed}')



# lab 3

class Course:
    def __init__(self, course_number, course_title):
        self.number = course_number
        self.title = course_title

    def print_info(self):
        print(f'Course Information:\n   Course Number: {self.number}\n   Course Title: {self.title}')
    # TODO: Define constructor with attributes

    # TODO: Define print_info()


class OfferedCourse(Course):
    def __init__(self, course_number, course_title, instructor_name, location, class_time):
        Course.__init__(self, course_number, course_title)
        self.instructor_name = instructor_name
        self.location = location
        self.class_time = class_time
    # TODO: Define constructor with attributes


if __name__ == "__main__":
    course_number = input()
    course_title = input()

    o_course_number = input()
    o_course_title = input()
    instructor_name = input()
    location = input()
    class_time = input()

    my_course = Course(course_number, course_title)
    my_course.print_info()

    my_offered_course = OfferedCourse(o_course_number, o_course_title, instructor_name, location, class_time)
    my_offered_course.print_info()

    print(f'   Instructor Name: {my_offered_course.instructor_name}')
    print(f'   Location: {my_offered_course.location}')
    print(f'   Class Time: {my_offered_course.class_time}')

    # I always have small syntax errors because of missed ) or (


class Book:
    def __init__(self, title, author, publisher, publication_date):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date

    def print_info(self):
        print('Book Information:')
        print(f'   Book Title: {self.title}')
        print(f'   Author: {self.author}')
        print(f'   Publisher: {self.publisher}')
        print(f'   Publication Date: {self.publication_date}')


class Encyclopedia(Book):
    def __init__(self, title, author, publisher, publication_date, edition, num_pages):
        Book.__init__(self, title, author, publisher, publication_date)
        self.edition = edition
        self.num_pages = num_pages

    def print_info(self):
        Book.print_info(self)
        print(f'   Edition: {self.edition}\n   Number of Pages: {self.num_pages}')
    # TODO: Define constructor with attributes:
    #       title, author, publisher, publication_date, edition, num_pages

    # TODO: Define a print_info() method that overrides the print_info()
    #       in the Book class



#lab 4
if __name__ == "__main__":
    title = input()
    author = input()
    publisher = input()
    publication_date = input()

    e_title = input()
    e_author = input()
    e_publisher = input()
    e_publication_date = input()
    edition = input()
    num_pages = int(input())

    my_book = Book(title, author, publisher, publication_date)
    my_book.print_info()

    my_encyclopedia = Encyclopedia(e_title, e_author, e_publisher, e_publication_date, edition, num_pages)
    my_encyclopedia.print_info()


# this was pretty similar to 3


# lab 5


class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self):
        print(f'   Plant name: {self.plant_name}')
        print(f'   Cost: {self.plant_cost}')


class Flower(Plant):
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        Plant.__init__(self, plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        print(f'   Plant name: {self.plant_name}')
        print(f'   Cost: {self.plant_cost}')
        print(f'   Annual: {self.is_annual}')
        print(f'   Color of flowers: {self.color_of_flowers}')


# TODO:  Define the print_list() function that prints a list of plant (or flower) objects

def print_list(garden):
    for i in range(len(garden)):
        print(f'Plant {i + 1} Information:')
        garden[i].print_info()
        print()


if __name__ == "__main__":
    my_garden = []

    user_string = input()

    while user_string != '-1':
        tokens = user_string.split()
        plant_type = tokens[0]
        plant_name = tokens[1]
        plant_cost = tokens[2]
        if plant_type == 'plant':
            my_plant = Plant(plant_name, plant_cost)
            my_garden.append(my_plant)
        elif plant_type == 'flower':
            is_annual = tokens[3]
            color_of_flowers = tokens[4]
            my_flower = Flower(plant_name, plant_cost, is_annual, color_of_flowers)
            my_garden.append(my_flower)
        user_string = input()

    print_list(my_garden)

#lab 5 i followed along in class when it was shown as an example