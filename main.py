import json


class DogDB:
    def __init__(self):
        self.dogs = []
        with open("dogs.json") as f:
            self.dogs = json.load(f)

    def get_dogs(self):
        with open("dogs.json") as f:
            self.dogs = json.load(f)
        return self.dogs

    def get_dog(self, dog_id):
        with open("dogs.json") as f:
            self.dogs = json.load(f)
        for dog in self.dogs:
            if dog["id"] == dog_id:
                return dog
        return {}

    def add_dog(self, dog):
        self.dogs.append(dog)
        with open("dogs.json", "w") as f:
            json.dump(self.dogs, f)
        return self.get_dogs()

    def update_dog(self, dog_id, dog):
        with open("dogs.json") as f:
            self.dogs = json.load(f)
        for i in range(len(self.dogs)):
            if self.dogs[i]["id"] == dog_id:
                self.dogs[i] = dog
                with open("dogs.json", "w") as f:
                    json.dump(self.dogs, f)
                return self.get_dog(dog_id)
        return {}

    def delete_dog(self, dog_id):
        for i in range(len(self.dogs)):
            if self.dogs[i]["id"] == dog_id:
                del self.dogs[i]
                with open("dogs.json", "w") as f:
                    json.dump(self.dogs, f)
                return self.get_dogs()
        return {}

    def get_dog_by_size(self, size):
        with open("dogs.json") as f:
            self.dogs = json.load(f)
        dogs = []
        for dog in self.dogs:
            if dog["size"] == size:
                dogs.append(dog)
        return dogs

db = DogDB()
