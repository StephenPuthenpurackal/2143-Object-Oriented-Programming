<div class="item-page" itemscope="" itemtype="https://schema.org/Article">

<div class="page-header">

# UML Activity Diagram: What is, Components, Symbol, EXAMPLE

</div>

  - Details  
    <span class="icon-calendar" aria-hidden="true"></span> Last Updated:
    06 February 2020

<div itemprop="articleBody">

<div>

<div class="top-ads-boxes" style="float:left;padding-right:6px;">

<div id="div-gpt-ad-1565016699961-0">

</div>

</div>

</div>

## <span id="1"></span>What is an Activity Diagram?

Activity diagram is defined as a UML diagram that focuses on the
execution and flow of the behavior of a system instead of
implementation. It is also called **object-oriented flowchart**.
Activity diagrams consist of activities that are made up of actions
which apply to behavioral modeling technology.

In this, UML tutorial you will learn,

  - [What is an Activity Diagram?](#1)
  - [Components of Activity Diagram](#2)
  - [Why use Activity Diagrams?](#3)
  - [Activity Diagram Notations](#4)
  - [How to draw an activity diagram?](#5)
  - [Example of Activity Diagram](#6)
  - [When Use Activity Diagram](#7)

## <span id="2"></span>Components of Activity Diagram

### Activities

It is a behavior that is divided into one or more actions. Activities
are a network of nodes connected by edges. There can be action nodes,
control nodes, or object nodes. Action nodes represent some action.
Control nodes represent the control flow of an activity. Object nodes
are used to describe objects used inside an activity. Edges are used to
show a path or a flow of execution. Activities start at an initial node
and terminate at a final node.

### Activity partition/swimlane

An activity partition or a swimlane is a high-level grouping of a set of
related actions. A single partition can refer to many things, such as
classes, use cases, components, or interfaces.

If a partition cannot be shown clearly, then the name of a partition is
written on top of the name of an activity. ****

### Fork and Join nodes

Using a fork and join nodes, concurrent flows within an activity can be
generated. A fork node has one incoming edge and numerous outgoing
edges. It is similar to one too many decision parameters. When data
arrives at an incoming edge, it is duplicated and split across numerous
outgoing edges simultaneously. A single incoming flow is divided into
multiple parallel flows.

A join node is opposite of a fork node as It has many incoming edges and
a single outgoing edge. It performs logical AND operation on all the
incoming edges. This helps you to synchronize the input flow across a
single output edge.

**Pins**

An activity diagram that has a lot of flows gets very complicated and
messy.

Pins are used to clearing up the things. It provides a way to manage the
execution flow of activity by sorting all the flows and cleaning up
messy thins. It is an object node that represents one input to or an
output from an action.

Both input and output pins have precisely one edge.

## <span id="3"></span>Why use Activity Diagrams?

Activity diagram allows you to create an event as an activity which
contains a collection of nodes joined by edges. An activity can be
attached to any modeling element to model its behavior. Activity
diagrams are used to model,

<div>

<div id="div-gpt-ad-9092914-1">

</div>

</div>

  - Use cases
  - Classes
  - Interfaces
  - Components
  - Collaborations

Activity diagrams are used to model processes and workflows. The essence
of a useful activity diagram is focused on communicating a specific
aspect of a system's dynamic behavior. Activity diagrams capture the
dynamic elements of a system.

Activity diagram is similar to a flowchart that visualizes flow from one
activity to another activity. Activity diagram is identical to the
flowchart, but it is not a flowchart. The flow of activity can be
controlled using various control elements in the UML diagram. In simple
words, an activity diagram is used to activity diagrams that describe
the flow of execution between multiple activities.

## <span id="4"></span>Activity Diagram Notations

Activity diagrams symbol can be generated by using the following
notations:

  - Initial states: The starting stage before an activity takes place is
    depicted as the initial state
  - Final states: The state which the system reaches when a specific
    process ends is known as a Final State
  - State or an activity box:
  - Decision box: It is a diamond shape box which represents a decision
    with alternate paths. It represents the flow of control.

![Activity Digram Notation and
Symbol](./images/c358d0ffac820b33a493a6d92ff168b209745cae.png)

## <span id="5"></span>How to draw an activity diagram?

Activity diagram is a flowchart of activities. It represents the
workflow between various system activities. Activity diagrams are
similar to the flowcharts, but they are not flowcharts. Activity diagram
is an advancement of a flowchart that contains some unique capabilities.

Activity diagrams include swimlanes, branching, parallel flow, control
nodes, expansion nodes, and object nodes. Activity diagram also supports
exception handling.

To draw an activity diagram, one must understand and explore the entire
system. All the elements and entities that are going to be used inside
the diagram must be known by the user. The central concept which is
nothing but an activity must be clear to the user. After analyzing all
activities, these activities should be explored to find various
constraints that are applied to activities. If there is such a
constraint, then it should be noted before developing an activity
diagram.

All the activities, conditions, and associations must be known. Once all
the necessary things are gathered, then an abstract or a prototype is
generated, which is later converted into the actual diagram.

Following rules must be followed while developing an activity diagram,

1.  All activities in the system should be named.
2.  Activity names should be meaningful.
3.  Constraints must be identified.
4.  Activity associations must be known.

## <span id="6"></span>Example of Activity Diagram

Let us consider mail processing activity as a sample for Activity
Diagram. Following diagram represents activity for processing e-mails.

![activity
diagram](./images/8bccee1920e80fdd1b01894335c8dec838093ed8.png)

In the above activity diagram, three activities are specified. When the
mail checking process begins user checks if mail is important or junk.
Two guard conditions \[is essential\] and \[is junk\] decides the flow
of execution of a process. After performing the activity, finally, the
process is terminated at termination node.

## <span id="7"></span>When Use Activity Diagram

Activity diagram is used to model business processes and workflows.
These diagrams are used in software modeling as well as business
modeling.

Most commonly activity diagrams are used to,

1.  Model the workflow in a graphical way, which is easily
    understandable.
2.  Model the execution flow between various entities of a system.
3.  Model the detailed information about any function or an algorithm
    which is used inside the system.
4.  Model business processes and their workflows.
5.  Capture the dynamic behavior of a system.
6.  Generate high-level flowcharts to represent the workflow of any
    application.
7.  Model high-level view of an object-oriented or a distributed system.

## Summary

  - Activity diagram is also called as **object-oriented flowcharts**.
  - Activity diagrams consist of activities that are made up of smaller
    actions.
  - Activity is a behavior that is divided into one or more actions.
  - It uses action nodes, control nodes and object nodes.
  - An activity partition or a swimlane is a high-level grouping of a
    set of related actions.
  - Fork and join nodes are used to generate concurrent flows within an
    activity.
  - Activity diagram is used to model business processes and workflows.

 

</div>

  - [<span class="icon-chevron-left" aria-hidden="true"></span>
    <span aria-hidden="true">Prev</span>](/state-machine-transition-diagram.html "State Machine Diagram: UML Tutorial with EXAMPLE")
  - [<span aria-hidden="true">Next</span>
    <span class="icon-chevron-right" aria-hidden="true"></span>](/interaction-collaboration-sequence-diagrams-examples.html "Interaction, Collaboration, Sequence Diagrams with EXAMPLES")

</div>