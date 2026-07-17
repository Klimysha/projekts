import pybullet as p
import pybullet_data
import time
import math
import keyboard

# Запуск графического окна и физического движка
physicsClient = p.connect(p.GUI, options="--opengl2")
p.setAdditionalSearchPath(pybullet_data.getDataPath()) 

# Настройка окружения
p.setGravity(0, 0, 0) 

# Настройка положения камеры (смотрим сверху вниз)
p.resetDebugVisualizerCamera(cameraDistance=125.0, cameraYaw=45, cameraPitch=-45, cameraTargetPosition=[0, 0, 1])

p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.configureDebugVisualizer(rgbBackground=[0, 0, 0]) 


# Описание класса для создания планет
class CreatePlanet:
    def __init__(self, radius, baseMass, position, color=[0.5, 0.5, 0.5, 1]):
        self.radius = radius
        self.baseMass = baseMass
        self.position = position
        self.color = color  

    def create(self):
        visual_shape_planet = p.createVisualShape(
            shapeType=p.GEOM_SPHERE, 
            radius=self.radius, 
            rgbaColor=self.color
        )
        collision_shape_planet = p.createCollisionShape(
            shapeType=p.GEOM_SPHERE, 
            radius=self.radius
        )
        planetId = p.createMultiBody( 
            baseMass=self.baseMass, 
            baseCollisionShapeIndex=collision_shape_planet, 
            baseVisualShapeIndex=visual_shape_planet, 
            basePosition=self.position
        )
        return planetId


# Спавн Солнца (в центре: x=0, y=0, z=1)
visual_shape_sun = p.createVisualShape(shapeType=p.GEOM_SPHERE, radius=6, rgbaColor=[1, 1, 0, 1]) 
collision_shape_sun = p.createCollisionShape(shapeType=p.GEOM_SPHERE, radius=1)
sunId = p.createMultiBody(baseMass=0, baseCollisionShapeIndex=collision_shape_sun, baseVisualShapeIndex=visual_shape_sun, basePosition=[0, 0, 1]) 

# СПАВН ПЛАНЕТ 
mercuryId = CreatePlanet(radius=1.5, baseMass=0, position=[10, 0, 1], color=[0.5, 0.5, 0.5, 1]).create()
veneraId  = CreatePlanet(radius=2.2, baseMass=0, position=[18, 0, 1], color=[0.9, 0.7, 0.4, 1]).create()
earthId   = CreatePlanet(radius=2.5, baseMass=0, position=[26, 0, 1], color=[0.0, 1.0, 0.0, 1.0]).create()
marsId    = CreatePlanet(radius=1.8, baseMass=0, position=[34, 0, 1], color=[1.0, 0.0, 0.0, 1.0]).create()
jupiterId = CreatePlanet(radius=4.5, baseMass=0, position=[46, 0, 1], color=[0.8, 0.6, 0.4, 1]).create()
saturnId  = CreatePlanet(radius=3.8, baseMass=0, position=[58, 0, 1], color=[0.9, 0.8, 0.6, 1]).create()
uranusId  = CreatePlanet(radius=3.0, baseMass=0, position=[70, 0, 1], color=[0.6, 0.8, 0.9, 1]).create()
neptuneId = CreatePlanet(radius=2.9, baseMass=0, position=[82, 0, 1], color=[0.2, 0.4, 0.9, 1]).create()

# Структура данных планет
planets_data = [
    [mercuryId, 10.0, 0.0, 0.04],
    [veneraId,  18.0, 0.0, 0.03],
    [earthId,   26.0, 0.0, 0.02],
    [marsId,    34.0, 0.0, 0.015],
    [jupiterId, 46.0, 0.0, 0.009],
    [saturnId,  58.0, 0.0, 0.007],
    [uranusId,  70.0, 0.0, 0.004],
    [neptuneId, 82.0, 0.0, 0.003],
]

# Переменные для контроля паузы
is_paused = False
space_was_pressed = False

print("Симуляция запущена. Нажмите 'Пробел' для паузы, 'Esc' для выхода.")

# Сделаем цикл бесконечным, пока открыто окно PyBullet
while p.isConnected():
    
    # Проверяем нажатие Пробела (с защитой от залипания)
    if keyboard.is_pressed("space"):
        if not space_was_pressed: # Переключаем паузу только в момент первого нажатия
            is_paused = not is_paused
            space_was_pressed = True
    else:
        space_was_pressed = False # Сбрасываем флаг, когда пробел отпустили

    # Выход из симуляции на клавишу Esc
    if keyboard.is_pressed("esc"):
        break

    # Если симуляция НЕ на паузе — двигаем планеты
    if not is_paused:
        for data in planets_data:
            planet_id = data[0]
            orbit_r   = data[1]
            angle     = data[2]
            speed     = data[3]
            
            new_x = orbit_r * math.cos(angle)
            new_y = orbit_r * math.sin(angle)
            new_z = 1.0  
            
            p.resetBasePositionAndOrientation(planet_id, [new_x, new_y, new_z], [0, 0, 0, 1])
            data[2] += speed

    # Обновление графики и физики происходит всегда, чтобы окно не зависало
    p.stepSimulation() 
    time.sleep(1./240.) 

p.disconnect()
print("Симуляция завершена.")
