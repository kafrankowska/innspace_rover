![image info](./data/imgs/rover_sim.png)
# Innspace Rover Autonomous Navigation System
---
This is a Innspace Rover Autonomous Navigation System implemented in ROS2 Humble. Workspace contains set of packages that enable to simulate, test, use and integrate systems required for autonomous navigation tasks.

## Table of contents
---

1. Installation
2. System documentation
3. Usage guide

### 1. Installation
---
Run set of commands in your terminal:
1. Create workdir and src folder
<pre><code>mkdir innspace_rover
</code></pre>

2. Clone the repository 
<pre><code>git clone git@github.com:kafrankowska/innspace_rover.git
rosdep install --from-paths src -r -y
colcon build --symlink-install
</code></pre>

3. Launch simulation
<pre><code>source install/setup.bash
ros2 launch rover_description launch_sim.launch.py
</code></pre>

### 2. System description
---
> Packages list: 
> 
>  - __rover_simulation__ - package responsible for defining simulation enviroment
> - __rover_description__ - package containing rover description


### rover_simulation
---


Tutaj opis paczki 

### rover_description
---

Tutaj opis paczki
