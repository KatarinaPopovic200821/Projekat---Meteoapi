"""Functions handling API endpoints."""

import database
import models




def getMeasurements():
    measurements = models.Measurement.query.all()
    measurements = map(lambda m: m.to_dict(), measurements)
    return list(measurements)


def createMeasurement(body):
    measurement = models.Measurement.from_dict(**body)
    database.db.session.add(measurement)
    database.db.session.commit()
    return measurement.to_dict()


def getMeasurementById(id):
    measurement = models.Measurement.query.filter_by(id=id).first()
    if measurement is None:
        return ("Measurement not found.", 404)
    return measurement.to_dict()


def updateMeasurementById(body, id):
    measurement = models.Measurement.query.filter_by(id=id).first()
    if measurement is None:
        return ("Measurement not found.", 404)
    measurement.lat = body["lat"]
    measurement.long = body["long"]
    measurement.lat = body["lat"]
    measurement.time = body["time"]
    measurement.variable = body["variable"]
    measurement.value = body["value"]
    database.db.session.commit()
    return 200


def removeMeasurementById(id):
    measurement = models.Measurement.query.filter_by(id=id).delete()
    if measurement is None:
        return ("Measurement not found.", 404)
    database.db.session.commit()
    return 200



def getLocations():
    locations = models.Location.query.all()
    locations = map(lambda m: m.to_dict(), locations)
    return list(locations)


def createLocation(body):
    location = models.Location.from_dict(**body)
    database.db.session.add(location)
    database.db.session.commit()
    return location.to_dict()

def getLocationById(id):
    location = models.Location.query.filter_by(id=id).first()
    if location is None:
        return ("Location not found.", 404)
    return location.to_dict()


def updateLocationById(body, id):
    location = models.Location.query.filter_by(id=id).first()
    if location is None:
        return ("Location not found.", 404)
    location.lat = body["lat"]
    location.long = body["long"]
    location.name = body["name"]
    location.country = body["country"]
    location.type = body["type"]
    location.altitude = body["altitude"]
    database.db.session.commit()
    return 200


def removeLocationById(id):
    location = models.Location.query.filter_by(id=id).delete()
    if location is None:
        return ("Location not found.", 404)
    database.db.session.commit()
    return 200

def getWeatherStations():
    weatherstation = models.WeatherStation.query.all()
    weatherstation = map(lambda n: n.to_dict(), weatherstation)
    return list(weatherstation)


def createWeatherStation(body):
    weatherstation = models.WeatherStation.from_dict(**body)
    database.db.session.add(weatherstation)
    database.db.session.commit()
    return weatherstation.to_dict()

def getWeatherStationById(id):
    weatherstation = models.WeatherStation.query.filter_by(id=id).first()
    if weatherstation is None:
        return ("Source not found.", 404)
    return weatherstation.to_dict()

def updateWeatherStationById(body, id):
    weatherstation = models.WeatherStation.query.filter_by(id=id).first()
    if weatherstation is None:
        return ("weatherstation not found.", 404)
    weatherstation.name = body["name"]
    weatherstation.id= body["location_id"]
    weatherstation.type= body["type"]
    weatherstation.capacity = body["capacity"]
    weatherstation.installation_date = body["installation_date"]
    weatherstation.last_maintenance_date = body["last_maintenance_date"]
    weatherstation.status = body["status"]
    weatherstation.operator = body["operator"]

    database.db.session.commit()
    return 200

def deleteWeatherStationById(id):
    weatherstation = models.WeatherStation.query.filter_by(id=id).delete()
    if not weatherstation:
        return ("weatherstation not found.", 404)
    database.db.session.commit()
    return 200




def getSources():
    source = models.Source.query.all()
    source = map(lambda n: n.to_dict(), source)
    return list(source)


def createSource(body):
    source = models.Source.from_dict(**body)
    database.db.session.add(source)
    database.db.session.commit()
    return source.to_dict()

def getSourceById(id):
    source = models.Source.query.filter_by(id=id).first()
    if source is None:
        return ("Source not found.", 404)
    return source.to_dict()

def updateSourceById(body, id):
    source = models.Source.query.filter_by(id=id).first()
    if source is None:
        return ("source not found.", 404)
    source.code = body["code"]
    source.name= body["name"]
    source.lat = body["lat"]
    source.long = body["long"]
    source.type= body["type"]
    source.description = body["description"]
    source.email = body["email"]
    source.phone = body["phone"]
    source.installation_date = body["installation_date"]
    
    database.db.session.commit()
    return 200

def removeSourceById(id):
    source = models.Source.query.filter_by(id=id).delete()
    if not source:
        return ("source not found.", 404)
    database.db.session.commit()
    return 200




def getVariables():
    variable = models.Variable.query.all()
    variable = map(lambda n: n.to_dict(), variable)
    return list(variable)


def createVariable(body):
    variable = models.Variable.from_dict(**body)
    database.db.session.add(variable)
    database.db.session.commit()
    return variable.to_dict()

def getVariableById(id):
    variable = models.Variable.query.filter_by(id=id).first()
    if variable is None:
        return ("Variable not found.", 404)
    return variable.to_dict()

def updateVariableById(body, id):
    variable = models.Variable.query.filter_by(id=id).first()
    if variable is None:
        return ("source not found.", 404)
    variable.name= body["name"]
    variable.data_type = body["data_type"]
    variable.unit = body["unit"]
    variable.accuracy= body["accuracy"]
    variable.measurement_range = body["measurement_range"]
    variable.frequency = body["frequency"]
    variable.source = body["source"]
    variable.description = body["description"]

    database.db.session.commit()
    return 200

def removeVariableById(id):
    variable = models.Variable.query.filter_by(id=id).delete()
    if not variable:
        return ("Variable not found.", 404)
    database.db.session.commit()
    return 200