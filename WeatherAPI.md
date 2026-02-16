# **FREE TIER LIMITATIONS**

Calls per month:     1 Million

Realtime weather:     Yes

Forecast Days     3 Day

Forecast Interval     Daily and Hourly

Marine Weather New     1 Day. No Tide Data     

Marine Weather Interval     Daily only

Historical Weather     Last 7 days

Search API     Yes

Astronomy API     Yes

IP Lookup     Yes

Sports API     Yes

Weather Maps     Yes

# **Introduction**

WeatherAPI.com provides access to free weather and geo data via a JSON/XML restful API. It allows developers to create desktop, web and mobile applications using this data very easy.

We provide following data through our API:

* Real-time weather  
* 14 day weather forecast  
* Historical weather  
* Marine Weather and Tide Data  
* Future Weather (Upto 365 days ahead)  
* Daily and hourly intervals  
* Pollen forecast (Pro+ plan and above) New  
* 15 min intervalNew (Enterprise only)  
* Astronomy  
* Time zone  
* Sports  
* Weather Maps New  
* Location data  
* Search or Autocomplete API  
* Weather Alerts  
* Air Quality Data  
* Bulk Request  
* Solar Irradiance  
* Evapotranspiration (Enterprise)  
* Wind at 100m (Enterprise) New  
* Pollen History (Enterprise) New

## **Getting Started**

You need to [signup](https://www.weatherapi.com/signup.aspx) and then you can find your API key under [your account](https://www.weatherapi.com/login.aspx), and start using API right away\!

Try our weather API by using interactive [API Explorer](https://www.weatherapi.com/api-explorer.aspx) or use [Swagger Tool](https://app.swaggerhub.com/apis-docs/WeatherAPI.com/WeatherAPI/1.0.2).

We also have SDK for popular framework/languages [available on Github for quick integrations](https://github.com/weatherapicom/).

Want to choose which weather field to return in the API response? Change it from [API response fields](https://www.weatherapi.com/my/fields.aspx).

If you find any features missing or have any suggestions, please [contact us](https://www.weatherapi.com/contact.aspx).

## **Authentication**

API access to the data is protected by an API key. If at anytime, you find the API key has become vulnerable, please regenerate the key using Regenerate button next to the API key.

Authentication to the WeatherAPI.com API is provided by passing your API key as request parameter through an API .

### **key parameter**

key=\<YOUR API KEY\>

## **Request**

##### **Request URL**

Request to WeatherAPI.com API consists of base url and API method. You can make both HTTP or HTTPS request to our API.

Base URL: [http://api.weatherapi.com/v1](https://www.weatherapi.com/docs/#)

| API | API Method |
| ----- | ----- |
| Current weather | /current.json or /current.xml |
| Forecast | /forecast.json or /forecast.xml |
| Search or Autocomplete | /search.json or /search.xml |
| History | /history.json or /history.xml |
| Alerts | /alerts.json or /alerts.xml |
| Marine | /marine.json or /marine.xml |
| Future | /future.json or /future.xml |
| Time Zone | /timezone.json or /timezone.xml |
| Sports | /sports.json or /sports.xml |
| Astronomy | /astronomy.json or /astronomy.xml |
| IP Lookup | /ip.json or /ip.xml |

#### **Request Parameters**

| Parameter |  | Description |
| ----- | ----- | ----- |
| key | Required | API Key |
| q | Required | Query parameter based on which data is sent back. It could be following: Latitude and Longitude (Decimal degree) e.g: q=48.8567,2.3508 city name e.g.: q=Paris US zip e.g.: q=10001 UK postcode e.g: q=SW1 Canada postal code e.g: q=G2J metar:\<metar code\> e.g: q=metar:EGLL iata:\<3 digit airport code\> e.g: q=iata:DXB auto:ip IP lookup e.g: q=auto:ip IP address (IPv4 and IPv6 supported) e.g: q=100.0.0.1 By ID returned from Search API. e.g: q=id:2801268 bulk New |
| days | Required only with forecast API method. | Number of days of forecast required. days parameter value ranges between 1 and 14\. e.g: days=5 If no days parameter is provided then only today's weather is returned. |
| dt (Required for History and Future API) | Restrict date output for Forecast and History API method. | For history API 'dt' should be on or after 1st Jan, 2010 in yyyy-MM-dd format (i.e. dt=2010-01-01) For forecast API 'dt' should be between today and next 14 day in yyyy-MM-dd format (i.e. dt=2010-01-01) For future API 'dt' should be between 14 days and 300 days from today in the future in yyyy-MM-dd format (i.e. dt=2023-01-01) |
| (Optional) unixdt | Unix Timestamp used by Forecast and History API method. | unixdt has same restriction as 'dt' parameter. Please either pass 'dt' or 'unixdt' and not both in same request. e.g.: unixdt=1490227200 |
| (Optional) end\_dt (Available for History API) | Restrict date output for History API method. | For history API 'end\_dt' should be on or after 1st Jan, 2010 in yyyy-MM-dd format (i.e. dt=2010-01-01) 'end\_dt' should be greater than 'dt' parameter and difference should not be more than 30 days between the two dates. **Only works for API on Pro plan and above.** |
| (Optional) unixend\_dt | Unix Timestamp used by History API method. | unixend\_dt has same restriction as 'end\_dt' parameter. Please either pass 'end\_dt' or 'unixend\_dt' and not both in same request. e.g.: unixend\_dt=1490227200 |
| (Optional) hour | Restricting forecast or history output to a specific hour in a given day. | Must be in 24 hour. For example 5 pm should be hour=17, 6 am as hour=6 |
| (Optional) alerts | Disable alerts in forecast API output | alerts=yes or alerts=no |
| (Optional) aqi | Enable/Disable Air Quality data in forecast API output | aqi=yes or aqi=no |
| (Optional) pollen New | Enable/Disable Pollen data in realtime, forecast, future and history API output | pollen=yes or pollen=no |
| (Optional) tides New | Enable/Disable Tide data in Marine API output | tides=yes or tides=no |
| (Optional) tp New | Get 15 min interval data for Forecast and History API. Available for Enterprise clients only. | tp=15 |
| (Optional) current\_fields New | Pass field names as comma seperated which should be returned in the current element. | current\_fields=temp\_c,wind\_mph |
| (Optional) day\_fields New | Pass field names as comma seperated which should be returned in the Forecast or History API day element. | day\_fields=temp\_c,wind\_mph |
| (Optional) hour\_fields New | Pass field names as comma seperated which should be returned in the Forecast or History API hour element. | hour\_fields=temp\_c,wind\_mph |
| (Optional) solar (Enterprise) New | Enable solar irradiance data in History API. Available for Enterprise clients only. | solar=yes |
| (Optional) et0 New | Enable Evapotranspiration data in Forecast and History API. Available for Business and Enterprise clients only. | et0=yes |
| (Optional) wind100mph (Enterprise) New | Enable wind data and return wind speed in mph at 100mt height in History API. Available for Enterprise clients only. | wind100mph=yes |
| (Optional) wind100kph (Enterprise) New | Enable wind data and return wind speed in kmph at 100mt height in History API. Available for Enterprise clients only. | wind100kph=yes |
| (Optional) lang | Returns 'condition:text' field in API in the desired language | Please pass 'lang code' from below table. e.g.: lang=fr **Language** **lang code** Arabic ar Bengali bn Bulgarian bg Chinese Simplified zh Chinese Traditional zh\_tw Czech cs Danish da Dutch nl Finnish fi French fr German de Greek el Hindi hi Hungarian hu Italian it Japanese ja Javanese jv Korean ko Mandarin zh\_cmn Marathi mr Polish pl Portuguese pt Punjabi pa Romanian ro Russian ru Serbian sr Sinhalese si Slovak sk Spanish es Swedish sv Tamil ta Telugu te Turkish tr Ukrainian uk Urdu ur Vietnamese vi Wu (Shanghainese) zh\_wuu Xiang zh\_hsn Yue (Cantonese) zh\_yue Zulu zu  |

## **Location Object**

Location object is returned with each API response. It is actually the matched location for which the information has been returned.

It returns information about the location including geo points, name, region, country and time zone information as well.

*When using [Search or Autocomplete API](https://www.weatherapi.com/docs/#apis-search) following fields are NOT returned tz\_id, localtime\_epoch and localtime.*

| Field | Data Type | Description |
| ----- | ----- | ----- |
| lat | decimal | Latitude in decimal degree |
| lon | decimal | Longitude in decimal degree |
| name | string | Location name |
| region | string | Region or state of the location, if availa |
| country | string | Location country |
| tz\_id | string | Time zone name |
| localtime\_epoch | int | Local date and time in unix time |
| localtime | string | Local date and time |

## **Weather Alerts**

[Forecast API](https://www.weatherapi.com/docs/#apis-forecast) and [Alerts API](https://www.weatherapi.com/docs/#apis-alerts) returns alerts and warnings issued by government agencies (USA, UK, Europe and Rest of the World) as an array if available for the location provided through the [Forecast API](https://www.weatherapi.com/docs/#apis-forecast) and [Alerts API](https://www.weatherapi.com/docs/#apis-alerts).

By default alerts are not returned. To get alerts back in the response from [Forecast API](https://www.weatherapi.com/docs/#apis-forecast), pass the parameter **alerts=yes**.

Note: Some of the alerts may be in local language of the location.

| Field | Data Type | Description |
| ----- | ----- | ----- |
| headline | string | Alert headline |
| msgType | string | Type of alert |
| severity | string | Severity of alert |
| urgency | string | Urgency |
| areas | string | Areas covered |
| category | string | Category |
| certainty | string | Certainty |
| event | string | Event |
| note | string | Note |
| effective | date | Effective |
| expires | string | Expires |
| desc | string | Description |
| instruction | string | Instruction |

#### **Example response of alerts**

                           "alerts":{  
    "alert":\[  
        {  
        "headline":"Flood Warning issued January 05 at 9:47PM EST until January 07 at 6:15AM EST by NWS",  
        "msgtype":"Alert",  
        "severity":"Moderate",  
        "urgency":"Expected",  
        "areas":"Calhoun; Lexington; Richland",  
        "category":"Met",  
        "certainty":"Likely",  
        "event":"Flood Warning",  
        "note":"Alert for Calhoun; Lexington; Richland (South Carolina) Issued by the National Weather Service",  
        "effective":"2021-01-05T21:47:00-05:00",  
        "expires":"2021-01-07T06:15:00-05:00",  
        "desc":"...The Flood Warning continues for the following rivers in South\\nCarolina...\\nCongaree River At Carolina Eastman affecting Richland, Calhoun\\nand Lexington Counties.\\nCongaree River At Congaree National Park-Gadsden affecting\\nCalhoun and Richland Counties.\\nNorth Fork Edisto River At Orangeburg affecting Orangeburg County.\\n...The Flood Warning is now in effect until Thursday morning...\\nThe Flood Warning continues for\\nthe Congaree River At Carolina Eastman.\\n\* Until Thursday morning.\\n\* At 9:28 PM EST Tuesday the stage was 115.6 feet.\\n\* Flood stage is 115.0 feet.\\n\* Minor flooding is occurring and minor flooding is forecast.\\n\* Recent Activity...The maximum river stage in the 24 hours ending\\nat 9:28 PM EST Tuesday was 118.2 feet.\\n\* Forecast...The river will rise to 115.7 feet just after midnight\\ntonight. It will then fall below flood stage tomorrow morning to\\n114.2 feet and begin rising again tomorrow evening. It will rise\\nto 114.3 feet early Thursday morning. It will then fall again and\\nremain below flood stage.\\n\* Impact...At 115.0 feet, Flooding occurs in low lying areas of the\\nCarolina Eastman Facility and at the Congaree National Park.\\n\* Flood History...This crest compares to a previous crest of 116.3\\nfeet on 12/03/2020.\\n&&",  
        "instruction":"A Flood Warning means that flooding is imminent or occurring. All\\ninterested parties should take necessary precautions immediately.\\nMotorists should not attempt to drive around barricades or drive\\ncars through flooded areas.\\nCaution is urged when walking near riverbanks.\\nAdditional information is available at www.weather.gov.\\nThe next statement will be issued Wednesday morning at 1000 AM EST."  
        },  
        {  
        "headline":"Flood Warning issued January 05 at 9:47PM EST until January 09 at 4:00AM EST by NWS",  
        "msgtype":"Alert",  
        "severity":"Moderate",  
        "urgency":"Expected",  
        "areas":"Calhoun; Richland",  
        "category":"Met",  
        "certainty":"Likely",  
        "event":"Flood Warning",  
        "note":"Alert for Calhoun; Richland (South Carolina) Issued by the National Weather Service",  
        "effective":"2021-01-05T21:47:00-05:00",  
        "expires":"2021-01-09T04:00:00-05:00",  
        "desc":"...The Flood Warning continues for the following rivers in South\\nCarolina...\\nCongaree River At Carolina Eastman affecting Richland, Calhoun\\nand Lexington Counties.\\nCongaree River At Congaree National Park-Gadsden affecting\\nCalhoun and Richland Counties.\\nNorth Fork Edisto River At Orangeburg affecting Orangeburg County.\\n...The Flood Warning is now in effect until early Saturday morning...\\nThe Flood Warning continues for\\nthe Congaree River At Congaree National Park-Gadsden.\\n\* Until late Friday night.\\n\* At 9:00 PM EST Tuesday the stage was 16.5 feet.\\n\* Flood stage is 15.0 feet.\\n\* Minor flooding is occurring and minor flooding is forecast.\\n\* Recent Activity...The maximum river stage in the 24 hours ending\\nat 9:00 PM EST Tuesday was 17.2 feet.\\n\* Forecast...The river is expected to fall below flood stage early\\nFriday morning and continue falling to 12.4 feet Sunday evening.\\n\* Impact...At 15.0 feet, Flooding begins in the Congaree National\\nPark. This will begin to produce flooding of portions of the lower\\nboardwalk.\\n\* Impact...At 17.0 feet, The access road to the Sandy Run\\nsubdivision becomes flooded. The lower boardwalk in the Congaree\\nNational Park becomes flooded by Cedar Creek.\\n\* Impact...At 18.0 feet, Several homes in the Sandy Run subdivision\\nalong the river become flooded. At 18 feet the river covers the\\nWeston Lake overlook in the Congaree National Park. Between 18 and\\n18.5 feet the river begins to cover sections of the elevated\\nboardwalk.\\n\* Flood History...This crest compares to a previous crest of 16.3\\nfeet on 12/03/2020.\\n&&",  
        "instruction":"A Flood Warning means that flooding is imminent or occurring. All\\ninterested parties should take necessary precautions immediately.\\nMotorists should not attempt to drive around barricades or drive\\ncars through flooded areas.\\nCaution is urged when walking near riverbanks.\\nAdditional information is available at www.weather.gov.\\nThe next statement will be issued Wednesday morning at 1000 AM EST."  
        }  
    \]  
}  
                              
                       

## **Air Quality Data**

Air Quality data is returned in the [Forecast API](https://www.weatherapi.com/docs/#apis-forecast), [History API](https://www.weatherapi.com/docs/#apis-history) and [Realtime API](https://www.weatherapi.com/docs/#apis-realtime) response. Depending upon your subscription plan we provide historical (from 1st March 2021 onwards), current and 3 day air quality data for the given location in json and xml.

It provides air quality index (see below) data on major pollutant gases like Carbon monoxide (CO), Ozone (O3), Nitrogen dioxide (NO2), Sulphur dioxide (SO2), PM 2.5 and PM 10\.

By default air quality data is not returned. To get air quality data back in the response from [Forecast API](https://www.weatherapi.com/docs/#apis-forecast), [History API](https://www.weatherapi.com/docs/#apis-history) and [Realtime API](https://www.weatherapi.com/docs/#apis-realtime), pass the parameter **aqi=yes**.

| Field | Data Type | Description |
| ----- | ----- | ----- |
| co | float | Carbon Monoxide (μg/m3) |
| o3 | float | Ozone (μg/m3) |
| no2 | float | Nitrogen dioxide (μg/m3) |
| so2 | float | Sulphur dioxide (μg/m3) |
| pm2\_5 | float | PM2.5 (μg/m3) |
| pm10 | float | PM10 (μg/m3) |
| us-epa-index | integer | US \- EPA standard. 1 means Good 2 means Moderate 3 means Unhealthy for sensitive group 4 means Unhealthy 5 means Very Unhealthy 6 means Hazardous |
| gb-defra-index | integer | UK Defra Index (See table below) |

#### **UK DEFRA INDEX Table**

| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :---: | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **Band** | Low | Low | Low | Moderate | Moderate | Moderate | High | High | High | Very High |
| **µgm\-3** | 0-11 | 12-23 | 24-35 | 36-41 | 42-47 | 48-53 | 54-58 | 59-64 | 65-70 | 71 or more |

## **Pollen Data**

Pollen data is returned in the [Realtime API](https://www.weatherapi.com/docs/#apis-realtime), [Forecast API](https://www.weatherapi.com/docs/#apis-forecast) and [Future API](https://www.weatherapi.com/docs/#apis-future) based on user subscription plan. We also do provide historical pollen data (from 1st January 2010 onwards) for our Enterprise plan users for any given location in json and xml.

It provides pollen data for Hazel, Alder, Birch, Oak, Grass, Mugwort and Ragweed in grains per cubic meter of air (grains/m³ or PPM) for United States, Canada, UK and Europe cities and towns.

By default pollen data is not returned. To get pollen data back in the response please pass the parameter **pollen=yes**.

| Field | Data Type | Description |
| ----- | ----- | ----- |
| Hazel | float | Pollen grains per cubic meter of air (grains/m³ or PPM) |
| Alder | float | Pollen grains per cubic meter of air (grains/m³ or PPM) |
| Birch | float | Pollen grains per cubic meter of air (grains/m³ or PPM) |
| Oak | float | Pollen grains per cubic meter of air (grains/m³ or PPM) |
| Grass | float | Pollen grains per cubic meter of air (grains/m³ or PPM) |
| Mugwort | float | Pollen grains per cubic meter of air (grains/m³ or PPM) |
| Ragweed | float | Pollen grains per cubic meter of air (grains/m³ or PPM) |

| Pollen concentration (grains/m³) or PPM | Risk level | Typical impact |
| ----- | ----- | ----- |
| 1 – 20 | Low | Mild symptoms in sensitive individuals |
| 20 – 100 | Moderate | Noticeable symptoms for many allergic individuals |
| 100 – 300 | High | Strong symptoms; most allergic individuals affected |
| 300+ | Very High | Severe symptoms; avoidance measures often recommended |

## **Weather Maps**

Weather Maps available for next 3 days in 1 hour interval. No API Key required and free to use.

To make our weathermaps integration easy we have provided a sample html for each weather map. See below.

Provided below is the tile path template to access our map:

| Type of Map | Path | Description |
| ----- | ----- | ----- |
| Tmp2m | https://weathermaps.weatherapi.com/tmp2m/tiles/{0}{1}/{z}/{x}/{y}.png | Temperature at 2m. [Tmp2m Demo](https://weathermaps.weatherapi.com/tmp2m/tiles/map.html). |
| Precip | https://weathermaps.weatherapi.com/precip/tiles/{0}{1}/{z}/{x}/{y}.png | Precipitation. [Precip Demo](https://weathermaps.weatherapi.com/precip/tiles/map.html). |
| Pressure | https://weathermaps.weatherapi.com/pressure/tiles/{0}{1}/{z}/{x}/{y}.png | Pressure. [Pressure Demo](https://weathermaps.weatherapi.com/pressure/tiles/map.html). |
| Wind Speed | https://weathermaps.weatherapi.com/wind/tiles/{0}{1}/{z}/{x}/{y}.png | Wind speed. [Wind Demo](https://weathermaps.weatherapi.com/wind/tiles/map.html). |

{0} is UTC Date in yyyyMMdd format. E.g: 1st Nov 2025 will be 20251101\.  
 {1} is UTC hour in 24 format. E.g:- 1 am will be 01\. 6 pm will be 18\.  
 {z} is zoom level  
 {x} is x-tile coordinate  
 {y} is y-tile coordinate

## **Bulk Request**

If you are on Pro+, Business or Enterprise plan then you may use our bulk weather option to send multiple locations to get weather for all the locations sent in a single request.

Each location sent in bulk operation is counted as 1 call. It works for all the API methods except Search API.

For bulk you need to pass in the querysting q=bulk and then pass a json body as POST method with utf-8 encoding. All the the other request parameters will be passed as query as usual.

Thanks to Dzebo Elvis for pointing out that the POST method should be used and not GET.

#### **Json format for sending multiple locations in the POST body.**

                           {  
    "locations": \[  
        {  
            "q": "53,-0.12",  
            "custom\_id": "my-id-1"  
        },  
        {  
            "q": "London",  
            "custom\_id": "any-internal-id"  
        },  
        {  
            "q": "90201",  
            "custom\_id": "us-zipcode-id-765"  
        }  
    \]  
}  
                              
                       

#### **Json format explanation**

| Parameter | Description |
| ----- | ----- |
| q (required) | You may pass lat and lon, US zipcode, UK postcode, city name, IP, etc. |
| custom\_id (optional) | We will return this custom\_id back in the response for you to use it at your end. It is for better management at your end. We don't use this id for anything. |

#### **Bulk Request Example**

                         
curl \--location \--request POST 'http://api.weatherapi.com/v1/current.json?key=YOUR\_API\_KEY\&q=bulk' \\  
\--header 'Content-Type: application/json' \\  
\--data '{  
    "locations": \[  
        {  
            "q": "53,-0.12",  
            "custom\_id": "my-id-1"  
        },  
        {  
            "q": "London",  
            "custom\_id": "any-internal-id"  
        },  
        {  
            "q": "90201",  
            "custom\_id": "us-zipcode-id-765"  
        }  
    \]  
}'  
                          
                       

##### **Bulk Response**

                           {  
    "bulk": \[  
        {  
            "query": {  
                "custom\_id": "my-id-1",  
                "q": "53,-0.12",  
                "location": {  
                    "name": "Boston",  
                    "region": "Lincolnshire",  
                    "country": "United Kingdom",  
                    "lat": 53.0,  
                    "lon": \-0.12,  
                    "tz\_id": "Europe/London",  
                    "localtime\_epoch": 1673620218,  
                    "localtime": "2023-01-13 14:30"  
                },  
                "current": {  
                    "last\_updated\_epoch": 1673620200,  
                    "last\_updated": "2023-01-13 14:30",  
                    "temp\_c": 8.7,  
                    "temp\_f": 47.7,  
                    "is\_day": 1,  
                    "condition": {  
                        "text": "Partly cloudy",  
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",  
                        "code": 1003  
                    },  
                    "wind\_mph": 24.2,  
                    "wind\_kph": 38.9,  
                    "wind\_degree": 260,  
                    "wind\_dir": "W",  
                    "pressure\_mb": 1005.0,  
                    "pressure\_in": 29.68,  
                    "precip\_mm": 0.0,  
                    "precip\_in": 0.0,  
                    "humidity": 74,  
                    "cloud": 75,  
                    "feelslike\_c": 4.4,  
                    "feelslike\_f": 39.9,  
                    "vis\_km": 10.0,  
                    "vis\_miles": 6.0,  
                    "uv": 2.0,  
                    "gust\_mph": 33.1,  
                    "gust\_kph": 53.3  
                }  
            }  
        },  
        {  
            "query": {  
                "custom\_id": "any-internal-id",  
                "q": "London",  
                "location": {  
                    "name": "London",  
                    "region": "City of London, Greater London",  
                    "country": "United Kingdom",  
                    "lat": 51.52,  
                    "lon": \-0.11,  
                    "tz\_id": "Europe/London",  
                    "localtime\_epoch": 1673620218,  
                    "localtime": "2023-01-13 14:30"  
                },  
                "current": {  
                    "last\_updated\_epoch": 1673620200,  
                    "last\_updated": "2023-01-13 14:30",  
                    "temp\_c": 11.0,  
                    "temp\_f": 51.8,  
                    "is\_day": 1,  
                    "condition": {  
                        "text": "Partly cloudy",  
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",  
                        "code": 1003  
                    },  
                    "wind\_mph": 23.0,  
                    "wind\_kph": 37.1,  
                    "wind\_degree": 270,  
                    "wind\_dir": "W",  
                    "pressure\_mb": 1010.0,  
                    "pressure\_in": 29.83,  
                    "precip\_mm": 0.0,  
                    "precip\_in": 0.0,  
                    "humidity": 58,  
                    "cloud": 75,  
                    "feelslike\_c": 8.1,  
                    "feelslike\_f": 46.5,  
                    "vis\_km": 10.0,  
                    "vis\_miles": 6.0,  
                    "uv": 2.0,  
                    "gust\_mph": 22.4,  
                    "gust\_kph": 36.0  
                }  
            }  
        },  
        {  
            "query": {  
                "custom\_id": "us-zipcode-id-765",  
                "q": "90201",  
                "location": {  
                    "name": "Bell",  
                    "region": "California",  
                    "country": "USA",  
                    "lat": 33.97,  
                    "lon": \-118.17,  
                    "tz\_id": "America/Los\_Angeles",  
                    "localtime\_epoch": 1673620220,  
                    "localtime": "2023-01-13 6:30"  
                },  
                "current": {  
                    "last\_updated\_epoch": 1673620200,  
                    "last\_updated": "2023-01-13 06:30",  
                    "temp\_c": 10.0,  
                    "temp\_f": 50.0,  
                    "is\_day": 0,  
                    "condition": {  
                        "text": "Clear",  
                        "icon": "//cdn.weatherapi.com/weather/64x64/night/113.png",  
                        "code": 1000  
                    },  
                    "wind\_mph": 2.2,  
                    "wind\_kph": 3.6,  
                    "wind\_degree": 10,  
                    "wind\_dir": "N",  
                    "pressure\_mb": 1020.0,  
                    "pressure\_in": 30.13,  
                    "precip\_mm": 0.0,  
                    "precip\_in": 0.0,  
                    "humidity": 74,  
                    "cloud": 0,  
                    "feelslike\_c": 10.3,  
                    "feelslike\_f": 50.5,  
                    "vis\_km": 16.0,  
                    "vis\_miles": 9.0,  
                    "uv": 1.0,  
                    "gust\_mph": 3.6,  
                    "gust\_kph": 5.8  
                }  
            }  
        }  
    \]  
}  
                              
                       

## **API Error Codes**

If there is an error, API response contains error message including error code for following 4xx HTTP Status codes.

| HTTP Status Code | Error code | Description |
| ----- | ----- | ----- |
| 401 | 1002 | API key not provided. |
| 400 | 1003 | Parameter 'q' not provided. |
| 400 | 1005 | API request url is invalid |
| 400 | 1006 | No location found matching parameter 'q' |
| 401 | 2006 | API key provided is invalid |
| 403 | 2007 | API key has exceeded calls per month quota. |
| 403 | 2008 | API key has been disabled. |
| 403 | 2009 | API key does not have access to the resource. Please check pricing page for what is allowed in your API subscription plan. |
| 400 | 9000 | Json body passed in bulk request is invalid. Please make sure it is valid json with utf-8 encoding. |
| 400 | 9001 | Json body contains too many locations for bulk request. Please keep it below 50 in a single request. |
| 400 | 9999 | Internal application error. |

# **APIs**

## **Realtime API**

Current weather or realtime weather API method allows a user to get up to date current weather information in json and xml. The data is returned as a Current Object.

Current object contains current or realtime weather information for a given city.

| Field | Data Type | Description |
| ----- | ----- | ----- |
| last\_updated | string | Local time when the real time data was updated. |
| last\_updated\_epoch | int | Local time when the real time data was updated in unix time. |
| temp\_c | decimal | Temperature in celsius |
| temp\_f | decimal | Temperature in fahrenheit |
| feelslike\_c | decimal | Feels like temperature in celsius |
| feelslike\_f | decimal | Feels like temperature in fahrenheit |
| windchill\_c | decimal | Windchill temperature in celcius |
| windchill\_f | decimal | Windchill temperature in fahrenheit |
| heatindex\_c | decimal | Heat index in celcius |
| heatindex\_f | decimal | Heat index in fahrenheit |
| dewpoint\_c | decimal | Dew point in celcius |
| dewpoint\_f | decimal | Dew point in fahrenheit |
| condition:text | string | Weather condition text |
| condition:icon | string | Weather icon url |
| condition:code | int | Weather condition unique code. |
| wind\_mph | decimal | Wind speed in miles per hour |
| wind\_kph | decimal | Wind speed in kilometer per hour |
| wind\_degree | int | Wind direction in degrees |
| wind\_dir | string | Wind direction as 16 point compass. e.g.: NSW |
| pressure\_mb | decimal | Pressure in millibars |
| pressure\_in | decimal | Pressure in inches |
| precip\_mm | decimal | Precipitation amount in millimeters |
| precip\_in | decimal | Precipitation amount in inches |
| humidity | int | Humidity as percentage |
| cloud | int | Cloud cover as percentage |
| is\_day | int | 1 \= Yes 0 \= No Whether to show day condition icon or night icon |
| uv | decimal | UV Index |
| gust\_mph | decimal | Wind gust in miles per hour |
| gust\_kph | decimal | Wind gust in kilometer per hour |
| short\_rad | decimal | (Available for paid plan users only) Shortwave solar radiation or Global horizontal irradiation (GHI) W/m² |
| diff\_rad | decimal | (Available for paid plan users only) Diffuse Horizontal Irradiation (DHI) W/m² |
| dni | decimal | (Available for paid plan users only) Direct Normal Irradiance (DNI) W/m² |
| gti | decimal | (Available for paid plan users only) Global Tilted Irradiance (GTI) W/m² |
| pollen (Available for paid plan users only) | element | See [pollen element](https://www.weatherapi.com/docs/#intro-pollen) |

## **Forecast API**

Forecast weather API method returns, depending upon your subscription plan level, upto next 14 day weather forecast and weather alert as json or xml. The data is returned as a Forecast Object.

Forecast object contains astronomy data, day weather forecast and hourly interval weather information for a given city.

forecastday: Parent element

forecastday \-\> day: 'day' element inside forecastday contains max/min temperature, average temperature

forecastday \-\> astro  
 forecastday \-\> hour:

| Forecastday | Parent element |
| ----- | ----- |
| forecastday \-\> day | day element contains: Max, min and average temperature Max wind speed Total precipitation Day weather condition |
| forecastday \-\> astro | astro element contains sunrise, sunset, moonrise, moonphase and moonset data |
| forecastday \-\> hour | hour element contains hour by hour weather forecast information |

#### **forecastday**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| date | string | Forecast date |
| date\_epoch | int | Forecast date as unix time. |
| day | element | See day element |
| astro | element | See astro element |
| air\_quality | element | See [aqi element](https://www.weatherapi.com/docs/#intro-aqi) |
| pollen | element | See [pollen element](https://www.weatherapi.com/docs/#intro-pollen) |
| hour | element | See hour element |

#### **day Element**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| maxtemp\_c | decimal | Maximum temperature in celsius for the day. |
| maxtemp\_f | decimal | Maximum temperature in fahrenheit for the day |
| mintemp\_c | decimal | Minimum temperature in celsius for the day |
| mintemp\_f | decimal | Minimum temperature in fahrenheit for the day |
| avgtemp\_c | decimal | Average temperature in celsius for the day |
| avgtemp\_f | decimal | Average temperature in fahrenheit for the day |
| maxwind\_mph | decimal | Maximum wind speed in miles per hour |
| maxwind\_kph | decimal | Maximum wind speed in kilometer per hour |
| totalprecip\_mm | decimal | Total precipitation in milimeter |
| totalprecip\_in | decimal | Total precipitation in inches |
| totalsnow\_cm | decimal | Total snowfall in centimeters |
| avgvis\_km | decimal | Average visibility in kilometer |
| avgvis\_miles | decimal | Average visibility in miles |
| avghumidity | int | Average humidity as percentage |
| [condition:text](https://www.weatherapi.com/docs/#weather-icons) | string | Weather condition text |
| [condition:icon](https://www.weatherapi.com/docs/#weather-icons) | string | Weather condition icon |
| [condition:code](https://www.weatherapi.com/docs/#weather-icons) | int | Weather condition code |
| uv | decimal | UV Index |
| daily\_will\_it\_rain | int | 1 \= Yes 0 \= No Will it will rain or not |
| daily\_will\_it\_snow | int | 1 \= Yes 0 \= No Will it snow or not |
| daily\_chance\_of\_rain | int | Chance of rain as percentage |
| daily\_chance\_of\_snow | int | Chance of snow as percentage |

#### **astro Element**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| sunrise | string | Sunrise time |
| sunset | string | Sunset time |
| moonrise | string | Moonrise time |
| moonset | string | Moonset time |
| moon\_phase | string | Moon phases. Value returned: New Moon Waxing Crescent First Quarter Waxing Gibbous Full Moon Waning Gibbous Last Quarter Waning Crescent |
| moon\_illumination | decimal | Moon illumination as % |
| is\_moon\_up | int | 1 \= Yes or 0 \=No Determine if the moon is currently up, based on moon set and moon rise time at the provided location and date. |
| is\_sun\_up | int | 1 \= Yes or 0 \=No Determine if the sun is currently up, based on sunset and sunrise time at the provided location and date. |

#### **hour Element**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| time\_epoch | int | Time as epoch |
| time | string | Date and time |
| temp\_c | decimal | Temperature in celsius |
| temp\_f | decimal | Temperature in fahrenheit |
| [condition:text](https://www.weatherapi.com/docs/#weather-icons) | string | Weather condition text |
| [condition:icon](https://www.weatherapi.com/docs/#weather-icons) | string | Weather condition icon |
| [condition:code](https://www.weatherapi.com/docs/#weather-icons) | int | Weather condition code |
| wind\_mph | decimal | Maximum wind speed in miles per hour |
| wind\_kph | decimal | Maximum wind speed in kilometer per hour |
| wind\_degree | int | Wind direction in degrees |
| wind\_dir | string | Wind direction as 16 point compass. e.g.: NSW |
| pressure\_mb | decimal | Pressure in millibars |
| pressure\_in | decimal | Pressure in inches |
| precip\_mm | decimal | Precipitation amount in millimeters |
| precip\_in | decimal | Precipitation amount in inches |
| snow\_cm | decimal | Snowfall in centimeters |
| humidity | int | Humidity as percentage |
| cloud | int | Cloud cover as percentage |
| feelslike\_c | decimal | Feels like temperature as celcius |
| feelslike\_f | decimal | Feels like temperature as fahrenheit |
| windchill\_c | decimal | Windchill temperature in celcius |
| windchill\_f | decimal | Windchill temperature in fahrenheit |
| heatindex\_c | decimal | Heat index in celcius |
| heatindex\_f | decimal | Heat index in fahrenheit |
| dewpoint\_c | decimal | Dew point in celcius |
| dewpoint\_f | decimal | Dew point in fahrenheit |
| will\_it\_rain | int | 1 \= Yes 0 \= No Will it will rain or not |
| will\_it\_snow | int | 1 \= Yes 0 \= No Will it snow or not |
| is\_day | int | 1 \= Yes 0 \= No Whether to show day condition icon or night icon |
| vis\_km | decimal | Visibility in kilometer |
| vis\_miles | decimal | Visibility in miles |
| chance\_of\_rain | int | Chance of rain as percentage |
| chance\_of\_snow | int | Chance of snow as percentage |
| gust\_mph | decimal | Wind gust in miles per hour |
| gust\_kph | decimal | Wind gust in kilometer per hour |
| uv | decimal | UV Index |
| short\_rad | decimal | (Available for paid plan users only) Shortwave solar radiation or Global horizontal irradiation (GHI) W/m² |
| diff\_rad | decimal | (Available for paid plan users only) Diffuse Horizontal Irradiation (DHI) W/m² |
| dni | decimal | (Available for paid plan users only) Direct Normal Irradiance (DNI) W/m² |
| gti | decimal | (Available for paid plan users only) Global Tilted Irradiance (GTI) W/m² |
| et0 (Business plan and above) | decimal | Evapotranspiration |
| air\_quality | element | See [aqi element](https://www.weatherapi.com/docs/#intro-aqi) |
| pollen | element | See [pollen element](https://www.weatherapi.com/docs/#intro-pollen) |

## **History API**

History weather API method returns, depending upon your subscription plan level, historical weather for a date on or after 1st Jan, 2010 as json and xml. The data is returned as a Forecast Object.

For Enterprise plan users we also return historical Solar Irradiance (from 1st Jan 2010 onwards), Evapotranspiration (from 1st Jan 2010 onwards), Pollen (from 1st Jan 2010 onwards) and Air Quality data (from 1st March 2021 onwards).

Forecast object contains astronomy data, day weather forecast and hourly interval weather information for a given city.

forecastday: Parent element

forecastday \-\> day: 'day' element inside forecastday contains max/min temperature, average temperature

forecastday \-\> astro  
 forecastday \-\> hour:

| Forecastday | Parent element |
| ----- | ----- |
| forecastday \-\> day | day element contains: Max, min and average temperature Max wind speed Total precipitation Day weather condition Air Quality data Pollen data |
| forecastday \-\> astro | astro element contains sunrise, sunset, moonrise and moonset data |
| forecastday \-\> hour | hour element contains hour by hour weather forecast information |

#### **forecastday**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| date | string | Forecast date |
| date\_epoch | int | Forecast date as unix time. |
| day | element | See day element |
| astro | element | See astro element |
| air\_quality | element | See [aqi element](https://www.weatherapi.com/docs/#intro-aqi) |
| pollen (Enterprise plan) | element | See [pollen element](https://www.weatherapi.com/docs/#intro-pollen) |
| hour | element | See hour element |

#### **day Element**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| maxtemp\_c | decimal | Maximum temperature in celsius for the day. |
| maxtemp\_f | decimal | Maximum temperature in fahrenheit for the day |
| mintemp\_c | decimal | Minimum temperature in celsius for the day |
| mintemp\_f | decimal | Minimum temperature in fahrenheit for the day |
| avgtemp\_c | decimal | Average temperature in celsius for the day |
| avgtemp\_f | decimal | Average temperature in fahrenheit for the day |
| maxwind\_mph | decimal | Maximum wind speed in miles per hour |
| maxwind\_kph | decimal | Maximum wind speed in kilometer per hour |
| totalprecip\_mm | decimal | Total precipitation in milimeter |
| totalprecip\_in | decimal | Total precipitation in inches |
| totalsnow\_cm | decimal | Total snowfall in centimeters |
| avgvis\_km | decimal | Average visibility in kilometer |
| avgvis\_miles | decimal | Average visibility in miles |
| avghumidity | int | Average humidity as percentage |
| [condition:text](https://www.weatherapi.com/docs/#weather-icons) | string | Weather condition text |
| [condition:icon](https://www.weatherapi.com/docs/#weather-icons) | string | Weather condition icon |
| [condition:code](https://www.weatherapi.com/docs/#weather-icons) | int | Weather condition code |
| uv | decimal | UV Index |
| daily\_will\_it\_rain | int | 1 \= Yes 0 \= No Will it will rain or not |
| daily\_will\_it\_snow | int | 1 \= Yes 0 \= No Will it snow or not |
| daily\_chance\_of\_rain | int | Chance of rain as percentage |
| daily\_chance\_of\_snow | int | Chance of snow as percentage |

#### **astro Element**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| sunrise | string | Sunrise time |
| sunset | string | Sunset time |
| moonrise | string | Moonrise time |
| moonset | string | Moonset time |
| moon\_phase | string | Moon phases. Value returned: New Moon Waxing Crescent First Quarter Waxing Gibbous Full Moon Waning Gibbous Last Quarter Waning Crescent |
| moon\_illumination | decimal | Moon illumination as % |
| is\_moon\_up | int | 1 \= Yes or 0 \=No Determine if the moon is currently up, based on moon set and moon rise time at the provided location and date. |
| is\_sun\_up | int | 1 \= Yes or 0 \=No Determine if the sun is currently up, based on sunset and sunrise time at the provided location and date. |

#### **hour Element**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| time\_epoch | int | Time as epoch |
| time | string | Date and time |
| temp\_c | decimal | Temperature in celsius |
| temp\_f | decimal | Temperature in fahrenheit |
| [condition:text](https://www.weatherapi.com/docs/#weather-icons) | string | Weather condition text |
| [condition:icon](https://www.weatherapi.com/docs/#weather-icons) | string | Weather condition icon |
| [condition:code](https://www.weatherapi.com/docs/#weather-icons) | int | Weather condition code |
| wind\_mph | decimal | Maximum wind speed in miles per hour |
| wind\_kph | decimal | Maximum wind speed in kilometer per hour |
| wind\_degree | int | Wind direction in degrees |
| wind\_dir | string | Wind direction as 16 point compass. e.g.: NSW |
| pressure\_mb | decimal | Pressure in millibars |
| pressure\_in | decimal | Pressure in inches |
| precip\_mm | decimal | Precipitation amount in millimeters |
| precip\_in | decimal | Precipitation amount in inches |
| snow\_cm | decimal | Snowfall in centimeters |
| humidity | int | Humidity as percentage |
| cloud | int | Cloud cover as percentage |
| feelslike\_c | decimal | Feels like temperature as celcius |
| feelslike\_f | decimal | Feels like temperature as fahrenheit |
| windchill\_c | decimal | Windchill temperature in celcius |
| windchill\_f | decimal | Windchill temperature in fahrenheit |
| heatindex\_c | decimal | Heat index in celcius |
| heatindex\_f | decimal | Heat index in fahrenheit |
| dewpoint\_c | decimal | Dew point in celcius |
| dewpoint\_f | decimal | Dew point in fahrenheit |
| will\_it\_rain | int | 1 \= Yes 0 \= No Will it will rain or not |
| will\_it\_snow | int | 1 \= Yes 0 \= No Will it snow or not |
| is\_day | int | 1 \= Yes 0 \= No Whether to show day condition icon or night icon |
| vis\_km | decimal | Visibility in kilometer |
| vis\_miles | decimal | Visibility in miles |
| chance\_of\_rain | int | Chance of rain as percentage |
| chance\_of\_snow | int | Chance of snow as percentage |
| gust\_mph | decimal | Wind gust in miles per hour |
| gust\_kph | decimal | Wind gust in kilometer per hour |
| uv | decimal | UV Index |
| short\_rad (Enterprise plan) | decimal | Shortwave solar radiation or Global horizontal irradiation (GHI) W/m² |
| diff\_rad (Enterprise plan) | decimal | Diffuse Horizontal Irradiation (DHI) W/m² |
| dni (Enterprise plan) | decimal | Direct Normal Irradiance (DNI) W/m² |
| direct\_rad (Enterprise plan) | decimal | Direct Radiation W/m² |
| wind\_mph\_100 (Enterprise plan) | decimal | Maximum wind speed at 100 mt in miles per hour |
| wind\_kph\_100 (Enterprise plan) | decimal | Maximum wind speed at 100 mt in kilometer per hour |
| wind\_degree\_100 (Enterprise plan) | int | Wind direction in degrees at 100 mt height |
| wind\_dir\_100 (Enterprise plan) | string | Wind direction as 16 point compass at 100 mt height. e.g.: NSW |
| et0 (Enterprise plan) | decimal | Evapotranspiration at 100 mt height. |
| air\_quality | element | See [aqi element](https://www.weatherapi.com/docs/#intro-aqi) |
| pollen (Enterprise plan) | element | See [pollen element](https://www.weatherapi.com/docs/#intro-pollen) |

## **Alerts API**

Alerts API returns alerts and warnings issued by government agencies (USA, UK, Europe and Rest of the World) as an array if available for the location provided json and xml. The data is returned as an Alerts Object.

Note: Some of the alerts may be in local language of the location.

| Field | Data Type | Description |
| ----- | ----- | ----- |
| headline | string | Alert headline |
| msgType | string | Type of alert |
| severity | string | Severity of alert |
| urgency | string | Urgency |
| areas | string | Areas covered |
| category | string | Category |
| certainty | string | Certainty |
| event | string | Event |
| note | string | Note |
| effective | date | Effective |
| expires | string | Expires |
| desc | string | Description |
| instruction | string | Instruction |

#### **Example response of alerts**

                           "alerts":{  
    "alert":\[  
        {  
        "headline":"Flood Warning issued January 05 at 9:47PM EST until January 07 at 6:15AM EST by NWS",  
        "msgtype":"Alert",  
        "severity":"Moderate",  
        "urgency":"Expected",  
        "areas":"Calhoun; Lexington; Richland",  
        "category":"Met",  
        "certainty":"Likely",  
        "event":"Flood Warning",  
        "note":"Alert for Calhoun; Lexington; Richland (South Carolina) Issued by the National Weather Service",  
        "effective":"2021-01-05T21:47:00-05:00",  
        "expires":"2021-01-07T06:15:00-05:00",  
        "desc":"...The Flood Warning continues for the following rivers in South\\nCarolina...\\nCongaree River At Carolina Eastman affecting Richland, Calhoun\\nand Lexington Counties.\\nCongaree River At Congaree National Park-Gadsden affecting\\nCalhoun and Richland Counties.\\nNorth Fork Edisto River At Orangeburg affecting Orangeburg County.\\n...The Flood Warning is now in effect until Thursday morning...\\nThe Flood Warning continues for\\nthe Congaree River At Carolina Eastman.\\n\* Until Thursday morning.\\n\* At 9:28 PM EST Tuesday the stage was 115.6 feet.\\n\* Flood stage is 115.0 feet.\\n\* Minor flooding is occurring and minor flooding is forecast.\\n\* Recent Activity...The maximum river stage in the 24 hours ending\\nat 9:28 PM EST Tuesday was 118.2 feet.\\n\* Forecast...The river will rise to 115.7 feet just after midnight\\ntonight. It will then fall below flood stage tomorrow morning to\\n114.2 feet and begin rising again tomorrow evening. It will rise\\nto 114.3 feet early Thursday morning. It will then fall again and\\nremain below flood stage.\\n\* Impact...At 115.0 feet, Flooding occurs in low lying areas of the\\nCarolina Eastman Facility and at the Congaree National Park.\\n\* Flood History...This crest compares to a previous crest of 116.3\\nfeet on 12/03/2020.\\n&&",  
        "instruction":"A Flood Warning means that flooding is imminent or occurring. All\\ninterested parties should take necessary precautions immediately.\\nMotorists should not attempt to drive around barricades or drive\\ncars through flooded areas.\\nCaution is urged when walking near riverbanks.\\nAdditional information is available at www.weather.gov.\\nThe next statement will be issued Wednesday morning at 1000 AM EST."  
        },  
        {  
        "headline":"Flood Warning issued January 05 at 9:47PM EST until January 09 at 4:00AM EST by NWS",  
        "msgtype":"Alert",  
        "severity":"Moderate",  
        "urgency":"Expected",  
        "areas":"Calhoun; Richland",  
        "category":"Met",  
        "certainty":"Likely",  
        "event":"Flood Warning",  
        "note":"Alert for Calhoun; Richland (South Carolina) Issued by the National Weather Service",  
        "effective":"2021-01-05T21:47:00-05:00",  
        "expires":"2021-01-09T04:00:00-05:00",  
        "desc":"...The Flood Warning continues for the following rivers in South\\nCarolina...\\nCongaree River At Carolina Eastman affecting Richland, Calhoun\\nand Lexington Counties.\\nCongaree River At Congaree National Park-Gadsden affecting\\nCalhoun and Richland Counties.\\nNorth Fork Edisto River At Orangeburg affecting Orangeburg County.\\n...The Flood Warning is now in effect until early Saturday morning...\\nThe Flood Warning continues for\\nthe Congaree River At Congaree National Park-Gadsden.\\n\* Until late Friday night.\\n\* At 9:00 PM EST Tuesday the stage was 16.5 feet.\\n\* Flood stage is 15.0 feet.\\n\* Minor flooding is occurring and minor flooding is forecast.\\n\* Recent Activity...The maximum river stage in the 24 hours ending\\nat 9:00 PM EST Tuesday was 17.2 feet.\\n\* Forecast...The river is expected to fall below flood stage early\\nFriday morning and continue falling to 12.4 feet Sunday evening.\\n\* Impact...At 15.0 feet, Flooding begins in the Congaree National\\nPark. This will begin to produce flooding of portions of the lower\\nboardwalk.\\n\* Impact...At 17.0 feet, The access road to the Sandy Run\\nsubdivision becomes flooded. The lower boardwalk in the Congaree\\nNational Park becomes flooded by Cedar Creek.\\n\* Impact...At 18.0 feet, Several homes in the Sandy Run subdivision\\nalong the river become flooded. At 18 feet the river covers the\\nWeston Lake overlook in the Congaree National Park. Between 18 and\\n18.5 feet the river begins to cover sections of the elevated\\nboardwalk.\\n\* Flood History...This crest compares to a previous crest of 16.3\\nfeet on 12/03/2020.\\n&&",  
        "instruction":"A Flood Warning means that flooding is imminent or occurring. All\\ninterested parties should take necessary precautions immediately.\\nMotorists should not attempt to drive around barricades or drive\\ncars through flooded areas.\\nCaution is urged when walking near riverbanks.\\nAdditional information is available at www.weather.gov.\\nThe next statement will be issued Wednesday morning at 1000 AM EST."  
        }  
    \]  
}  
                              
                       

## **Marine Weather API**

Marine weather API method returns upto next 7 day (depending upon your subscription plan level) marine and sailing weather forecast and tide data (depending upon your price plan level) as json or xml. The data is returned as a Marine Object.

Marine object, depending upon your price plan level, contains astronomy data, day weather forecast and hourly interval weather information and tide data for a given sea/ocean point.

forecastday: Parent element

forecastday \-\> day: 'day' element inside forecastday contains max/min temperature, average temperature

forecastday \-\> astro  
 forecastday \-\> tide  
 forecastday \-\> hour:

| Forecastday | Parent element |
| ----- | ----- |
| forecastday \-\> day | day element contains: Max, min and average temperature Max wind speed Total precipitation Day weather condition |
| forecastday \-\> astro | astro element contains sunrise, sunset, moonrise and moonset data |
| forecastday \-\> tides | tides element contains high and low tide data |
| forecastday \-\> hour | hour element contains hour by hour weather forecast information |

#### **forecastday**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| date | string | Forecast date |
| date\_epoch | int | Forecast date as unix time. |
| day | element | See day element |
| astro | element | See astro element |
| tides | element | See tides element |
| hour | element | See hour element |

#### **day Element**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| maxtemp\_c | decimal | Maximum temperature in celsius for the day. |
| maxtemp\_f | decimal | Maximum temperature in fahrenheit for the day |
| mintemp\_c | decimal | Minimum temperature in celsius for the day |
| mintemp\_f | decimal | Minimum temperature in fahrenheit for the day |
| avgtemp\_c | decimal | Average temperature in celsius for the day |
| avgtemp\_f | decimal | Average temperature in fahrenheit for the day |
| maxwind\_mph | decimal | Maximum wind speed in miles per hour |
| maxwind\_kph | decimal | Maximum wind speed in kilometer per hour |
| totalprecip\_mm | decimal | Total precipitation in milimeter |
| totalprecip\_in | decimal | Total precipitation in inches |
| avgvis\_km | decimal | Average visibility in kilometer |
| avgvis\_miles | decimal | Average visibility in miles |
| avghumidity | int | Average humidity as percentage |
| [condition:text](https://www.weatherapi.com/docs/#weather-icons) | string | Weather condition text |
| [condition:icon](https://www.weatherapi.com/docs/#weather-icons) | string | Weather condition icon |
| [condition:code](https://www.weatherapi.com/docs/#weather-icons) | int | Weather condition code |
| uv | decimal | UV Index |

#### **astro Element**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| sunrise | string | Sunrise time |
| sunset | string | Sunset time |
| moonrise | string | Moonrise time |
| moonset | string | Moonset time |
| moon\_phase | string | Moon phases. Value returned: New Moon Waxing Crescent First Quarter Waxing Gibbous Full Moon Waning Gibbous Last Quarter Waning Crescent |
| moon\_illumination | decimal | Moon illumination as % |
| is\_moon\_up | int | 1 \= Yes or 0 \=No Determine if the moon is currently up, based on moon set and moon rise time at the provided location and date. |
| is\_sun\_up | int | 1 \= Yes or 0 \=No Determine if the sun is currently up, based on sunset and sunrise time at the provided location and date. |

#### **tides Element**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| tide\_time | string | Local tide time |
| tide\_height\_mt | float | Tide height in mt |
| tide\_type | string | Type of tide i.e. High or Low |

#### **hour Element**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| time\_epoch | int | Time as epoch |
| time | string | Date and time |
| temp\_c | decimal | Temperature in celsius |
| temp\_f | decimal | Temperature in fahrenheit |
| [condition:text](https://www.weatherapi.com/docs/#weather-icons) | string | Weather condition text |
| [condition:icon](https://www.weatherapi.com/docs/#weather-icons) | string | Weather condition icon |
| [condition:code](https://www.weatherapi.com/docs/#weather-icons) | int | Weather condition code |
| wind\_mph | decimal | Maximum wind speed in miles per hour |
| wind\_kph | decimal | Maximum wind speed in kilometer per hour |
| wind\_degree | int | Wind direction in degrees |
| wind\_dir | string | Wind direction as 16 point compass. e.g.: NSW |
| pressure\_mb | decimal | Pressure in millibars |
| pressure\_in | decimal | Pressure in inches |
| precip\_mm | decimal | Precipitation amount in millimeters |
| precip\_in | decimal | Precipitation amount in inches |
| humidity | int | Humidity as percentage |
| cloud | int | Cloud cover as percentage |
| feelslike\_c | decimal | Feels like temperature as celcius |
| feelslike\_f | decimal | Feels like temperature as fahrenheit |
| windchill\_c | decimal | Windchill temperature in celcius |
| windchill\_f | decimal | Windchill temperature in fahrenheit |
| heatindex\_c | decimal | Heat index in celcius |
| heatindex\_f | decimal | Heat index in fahrenheit |
| dewpoint\_c | decimal | Dew point in celcius |
| dewpoint\_f | decimal | Dew point in fahrenheit |
| is\_day | int | 1 \= Yes 0 \= No Whether to show day condition icon or night icon |
| vis\_km | decimal | Visibility in kilometer |
| vis\_miles | decimal | Visibility in miles |
| gust\_mph | decimal | Wind gust in miles per hour |
| gust\_kph | decimal | Wind gust in kilometer per hour |
| sig\_ht\_mt | decimal | Significant wave height in metres |
| swell\_ht\_mt | decimal | Swell wave height in metres |
| swell\_ht\_ft | decimal | Swell wave height in feet |
| swell\_dir | decimal | Swell direction in degrees |
| swell\_dir\_16\_point | decimal | Swell direction in 16 point compass |
| swell\_period\_secs | decimal | Swell period in seconds |
| water\_temp\_c (Pro+ plan and above) | decimal | Water temperature in Celcius |
| water\_temp\_f (Pro+ plan and above) | decimal | Water temperature in Fahrenheit |
| uv | decimal | UV Index |

## **Future Weather API**

Future weather API method returns weather in a 3 hourly interval in future for a date between 14 days and 300 days from today in the future.

Forecast object contains astronomy data, day weather forecast and hourly interval weather information for a given city.

forecastday: Parent element

forecastday \-\> day: 'day' element inside forecastday contains max/min temperature, average temperature

forecastday \-\> astro  
 forecastday \-\> hour:

| Forecastday | Parent element |
| ----- | ----- |
| forecastday \-\> day | day element contains: Max, min and average temperature Max wind speed Total precipitation Day weather condition |
| forecastday \-\> astro | astro element contains sunrise, sunset, moonrise and moonset data |
| forecastday \-\> hour | hour element contains hour by hour weather forecast information |

#### **forecastday**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| date | string | Forecast date |
| date\_epoch | int | Forecast date as unix time. |
| day | element | See day element |
| astro | element | See astro element |
| hour | element | See hour element |

#### **day Element**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| maxtemp\_c | decimal | Maximum temperature in celsius for the day. |
| maxtemp\_f | decimal | Maximum temperature in fahrenheit for the day |
| mintemp\_c | decimal | Minimum temperature in celsius for the day |
| mintemp\_f | decimal | Minimum temperature in fahrenheit for the day |
| avgtemp\_c | decimal | Average temperature in celsius for the day |
| avgtemp\_f | decimal | Average temperature in fahrenheit for the day |
| maxwind\_mph | decimal | Maximum wind speed in miles per hour |
| maxwind\_kph | decimal | Maximum wind speed in kilometer per hour |
| totalprecip\_mm | decimal | Total precipitation in milimeter |
| totalprecip\_in | decimal | Total precipitation in inches |
| avgvis\_km | decimal | Average visibility in kilometer |
| avgvis\_miles | decimal | Average visibility in miles |
| avghumidity | int | Average humidity as percentage |
| [condition:text](https://www.weatherapi.com/docs/#weather-icons) | string | Weather condition text |
| [condition:icon](https://www.weatherapi.com/docs/#weather-icons) | string | Weather condition icon |
| [condition:code](https://www.weatherapi.com/docs/#weather-icons) | int | Weather condition code |
| uv | decimal | UV Index |

#### **astro Element**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| sunrise | string | Sunrise time |
| sunset | string | Sunset time |
| moonrise | string | Moonrise time |
| moonset | string | Moonset time |
| moon\_phase | string | Moon phases. Value returned: New Moon Waxing Crescent First Quarter Waxing Gibbous Full Moon Waning Gibbous Last Quarter Waning Crescent |
| moon\_illumination | decimal | Moon illumination as % |
| is\_moon\_up | int | 1 \= Yes or 0 \=No Determine if the moon is currently up, based on moon set and moon rise time at the provided location and date. |
| is\_sun\_up | int | 1 \= Yes or 0 \=No Determine if the sun is currently up, based on sunset and sunrise time at the provided location and date. |

#### **hour Element**

| Field | Data Type | Description |
| ----- | ----- | ----- |
| time\_epoch | int | Time as epoch |
| time | string | Date and time |
| temp\_c | decimal | Temperature in celsius |
| temp\_f | decimal | Temperature in fahrenheit |
| [condition:text](https://www.weatherapi.com/docs/#weather-icons) | string | Weather condition text |
| [condition:icon](https://www.weatherapi.com/docs/#weather-icons) | string | Weather condition icon |
| [condition:code](https://www.weatherapi.com/docs/#weather-icons) | int | Weather condition code |
| wind\_mph | decimal | Maximum wind speed in miles per hour |
| wind\_kph | decimal | Maximum wind speed in kilometer per hour |
| wind\_degree | int | Wind direction in degrees |
| wind\_dir | string | Wind direction as 16 point compass. e.g.: NSW |
| pressure\_mb | decimal | Pressure in millibars |
| pressure\_in | decimal | Pressure in inches |
| precip\_mm | decimal | Precipitation amount in millimeters |
| precip\_in | decimal | Precipitation amount in inches |
| humidity | int | Humidity as percentage |
| cloud | int | Cloud cover as percentage |
| feelslike\_c | decimal | Feels like temperature as celcius |
| feelslike\_f | decimal | Feels like temperature as fahrenheit |
| windchill\_c | decimal | Windchill temperature in celcius |
| windchill\_f | decimal | Windchill temperature in fahrenheit |
| heatindex\_c | decimal | Heat index in celcius |
| heatindex\_f | decimal | Heat index in fahrenheit |
| dewpoint\_c | decimal | Dew point in celcius |
| dewpoint\_f | decimal | Dew point in fahrenheit |
| will\_it\_rain | int | 1 \= Yes 0 \= No Will it will rain or not |
| will\_it\_snow | int | 1 \= Yes 0 \= No Will it snow or not |
| is\_day | int | 1 \= Yes 0 \= No Whether to show day condition icon or night icon |
| vis\_km | decimal | Visibility in kilometer |
| vis\_miles | decimal | Visibility in miles |

## **Search/Autocomplete API**

WeatherAPI.com Search or Autocomplete API returns matching cities and towns as an array of [Location](https://www.weatherapi.com/docs/#intro-location) object.

## **IP Lookup API**

IP Lookup API method allows a user to get up to date information for an IP address in json and xml.

| Field | Data Type | Description |
| ----- | ----- | ----- |
| ip | string | IP address |
| type | string | ipv4 or ipv6 |
| continent\_code | string | Continent code |
| continent\_name | string | Continent name |
| country\_code | string | Country code |
| country\_name | string | Name of country |
| is\_eu | bool | true or false |
| geoname\_id | string | Geoname ID |
| city | string | City name |
| region | string | Region name |
| lat | decimal | Latitude in decimal degree |
| lon | decimal | Longitude in decimal degree |
| tz\_id | string | Time zone |

## **Astronomy API**

Astronomy API method allows a user to get up to date information for sunrise, sunset, moonrise, moonset, moon phase and illumination in json and xml.

| Field | Data Type | Description |
| ----- | ----- | ----- |
| sunrise | string | Sunrise local time |
| sunset | string | Sunset local time |
| moonrise | string | Moonrise local time |
| moonset | string | Moonset local time |
| moon\_phase | string | Moon phases. Value returned: New Moon Waxing Crescent First Quarter Waxing Gibbous Full Moon Waning Gibbous Last Quarter Waning Crescent |
| moon\_illumination | int | Moon illumination |
| is\_moon\_up | int | 1 \= Yes or 0 \=No Determine if the moon is currently up, based on moon set and moon rise time at the provided location and date. |
| is\_sun\_up | int | 1 \= Yes or 0 \=No Determine if the sun is currently up, based on sunset and sunrise time at the provided location and date. |

## **Time Zone API**

Time Zone API method allows a user to get up to date time zone and local time information in json and xml.

| Field | Data Type | Description |
| ----- | ----- | ----- |
| tz\_id | string | Time zone id |
| localtime\_epoch | int | Local time in epoch. |
| localtime | string | Local time in yyyy-MM-dd HH:mm format |

## **Sports API**

Sports API method allows a user to get listing of all upcoming sports events for football, cricket and golf in json and xml.

| Field | Data Type | Description |
| ----- | ----- | ----- |
| stadium | string | Name of stadium |
| country | int | Country |
| region | string | Region |
| tournament | string | Tournament name |
| start | string | Start local date and time for event in yyyy-MM-dd HH:mm format. |
| match | string | Match name |

## **Example**

WeatherAPI.com API is so easy to implement. Look at following examples on how you can form a request to get data either through a web browser or in your application.

1. So to get current weather for London: JSON: http://api.weatherapi.com/v1/current.json?key=\<YOUR\_API\_KEY\>\&q=London  
2.   
    XML: http://api.weatherapi.com/v1/current.xml?key=\<YOUR\_API\_KEY\>\&q=London  
   To get 7 day weather for US Zipcode 07112: JSON: http://api.weatherapi.com/v1/forecast.json?key=\<YOUR\_API\_KEY\>\&q=07112\&days=7  
3.   
    XML: http://api.weatherapi.com/v1/forecast.xml?key=\<YOUR\_API\_KEY\>\&q=07112\&days=7  
   Search for cities starting with Lond: JSON: http://api.weatherapi.com/v1/search.json?key=\<YOUR\_API\_KEY\>\&q=lond  
    XML: http://api.weatherapi.com/v1/search.xml?key=\<YOUR\_API\_KEY\>\&q=lond

## **Integrations**

Please use our [API Explorer](https://www.weatherapi.com/api-explorer.aspx) to see how the request is formed and what response to expect.

With [Note API Connector](https://noteapiconnector.com/) \+ WeatherAPI, teams can sync real-time conditions, 1–14-day forecasts, and historical weather into Notion to power weather-aware calendars, task checklists, and staffing plans across sites, jobs, or properties. They can also build risk dashboards that surface severe-weather alerts and air-quality data, and generate daily briefings or post-incident reports comparing planned work with observed conditions.

We also have SDK for popular framework/languages [available on Github for quick integrations](https://github.com/weatherapicom/).

# **Resources**

## **Weather Icons and Codes**

In the JSON response we return a condition:code which is a code for describing weather. For example clear, sunny, etc.

You may retrieve the whole condition list as JSON to implement different weather icons or apply other logic to your application. It also includes multi-language translations of weather condition text.

Multilingual Condition list URL: [https://www.weatherapi.com/docs/conditions.json](https://www.weatherapi.com/docs/conditions.json)

English Condition list URL (CSV): [https://www.weatherapi.com/docs/weather\_conditions.csv](https://www.weatherapi.com/docs/weather_conditions.csv)

English Condition list URL (JSON): [https://www.weatherapi.com/docs/weather\_conditions.json](https://www.weatherapi.com/docs/weather_conditions.json)

English Condition list URL (XML): [https://www.weatherapi.com/docs/weather\_conditions.xml](https://www.weatherapi.com/docs/weather_conditions.xml)

Please download the list and use it offline instead of directly linking into your application.

## **Link Back**

If you are on our free plan we would appreciate if you could provide a link back to our service.

##### **HTML LINK BACK CODE EXAMPLES**

You may choose any of the below HTML code and place it on the website you have provided during the Free plan upgrade.

##### **Text**

`Powered by <a href="https://www.weatherapi.com/" title="Free Weather API">WeatherAPI.com</a>`

***Preview***  
 Powered by [WeatherAPI.com](https://www.weatherapi.com/)

##### **Image**

`<a href="https://www.weatherapi.com/" title="Free Weather API"><img src='//cdn.weatherapi.com/v4/images/weatherapi_logo.png' alt="Weather data by WeatherAPI.com" border="0"></a>`

