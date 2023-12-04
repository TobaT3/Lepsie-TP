from edupage_api import Edupage
from edupage_api.timeline import EventType
from datetime import datetime
import logging

edupage = Edupage()

edupage.login("mail", "heslo", "sgcenada")

#print(edupage.get_notifications())

def getTest():
    examsids = ["bexam", "oexam", "rexam", "pexam", "sexam"]

    testlist = []

    for event in edupage.get_notifications():
        data = event.additional_data
        if event.additional_data and event.additional_data != []:
            if "typ" in data:
                if data["typ"] in examsids:
                    testlist.append({"name": data["name"], "date": data["date"], "time": data["cas_udalosti"]})
    
    return testlist
    
                    

def getGrades():
    allgrades = edupage.get_grades()

if __name__ == "__main__":
    getTest()
