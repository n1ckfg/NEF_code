import json
import latk

def loadJson(filepath):
    with open(filepath, "r", encoding="utf-8") as f: 
        data = json.load(f)
        return data

filename = "record_00000006_stage2_cubic.json"
#filename = "record_00000952_stage2_cubic.json"

scaler = 100.0

outputname = filename.split(".json")[0] + ".latk"
json = loadJson(filename)
jsonStrokes = json["curves_ctl_pts"]

print("Total strokes: " + str(len(jsonStrokes)))

la = latk.Latk(init=True)

for stroke in jsonStrokes:
    newPoints = []
    for point in stroke:
        x = point[0] / scaler
        y = point[1] / scaler
        z = point[2] / scaler
        newPoints.append(latk.LatkPoint((x, y, z)))
    newStroke  =latk.LatkStroke(newPoints)
    la.layers[0].frames[0].strokes.append(newStroke)

la.write(outputname)