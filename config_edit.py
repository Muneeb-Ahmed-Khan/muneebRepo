import re
filename = 'C:/tensorflow_env/models/research/object_detection/muneebRepo/training/faster_rcnn_inception_v2_pets.config'
with open(filename) as f:
  s = f.read()
with open(filename, 'w') as f:
  s = re.sub('37', '1', s) #number of classes to train for, default was 37 so , i substituted it with 1. which is how many i am using
  s = re.sub('PATH_TO_BE_CONFIGURED/model.ckpt', '/content/models/research/object_detection/faster_rcnn_inception_v2_coco_2018_01_28/model.ckpt', s)
  s = re.sub('PATH_TO_BE_CONFIGURED/pet_faces_train.record-\?\?\?\?\?-of-00010', '/content/models/research/object_detection/muneebRepo/train.record', s)
  s = re.sub('PATH_TO_BE_CONFIGURED/pet_faces_val.record-\?\?\?\?\?-of-00010', '/content/models/research/object_detection/muneebRepo/test.record', s)
  s = re.sub('PATH_TO_BE_CONFIGURED/pet_label_map.pbtxt', '/content/models/research/object_detection/muneebRepo/training/label_map.pbtxt', s)
  s = re.sub('1101', '105', s)  #number of test examples. number of pictures in test folder , default was 1101 . i replaced it with 105, whcih are how many pictures i am currently using in this dataset
  f.write(s)
