# rubiksCubeCode

A Processing.py sketch that visualizes, then (hopefully) solves a 3x3x3 Rubiks Cube.

## Goals

The Goals Of This Program Are To:

- [X] visualize a rubiks cube
- [X] move according to user inputs
- [X] track/retrieve current state of the cube using a 3-D array
- [X] generate and apply a random scramble
- [ ] have every single, double, and cube rotation move available 
- [ ] be able to solve the cube consistantly
- [ ] export a string containing the scramble and solve moveset
- [ ] improve efficiency of solves
- [ ] reduce the number of moves by:
    - [ ] making the code color neutral, and picking a good cross to solve with
    - [ ] looking for ideal/easier f2l pairs to complete first
    - [ ] eliminating unnessasary moves that keep a pair or cross intact even when there isn't one
    - [ ] implementing Valk Last Slot (this is over 200 algs so this would take a long time)
- [ ] reduce the time to solve by:
    - [ ] taking unnessasary code out of the draw() function
    - [ ] eliminating variables that are unused or can be implemented better
    - [ ] adding a quick solve or lowest move option to change between different methods
- [ ] link the Cube array to the visuals so you can directly map things to the visual cube
- [ ] take the scramble and solve moveset and apply it to a real life cube
- [ ] implement cameras to sense color to solve the cube from any state
- [ ] a very long term goal is to see how Deep Learning reacts to solving the cube
