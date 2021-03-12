## Image file/text file/any file rename 
import os
path = '/home/selva/Selva/Products/Task/Datas/Images/passport'
files = os.listdir(path)
for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.png'])))
