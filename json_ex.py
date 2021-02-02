import json

with open('states.json', 'r') as f:
    states = json.load(f)

type(states)
type(states['states'])
type(states['states'][0])
type(states['states'][0]['name'])
type(states['states'][0]['name'][0])

print(states)
print(states['states'])
print(states['states'][0])
print(states['states'][0]['name'])
print(states['states'][0]['name'][0])
