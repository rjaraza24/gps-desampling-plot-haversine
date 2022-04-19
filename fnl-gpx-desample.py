from gpx_converter import Converter
import gpxpy.gpx

from gpxplotter import (
    create_folium_map,
    read_gpx_file,
    add_segment_to_map,
)

#https://pypi.org/project/gpxpy/
#https://gpxplotter.readthedocs.io/en/latest/


#Set Sample Rate
k = 30
#Change dsm-out-K.gpx
f = open(r"C:\Users\63956\Desktop\Report\mar30\desampling\gpx-dsm2-30-test.gpx", "w+")


#opening the GPX file
for track in read_gpx_file(r"C:\Users\63956\Desktop\Report\mar30\desampling\2022-02-18_104240_test6.gpx"):
 #print(track)
 for i, segment in enumerate(track['segments']):
     sg_lat = list(segment['lat'])
     sg_lon = list(segment['lon'])
     sg_time = list(segment['time'])
     sg_vlc = list(segment['Velocity / km/h'])

#rename the variables from the list created from track[]
latitudes = sg_lat
longitudes = sg_lon
times = sg_time
vlc = sg_vlc

#print(len(latitudes), len(longitudes), len(times), len(elev) )
lst_tme = str(times[-1])


#Splicing method based on k sample rate
splc_lat = latitudes[0::k]
splc_lon = longitudes[0::k]
splc_tme = times[0::k]
splc_vlc = vlc[0::k]

splc_lat.append(latitudes[-1])
splc_lon.append(longitudes[-1])
splc_tme.append(times[-1])
splc_vlc.append(vlc[-1])


#Round off velocity
rndd_vlc = [round(num, 3) for num in splc_vlc]

#creating a GPX xml
gpx = gpxpy.gpx.GPX()

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)


#appending elements to the GPX
for x in range(len(splc_lat)):
    gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(splc_lat[x], splc_lon[x], speed=rndd_vlc[x], time=splc_tme[x]))

print('Created GPX:', gpx.to_xml('1.0'))

f.write(str(gpx.to_xml('1.0')))
print(type(gpx))

f.close()

#Copy terminal output XML string
#Create a textfile -- XML.gpx
#Open it at VS Code-Trust-View Map



##########

