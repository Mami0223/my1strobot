import raspArmS
import time

ras = raspArmS.RaspArmS()
ras.start()

planlist = ras.getPlanGoseList()
xnowpos = planlist[0][0]
ynowpos = planlist[0][1]
znowpos = planlist[0][2]
gnowpos = planlist[0][3]

for i in range(100):
    if xnowpos > 0:
        if ynowpos > 0:
            ras.servoAngInput(
                [xnowpos-i*abs(xnowpos)/100, ynowpos-i*abs(ynowpos)/100, 0, 0])  # X,yを0に
        else:
            ras.servoAngInput(
                [xnowpos-i*abs(xnowpos)/100, ynowpos+i*abs(ynowpos)/100, 0, 0])
    else:
        if ynowpos > 0:
            ras.servoAngInput(
                [xnowpos+i*abs(xnowpos)/100, ynowpos-i*abs(ynowpos)/100, 0, 0])
        else:
            ras.servoAngInput(
                [xnowpos+i*abs(xnowpos)/100, ynowpos+i*abs(ynowpos)/100, 0, 0])
    time.sleep(0.01)


# ras.changeSpeed(1)  # 0~100
#ras.servoAngInput([0, 0, 0, 0])
for i in range(50):
    ras.servoAngInput([i, 0, 0, 0])  # 右に50度
    time.sleep(0.01)

time.sleep(1)
for i in range(121):
    ras.servoAngInput([50, -i, 0, 0])  # 手前に120度
    time.sleep(0.01)
time.sleep(1)
# ras.moveXYZ([90, 140, 0, 50])
# ras.gripper('catch')
time.sleep(1)
ras.gripper('loose')
# time.sleep(1)
# ras.savePlanJson()

ras.createNewPlan()
ras.newPlanAppend()
ras.savePlanJson()
