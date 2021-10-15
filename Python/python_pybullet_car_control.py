"""hello everyone!!! I am Pratyush and this is a basic pybullet project to make a keyboard controlled car(husky) using torque control(you can use velocity control instead) and to show the information about joints this car is having.

controls:
          1. forward arrow key ==> forward
          2. backward arrow key ==> backward
          3. left arrow key ==> left rotate
          4. right arrow key ==> right rotate
          5. 'r' button ==> reverse
          6. 'a' button ==> increase speed"""

import pybullet as p
import pybullet_data

p.connect(p.GUI)  # or p.SHARED_MEMORY or p.DIRECT
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")
p.setGravity(0, 0, -10)  # setting environment gravity
carpos = [0, 0, 0.1]

car = p.loadURDF("husky/husky.urdf", carpos[0], carpos[1], carpos[2])

numJoints = p.getNumJoints(car)  # getting information of joints
for joint in range(numJoints):
    print(p.getJointInfo(car, joint)[0:2])

a = 0
maxForce = 50  # Newton

while 1:
    keys = p.getKeyboardEvents()

    for k, v in keys.items():

        if v & p.KEY_IS_DOWN:
            if k == p.B3G_LEFT_ARROW:

                targetVel = 1.51

                for joint in range(2, 6):
                    p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL, force=49.8)

                p.setJointMotorControl2(
                    car, jointIndex=2, controlMode=p.TORQUE_CONTROL, force=-62.3 - a
                )
                p.setJointMotorControl2(
                    car, jointIndex=3, controlMode=p.TORQUE_CONTROL, force=62.3 + a
                )
                p.setJointMotorControl2(
                    car, jointIndex=4, controlMode=p.TORQUE_CONTROL, force=-62.3 - a
                )
                p.setJointMotorControl2(
                    car, jointIndex=5, controlMode=p.TORQUE_CONTROL, force=62.3 + a
                )

                p.stepSimulation()
            if k == p.B3G_RIGHT_ARROW:

                targetVel = 1.51

                for joint in range(2, 6):
                    p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL, force=49.8)

                p.setJointMotorControl2(
                    car, jointIndex=2, controlMode=p.TORQUE_CONTROL, force=62.3 + a
                )
                p.setJointMotorControl2(
                    car, jointIndex=3, controlMode=p.TORQUE_CONTROL, force=-62.3 - a
                )
                p.setJointMotorControl2(
                    car, jointIndex=4, controlMode=p.TORQUE_CONTROL, force=62.3 + a
                )
                p.setJointMotorControl2(
                    car, jointIndex=5, controlMode=p.TORQUE_CONTROL, force=-62.3 - a
                )

                p.stepSimulation()

            if k == p.B3G_UP_ARROW:

                targetVel = -1.51 - a
                for joint in range(2, 6):
                    p.setJointMotorControl2(
                        car,
                        joint,
                        p.VELOCITY_CONTROL,
                        targetVelocity=targetVel,
                        force=maxForce,
                    )

                p.stepSimulation()

            if k == p.B3G_DOWN_ARROW:
                targetVel = 1.51 + a
                for joint in range(2, 6):
                    p.setJointMotorControl2(
                        car,
                        joint,
                        p.VELOCITY_CONTROL,
                        targetVelocity=targetVel,
                        force=maxForce,
                    )

                p.stepSimulation()

            if k == ord("r"):

                targetVel = 1.51

                for joint in range(2, 6):
                    p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL, force=49.8)

                p.setJointMotorControl2(
                    car, jointIndex=2, controlMode=p.TORQUE_CONTROL, force=62.3
                )
                p.setJointMotorControl2(
                    car, jointIndex=3, controlMode=p.TORQUE_CONTROL, force=-62.3
                )
                p.setJointMotorControl2(
                    car, jointIndex=4, controlMode=p.TORQUE_CONTROL, force=62.3
                )
                p.setJointMotorControl2(
                    car, jointIndex=5, controlMode=p.TORQUE_CONTROL, force=-62.3
                )

                p.stepSimulation()

        if v & p.KEY_WAS_RELEASED:

            targetVel = 0
            for joint in range(2, 6):
                p.setJointMotorControl2(
                    car,
                    joint,
                    p.VELOCITY_CONTROL,
                    targetVelocity=targetVel,
                    force=maxForce,
                )

            p.stepSimulation()

        if k == ord("a"):
            if v & p.KEY_WAS_RELEASED:
                a = a + 1


p.getContactPoints(car)
p.disconnect()
