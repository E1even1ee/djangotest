## 26/06/2018 - 04/07/2018
### Summary
This is definitely a **brand** new way to solve the problem, as it makes the machine to actually learn similar pattern of receipt from training data set. The way it understands things, especially in detail, is literally not decided by humans but conducted by itself, which is the most interesting part of it. Below is the configuration process of it using Tensorflow Object Detection module. Mostly I followed this guy's approach
https://github.com/E1even1ee/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10
### Required packages
pillow, lxml, Cython, matplotlib, pandas, opencv, tensorflow(gpu version preferred)
### Convolution Neural Networks
Whenever you open a terminal to do the training or run something accordingly, set the environment first, otherwise it will show variate errors.
```
set PYTHONPATH=C:\tensorflow1\models;C:\tensorflow1\models\research;C:\tensorflow1\models\research\slim

set PATH=%PATH%;PYTHONPATH
```
Double check the path by 
```
echo %PYTHONPATH%
echo %PATH%
```
Build and install
```
(python3) C:\tensorflow1\models\research>protoc --python_out=. .\object_detection\protos\anchor_generator.proto .\object_detection\protos\argmax_matcher.proto .\object_detection\protos\bipartite_matcher.proto .\object_detection\protos\box_coder.proto .\object_detection\protos\box_predictor.proto .\object_detection\protos\eval.proto .\object_detection\protos\faster_rcnn.proto .\object_detection\protos\faster_rcnn_box_coder.proto .\object_detection\protos\grid_anchor_generator.proto .\object_detection\protos\hyperparams.proto .\object_detection\protos\image_resizer.proto .\object_detection\protos\input_reader.proto .\object_detection\protos\losses.proto .\object_detection\protos\matcher.proto .\object_detection\protos\mean_stddev_box_coder.proto .\object_detection\protos\model.proto .\object_detection\protos\optimizer.proto .\object_detection\protos\pipeline.proto .\object_detection\protos\post_processing.proto .\object_detection\protos\preprocessor.proto .\object_detection\protos\region_similarity_calculator.proto .\object_detection\protos\square_box_coder.proto .\object_detection\protos\ssd.proto .\object_detection\protos\ssd_anchor_generator.proto .\object_detection\protos\string_int_label_map.proto .\object_detection\protos\train.proto .\object_detection\protos\keypoint_box_coder.proto .\object_detection\protos\multiscale_anchor_generator.proto .\object_detection\protos\graph_rewriter.proto
```
```
C:\tensorflow1\models\research> python setup.py build
C:\tensorflow1\models\research> python setup.py install
```
#### Define all the allocation of objects by rectangles using LabelImg
![LabelImg](https://github.com/E1even1ee/djangotest/blob/master/Documents/Dairy%20Pictures/labelImg.jpg)
The image .xml data will be used to create .csv files containing all the data for the train and test images
```
C:\tensorflow1\models\research\object_detection> python xml_to_csv.py
```
![CSV](https://github.com/E1even1ee/djangotest/blob/master/Documents/Dairy%20Pictures/xml_to_csv.jpg)
<br />
For example, say you are training a classifier to detect receipts and invoices. You will replace the following code in generate_record.py:

```
# TO-DO replace this with label map
def class_text_to_int(row_label):
    if row_label == 'nine':
        return 1
    elif row_label == 'ten':
        return 2
    elif row_label == 'jack':
        return 3
    elif row_label == 'queen':
        return 4
    elif row_label == 'king':
        return 5
    elif row_label == 'ace':
        return 6
    else:
        None
```

With this:

```
# TO-DO replace this with label map
def class_text_to_int(row_label):
    if row_label == 'receipt':
        return 1
    elif row_label == 'invoice':
        return 2
    else:
        None
```

Then, generate the TFRecord files by issuing these commands from the \object_detection folder:

```
python generate_tfrecord.py --csv_input=images\train_labels.csv --image_dir=images\train --output_path=train.record
python generate_tfrecord.py --csv_input=images\test_labels.csv --image_dir=images\test --output_path=test.record
```
Create a new file and save it as labelmap.pbtxt in the C:\tensorflow1\models\research\object_detection\training folder
```
item {
  id: 1
  name: 'receipt'
}

item {
  id: 2
  name: 'invoice'
}
```
Navigate to C:\tensorflow1\models\research\object_detection\samples\configs and copy the faster_rcnn_inception_v2_pets.config file into the \object_detection\training directory. Then, open the file with a text editor. There are several changes to make to the .config file, mainly changing the number of classes and examples, and adding the file paths to the training data.

Make the following changes to the faster_rcnn_inception_v2_pets.config file. Note: The paths must be entered with single forward slashes (NOT backslashes), or TensorFlow will give a file path error when trying to train the model! Also, the paths must be in double quotation marks ( " ), not single quotation marks ( ' ).

-   Line 9. Change num_classes to the number of different objects you want the classifier to detect. For the above basketball, shirt, and shoe detector, it would be num_classes : 3 .
    
-   Line 110. Change fine_tune_checkpoint to:
    
    -   fine_tune_checkpoint : "C:/tensorflow1/models/research/object_detection/faster_rcnn_inception_v2_coco_2018_01_28/model.ckpt"
-   Lines 126 and 128. In the train_input_reader section, change input_path and label_map_path to:
    
    -   input_path : "C:/tensorflow1/models/research/object_detection/train.record"
    -   label_map_path: "C:/tensorflow1/models/research/object_detection/training/labelmap.pbtxt"
-   Line 132. Change num_examples to the number of images you have in the \images\test directory.
    
-   Lines 140 and 142. In the eval_input_reader section, change input_path and label_map_path to:
    
    -   input_path : "C:/tensorflow1/models/research/object_detection/test.record"
    -   label_map_path: "C:/tensorflow1/models/research/object_detection/training/labelmap.pbtxt"

Save the file after the changes have been made. That’s it! The training job is all configured and ready to go!
```
python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config
```
#### Check the Tensorboard during training
```
C:\tensorflow1\models\research\object_detection>tensorboard --logdir=training
```
#### Export Inference Graph
Now that training is complete, the last step is to generate the frozen inference graph (.pb file). From the \object_detection folder, issue the following command, where “XXXX” in “model.ckpt-XXXX” should be replaced with the highest-numbered .ckpt file in the training folder:

```
python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph
```

This creates a frozen_inference_graph.pb file in the \object_detection\inference_graph folder. The .pb file contains the object detection classifier