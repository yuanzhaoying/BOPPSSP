# discount rate
r = 0.01

# Create project class
class Project(object):
    def __init__(self, j, d):
        self.j = j  # Project Number
        self.d = d  # Project duration
        self.r = []  # Resource availability
        self.p = 0  # Cash inflow
        self.c = 0  # Cash outflow
        self.due_time = 0  # Planned delivery date
        self.deadline = 0  # Latest completion time
        self.c_trad = 0  # Project delay cost
        self.s = 0  # Project Start Time

# Input test set file
def read_in(file):
    global N, T, projects, K, R, pij, C0, m, set_inter_project_1, p_l
    # initialize variable
    projects = []
    R = []
    set_inter_project =[]
    file_input = open(file, "r")
    line = file_input.readline()
    s = line.split()
    N = int(s[0])
    K = int(s[1])
    T = int(s[2])
    C0 = int(s[3])
    m = int(s[4])
    line = file_input.readline()
    r_list = line.split()
    for i in r_list:
        R.append(int(i))
    line = file_input.readline()
    set_list = line.split()
    for i in set_list:
        set_inter_project.append(int(i))
    set_inter_project_1 = []
    index = 0
    for index_id in range(3, round(m / 2 + 1)):
        for _ in range(10):
            sublist = set_inter_project[index:index + index_id]
            set_inter_project_1.append(sublist)
            index += index_id
    p_l = []
    line = file_input.readline()
    p_list = line.split()
    for i in p_list:
        p_l.append(int(i))
    line = file_input.readline()
    pij = [[] for _ in range(N)]
    i = 0
    while i < N:
        s = line.split()
        d = int(s[0])
        projects.append(Project(i + 1, d))
        k = 0
        for k in range(K):
            projects[i].r.append(int(s[k + 1]))
        projects[i].p = int(s[k + 2])
        projects[i].c = int(s[k + 3])
        projects[i].due_time = int(s[k + 4])
        projects[i].deadline = int(s[k + 5])
        projects[i].c_trad = int(s[k + 6])
        for j in range(N):
            pij[i].append(int(s[k + j + 7]))
        line = file_input.readline()
        i += 1
    file_input.close()

# Evaluate individuals
def update_PA(PA1, population):
    for pi in population:
        objective1 = pi[0]
        objective2 = pi[1]
        update_if = True
        for i in range(len(PA1)):
            if PA1[i][0] >= objective1 and PA1[i][1] <= objective2:
                update_if = False
                break
            elif PA1[i][0] <= objective1 and PA1[i][1] >= objective2:
                PA1[i] = 0
        if update_if:
            PA1.append(pi)
        while 0 in PA1:
            PA1.remove(0)
    return PA1