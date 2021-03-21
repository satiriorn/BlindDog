import agents

class Water(agents.Thing):
    pass
class Food(agents.Thing):
    pass

class BlindDog(agents.Agent):
    location = [0,1] #location = 1
    _food, _water = None, None
    def movedown(self): self.location[1] += 1 #self.location += 1
    def eat(self, thing): return (lambda: True if isinstance(thing, Food) else False)()
    def drink(self, thing): return (lambda: True if isinstance(thing, Water) else False)()


class Park2D(agents.GraphicEnvironment):
    def percept(self, agent): return self.list_things_at(agent.location)

    def execute_action(self, agent, action):
        if action == "move down":
            print('{} decided to {} at location: {}'.format(str(agent)[1:-1], action, agent.location))
            agent.movedown()
        elif action == "eat":
            items = self.list_things_at(agent.location, tclass=Food)
            if len(items) != 0:
                if agent.eat(items[0]):
                    print('{} ate {} at location: {}'
                          .format(str(agent)[1:-1], str(items[0])[1:-1], agent.location))
                    self.delete_thing(items[0])
        elif action == "drink":
            items = self.list_things_at(agent.location, tclass=Water)
            if len(items) != 0:
                if agent.drink(items[0]):
                    print('{} drank {} at location: {}'
                          .format(str(agent)[1:-1], str(items[0])[1:-1], agent.location))
                    self.delete_thing(items[0])

    def is_done(self):
        no_edibles = not any(isinstance(thing, Food) or isinstance(thing, Water) for thing in self.things)
        dead_agents = not any(agent.is_alive() for agent in self.agents)
        return dead_agents or no_edibles

def program(percepts):
    for p in percepts:
        if isinstance(p, Food): return 'eat'
        elif isinstance(p, Water): return 'drink'
    return 'move down'

park = Park2D(5,20, color={'BlindDog': (200,0,0), 'Water': (0, 200, 200), 'Food': (230, 115, 40)}) # park width is set to 5, and height to 20
dog = BlindDog(program)
dogfood = Food()
water = Water()
park.add_thing(dog, [0,1])
park.add_thing(dogfood, [0,5])
park.add_thing(water, [0,7])
morewater = Water()
park.add_thing(morewater, [0,15])
print("BlindDog starts at (1,1) facing downwards, lets see if he can find any food!")
park.run(20)