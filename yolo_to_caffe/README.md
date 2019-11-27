# convert txt to xml format
```
PREREQUISITES :::INSTALL ElementTree::::link::::http://effbot.org/zone/element-index.htm
:::::::::::::::::$ pip install Pillow::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

```
1: create a folder named "annotations" and "images" inside yolo_to_caffe.

2: place labels from yolo annotation tool to "annotations" folder also place the corresponding images inside "images" folder.

3: replace the dictionary CLASS_MAPPING (line:34) in txt_to_xml_v1.py according to your class.

4: Run ![txt_to_xml_v1.py](https://github.com/adarshksudarsan/MACHINE_LEARNING/blob/master/yolo_to_caffe/txt_to_xml_v1.py) and you will find the converted labels under "converted_label".

