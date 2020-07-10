https://zenodo.org/record/3819464


https://ieee-dataport.org/open-access/coronavirus-covid-19-geo-tagged-tweets-dataset

https://raw.githubusercontent.com/doublebyte1/da-interview/master/COVID.csv

https://plugins.qgis.org/plugins/qweetgis/

Keyword search:
Grab tweets about COVID, by userplace

Social activity
https://plugins.qgis.org/plugins/SocialActivity/

Grab real points around a location (1000)

cat users_geo.json | jq .

cat users_geo.json | jq -r '. | [.[] | tostring] | @csv'



cat users_geo.json | jq -r '.[] | .[0] | .user_id, .features.location  | tostring'


https://medium.com/@compatt84/qweetgis-qgis-3-plugin-for-twitter-93005f2e5ec8

https://github.com/doublebyte1/bts_geospatial/blob/master/World_Countries.rar


QWeetGIS: twitter streaming API