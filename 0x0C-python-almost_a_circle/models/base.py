#!/usr/bin/python3

'''defining base model class.'''
import json
import csv
import turtle


class Base:
    '''Base model.

    This Represents the "base" for all other classes.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Initializing a new Base.

        Arguments:
            id (int): The identity of the new Base.
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Returns the JSON string representation
        of list_dictionaries
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Writes the JSON string representation
        of list_objs to a file
        '''
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        '''
        Returns the list represented by json_string
        '''
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Returns an instance with all attributes already set
        '''
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''
        Returns a list of instances from a JSON file
        '''
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
        except FileNotFoundError:
            return []

        data = cls.from_json_string(json_data)
        instances = [cls.create(**item) for item in data]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        Serializes list_objs to a CSV file
        '''
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == 'Rectangle':
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == 'Square':
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        '''
        Deserializes a CSV file into a list of instances
        '''
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    row = [int(val) for val in row]
                    if cls.__name__ == 'Rectangle':
                        instance = cls(*row[1:])
                    elif cls.__name__ == 'Square':
                        instance = cls(row[1])
                    instance.id = row[0]
                    instances.append(instance)
        except FileNotFoundError:
            return []

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''
        Opens a window and draws all the Rectangles
        and Squares using Turtle graphics module
        '''
        screen = turtle.Screen()
        screen.bgcolor("white")
        pen = turtle.Turtle()

        '''Draw rectangles'''
        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.color("red")
            pen.forward(rectangle.width)
            pen.left(90)
            pen.forward(rectangle.height)
            pen.left(90)
            pen.forward(rectangle.width)
            pen.left(90)
            pen.forward(rectangle.height)
            pen.left(90)

        '''Draw squares'''
        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("blue")
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        turtle.done()
