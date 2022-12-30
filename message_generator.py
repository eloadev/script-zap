import json


class Message:
    def define_message(self):
        with open("scriptMovies.json", encoding='utf-8') as scripts:
            data = json.load(scripts)

        for x in data:
            print(x['id'], ": ", x['title'])

        option = int(input("Type the corresponding number for the movie script:  "))

        movie = None

        for y in data:
            if y['id'] == option:
                movie = y
                break

        split_script = movie['script'].split("\n")

        return split_script
