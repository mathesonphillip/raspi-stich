#!/usr/bin/python3


##
# Copy SD Contents
# Stich with ffmpeg
#
#
##



import sys
import datetime
import glob
import shutil
import os
import time

FOLDER_NAME="/media/pi/*/timelapse"
DESTINATION="/home/pi/timelapse/copy"

def main():


    print("\nWaiting for drive mount\n")
    time.sleep(5)


    print(FOLDER_NAME)

    for name in glob.glob(f'{FOLDER_NAME}'):
        print(f"Found '{FOLDER_NAME}' folder: {name}")
        
        os.makedirs(DESTINATION, exist_ok=True)

        for image in glob.glob(f'{name}/*.jpg'):
            print(f'\t{image}')
            shutil.copy(image, DESTINATION)


    print("\nWaiting 10secs and will remove copied images\n")
    time.sleep(10)


    for name in glob.glob(f'{DESTINATION}'):

        for image in glob.glob(f'{DESTINATION}/*.jpg'):
            os.remove(image)
            print(f'Deleted: {image}')


        os.rmdir(DESTINATION)
        print(f'Deleted: {DESTINATION}')


    print("\nClosing in 10 seconds\n")
    time.sleep(10)




if __name__ == "__main__":
    print("MAIN")
    # FOLDER_NAME="./*/*/timelapse"
    # DESTINATION="./copy"
    main()