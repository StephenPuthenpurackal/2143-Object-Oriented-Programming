## Program 3 - Modeling Covid19 Part 2
#### Due: 05-11-2020 (Monday @ 5:00 p.m.)

## Overview

I've been on Discord almost every night at 7:00 p.m. for the last two weeks talking about Python and this project. There are code examples available in a few locations, including:

- This directory has: [Code_Examples](./Code_Examples/)
- The Resources directory has: 
  - [10-PyGame](../../Resources/10-PyGame/)
  - [11-SIM](../../Resources/11_SIM)

### Disease Model

Not every simulation uses the same "model". We are using the SIR model (or a simple variation of) becuase it is straightforward and fits our purposes. However if we decide to use another model, we don't want our "simulation" to be tightly coupled with only a single disease model. For example the SEIR model or the SIS model. Therefore I propose a class that will allow us to load any model. 

The SIR model: 

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/sir_flow_diagram_2020.png" width="500">

**State Descriptions:** 

| #    | State       | Description                                     | Exceptions                 |
| :--- | :---------- | :---------------------------------------------- | :------------------------- |
| 1    | Susceptible | Any person who can catch the disease            | Already infected or immune |
| 2    | Infectious  | A person that has the disease and is contagious | Quarantined                |
| 3    | Recovered   | A person who had the disesase and recovered     |                            |

**Possible State Colors:**

| #    | State       | Color  | Image                                 |
| :--- | :---------- | :----- | :------------------------------------ |
| 1    | Susceptible | Yellow | ![](./images/person_yellow_64x64.png) |
| 2    | Infectious  | Red    | ![](./images/person_red_64x64.png)    |
| 3    | Recovered   | Green  | ![](./images/person_green_64x64.png)  |

### Other Colors

| White    | Gray | Purple  | Orange  | Peach  | Dark Pink  | Light Blue | Turquoise | 
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|![](./images/person_white_64x64.png)|![](./images/person_gray_64x64.png)| ![](./images/person_purple_64x64.png)| ![](./images/person_orange_64x64.png)|  ![](./images/person_peach_64x64.png)| ![](./images/person_dark_pink_64x64.png)| ![](./images/person_light_blue_64x64.png)| ![](./images/person_turquoise_64x64.png)| 

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/covid19a_uml_2020.png" height="150">




### Simulation Class



|                                          Sim Disease Variables                                          |                                     Sim Additional Variables 2                                      |
| :-----------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------: |
| <img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/covid19_sir_model_vals.png" width="350"> | <img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/covid19_sim_params.png" width="200"> |

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/covid19b_uml_2020.png" width="150">


### Other Possible Classes

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/covid19_uml_2020.png" width="350">




## Discussion

This project is to take the **SIR** model and visualize a Covid19 outbreak with a population of people (or any flu basically). We did not discuss specifics in the beginning since we were really getting up to speed with python. Also, I wanted everyone to approach the problem in their own way. We looked at a [3 Blue One Brown video](https://www.youtube.com/watch?v=gxAaO2rsdIs&t=460s) modeling disease outbreak, and this will be our major influence for our last program. Not his visualizations, but the major influences to the outbreak that he discusses. Your program will do visualizations, but your grade will be determined on how you organize and design each of your classes.

Don't forget about the [Dry Principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) when creating your classes. Each class should be responsible for one logical component of your simulation. I gave some examples at the top of this document, but there are many viable solutions.

## Project



### Deliverables

Deliverables coming







