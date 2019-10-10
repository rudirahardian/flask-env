from model.PlantsModel import PlantsModel
from app import db

class PlantsRepository(PlantsModel):
    def __init__(self):
        pass

    def addPlants(self, name, category):
        data = PlantsModel(name, category)
        db.session.add(data)
        db.session.commit()
        print(data.id)
        return data

    def updatePlants(self, x, name, category):
        plants = PlantsModel.query.filter_by(id=x).first()
        plants.name = name
        plants.category = category
        db.session.commit()

    def deletePlants(self, x):
        PlantsModel.query.filter_by(id=x).delete()
        db.session.commit()