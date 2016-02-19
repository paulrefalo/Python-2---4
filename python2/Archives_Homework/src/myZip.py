import os
import zipfile
from os import listdir
from os.path import isfile, join
import shutil
import glob
    
def zipDir(path):
    """Make ZipFile planets.zip then zip only files in the tmpDir"""
    home = os.getcwd()  # remember where we are 
    zf = zipfile.ZipFile('planets.zip', 'w', zipfile.ZIP_DEFLATED) # zip file here too
    root = os.path.split(path)[0]
    os.chdir(root)

    basename = os.path.basename(path)

    for file in os.listdir(path):
        if os.path.isfile(os.path.join(basename) + "/" + file):
            zf.write(os.path.join(basename) + "/" + file)

    zf.close()
    os.chdir(home)  # last thing before returning

    return zf.namelist()


if __name__ == "__main__":
    hotels = ["sheraton", "hilton", "marriot"]
    thepath = "v:\\workspace\\hotels"  # all students have v:/workspace, only hotels is new
    expected = ["hotels/"+hotel for hotel in hotels]
    if not os.path.exists(thepath):
        os.mkdir(thepath)
    for n in hotels:  # effectively setUp()
        f = open(os.path.join(thepath,n), 'w')
        f.write("website: hits:")
        f.close()
    zipDir("v:/workspace/hotels")
    zf = zipfile.ZipFile("planets.zip")
    observed = zf.namelist()
    print("namelist:", observed)
    print("expected:", expected)
    if set(expected) == set(observed):
        print("The test passes")
    else:
        print("The test fails")
    shutil.rmtree(thepath)  # effectively tearDown() 
