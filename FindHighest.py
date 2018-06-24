import json
json_file=open("c:/python/input.txt","r",encoding="utf-8")
input=json.load(json_file)
json_file.close()
print(input)
print(input["images"])
print("The Camera that has the highest image size is %s" %input["camera_id"])
print("The Highest image from Camera : %s" % max(input["images"], key=lambda item:item['file_size']))