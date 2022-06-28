from gpsdclient import GPSDClient
import matplotlib.pyplot as plt
client = GPSDClient(host="127.0.0.1")
img = plt.imread("Graph3.png")
fig, ax = plt.subplots()
ax.imshow(img, extent = [-77.08943, -77.08872, 38.93247, 38.93189])
# # get your data as json strings:
# for result in client.json_stream():
#     print(result)
# or as python dicts (optionally convert time information to `datetime` objects)
#plt.axis([-77.08940, -77.08871, 38.93239, 38.93223])
for result in client.dict_stream(convert_datetime=True):
    if result["class"] == "TPV":
        # global x
        # global y
        print("Latitude: %s" % result.get("lat", "n/a"))
        y = result.get("lat", "n/a")
        print("Longitude: %s" % result.get("lon", "n/a"))
        x = result.get("lon", "n/a")
        plt.scatter(x, y)
        plt.pause(.5)    
plt.show()
    
        
    
