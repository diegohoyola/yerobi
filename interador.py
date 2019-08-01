import json
import configparser
import mysql.connector as my
import datetime
def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

Config = configparser.ConfigParser()



Config.read("node_modules\\claves.seed")
print(Config.sections())
print(Config.options('MySQLHOMI'))
print(Config.get('MySQLHOMI', 'hostname'))
print(Config.get('MySQLHOMI', 'user'))
print(Config.get('MySQLHOMI', 'password'))
#configFile=ConfigSectionMap()
config=json.load(open("node_modules\\config.json"))  
#print(configFile["username"])
print(config["user"])

numdays=8
base = datetime.datetime.today()-datetime.timedelta(days=1)
#base.strftime("%m/%d/%Y")
date_list = [(base - datetime.timedelta(days=x)).strftime("%Y-%m-%d") for x in range(numdays)]
print(date_list)
