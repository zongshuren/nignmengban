import os
# try:...Exception..
# try:
#     os.rmdir("aa")
# except OSError as e:
#     print(e)
#     file = open('error.text', 'a+', encoding='utf-8')
#     file.write(str(e))
#     file.close()

# try:..Exception..else
try:
    os.rmdir("aa")
except OSError as e:
    print(e)
    file = open('error.text', 'a+', encoding='utf-8')
    file.write(str(e))
    file.close()
else:
    print('你好我就好') # 跟try下面的代码是一起的try能执行


try:
    os.rmdir("aa")
except OSError as e:
    print(e)
    file = open('error.text', 'a+', encoding='utf-8')
    file.write(str(e))
    file.close()
finally:
    print('你好我就好')