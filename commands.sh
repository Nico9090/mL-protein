#!/bin/bash

echo "These are the files in your directory: "
ls
echo -e "Today's weather.\n The skies are very cloudy!\n The air is moist!"

time=$(date)

echo "Right now, it is $time"
bold=$(tput bold)

echo "${bold}Right now, it is $time"

name="Marcella"
echo "$name"

fname="Nic"
lname="Kojo"
echo "Hello $fname $lname"

echo "What is your favorite phone? "
read mobile

echo "Really?! Your favorite phone is $mobile?"
