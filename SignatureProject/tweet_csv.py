"""
 [1] "id"                      "handle"                 
 [3] "text"                    "is_retweet"             
 [5] "original_author"         "time"                   
 [7] "in_reply_to_screen_name" "in_reply_to_status_id"  
 [9] "in_reply_to_user_id"     "is_quote_status"        
[11] "lang"                    "retweet_count"          
[13] "favorite_count"          "longitude"              
[15] "latitude"                "place_id"               
[17] "place_full_name"         "place_name"             
[19] "place_type"              "place_country_code"     
[21] "place_country"           "place_contained_within" 
[23] "place_attributes"        "place_bounding_box"     
[25] "source_url"              "truncated"              
[27] "entities"                "extended_entities" 


I want:
handle,text_retweet,original_author,
"""

import csv

# row[1] = handle

with open('tweets2.csv') as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		print(row[1].upper())
