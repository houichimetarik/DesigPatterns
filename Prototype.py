"""
Name: prototype, type: creational
Problem:
- creating the object is very complex for the client due to the high number of parameters required and
  the complex subclassing and interface implementations
- The client is required to know a lot about the object's composition and characteristics in order to create it
- the object creation is expensive in terms of time and resources
- There are already existed similar objects ( like those that the client wants to create) in the system.
- we need to reduce the number of classes used in the client code
solution:
- one idea to do this is to provide the client with the possibility to copy and use already existed objects
- make the object able to clone itself, we can't let an other class to clone it because it may violate encapsulation
- create a class that creates the objects ( prototypes ) then provide a static parameterized method to dynamically return
  the specific prototype wanted by the client
Consequences:
- Prototyping is another way for specializing a class other than inheritance.
- hiding the complexity of objects creation from the client
- reduced number of classes
- implementing the object is the client's code can be done without specifying the concrete class of the
  object itself , thus the client's code is completely decoupled
"""

