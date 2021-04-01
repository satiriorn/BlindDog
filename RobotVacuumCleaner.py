import agents, random

class Clean(agents.Thing): pass
class Dirty(agents.Thing): pass

class Park2D(agents.GraphicEnvironment):
    moveR, moveD, startloc  = True, True, False
    locationsquare = [0, 1]
    level = 1
    def percept(self, agent): return self.list_things_at(agent.location)

    def execute_action(self, agent, action):
        print(agent.performance)
        print(agent.location)
        if self.startloc:
            if action == 'Continue':
                self.AgentSquare(agent)
                self.AgentSnake(agent)
            elif action == 'Suck':
                self.LastLocationDirty = agent.location
                self.add_thing(Clean(), agent.location)
                self.delete_thing(self.list_things_at(agent.location, tclass=Dirty)[0])
                agent.performance += 10
        else:
            if agent.location[1] != 0: agent.location[1] -= 1
            elif agent.location[0] != 0: agent.location[0] -= 1
            elif agent.location[1] + agent.location[0] == 0: self.startloc = True

    def AgentSnake(self, agent):
        agent.performance -= 1
        if self.moveR and agent.location[0] != self.width - 1: agent.location[0] += 1
        elif self.moveR and agent.location[0] == self.width - 1:
            self.moveR = False
            agent.location[1] += 1
        elif agent.location[0] != 0 and self.moveR == False: agent.location[0] -= 1
        elif agent.location[0] == 0 and self.moveR == False:
            self.moveR = True
            agent.location[1] += 1
        elif agent.location[0] == self.width - 1 and agent.location[1] == self.width - 1 or agent.location[0] == 0 and \
                agent.location[1] == self.width - 1:
            print(agent.performance)
            self.is_done()

    def AgentSquare(self, agent):
        if self.moveD == False and self.moveR == False and agent.location == self.locationsquare:
            for x in range(len(self.locationsquare)):self.locationsquare[x]+=1
            self.level +=1
            self.moveR = True
        if self.locationsquare ==[self.level-1, self.level]:
            print(agent.performance)
            self.is_done()
        agent.performance -= 1
        if self.moveR and agent.location[0] != self.width - self.level: agent.location[0] += 1
        elif self.moveR and agent.location[0] == self.width - self.level:
            self.moveR = False
            self.moveD = True
            agent.location[1] += 1
        elif self.moveD and agent.location[1] != self.height - self.level: agent.location[1] += 1
        elif self.moveD and agent.location[1] == self.height - self.level:
            self.moveD = False
            agent.location[0] -= 1
        elif agent.location[0]!=self.locationsquare[0]: agent.location[0] -= 1
        elif agent.location[0]==self.locationsquare[0]: agent.location[1] -= 1

    def is_done(self):
        no_edibles = not any(isinstance(thing, Clean) or isinstance(thing, Dirty) for thing in self.things)
        dead_agents = not any(agent.is_alive() for agent in self.agents)
        return dead_agents or no_edibles


class RobotVacuum(agents.Agent):
    location = [random.randint(2, 7), random.randint(2, 7)]
    AgentSnake = False

def program(percepts):
    for p in percepts:
        if isinstance(p, Dirty):
            return 'Suck'
        elif isinstance(p, Clean):
            return "Continue"

def main():
    park = Park2D(10, 10, color={'RobotVacuum': (200, 0, 0), 'Clean': (0, 200, 200), 'Dirty': (230, 115, 40)})
    robot = RobotVacuum(program)
    for x in range(10):
        for y in range(10):
            park.add_thing((lambda: Clean() if random.randint(0, 1) == 0 else Dirty())(), [x, y])
    park.add_thing(robot, robot.location)
    park.run(250)

main()