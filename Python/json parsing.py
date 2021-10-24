import json

input = '''[
	{	"id" : "001",
		"x" : "2",
		"name" : "Chuck"
	},
	{	"id" : "009",
		"x" : "2",
		"name" : "Duck"
	}
]'''

info = json.loads(input)

print('User count:', len(info))
print(info)
for item in info:
	print(item)