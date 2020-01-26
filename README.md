# GEE_chart_to_CSV

### This files helps organizing downloaded CSV files from Google Earth Engine's chart export.

* Before you start: download multiple CSV files from chart export function in Google Earth Engine 


* copy all files in folder of your choice 
* enter path to files into line 8 (input_path) and set your Sentinel-1 orbit parameters
    * _works fine with all kinds of GEE chart exports with some minor tweaks but was mainly developed for Sentinel-1 data_
* automatic creation of result folder and extraction of data into one single CSV file with only one date column
