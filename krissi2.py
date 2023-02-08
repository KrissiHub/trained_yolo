import os
from roboflow import Roboflow
os.system("export COMET_API_KEY=SpIOoePX20i12MbnmHKU4BuZp")
os.system("export COMET_PROJECT_NAME=Hoverfly-Detection-2")
'''rf = Roboflow(api_key="Q6FgEEqPPUhAU2Vhx1lf")
project = rf.workspace("leibniz-universitt-hannover-bachelorarbeit").project("hoverfly-detection")
dataset = project.version(2).download("yolov5")'''
os.system("python3 train.py --img 640 --batch 16 --epochs 20 --data Hoverfly-Detection-2/data.yaml --weights yolov5s.pt")
