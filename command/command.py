import datetime
from sqlalchemy import false, null
from comment.comment import *
from get.get import getInfo, getOneFile
from set.set import setDirectory
from create.create import CreaterDir
from cek.cek import CekValidToken, cekPath
from config.config import AppConfig
import os
import sys
import requests


def cdd(dir):
    x = len(dir)
    if(x > 1):

        return print(Error("""

        cdd takes 1 argument you give 2

        """))
    else:
        if(cekPath(dir[0])):
            setDirectory(dir[0]+'/')
            return dd()
        else:
            print("Directory "+Error(dir[0]) +
                  " is not exist, do you want to create it? [y/n] : ", end="")
            c = input()
            if c == 'y':
                CreaterDir(dir[0])
                setDirectory(dir[0])

                return print("Directory has been created and set to " + Success(dir[0]))
            else:
                return False


def dd():

    x = getInfo()
    return print("Your Download DIRECTORY in " + Success(x.get('DIRECTORY', 'path')))


def ls():
    x = getInfo()
    path = x.get('DIRECTORY', 'path')
    if(os.listdir(path)):
        pass
    else:
        print("Directory is empty")
        return False
    for i in os.listdir(path):

        if(os.path.isfile(path+'/'+i)):
            print(path + " ~ " + LightGreen(i))
        else:
            print(path + " ~ " + Info(i))


def clear():
    os.system('cls')
    return True


def download(id_file):
    x = getInfo()
    source = AppConfig().get('APP_BASE_DOWNLOAD')
    path = x.get('DIRECTORY', 'path')
    token = x.get('AUTH', 'token')
    if(CekValidToken(token)):

        if(len(id_file) > 1):
            return print(Error("""
            Download takes 1 argument you give 2
            """))
        else:
            if(len(id_file) < 1):
                return print(Error("""
                Download takes 1 argument you give 0
                """))
            else:
                if(CekValidToken(token)):
                    file_info = getOneFile(id_file[0])
                    if(file_info):

                        with open(path + file_info['file_name'], "wb") as f:
                            print("Downloading: %s" % file_info['file_name'])
                            response = requests.get(
                                source+file_info['id_file'], stream=True)
                            total_length = response.headers.get(
                                'content-length')

                            if total_length is None:  # no content length header
                                f.write(response.content)
                            else:
                                dl = 0
                                total_length = int(total_length)
                                for data in response.iter_content(chunk_size=4096):
                                    dl += len(data)
                                    f.write(data)
                                    done = int(50 * dl / total_length)
                                    sys.stdout.write("\r[%s%s]" % (
                                        Success('=') * done, ' ' * (50-done)))
                                    sys.stdout.flush()
                        print('\n')
                        print("Download success!")
                    else:
                        print("File not found")
                else:
                    return exit()
    else:
        return exit()


# def camera():

#     import cv2

#     face_cascade = cv2.CascadeClassifier(
#         'd:/python/haarcascade_frontalface_default.xml')

#     cap = cv2.VideoCapture(0)

#     while 1:
#         ret, img = cap.read()
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#         for (x, y, w, h) in faces:
#             cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#             roi_gray = gray[y:y+h, x:x+w]
#             roi_color = img[y:y+h, x:x+w]

#         cv2.imshow('deteksi wajah', img)
#         k = cv2.waitKey(30) & amp
#         0xff
#         if k == 27:
#             break

#     cap.release()
#     cv2.destroyAllWindows()
