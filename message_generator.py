import json


class Message:
    def define_message(self):
        with open("scriptMovies.json", encoding='utf-8') as scripts:
            data = json.load(scripts)

        for x in data:
            print(x['id'], ": ", x['title'])

        option = int(input("Type the corresponding number for the movie script:  "))

        script = None

        for y in data:
            if y['id'] == option:
                script = y
                break

        return script

