# At https://www.khronos.org/registry/gles/
# At https://www.opengl.org/registry/
# [].map.call($$('ol>li'), (v) => ({name: v.innerText, href: v.children[0].href}) )

import json, urllib.request, os
all_items = json.load(open('extensions.json'))
for n, v in all_items.items():
	os.makedirs(n, exist_ok=True)
	os.chdir(n)
	for u in v:
		name = u['name'].split('\n')[0]
		href = u['href']
		print(n+': '+href+' -> '+name)
		r = urllib.request.urlopen(href).read()
		open(name+'.txt', 'wb').write(r)
	os.chdir('..')
