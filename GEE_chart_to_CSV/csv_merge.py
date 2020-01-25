import os
import glob
import pandas as pd
from os.path import basename


def main():
    # extraction of current path and number of available CSV-files in used folder
    input_path = "example_path"
    extension = 'csv'
    list_csv = glob.glob(input_path + "*" + extension)

    # set Sentinel-1 polarization, orbit and your classname
    polarization = "VV"
    orbit_direction = "Descending"
    class_name = "example_class"

##########          NO USER INPUT BEYOND THIS POINT NEEDED          ##########


    # create result subfolder
    subdir = os.path.join(input_path, 'result/')
    os.makedirs(subdir, exist_ok=True)

    csv_merge(list_csv, class_name, polarization, orbit_direction, subdir)


def csv_merge(list_csv, class_name, polarization, orbit_direction, subdir):
    # reading first CSV-file
    data = pd.read_csv(list_csv[0])

    # loop for extraction of individual values
    for i,file in enumerate(list_csv[:len(list_csv)-1]):
        read = pd.read_csv(file)
        #print(file)
        data[polarization + str(i)] = read[polarization].values

    # storing extracted data in one file
    data.to_csv(path_or_buf= subdir + class_name + "_" + orbit_direction + "_" + polarization + ".csv")

if __name__ == '__main__':
    main()