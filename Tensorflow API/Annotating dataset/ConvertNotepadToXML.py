import os
import re
for y in range(1,1200):
    count=1
    try:
        xmlfile = open("windmill_"+str(y)+".xml","r")
        
    except IOError:
        count=0
    if (count == 1):

        line= xmlfile.readlines()
        line =  re.sub("[<> \t .png j]","\n",line[0])
        line = line.split("\n")
        
        count=0
        xmin = line[145]
        ymin = line[154]
        xmax = line[162]
        ymax = line[169]
        xmlfile.close()
        xmlfile = open("windmill_"+str(y)+".xml","w")
        xmlfile.write('<?xml version="1.0"?>')
        xmlfile.write('<annotation>')
        xmlfile.write('	<folder> ISRO </folder>')
        xmlfile.write('	<filename>'+"windmill_"+str(y) +".jpg"+'</filename>')
        xmlfile.write('	<source>')
        xmlfile.write('		<database>ISRO windmill dataset</database>')
        xmlfile.write('		<annotation>ISRO</annotation>')
        xmlfile.write('		<image> Satellite </image>')
        xmlfile.write('	</source>')	
        xmlfile.write('	<size>')
        xmlfile.write('		<width>1024</width>')
        xmlfile.write('		<height>1024</height>')
        xmlfile.write('		<depth>3</depth>')
        xmlfile.write('	</size>')
        xmlfile.write('	<segmented>0</segmented>')
        xmlfile.write('	<object>')
        xmlfile.write('		<name>Windmill</name>')
        xmlfile.write('		<pose>Top</pose>')
        xmlfile.write('		<truncated>0</truncated>')
        xmlfile.write('		<occluded>0</occluded>')
        xmlfile.write('		<bndbox>')
        xmlfile.write('			<xmin>'+str(xmin)+'</xmin>')
        xmlfile.write('			<ymin>'+str(ymin)+'</ymin>')
        xmlfile.write('			<xmax>'+str(xmax)+'</xmax>')
        xmlfile.write('			<ymax>'+str(ymax)+'</ymax>')
        xmlfile.write('		</bndbox>')
        xmlfile.write('		<difficult>0</difficult>')
        xmlfile.write('	</object>')
        xmlfile.write('</annotation>')

    else:
        pass