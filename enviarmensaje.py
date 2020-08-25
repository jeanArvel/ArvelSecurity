import requests
iFTTTMakerSecretKey = "fhENYLysxNY7P-3fl5qCInsEilgv_SH6TjcpGMVjvWP"
# The IFTTT Maker Channel URLs as configured in your IFTTT recipes for SunRise and SunSet
iFTTTSunRiseURL = "https://maker.ifttt.com/trigger/delantero/with/key/" + iFTTTMakerSecretKey
print ("SunRise is here!")
r = requests.get(iFTTTSunRiseURL)
print ("The resulting HTTP GET status code was " + str(r.status_code))
