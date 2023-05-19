from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    def __repr__(self):
        return '<User {}>'.format(self.username)

class CPU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    Core = db.Column(db.String(64))
    Number_of_Cores = db.Column(db.String(64))
    Number_of_threads = db.Column(db.String(64))
    Process_technology = db.Column(db.String(64))
    Connector = db.Column(db.String(64))
    Frequency = db.Column(db.String(64))
    Multiplier = db.Column(db.String(64))
    HTT_Bclk = db.Column(db.String(64))
    Memory_type = db.Column(db.String(64))
    L1_cache = db.Column(db.String(64))
    L2_cache = db.Column(db.String(64))
    L3_cache = db.Column(db.String(64))
    Supply_voltage = db.Column(db.String(64))
    TDP = db.Column(db.String(64))
    Number_of_transistors = db.Column(db.String(64))
    Crystal_area = db.Column(db.String(64))
    Limit_temperature = db.Column(db.String(64))
    Instruction_set = db.Column(db.String(64))
    Other_Features = db.Column(db.String(64))
    Date_of_issue = db.Column(db.String(64))
    Cost = db.Column(db.String(64))


