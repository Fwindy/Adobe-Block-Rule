import requests

url = "https://raw.githubusercontent.com/ignaciocastro/a-dove-is-dumb/main/clash.yaml"
response = requests.get(url)
content = response.text

lines = content.splitlines()
comments = []
domains = []

in_payload_section = False

for line in lines:
    if line.startswith('#'):
        comments.append(line)
    elif line.strip() == 'payload:':
        in_payload_section = True
    elif in_payload_section and line.strip().startswith('- DOMAIN,'):
        domains.append(line.replace("DOMAIN,", "'") + "'")

output = '\n'.join(comments) + '\npayload:\n' + '\n'.join(domains)

with open('clash.yaml', 'w') as file:
    file.write(output)
