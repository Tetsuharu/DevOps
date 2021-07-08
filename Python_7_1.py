if __name__ == '__main__':
    pass


import os
os.chdir('test')
print('文件中包含“qytang"关键字的文件为：')

print('方案一：')

for file_or_dir in os.listdir(os.getcwd()):
    if os.path.isfile(file_or_dir):
        for x in open(file_or_dir):
            if "qytang" in x:
                print(file_or_dir)


print('方案二：')
for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    for y in files:
        for z in open(y):
            if "qytang" in z:
                print(y)

# 完成清理工作
os.chdir('..')
for root, dirs, files in os.walk('test', topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
os.removedirs('test')








