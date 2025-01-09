# Project Description

The task involves programming the eebot to effectively navigate a complex maze utilizing its guidance system. The robot initiates its journey at an entry point, a S-turn, making decisions at intersections, and possessing the capability to execute a 180° turn in response to the front bumper being triggered upon colliding with a wall. The implementation leverages diverse sensor inputs, enabling the robot to operate dynamically and adapt to different scenarios. The project achieves its objective by orchestrating the eebot's movement through distinct states, encompassing forward and reverse motions, turns, and the interpretation of sensor readings.

## Accomplishments

- A **state machine** was implemented to manage the robot's behavior, facilitating seamless transitions between various states such as forward, reverse, turning, and standby.
- The state machine incorporated a **dispatcher** that dictated the transition to the appropriate state based on sensor readings, ensuring accurate motor actions.
- Specialized **motor control subroutines** were developed for both the port and starboard motors, granting precise control over the robot's movement.
- Leveraging insights from previous lab assignments, these subroutines contributed to the refinement of motor control mechanisms.
- A **subroutine for reading sensor inputs** was implemented, playing a pivotal role in decision-making processes to determine the robot's next move.
- The implementation drew guidance from the **Guider PDF** provided for the eebot.
![image](https://github.com/user-attachments/assets/8526d3ba-7ee2-4752-8111-58b5683bda7b)
