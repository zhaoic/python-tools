#! /usr/bin/env python
import sys,os,time

del_str = '曲目 '

def fixname():
    dir = os.getcwd()
    files = os.listdir(dir)
    print(files)
    for file in files:
        a = file.replace(del_str,'')
        print (file+'--->'+a)
        os.rename(file,a)

# img_dir = img_dir.replace('\\','/')
#  i=0
start=time.time()
# change_name(img_dir)
if __name__ == "__main__":
    fixname()
c=time.time()-start
# print('process %s files'%(i))
print ('run time: %0.2f'%(c))