
# BOPPSSP
Datasets from Hongbo Li, Zhijie Yuan, Manman Yang, Zhaoying Yuan and Xianchao Zhang, (2025, working paper), Project portfolio selection and scheduling considering net present value and delayed delivery.

Datasets test project data sets:
Data sets used for calculation experiments.
J1: 80 instances with 30 projects each.
J2: 80 instances with 60 projects each.
J3: 80 instances with 90 projects each.
J4: 80 instances with 120 projects each.
All file data in folders J1 to J4 are expressed as follows:
The first line respectively indicates: Num. of candidate projects, Num. of resource types, Planning horizon, Initial capital and Max. num. of selected projects.
The second line respectively indicates: Availability of each resource.
The third line indicates: set of projects interactions I_l (|I_l|=3,4,…,m/2) in this instance. The data is expressed as 10 groups of 3-project interactions, 10 groups of 4-project interactions ... 10 groups of m/2-project interactions.
The fourth line indicates: Interaction cash flows of set of projects interactions I_l (|I_l |=3,4,…,m/2) in this instance.
From the fifth line to the last line, there are a total of N lines (N = Num. of candidate projects). Each line respectively indicates: Project duration, Resource availability, Cash inflow, Cash outflow, Planned delivery date, Latest completion time, Unit cost of project delay and the cash flow of pairs of projects interactions between this project and each project (|I_l|=2).

Cplex:
Files used for cplex scheduling.
