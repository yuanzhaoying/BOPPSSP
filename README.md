# BOPPSSP

Datasets from Hongbo Li, Zhijie Yuan, Manman Yang, Zhaoying Yuan and Xianchao Zhang, (2025, working paper), Project portfolio selection and scheduling considering net present value and delayed delivery.

## project data:

Data sets used for computational experiments.

- **J1**: 80 instances, each with 30 candidate projects (where $N=30$ for J1). 
- **J2:** 80 instances, each with 60 candidate projects (where $N=60$ for J2). 
- **J3:** 80 instances, each with 90 candidate projects (where $N=90$ for J3). 
- **J4:** 80 instances, each with 120 candidate projects (where $N=120$ for J4). 

Each file in J1-J4 folder represents an instance, and all RCP files share the same format. 

**Data structure:**

**Line 1:** The first number indicates the Number of candidate projects, the second number indicates the Number of resource types, the third number indicates the Planning horizon, the fourth number indicates the Initial capital, and the fifth number indicates the Maximum number of selected projects.

**Line 2:** The first number indicates the Availability of the first resource type, the second number indicates the Availability of the second resource type, and so on.

**Line 3:** Represents all set of projects interactions sets $I_l \quad(|I_l|=3,4,\cdots,\frac{m}{2})$. The $1^{st}$ to $3^{rd}$ numbers represent the first group of three-project interactions, the $4^{th}$ to $6^{th}$ numbers represent the second group of three-project interactions, and so on, with a total of ten groups of three-project interactions. Then there are ten groups of four-project interactions, up to ten groups of $\frac{m}{2}$-project interactions.

**Line 4:** Represents all Interaction cash flows for set of projects interactions $I_l$. The $1^{st}$ to $10^{th}$ numbers indicate the cash flows for the ten groups of three-project interactions, the $11^{th}$ to $20^{th}$ numbers indicate the cash flows for the ten groups of four-project interactions, and so on. The $(5m-11)^{th}$ to $(5m-20)^{th}$ numbers indicate the cash flows for the ten groups of $\frac{m}{2}$-project interactions.

**Lines 5 to $N$:** In each line, the first number indicates the Duration, the $2^{nd}$ to $(r+1)^{th}$ numbers (where $r$ is the number of resource types in this instance) indicate the Resource availability, the $(r+2)^{th}$ number indicates the Cash inflow, the $(r+3)^{th}$ number indicates the Cash outflow, the $(r+4)^{th}$ number indicates the Planned delivery date, the $(r+5)^{th}$ number indicates the Latest completion time, the $(r+6)^{th}$ number indicates the Unit cost of delay, and the $(r+7)^{th}$ to $(r+N+6)^{th}$ numbers represent the pairs of projects interactions cash flows between this project and the $1^{st}$ to $N^{th}$ projects.

## CPLEX Code:

Python files for solving problems using CPLEX. 

- `Cplex.py`: Contains the CPLEX scheduling function and the program's main function.  
- `Method.py`: Supporting functions called by `Cplex.py`, including discount rate assignment, project class definitions, dataset reading, and individual evaluation functions.

