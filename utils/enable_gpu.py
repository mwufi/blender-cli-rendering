import bpy

# Mark all scene devices as GPU for cycles
bpy.context.scene.cycles.device = 'GPU'

print("---------------   SCENE LIST   ---------------")
for scene in bpy.data.scenes:
    print(scene.name)
    scene.cycles.device = 'GPU'
    scene.render.resolution_percentage = 200 
    scene.cycles.samples = 128

# Enable CUDA
bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'

# Enable and list all devices, or optionally disable CPU
print("----------------------------------------------")
for devices in bpy.context.preferences.addons['cycles'].preferences.get_devices():
    for d in devices:
        d.use = True
        # if d.type == 'CPU':
        #     d.use = False
        print("Device '{}' type {} : {}" . format(d.name, d.type, d.use))
print("----------------------------------------------")