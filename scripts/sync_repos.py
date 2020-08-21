from pathlib import Path
import os
import shutil

# copy index over

directory = os.getcwd()

p = Path(directory)
root = str(p.parents[0])

shutil.move(directory + '/src/constants/index-link-list.js', directory)
shutil.rmtree(root + '/edb_docs/src/advocacy_components')
shutil.copytree(directory + '/src/advocacy_components', root + '/edb_docs/src/advocacy_components')
shutil.rmtree(directory + '/src')
shutil.rmtree(directory + '/static/edb-icons')
shutil.copytree(root + '/edb_docs/src', directory + '/src')
shutil.copytree(root + '/edb_docs/static/edb-icons', directory + '/static/edb-icons')
os.remove(directory + '/src/constants/index-link-list.js')
shutil.move(directory + '/index-link-list.js', directory + '/src/constants')