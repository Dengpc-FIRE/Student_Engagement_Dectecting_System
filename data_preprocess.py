import os
import cv2

"""data_path = os.path.join(os.getcwd(), "../..")
train_path = os.path.join(data_path, "data_set", "FER2013")
face_data = pd.read_csv(os.path.join(data_path,"data_set", 'face_data.csv'))

emotion = face_data.iloc[1:, 0].values
usage = face_data.iloc[1:, 1].values
pixels = face_data.iloc[1:, 2].values

for i in range(len(emotion)):
    save_dir = None
    if usage[i] == 'Training':
        continue
    else:
        save_dir = os.path.join(train_path, "val", str(emotion[i]))
    file_list = os.listdir(save_dir)
    nums = len(file_list)
    img_dir = os.path.join(save_dir, 'fer_{}.png'.format(nums + 1))
    img = pixels[i].split(' ')
    img = np.array([np.uint8(pixel) for pixel in img])
    img = img.reshape((48, 48))
    cv2.imwrite(img_dir, img)"""


cwd = os.getcwd()
basic_path = os.path.join(cwd, '..', 'data_set', 'engagement_data', 'face_photos')
basic_path = os.path.abspath(basic_path)
type_list = ['unengaged', 'neutral', 'engaged']


def preprocessing(base_dir, typenum, entype):
    imgs_dir = os.path.join(base_dir, str(typenum))
    file_list = os.listdir(imgs_dir)
    save_path = os.path.join(base_dir, entype)
    nums = len(file_list)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    for i in range(nums):
        img_dir = os.path.join(imgs_dir, file_list[i])
        face = cv2.imread(img_dir)
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        face = cv2.resize(face, (48, 48))
        cv2.imwrite(os.path.join(save_path, 'img_{}.png'.format(i + 1)), face)


for i in range(3):
    preprocessing(basic_path, typenum=i + 1, entype=type_list[i])