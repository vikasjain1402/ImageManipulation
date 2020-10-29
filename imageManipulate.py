from PIL import Image
import os



source_diectory="/home/vikas/Pictures/"
dest_diectory=os.path.join(source_diectory,"/test/")
desired_size=100000
os.makedirs(dest_diectory,exist_ok=True)

for file in os.listdir(source_diectory):

    fname,fext=os.path.splitext(file)
    if fext==".jpeg" or fext==".png" or fext==".jpg":
        fp=os.path.join(source_diectory,file)
        try:
            i=Image.open(fp)
        except Exception as e:
            print(e)
        size=os.path.getsize(fp)
        delta=0
        xpx,ypx=i.size
        while size>desired_size:
            i.thumbnail((xpx-delta,ypx-delta))
            file_dest_path=f'{dest_diectory}/{fname}-{xpx-delta}*{ypx-delta}.{fext}'
            i.save(file_dest_path)
            size=os.path.getsize(file_dest_path)
            print(i.size)
            delta+=100
        print("Image Size Reduced to ",os.path.getsize(file_dest_path),"Bytes from ",os.path.getsize(fp),"Bytes","i.e","{:.0f}%".format(os.path.getsize(file_dest_path)/os.path.getsize(fp)*100))
        break