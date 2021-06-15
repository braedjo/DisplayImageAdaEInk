#!/usr/bin/env bash

PS3="Please choose run mode: "

printf "Dumpy MFG -- E-Ink Control\n\n"

OPTLIST=(Slideshow Remote Local)

select opt in ${OPTLIST[@]} quit; do

  case $opt in
    Slideshow)
      printf "\nLaunching Slideshow\n"
      sleep 5
      python imageswap.py &
      python slideshow.py
      break
      ;;
    Remote)
      printf "\nthis shid not yet implemented G!\n\n"
      printf "Closing\n"
      break
      ;;
    Local)
      printf "Starting WG Tunnel...\n"
      sleep 2
      sudo wg-quick up pootunnel
      printf "Waiting 25 Secs\n"
      sleep 25
      python main.py
      break
      ;;
    quit)
      printf "\nClosing"
      break
      ;;
    *) 
      printf "\nInvalid option $REPLY\n"
      ;;
  esac
done