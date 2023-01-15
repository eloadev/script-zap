import json


class Message:
    def define_message(self):
        with open("scriptMovies.json", encoding='utf-8') as scripts:
            json_scripts = json.load(scripts)

        for movie in json_scripts:
            print(movie['id'], ": ", movie['title'])

        option = int(input("Type the corresponding number for the movie script:  "))

        chosen_movie = None

        for movie in json_scripts:
            if movie['id'] == option:
                chosen_movie = movie
                break

        split_script = chosen_movie['script'].split("\n")

        return split_script
