__author__ = 'steffenfb'

import urllib2
import xml.etree.ElementTree as ET
from datetime import datetime



class Timeslot:

    def __init__(self, fromtime, totime, windspeed, direction):
        self.fromtime = fromtime
        self.totime = totime
        self.windspeed = windspeed
        self.direction = direction


# add to url to fetch:
    #/varsel_time_for_time.xml
    #/varsel.xml

def fetch_xml(url, treshold):
    data = urllib2.urlopen(url)

    tree = ET.parse(data)
    root = tree.getroot()
    forecast = root.find('forecast')

    tab = forecast.find('tabular')
    times = tab.findall('time')

    for t in times:
        time=  t.attrib
        windspeed = t.find('windSpeed').attrib
        windDir = t.find('windDirection').attrib

        if(windspeed >= treshold):
            Timeslot(stringToTime(time['from']),stringToTime(time['to']),windspeed, windDir )

fetch_xml('http://www.yr.no/sted/Norge/Akershus/B%C3%A6rum/Halden_brygge/varsel.xml', 6)



def stringToTime(string):
    return datetime.strptime('2016-07-01T20:00:00', '%Y-%m-%dT%H:00:00')

