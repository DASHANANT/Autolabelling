## Directory Structure should be as following:

```
Dataset                     
    object                       ---------Root Directory path
        testing            
            image
               000000.png
            label
               000000.txt
            pc                  ---------- Data Directory path
               000000.bin       ---------- Data Path
            
        training
            
            image
               000000.png
            label
               000000.txt
            pc
               000000.bin           
```

## For Lidar Visualization pass arguments with main script

```shell
$ python main.py 

  Arguments:
  -h, --help            show this help message and exit
  --rd                  Root Directory path
  --dd                  Data Directory path
  --dp                  Direct Data path
  --i                   specific index of data in Data Directory
  --n                   number of attributes to be extracted from binary
  --vwp                 visualize point cloud
  --bv                     ==bird view
  --ev                     --Environment view
  --eva                 elevation angle
  --azim                azimuth angle
  --rmg                 remove ground points
  --vwc                 visualize camera image  

```

```shell
$ python main.py
```
Specify root,data directories path or direct data path

    ```shell
    $ python main.py --rd ../path/to/Dataset/object
    ```

    you can pass data file Index (default = 0th file ) 

    ```shell
    $ python main.py --dd ../path/to/Dataset/object/pc --i 56
    ```

    ```shell
    $ python main.py --dd ../path/to/Dataset/object/pc/00000.bin
    ```


Visualize LiDAR bird view
```
$ python main.py --dd ../00000.bin --vwp --bv 
```

Visualize LiDAR with environment view at angled 35 degree and respective camera image
```
$ python main.py --dd ../00000.bin --vwp --vwc --ev --eva 35
```

