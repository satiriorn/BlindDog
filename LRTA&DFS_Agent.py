import agents, search

class Unspecified(agents.Thing): pass
class Specified(agents.Thing): pass
class ControlPoint(agents.Thing): pass

class Park2D(agents.GraphicEnvironment):
    moveR, moveD, startloc  = True, True, False
    locationsquare = [0, 1]
    level = 1
    def percept(self, agent): return self.list_things_at(agent.location)

    def execute_action(self, agent, action):
        print(agent.location)
        if action == "Unspecified"and agent.SearchPoint:
            if agent.location_point[0]<agent.location[0] and agent.location_point[0] != agent.location[0]:
                agent.location[0]-=1
            elif agent.location_point[0] > agent.location[0] and agent.location_point[0] != agent.location[0]:
                agent.location[0]+=1
            elif agent.location_point[0] == agent.location[0]:
                if agent.location_point[1]< agent.location[1]:
                    agent.location[1]-=1
                else:
                    agent.location[1] += 1
            self.add_thing(Specified(), agent.location)
        if agent.SearchPoint==False:
            if agent.location[1] != 0: agent.location[1] -= 1
            elif agent.location[0] != 0: agent.location[0] -= 1
            elif agent.location[1] + agent.location[0] == 0: self.startloc = True
        elif self.startloc:
            self.AgentSnake(agent)
        if agent.location_point == agent.location:
            agent.SearchPoint = False
            self.AgentSnake(agent)


    def AgentSnake(self, agent):
        if self.moveR and agent.location[0] != self.width - 1:
            agent.location[0] += 1
        elif self.moveR and agent.location[0] == self.width - 1:
            self.moveR = False
            agent.location[1] += 1
        elif agent.location[0] != 0 and self.moveR == False:
            agent.location[0] -= 1
        elif agent.location[0] == 0 and self.moveR == False:
            self.moveR = True
            agent.location[1] += 1
        elif agent.location[0] == self.width - 1 and agent.location[1] == self.width - 1 or agent.location[
            0] == 0 and \
                agent.location[1] == self.width - 1:
            self.is_done()

    def is_done(self):
        no_edibles = not any(isinstance(thing, Unspecified) or isinstance(thing, Specified) for thing in self.things)
        dead_agents = not any(agent.is_alive() for agent in self.agents)
        return dead_agents or no_edibles


class RobotVacuum(agents.Agent):
    location = [1, 8]
    SearchPoint = True

def program(percepts):
    for p in percepts:
        if isinstance(p, Specified):
            return "Obstacle"
        elif isinstance(p, Unspecified):
            return 'Unspecified'


def main():
    park = Park2D(10, 10, color={'RobotVacuum': (200, 0, 0), 'Specified': (0, 200, 200), 'Unspecified': (230, 115, 40),
                                 'Obstacle': (0, 0, 200), 'ControlPoint': (0, 200, 0)})
    loc_point = [8, 1]
    robot = RobotVacuum(program, loc_point)
    for x in range(10):
        for y in range(10):
            park.add_thing(Unspecified(), [x, y])
    park.add_thing(ControlPoint(), loc_point)
    for x in range(0, 4):
            park.add_thing(agents.Obstacle(), [x, 5])
    for y in range(5, 8):
        park.add_thing(agents.Obstacle(), [3, y])
    park.add_thing(robot, robot.location)
    park.run(250)
    print(park.get_world())
main()