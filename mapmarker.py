# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 09:55:17 2016

@author: John
"""

from __future__ import print_function
import csv

class Map(object):
    def __init__(self):
        self._points = []
    def add_point(self, coordinates):
        self._points.append(coordinates)
    def __str__(self):
        centerLat = sum(( x[0] for x in self._points )) / len(self._points)
        centerLon = sum(( x[1] for x in self._points )) / len(self._points)
        markersCode = "\n".join(
            [ """new google.maps.Marker({{
                position: new google.maps.LatLng({lat}, {lon}),
                map: map
                }});""".format(lat=x[0], lon=x[1]) for x in self._points
            ])
        return """
            <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false"></script>
            <div id="map-canvas" style="height: 100%; width: 100%"></div>
            <script type="text/javascript">
                var map;
                function show_map() {{
                    map = new google.maps.Map(document.getElementById("map-canvas"), {{
                        zoom: 11,
                        center: new google.maps.LatLng({centerLat}, {centerLon})
                    }});
                    {markersCode}
                }}
                google.maps.event.addDomListener(window, 'load', show_map);
            </script>
        """.format(centerLat=centerLat, centerLon=centerLon,
                   markersCode=markersCode)




if __name__ == "__main__":
        map = Map()
        # Add Beijing, you'll want to use your geocoded points here:
        f = open('blighted_lat_lon.csv','rt')
        myReader = csv.reader(f)         
        for row in myReader:                
            #map.add_point((38.924935,-77.0002052))
            if row[0] != "Lat":
                map.add_point((float(row[0]),float(row[1])))
        
        with open("output.html", "w") as out:
            print(map, file=out)
        f.close()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            