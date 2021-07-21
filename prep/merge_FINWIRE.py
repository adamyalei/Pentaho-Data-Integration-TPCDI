import shutil
import os

def concatFiles():
    path = '/Users/testing/pdgf/output/Batch1/FINWIRE/FINWIRE_txt'
    files = os.listdir(path)
    with open("/Users/testing/pdgf/output/Batch1/FINWIRE/merged.txt", "wb") as fo:
            for f in sorted(files):
                with open(os.path.join(path, f), "rb") as fi:
                    shutil.copyfileobj(fi, fo)

concatFiles()
print('finished')
