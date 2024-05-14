import argparse
import json
import os
import os.path as osp
import warnings
 
import PIL.Image
import yaml
 
from labelme import utils
import base64
 
def main(source_path,storege_path,label_mapping):
    for i in os.listdir(source_path):
        path = os.path.join(source_path, i)

        if os.path.isfile(path) and path.endswith('json'):
            data = json.load(open(path))

            if data['imageData']:
                imageData = data['imageData']
            else:
                # imagePath = os.path.join(os.path.dirname(path), data['imagePath'][-8:])  #使用师兄标注的
                imagePath = os.path.join(os.path.dirname(path), data)  #使用师兄标注的
                with open(imagePath, 'rb') as f:
                    imageData = f.read()
                    imageData = base64.b64encode(imageData).decode('utf-8')
            img = utils.img_b64_to_arr(imageData)
            label_name_to_value = {'_background_': 0}
            for shape in data['shapes']:
                label_name = shape['label']
                if label_name in label_name_to_value:
                    label_value = label_name_to_value[label_name]
                else:
                    if label_mapping:
                        label_value=label_mapping[label_name]
                    else:
                        label_value = len(label_name_to_value)
                    label_name_to_value[label_name] = label_value

            # label_values must be dense
            label_values, label_names = [], []
            for ln, lv in sorted(label_name_to_value.items(), key=lambda x: x[1]):
                label_values.append(lv)
                label_names.append(ln)

            # assert label_values == list(range(len(label_values)))

            lbl = utils.shapes_to_label(img.shape, data['shapes'], label_name_to_value)

            captions = ['{}: {}'.format(lv, ln)
                        for ln, lv in label_name_to_value.items()]
            lbl_viz = utils.draw_label(lbl, img,alpha=0.3)
            #
            if not os.path.exists(storege_path):
                os.mkdir(storege_path)

            #mask
            label_path = os.path.join(storege_path,"mask")
            if not os.path.exists(label_path):
                os.mkdir(label_path)
            utils.lblsave(osp.join(label_path, i[:-5]+'.png'), lbl)

            #source img
            img_path =  os.path.join(storege_path,"imgs")
            if not os.path.exists(img_path):
                os.mkdir(img_path)
            PIL.Image.fromarray(img).save(osp.join(img_path, i[:-5]+'.jpg'))

            #fix
            yaml_path = os.path.join(storege_path,"yaml")
            if not os.path.exists(yaml_path):
                os.mkdir(yaml_path)
            info = dict(label_names=label_names)
            with open(osp.join(yaml_path, i[:-5]+'.yaml'), 'w') as f:
                yaml.safe_dump(info, f, default_flow_style=False)

            label_viz_path = os.path.join(storege_path,"label_viz")
            if not os.path.exists(label_viz_path):
                os.mkdir(label_viz_path)
            PIL.Image.fromarray(lbl_viz).save(osp.join(label_viz_path, i[:-5]+'.png'))

            print('Saved : %s' % str(i))
if __name__ == '__main__':
    """
    
    """
    source_path="/Users/dongzai/PycharmProjects/MySegPro/SegDatasets/Throat/train" #用labelme标注的json文件 所在目录
    storege_path = "/Users/dongzai/PycharmProjects/SSL4MIS/data/throat" # 转换之后的文件目录 最终会在下面生产 imgs label_viz maks yaml 目录
    assert source_path
    assert storege_path
    label_mapping={
        "epiglottis":1,
        "throat":2,
        "pyriform_sinus":3,
        "vocal_cords":4,
        # "vocal_cords_open":4,
        # "vocal_cords_close":5
    }
    main(source_path,storege_path,label_mapping)