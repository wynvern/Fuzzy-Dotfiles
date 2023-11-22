#!/bin/sh

argumentTheme=$1

if [ "$argumentTheme" -eq 1 ]; then
    echo "The value is 1."

    hyprctl hyprpaper wallpaper "HDMI-A-1,/home/wynvern/.config/hypr/wallpapers/wp1.png"
    pkill waybar
    /home/wynvern/.config/waybar/runWaybar.sh style2.css &
fi

if [ "$argumentTheme" -eq 2 ]; then
    echo "The value is 1."

    hyprctl hyprpaper wallpaper "HDMI-A-1,/home/wynvern/.config/hypr/wallpapers/wp2.jpg"
    pkill waybar
    /home/wynvern/.config/waybar/runWaybar.sh style1.css &
fi