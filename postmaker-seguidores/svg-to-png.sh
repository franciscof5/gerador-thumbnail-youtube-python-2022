#!/bin/sh

for file in '/mnt/24860678-791e-4d8d-ab99-c76390855d86/Dropbox/vamoslonge-thumbs/thumbmaker-relatos-viajados/svg'
do
     /usr/bin/inkscape -z -f "${file}" -w 720 -e "${file}.png"
done

mv *.png png