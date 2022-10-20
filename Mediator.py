"""
Name: prototype, type: Behavioral
Problem:
- The problem needs to have a lot of objects communicating with each other
- the interdependencies among the objects is complex, unstructured and difficult to understand
- The application's behavior is distributed among multiple classes and need to be dynamically customizable
  but using inheritance/subclassing is impractical
solution:
- The idea here is to encapsulate the communications among objects in a new object called 'mediator' this object acts like
  a router for the other objects
- every object must provide an interface that defines how it communicates with other objects, the mediator object can't provide
  such interface because that will violate the encapsulation principle of those objects
- thus every object can use the mediator to handle communications with the others
Consequences:
- the client's code is decoupled from the concrete objects that communicate with each others
- it increase the usability, since we can reuse the objects in an other application by only customizing the mediator
  which act here a protocol of communication
- the control over communication is centralized, the complexity of communication required by the objets is traded by the
  complexity in the mediator, however the mediator may becomes so hard to maintain.
"""