from Problems import Problem_Class1, Problem_Class2, Problem_Class3, Problem_Class4, Problem_Class5
from Algorithms.Hill_Climbing import Hill_Climbing_normal, Hill_Climbing_stochastic, Hill_Climbing_randomRestart, Hill_Climbing_firstChoice
from Algorithms import Genetic,Simulated_Annealing, BFS, Two_Sided, A_Star, Uniform_Cost
from Algorithms.DFS import DFS, DFS_Limited_Depth, DFS_Iterative_Deepening
import logging.handlers, os



handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", "/home/kasra/Desktop/Report.log"), 'w')
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "DEBUG"))
root.addHandler(handler)

pc1 = Problem_Class1.Problem_Class1(None)
pc2 = Problem_Class2.Problem_Class2(None)
pc3 = Problem_Class3.Problem_Class3(None)
pc4 = Problem_Class4.Problem_Class4(None)
pc5 = Problem_Class5.Problem_Class5(None)

run = True
while run:
    a = input("\nChoose problem class:\n")
    b = int(a)
    if b == 1:
        bfs = BFS.BFS()
        bfs.solve(pc1, True)
        two_sided = Two_Sided.Two_Sided()
        two_sided.solve(pc1)
        dfs = DFS.DFS()
        print("\nDFS:")
        dfs.solve(pc1, None, 0)

    elif b == 2:
        bfs = BFS.BFS()
        bfs.solve(pc2, True)
        dfs = DFS_Limited_Depth.DFS_Limited_Depth()
        print("\nDFS_limited_depth:")
        dfs.solve(pc2, None, 0, 10)
        astar = A_Star.A_Star()
        astar.solve(pc2)

    elif b == 3:
        uc = Uniform_Cost.Uniform_Cost()
        uc.solve(pc3)
        print("\nDFS_Iterative_Deepening:")
        idg = DFS_Iterative_Deepening.DFS_Iterative_Deepening()
        idg.solve(pc3, None, 0)

    elif b == 4:
        init_state = pc4.initial_state()
        hcn = Hill_Climbing_normal.Hill_Climbing_normal()
        hcn.solve(pc4, init_state)
        hcs = Hill_Climbing_stochastic.Hill_Climbing_stochastic()
        hcs.solve(pc4, init_state)
        hcr = Hill_Climbing_randomRestart.Hill_Climbing_randomRestart()
        hcr.solve(pc4, init_state)
        hcf = Hill_Climbing_firstChoice.Hill_Climbing_firstChoice()
        hcf.solve(pc4, init_state)

    elif b == 5:
        sa = Simulated_Annealing.SimulatedAnnealing(root)
        print("linear:")
        sa.solve(pc5, 1)
        print("exponential:")
        sa.solve(pc5, 2)
        print("logarithmic:")
        sa.solve(pc5, 3)

    elif b == 6:
        edges = [[0, 1], [0, 2], [1, 2], [1, 3], [3, 4], [2, 5], [4, 5], [5, 6], [6, 7], [0, 7], [4, 8], [5, 8], [4, 9],
                 [10, 11], [10, 12], [11, 12], [11, 13], [13, 14], [12, 15], [14, 15], [15, 16], [16, 17], [10, 17],
                 [14, 18], [15, 18], [14, 19], [8, 10], [6, 17], [14, 17], [10, 16]]
        gn = Genetic.Genetic()
        gn.find_optimum_allocation(4, 20, edges, 50, 0.05)

    elif b == -1:
        run = False

pc1 = Problem_Class1.Problem_Class1(None)




# pc4 = Problem_Class4.Problem_Class4(None)

# print(pc4.initial_state())
# pc4.get_childs(pc4.initial_state())
# i = pc4.initial_state()
# print(pc4.check_state_equality(i,pc4.get_childs(i)[0]))
# print(pc4.cost(i))
# hc = Hill_Climbing_stochastic.Hill_Climbing_stochastic()
# hc.solve(pc4)


# pc5 = Problem_Class5.Problem_Class5(None)
# print(pc5.cost(pc5.initial_state()))
# e = pc5.get_childs(pc5.initial_state())
# print(pc5.cost(e))
# for i in range(3):
#     e = pc5.get_childs(e)
#     print(pc5.cost(e))
    # print(e)








# x = pc2.initial_state()
# print(pc2.check_state_equality(x, x))
# print(pc1.check_state_equality(pc1.initial_state(), pc1.initial_state()))
#
# dfs1 = DFS.DFS()
# dfs1.solve(pc2, None, 0)

# dfs2 = DFS_Limited_Depth.DFS_Limited_Depth()
# dfs2.solve(pc2, None, 0)

# print(pc2.heuristic([2,1,3,4,5,6,7,8,0]))
# print(pc2.goal_state([1, 2, 3, 4, 5, 6, 7, 8, 0]))
# print("!!!")
# bfs1 = BFS.BFS()
# bfs1.solve(pc2)

# ts = Two_Sided.Two_Sided()
# ts.solve(pc1)

# for i in pc1.initial_state()[1]:
#
#     # print(str(i) + " " + str(state2))
#     if i in copy.deepcopy(pc1.initial_state())[1]:
#         print("true")
#     else:
#         print("false")

# print(str(11 in pc1.initial_state()[0]))


