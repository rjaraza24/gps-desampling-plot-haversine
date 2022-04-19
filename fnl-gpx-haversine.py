from gpx_converter import Converter
from math import radians, cos, sin, asin, sqrt
import gpxpy



#reading original GPX
#dic = Converter(input_file=r"C:\Users\63956\Desktop\Report\mar30\desampling\2022-02-18_104240_test6.gpx").gpx_to_dictionary(latitude_key='lat', longitude_key='lon')

#reading desampled GPX
dic = Converter(input_file=r"C:\Users\63956\Desktop\Report\mar30\desampling\gpx-dsm2-1.gpx").gpx_to_dictionary(latitude_key='lat', longitude_key='lon')
#dic = Converter(input_file=r"C:\Users\63956\Desktop\Report\mar30\desampling\gpx-dsm2-10.gpx").gpx_to_dictionary(latitude_key='lat', longitude_key='lon')
#dic = Converter(input_file=r"C:\Users\63956\Desktop\Report\mar30\desampling\gpx-dsm2-30.gpx").gpx_to_dictionary(latitude_key='lat', longitude_key='lon')

f = open(r"C:\Users\63956\Desktop\Report\mar30\desampling\hvs-out-1.txt", "w+")


#degree
latitudes_deg = list(dic['lat'])
longitudes_deg = list(dic['lon'])
LatLonList_deg = list(zip(latitudes_deg, longitudes_deg))
#veloc = list(dic['velocity'])


#radians
latitudes = list(map(radians,dic['lat']))
longitudes = list(map(radians,dic['lon']))

max_d = 0

distance = []



LatLonList = list(zip(latitudes, longitudes))

for n in range(len(LatLonList)-1):

    dlat = LatLonList[n][0] - LatLonList[n+1][0]  # this is for i
    dlon = LatLonList[n][1] - LatLonList[n+1][1]  # this is for j

    a = sin(dlat/2)**2 + cos(LatLonList[n][0]) * cos(LatLonList[n+1][0]) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371000 # Radius of earth in meters

    #distance.append((c * r))
    #distance.append(round((c * r), 2))
    distance = round((c*r),4)
    max_d = max_d + distance
 #   print(LatLonList[n][0], LatLonList[n][1] distance)
    #print("(% s , % s) & (% s , % s) --> % s meters" % (LatLonList_deg[n][0], LatLonList_deg[n][1],
                                                        #LatLonList_deg[n+1][0], LatLonList_deg[n+1][1], distance))
    f.write("(% s , % s) & (% s , % s) --> % s meters \r\n" % (LatLonList_deg[n][0], LatLonList_deg[n][1],
                                                        LatLonList_deg[n+1][0], LatLonList_deg[n+1][1], distance))
print("Total Distance: " + str(round(max_d,4)) + " meters")
f.write("Total Distance: " + str(round(max_d,4)) + " meters")
f.close()
