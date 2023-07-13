#!/bin/bash
echo -e "The IP address is: \e[1;32m`hostname -I`\e[1;m"


#rsync  -e ssh -auvzp /home/pi/SocialDrinking/ root@vps77143.vps.ovh.ca:/root/Dropbox/Pies/SocialDrinking/

cd /home/pi/video/
ffmpeg -y -i $1 -c:v libx264 -pix_fmt yuv420p -preset superfast -crf 20 "${1}.mp4"

echo "${1}.mp4 is saved"

