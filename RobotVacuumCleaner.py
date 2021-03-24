import agents, random

class Clean(agents.Thing):
    pass
class Dirty(agents.Thing):
    pass

class Park2D(agents.GraphicEnvironment):
    def percept(self, agent):
        return self.list_things_at(agent.location)

def execute_action(self, agent, action):
    if action == 'Right':
        agent.location = agents.loc_B
        agent.performance -= 1
    elif action == 'Left':
        agent.location = agents.loc_A
        agent.performance -= 1
    elif action == 'Suck':
        if self.status[agent.location] == 'Dirty':
            agent.performance += 10
        self.status[agent.location] = 'Clean'
    """
    if action == "Go":
        print('go to the location: {}'.format(agent.location))
        agent.movedown()
    else:
            Action = {
                "Clean": lambda: self.action(action, "Clean", 'Clean at location: {}', agent, Clean),
                "Dirty": lambda: self.action(action, "Dirty", "Dirty at location: {}", agent, Dirty)
            }
            Action[action]()

    def action(self, action, actiontext, text, agent, tclass):
        if action == actiontext:
            items = self.list_things_at(agent.location, tclass=tclass)
            if len(items) != 0:
                if (lambda thing, tclass: True if isinstance(thing, tclass) else False)(items[0], tclass):
                    print(text.format(agent.location))
                    self.delete_thing(items[0])
    """

    def is_done(self):
        no_edibles = not any( isinstance(thing, Clean) or isinstance(thing, Dirty) for thing in self.things)
        dead_agents = not any(agent.is_alive() for agent in self.agents)
        return dead_agents or no_edibles

class RobotVacuum(agents.Agent):
    Score = 0
    location = [random.randint(0, 10), random.randint(0, 10)]

    def moveforward(self, success=True):
        if not success:
            return
        if self.direction.direction == agents.Direction.R:
            self.location[0] += 1
        elif self.direction.direction == agents.Direction.L:
            self.location[0] -= 1
        elif self.direction.direction == agents.Direction.D:
            self.location[1] += 1
        elif self.direction.direction == agents.Direction.U:
            self.location[1] -= 1

    def turn(self, d):
        self.direction = self.direction + d


def SimpleReflexAgentProgram():
    def program(percept):
        loc, status = percept
        return ('Suck' if status == 'Dirty'
                else 'Right' if loc == agents.loc_A
        else 'Left')
    return program


def main():
    park = Park2D(10, 10, color={'RobotVacuum': (200, 0, 0), 'Clean': (0, 200, 200), 'Dirty': (230, 115, 40)})
    robot = RobotVacuum(SimpleReflexAgentProgram())
    for x in range(10):
        park.add_thing((lambda : Clean() if random.randint(0, 1) == 0 else Dirty())(), [x, x])
    park.add_thing(robot, robot.location)
    park.run(20)

main()
