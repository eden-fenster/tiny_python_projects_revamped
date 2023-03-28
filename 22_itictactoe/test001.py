from dataclasses import dataclass

@dataclass
class State:
    name: str
    size: int

state = State(name="start", size=2)
print(state)
state.name = "new"
print(state)