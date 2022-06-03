GeoIP and RDAP Lookup operational via CLI 

parse_txt.py parses given text file (specified in main) for Ip addresses through built in package: RegEx

geo_lookup.py and RDAP.py utilize python module Requests for http requests - further manipulation done with built in package: json

Caching done via requests_cache


To run:

Setup your python enviornment and clone the git repo

Navigate your command line to the location of PIP, and type the following:

pip install requests 
pip install requests-cache

Finally run main.py and follow the printed statements

