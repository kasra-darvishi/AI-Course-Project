from Problems import Problem_Class1


class BFS:
    visited_states = []
    queue = []
    stop = False
    cntr = 200
    def __init__(self):
        a = 2

    def solve(self, problem_instance, do_graph_search):

        print("\nBFS:")
        self.queue = []
        self.visited_states = []
        self.stop = False
        self.queue.append([problem_instance.initial_state(), ''])
        current_state = None

        numberOfProduced = 0
        numberOfExpanded = 0
        depth = 0
        maxNumberOfNodesInMem = 0

        while not self.stop:
            mx = len(self.visited_states) + len(self.queue)
            if mx > maxNumberOfNodesInMem:
                maxNumberOfNodesInMem = mx

            self.cntr = self.cntr - 1
            current_state = self.queue.pop(0)
            numberOfExpanded += 1
            # print(current_state)

            temp_state = current_state
            tmp_childs = problem_instance.get_childs(current_state[0])
            numberOfProduced += len(tmp_childs)
            for child_state in tmp_childs:
                if not self.repetitive_state(child_state[0], problem_instance):
                    if do_graph_search:
                        self.visited_states.append(child_state[0])
                    if temp_state == None:
                        self.queue.append([child_state[0], child_state[1]])
                        if problem_instance.goal_state(child_state[0]):
                            self.stop = True
                            print(child_state[1])
                    else:
                        self.queue.append([child_state[0], temp_state[1] + ' ' + child_state[1]])
                        if problem_instance.goal_state(child_state[0]):
                            self.stop = True
                            final = temp_state[1] + ' ' + child_state[1]
                            print("moves:" + final)
                            print("depth: " + str(final.count(' ')))
                            print("number of expanded: " + str(numberOfExpanded))
                            print("number of produced: " + str(numberOfProduced))
                            print("max number of nodes in memory: " + str(maxNumberOfNodesInMem))



    def repetitive_state(self, state, problem_instance: Problem_Class1.Problem_Class1):
        for s in self.visited_states:
            if problem_instance.check_state_equality(s, state):
                return True
        return False



