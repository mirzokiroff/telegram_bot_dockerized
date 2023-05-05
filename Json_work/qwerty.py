import requests
import json
import yaml
import time


response = requests.get("https://jsonplaceholder.typicode.com/photos")
photos = json.loads(response.text)
photo = response.json()
start = time.time()

with open(f"../photos1.json", 'w') as file:
    json.dump(photos, file, indent=4)

with open('photo1.yaml', 'w') as f:
    yaml.dump(photo, f, indent=4)

end = time.time()
print(int(end - start))

# 0.5892980098724365 - yaml
# 0.03552412986755371 - json
from threading import Thread


def task(n):
    time.sleep(4)
    print(f'Task {n} bajarildi')


start = time.time()

oqimlar = []
for i in range(10):
    oqimlar.append(Thread(target=task, args=(i,), daemon=True))

for oqim in oqimlar:
    oqim.start()

time.sleep(6)

for oqim in oqimlar:
    oqim.join()


end = time.time()
print(int(end - start), '- seconds')