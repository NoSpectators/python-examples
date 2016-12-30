# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults #GetUpdatedPropertyDetails


address = '2735 4TH ST'
zipcode = '20002'
zillow_data = ZillowWrapper("X1-ZWz19oz2bm36dn_9prl8")
deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
result = GetDeepSearchResults(deep_search_response)

zillow_id = result.zillow_id # zillow id, needed for the GetUpdatedPropertyDetails
home_type = result.home_type
home_detail_link = result.home_detail_link
graph_data_link = result.graph_data_link
map_this_home_link = result.map_this_home_link
lat = result.latitude
lon = result.longitude 
#coords = result.coordinates #(as GEOS point)
tax_year = result.tax_year
tax_value = result.tax_value
year_built = result.year_built
property_size = result.property_size
home_size = result.home_size
bathrooms = result.bathrooms
bedrooms = result.bedrooms
last_sold_date = result.last_sold_date
last_sold_price_currency = result.last_sold_price_currency
last_sold_price = result.last_sold_price
zestimate_amount = result.zestimate_amount
zestimate_last_updated = result.zestimate_last_updated
zestimate_value_change = result.zestimate_value_change
zestimate_valuation_range_high = result.zestimate_valuation_range_high
zestimate_valuationRange_low = result.zestimate_valuationRange_low
zestimate_percentile = result.zestimate_percentile
print home_type, lat, lon, last_sold_date, property_size, tax_year, tax_value, last_sold_price

#more info!
#updated_property_details_response = zillow_data.get_updated_property_details(zillow_id)
#result = GetUpdatedPropertyDetails(updated_property_details_response)
#home_info = result.home_info
#year_updated = result.year_updated
#floor_material= result.floor_material
#num_floors = result.num_floors
#basement= result.basement
#roof = result.roof
#view = result.view
#parking_type = result.parking_type
#heating_sources = result.heating_sources
#heating_system = result.heating_system
#rooms = result.rooms
#home_description = result.home_description
#neighborhood = result.neighborhood
#school_district = result.school_district
#print basement, rooms, neighborhood, school_district

 