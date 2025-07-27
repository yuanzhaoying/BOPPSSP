def schedule(e):
    start = time.time()
    mdl = Model(name='schedule')
    # Define: X_i,t
    var_list_X = [(i, t) for i in range(N) for t in range(T)]
    X = mdl.binary_var_dict(var_list_X)
    # Define: P_i
    var_list_P = [i for i in range(N)]
    P = mdl.integer_var_dict(var_list_P)
    u = mdl.binary_var_dict(var_list_P)
    z = mdl.continuous_var_dict([(i, t) for i in range(N) for t in range(T)])
    # Define: y_l
    y = mdl.binary_var_list(L, name="y")
    # Define: g_l
    g = mdl.continuous_var_list(L, name="g")
    # Define: u_lk
    u_lk = {}
    for l in range(L):
        I_l = I_list[l]
        len_I_l = len(I_l)
        u_lk[l] = mdl.binary_var_list(len_I_l)
    # Define: delta_lt
    delta = {}
    for l in range(L):
        delta[l] = mdl.binary_var_list(T)
    # Define: w_lt
    w = {}
    for l in range(L):
        w[l] = mdl.binary_var_list(T)


    # ========== linearization constraints ==========
    mdl.add_constraint(sum(p[i] * z[(i, t)] for i in range(N) for t in range(T)) <= e)  # ɛ Constraints
    for i in range(N):
        mdl.add_constraint(P[i] >= sum([(t + d[i] ) * X[i, t] for t in range(T)]) - h[i])
        mdl.add_constraint(P[i] >= 0)
        mdl.add_constraint(sum([(t + d[i] ) * X[i, t] for t in range(T)]) <= End[i])  # Deadline constraint for completion
        mdl.add_constraint(sum([X[i, t] for t in range(T)]) <= 1)  # Each activity can only be selected once
    mdl.add_constraint(sum([sum([X[i, t] for t in range(T) for i in range(N)])]) <= m)  # Constraint on the total number of candidate projects
    for i in range(N):
        for t in range(T):
            mdl.add_constraint(z[(i, t)] <= P[i])
            mdl.add_constraint(z[(i, t)] <= 10e5 * X[(i, t)])
            mdl.add_constraint(z[(i, t)] >= P[i] - 10e5 * (1 - X[(i, t)]))
            mdl.add_constraint(z[(i, t)] >= 0)
    # Capital constraints
    C_t_prev = C0
    for t in range(T):
        C_t =  (C_t_prev + 0.8 * sum(delta[l][t] * c_l[l] for l in range(L)) +  sum([sum([0.8 * (C_in[i] * sum([X[i, (t0 - d[i] + 1)] for t0 in range(d[i] - 1, t + 1)]) - C_out[i] * sum([X[i, t0] for t0 in range(t + 1)])) for i in range(N)])]))
        mdl.add_constraint(C_t >= 0)
        C_t_prev = C_t
    # Resource constraints
    for k in range(K):
        for t in range(T):
            mdl.add_constraint(sum([sum([X[i, t] for t in range(max(0, t - d[i] + 1), (t + 1))]) * r[i][k] for i in range(N)]) <= R[k])

    # y_l constraints
    for l in range(L):
        I_l = I_list[l]
        len_I_l = len(I_l)
        sum_x = mdl.sum(X[(i , t)] for i in I_l for t in range(T))
        mdl.add_constraint(y[l] * len_I_l <= sum_x)
        mdl.add_constraint(y[l] >= sum_x - (len_I_l - 1))

    # g_l constraints
    for l in range(L):
        I_l = I_list[l]
        len_I_l = len(I_l)
        for k in range(len_I_l):
            i = I_l[k]
            sum_g = mdl.sum(X[(i , t)] * (t + d[i ] - 1) for t in range(T))
            mdl.add_constraint(g[l] >= sum_g)
            mdl.add_constraint(sum_g >= g[l] - 10e5 * (1 - u_lk[l][k]))
        mdl.add_constraint(mdl.sum(u_lk[l][k] for k in range(len_I_l)) >= 1)

    # delta_lt constraints
    for l in range(L):
        mdl.add_constraint(mdl.sum(delta[l][t] for t in range(T)) == 1)
        mdl.add_constraint(g[l] == mdl.sum((t) * delta[l][t] for t in range(T)))

    # w_lt constraints
    for l in range(L):
        for t in range(T):
            mdl.add_constraint(w[l][t] <= y[l])
            mdl.add_constraint(w[l][t] <= delta[l][t])
            mdl.add_constraint(w[l][t] >= y[l] + delta[l][t] - 1)

    # ========== Define the objective function ==========
    mdl.maximize(sum(sum(c_l[l] * theta[t] * w[l][t] for t in range(T)) for l in range(L)) +
        sum([sum([(X[i, t] * (C_in[i] * Rho ** (t + d[i]) - C_out[i] * Rho ** t)) for t in range(T)]) for i in range(N)]) )
    # Limit solution time
    mdl.set_time_limit(limit_time)
    mdl.solve()
    # Calculation objective 1
    object1 = mdl.solution.get_objective_value()
    # Calculation objective 2
    object2 = sum(p[i] * z[(i, t)].solution_value for i in range(N) for t in range(T))
    end = time.time()
    time_temp = end - start
    return object1, object2, time_temp