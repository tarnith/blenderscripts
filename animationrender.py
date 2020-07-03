import bpy

renderpath = "yourfilepath" # Your desired output path for the frames

for frame in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end + 1):
    # Iterates through the current scenes frames as set in the sequencer
    
    bpy.context.scene.frame_set(frame) # Sets frame to current value from the loop
    bpy.context.scene.render.filepath = filepath + str(frame) # Sets filepath and concatenates current frame to the path
    bpy.ops.render.render(write_still=True) # Calls the render operation for each frame
