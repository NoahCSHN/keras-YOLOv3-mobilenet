import xml.etree.ElementTree as ET
from os import getcwd
import os

# sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]
sets=[('2007', 'train'), ('2007', 'val')]

classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

voc_dir = r'F:/2_doc/7_datasets/VOC07/VOCtrainval_06-Nov-2007'

def convert_annotation(year, image_id, list_file):
    in_file = open('%s/VOCdevkit/VOC%s/Annotations/%s.xml'%(voc_dir, year, image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

os.chdir(r'F:\1_code\python\keras-YOLOv3-mobilenet')
wd = getcwd()

for year, image_set in sets:
    image_ids = open('%s/VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(voc_dir, year, image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg'%(voc_dir, year, image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()

