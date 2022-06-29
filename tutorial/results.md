# 결과

## std_msgs 사용

#### 실행
terminal 1
```
roscore
```

terminal 2
```
cd tutorial_ws/
source devel/setup.bash
rosrun tutorial pub.py 

[INFO] [1656483485.767920]: Two topics are publishing : 3 10
[INFO] [1656483485.968202]: Two topics are publishing : 12 16
[INFO] [1656483486.167826]: Two topics are publishing : 17 10
[INFO] [1656483486.368300]: Two topics are publishing : 17 12
[INFO] [1656483486.568049]: Two topics are publishing : 18 3
...
```

terminal 3
```
cd tutorial_ws/
source devel/setup.bash
rosrun tutorial add.py 

[INFO] [1656483485.949135]: Addition is : 13
[INFO] [1656483486.149039]: Addition is : 28
[INFO] [1656483486.349311]: Addition is : 27
[INFO] [1656483486.549280]: Addition is : 29
[INFO] [1656483486.749030]: Addition is : 21
...
```

## custom msg 파일 사용

#### 실행
terminal 1
```
roscore
```

terminal 2
```
cd tutorial_ws/
source devel/setup.bash
rosrun tutorial custom_msg_pub.py

[INFO] [1656483610.527363]: Custom topic is publishing : 8 8
[INFO] [1656483610.727347]: Custom topic is publishing : 18 3
[INFO] [1656483610.927320]: Custom topic is publishing : 4 16
[INFO] [1656483611.127341]: Custom topic is publishing : 20 14
[INFO] [1656483611.327392]: Custom topic is publishing : 8 8
...
```

terminal 3
```
cd tutorial_ws/
source devel/setup.bash
rosrun tutorial custom_msg_add.py

[INFO] [1656483610.713309]: Addition is : 16
[INFO] [1656483610.913431]: Addition is : 21
[INFO] [1656483611.113500]: Addition is : 20
[INFO] [1656483611.313292]: Addition is : 34
[INFO] [1656483611.513351]: Addition is : 16
...
```
