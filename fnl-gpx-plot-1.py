#https://gpxplotter.readthedocs.io/en/latest/auto_examples/maps/plot_003_velocity.html#sphx-glr-auto-examples-maps-plot-003-velocity-py


from re import X
import numpy as np
import folium
from folium.plugins import BeautifyIcon
from gpxplotter import (
    create_folium_map,
    read_gpx_file,
    add_segment_to_map,
)
from gpxplotter.common import cluster_velocities


line_options1 = {'weight': 13, 'color': '#006d2c'}
line_options2 = {'weight': 8, }

the_map = create_folium_map(tiles='openstreetmap_humanitarian')


# for track in read_gpx_file(r"C:\Users\63956\Desktop\Report\mar30\desampling\2022-02-18_104240_test6.gpx"):
for track in read_gpx_file(r"C:\Users\63956\Desktop\Report\mar30\desampling\gpx-dsm2-30.gpx"):

    for i, segment in enumerate(track['segments']):

        sg_latlon = list(segment['latlon'])
        sg_time = list(segment['time'])
        sg_vlc = list(segment['Velocity / km/h'])

        # sg_latlon = list(segment['latlon'])
        # sg_time = list(segment['time'])
        # sg_vlc = list(segment['speed'])


        #for x in range(len(sg_latlon)-2):
            #print("Coordinates : % s -- Time: % s -- Velocity: % s kph " % (sg_latlon[x],sg_time[X], sg_vlc[x] ))



        #print(i, segment['Velocity / km/h'])
        segment['velocity-level'] = cluster_velocities(
            segment['velocity'], n_clusters=19,
        )
        add_segment_to_map(the_map, segment,
                           line_options=line_options1,
                           add_start_end=False)
        add_segment_to_map(the_map, segment, color_by='velocity-level',
                           cmap='RdYlGn_09', line_options=line_options2,
                           add_start_end=False)
        # Find 1 km locations:
        maxd = max(segment['Distance / km'])
        locations = np.arange(1, maxd, 1)
        location_idx = []
        for j in locations:
            diff = abs(j - segment['Distance / km'])
            idx = np.argmin(diff)
            location_idx.append(idx)
        for dist, j in zip(locations, location_idx):
            icon = BeautifyIcon(text_color='#262626', border_color='#006d2c',
                                background_color='#ffffff', number=dist,
                                icon_shape='marker', border_width=3)
            marker = folium.Marker(
                location=segment['latlon'][j],
                icon=icon,
                tooltip=f'{dist} km',
                popup=f'{segment["time"][j].strftime("%H:%M:%S")}',
            )
            marker.add_to(the_map)
        # Add end marker:
        marker = folium.Marker(
            location=segment['latlon'][-1],
            icon=folium.Icon(icon='home'),
            tooltip=f'{segment["Distance / km"][-1]:.2f} km',
            popup=f'{segment["time"][i].strftime("%H:%M:%S")}',
        )
        marker.add_to(the_map)



the_map.save(r"C:\Users\63956\Desktop\Report\mar30\desampling\map_gpx_30_mrch.html")
# To store the map as a HTML page:


# To display the map in a Jupyter notebook:
#the_map