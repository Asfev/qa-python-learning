bug = {'id': 42, 'status': 'open', 'severity': 'high'}

print(bug['status'])  #open
print(bug.get('assignee'))    #None
print(bug.get('assignee','не назначен'))  #не назначен
print('severity' in bug)  #True


bug_2 = {'id': 42, 'status': 'open'}

bug_2['status'] = 'closed'
print(bug_2)    #{'id': 42, 'status': 'closed'}  
bug_2['priority'] = 'high'
print(bug_2)    #{'id': 42, 'status': 'closed', 'priority': 'high'}
del bug_2['id']
print(bug_2)    #{'status': 'closed', 'priority': 'high'}


headers = {'Authorization': 'token abc', 'Content-Type': 'application/json'}

for key, value in headers.items():
    print(f'{key}: {value}')

# Authorization: token abc
# Content-Type: application/json


defaults = {'timeout': 5, 'retries': 3}
overrides = {'timeout': 10, 'base_url': 'https://api.example.com'}

config = defaults.copy()
config.update(overrides)
print(config)
print(len(config))
# {'timeout': 10, 'retries': 3, 'base_url': 'https://api.example.com'}
# 3

# config = {**defaults, **overrides}
# print(config)
# print(len(config))    #второй способ через распаковку словарей в новый литерал