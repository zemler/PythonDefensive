#Author: Jan "zemler" Zemla

import sys
import hashlib
import os

catalog_name = sys.argv[1]


#Calculating file md5sum:
def file_md5(filename):
    md5_sum = hashlib.md5()
    with open(filename,"rb") as file:
        while True:
            data = file.read(8192)
            if not data:
                break
            md5_sum.update(data)
    return md5_sum.hexdigest()
            
# Repeating file_md5 for every file in directory            
if __name__ == "__main__":
    with open('/tmp/result.txt','w') as result:
        for specific_file in os.listdir(catalog_name):
            file_path = os.path.join(catalog_name, specific_file)
            if os.path.isfile(file_path):
                file_sum = file_md5(file_path)
                result.write(f"{specific_file} {file_sum}\n")
    