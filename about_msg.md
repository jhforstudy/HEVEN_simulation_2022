# About msg file

``msg`` 파일은 ROS 통신에서 주고받는 topic의 정보들이 담기는 **틀**이라고 생각할 수 있다. <br>
코드 리뷰를 통해 ``msg`` 파일에 대해 이해해 보자.

### msg 파일 사용법

#### 코드 리뷰
현재 레포지토리의 ``gen_ros/scripts/gps.py`` 를 보자.
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from morai_msgs.msg import GPSMessage


class erp_gps():
    def __init__(self):
        rospy.init_node('gps', anonymous=True)
        rospy.Subscriber("/gps", GPSMessage, self.gpsCB)
        rospy.spin()

    def gpsCB(self,data):
        print("latitude {}".format(data.latitude))
        print("longitude {}".format(data.longitude))
        print("eastOffset {}".format(data.eastOffset))
        print("northOffset {}".format(data.northOffset))

```

``morai_msgs.msg`` 에서 ``GPSMessage``라는 ``msg`` 파일을 import 하여 사용하고 있고,<br>
``erp_gps`` 클래스의 생성자 부분을 보면
```python
rospy.Subscriber("/gps", GPSMessage, self.gpsCB)
```
``GPSMessage``라는 형태의 topic을 subscribe하는 Subscriber를 선언한 것을 알 수 있다.<br>
그렇다면 ``GPSMessage`` 라는 topic의 형태, 즉 ``GPSMessage.msg`` 파일은 어디에 있는 것일까?<br>

#### msg 파일의 위치
``morai_msgs-master/msg`` 디렉터리에 들어가면 여러 ``msg`` 파일이 담겨있는 것을 볼 수 있다.<br>
그중에서 ``GPSMessage.msg`` 파일을 찾을 수 있을 것이고, 열어보면

```
Header header

float64 latitude
float64 longitude
float64 altitude

float64 eastOffset
float64 northOffset
int16 status
```

다음과 같은 형태의 틀을 갖고 있는 것을 알 수 있다.<br>
ROS에서 기본적으로 제공하는 ``msg`` 파일을 사용할 수도 있으며, [msg 파일 사용법](https://2-54.tistory.com/8)<br>
필요하다면 직접 만들어 사용할 수도 있다. [새로운 msg 파일 작성법](https://velog.io/@717lumos/ROS-msg%EB%A9%94%EC%8B%9C%EC%A7%80-%EB%A7%8C%EB%93%A4%EA%B8%B0)
