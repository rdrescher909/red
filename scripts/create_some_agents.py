from lib import Agent
import json
import mysql.connector as con


with open('config.json') as config_file:
    config = json.load(config_file)

db_connection = con.connect(**config)

Agent.create_agent(db_connection, 1, "Joe", "C", "McKenzie", 586, 123456, 586, 123457, "jmckenzie@gmail.com", "50592 Van Dyke Ave", "Shelby Twp", "MI", 48309, 1, None, None)
Agent.create_agent(db_connection, 2, "Mary", "M", "Rose", 313, 5662134, 248, 4213889, "mrose@gmail.com", "123 W Maple Ave", "Bloomfield Hills", "MI", 48230, 2, None, None)
Agent.create_agent(db_connection, 3, "John", "D", "Doe", 586, 1234567, 586, 1234568, "jddoe@gmail.com", "123 W Maple Ave", "Bloomfield Hills", "MI", 48230, 3, None, None)
Agent.create_agent(db_connection, 4, "Jane", "E", "Doe", 586, 1234569, 586, 1234570, "jedoe@gmail.com", "1234 W Grove St", "Farmington", "MI", 48230, 4, None, None)