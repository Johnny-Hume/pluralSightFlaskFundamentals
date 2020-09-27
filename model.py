import json


def load_db():
    with open("flashcards_db.json") as f:
        return json.load(f)


def save_db():
    with open("flashcards_db.json", "w") as f:
        return json.dump(db, f)


def remove_element(question):
    load_db()
    for element in db:
        element.pop(question, None)
    save_db()


db = load_db()
