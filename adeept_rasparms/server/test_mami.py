import raspArmS
import time

ras = raspArmS.RaspArmS()
ras.changeSpeed(10)  # 0~100
ras.start()
ras.servoAngInput([0, 0, 0, 0])  # 角度指定
time.sleep(2)
ras.servoAngInput([90, 0, 0, 80])  # 角度指定
ras.gripper('catch')
time.sleep(2)
ras.gripper('loose')
time.sleep(1)

ras.savePlanJson()

ras.gripper(0)
time.sleep(1)
ras.gripper(-90)
time.sleep(1)
ras.servoAngInput([0, 0, 0, 0])  # 角度指定
