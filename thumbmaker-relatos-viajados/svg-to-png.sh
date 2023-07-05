#!/bin/bash

#for file in '/mnt/24860678-791e-4d8d-ab99-c76390855d86/Dropbox/vamoslonge-thumbs/thumbmaker-relatos-viajados'
for file in *{.svg,.SVG};
do
     echo ${file}
     /usr/bin/inkscape -z -f "${file}" -w 720 -e "${file}.png"
done

mv *.png png

scp /mnt/24860678-791e-4d8d-ab99-c76390855d86/Dropbox/vamoslonge-thumbs/thumbmaker-relatos-viajados/png/* root@45.33.113.61:/var/www/html/vamoslonge/thumbs