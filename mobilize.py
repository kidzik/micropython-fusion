from fusion import Fusion
import pandas as pd

ts = 0.01
fuse = Fusion(lambda x,y: y-x)

data = pd.read_table("data/sensor.txt")
rows = data.iterrows()

df = pd.DataFrame(columns=['heading','pitch','roll'])

for count, row in rows:
    fuse.update(row[14:17], row[17:20], row[20:23], ts=ts*count)
    print("Heading, Pitch, Roll: {:7.3f} {:7.3f} {:7.3f}".format(fuse.heading, fuse.pitch, fuse.roll))

    df = df.append({'heading': fuse.heading,
                    'pitch': fuse.pitch,
                    'roll': fuse.roll}, ignore_index=True)

df.to_csv("data/output.txt")
