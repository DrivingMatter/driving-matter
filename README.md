# DrivingMatter: Autonomous RC Car using Raspberry Pi

## Introduction

The aim of the project is to assemble an Raspberry Pi controlled robot car. The scope includes the assembly of motors and required parts from the hardware perspective. It also includes programming so that the car can be sent signals wirelessly to a PC-based front-end to initiate actions such as ignition, movement, steering etc. Finally, from the software end, it requires a front-end through which the car will be controlled. This front-end will provide both a GUI-based interface (which will show the images being captured by the car through its camera) as well as other statistics of the movement. It will also provide library bindings to programmatically control the car through another software.

## Folder Structure

### CarServer

Its contains the code that run inside the car and provide controls to remote pc via WS Server.

### pyDrivingMatter

Its contains the code related to Python library which controls the car through remote pc.

### GUI

Its contains the Graphical interface of the interfaces provided in pyDrivingMatter.

### Trash

Its contains the code which are obsolete.

## Documentation

Check [wiki page](https://gitlab.com/UntitledGroup/driving-matter/wikis/home) of this project.

## Members

Syed Owais Ali Chishti - [p146011@nu.edu.pk](mailto:p146011@nu.edu.pk)

Hafiz M. Bilal Zaib - [p146099@nu.edu.pk](mailto:p146099@nu.edu.pk)

Sana Riaz - [p146114@nu.edu.pk](mailto:p146114@nu.edu.pk)

## Supervisor

Dr. Mohammad Nauman - [mohammad.nauman@nu.edu.pk](mailto:mohammad.nauman@nu.edu.pk)

## Useful Links

Proposal of this Project - [https://gitlab.com/UntitledGroup/fyp-proposal](https://gitlab.com/UntitledGroup/fyp-proposal)

Presentation of this Project - [https://gitlab.com/UntitledGroup/fyp-defense-presentation](https://gitlab.com/UntitledGroup/fyp-defense-presentation)

LaTeX Document of this Project - [https://gitlab.com/UntitledGroup/fyp-documentation](https://gitlab.com/UntitledGroup/fyp-documentation)

## License

To be decided.