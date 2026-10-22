```mermaid
classDiagram
    Animal <|-- Dog

    class Animal {
        +String name
        +eat() void
    }

    class Dog {
        +String breed
        +bark() void
    }
```
