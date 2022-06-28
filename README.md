# HEVEN_simulation_2022
Autonomous driving with MORAI simulation, 2022 HEVEN<br>
[MORAI Simulator manual](https://morai-sim-for-wego-help.scrollhelp.site/user-manual/)

## 작업환경 세팅

#### 워크스페이스 생성
```
mkdir simul_ws/
cd simul_ws
git clone https://github.com/jhforstudy/HEVEN_simulation_2022.git
```

#### 패키지 빌드
먼저, clone 받은 폴더명을 ``src``로 변경한다. (패키지 빌드를 위해)
이후, 워크스페이스 폴더 내에서
```
catkin_make
```

## 시뮬레이터 실행

#### MORAI 시뮬레이터 실행
MORAI 시뮬레이터가 들어있는 디렉터리로 이동 후, 아래와 같이 실행한다.
```
chmod +x MORAISim.sh
chmod +x MoraiLauncher_Lin.x86_64
./MORAISim.sh
```

#### rosbridge 실행
*주의* : 패키지 안에 ``morai_msg`` 등 외부에서 받은 ``msg`` 파일들을 사용해서 통신하므로, 워크스페이스 내에서 source를 해주고 실행해야 에러가 나지 않는다.
```
cd simul_ws/
source devel/setup.bash
roslaunch rosbridge_server rosbridge_websocket.launch 
```
``msg`` 파일은 topic의 정보를 담는 틀의 역할을 한다. ROS에서 제공해주는 ``msg`` 파일의 경우 (``std_msgs``, ``sensor_msgs`` 등) 바로 사용할 수 있지만, 새로 만든 ``msg`` 파일의 경우 해당 작업환경에서 ``source devel/setup.bash``를 해주어야 인식할 수 있다.

[msg 파일에 관한 자세한 설명](https://github.com/jhforstudy/HEVEN_simulation_2022/blob/main/about_msg.md)


## 센서 연결

MORAI 시뮬레이터 실행 후, ``F4``를 누르면 Network Setting 메뉴가 열린다.
사용하는 컴퓨터의 ip를 적용해주어야 한다
```ifconfig```
명령어로 [컴퓨터의 ip](https://minddoodle.tistory.com/7)를 검색하자.

설정 완료 후, 하단 Sensor setting 메뉴에 들어가서 아래와 같이 설정한다.

#### IMU
![imu](https://user-images.githubusercontent.com/48710703/175962573-2f5ccdc4-e6ef-43b8-a946-1c428d028b5a.png)

#### GPS
![gps](https://user-images.githubusercontent.com/48710703/175962611-7867245b-93ed-4cd0-ad6a-cdc076f35026.png)

#### 3D LIDAR
![lidar](https://user-images.githubusercontent.com/48710703/175962657-2abbd927-df7e-47ee-a83d-0b3524b4569d.png)

#### CAMERA
![camera](https://user-images.githubusercontent.com/48710703/175962721-0a6338a4-1395-4923-b927-63c502d1f745.png)

각각의 센서 설정을 완료하고, ``CONNECT`` 버튼을 눌러 rosbridge 터미널에서 client가 추가되는지 확인하자. 만약 에러가 발생하면 데이터를 받아올 수 없다.



### To-do list

1. subscribe한 topic을 한번에 관리하는 Database 클래스 만들기
2. 3D lidar를 받아올 때 velodyne 드라이버를 통해서가 아닌, 시뮬레이터 topic (`PointCloud2`)을 직접 받아오기
