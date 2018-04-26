function theta = nesterov_momentum(df, iters, theta1, gamma1, gamma_damp, beta, epsilon)


v = zeros(iters,1);
theta = zeros(iters,1);
gamma = zeros(iters,1);
v1 = 0;

v(1) = v1;
theta(1) = theta1;
gamma(1) = gamma1;

for t=2:iters
    gamma(t) = gamma(t-1)*gamma_damp;
    v(t) = beta*v(t-1) - epsilon*df(theta(t-1) + gamma(t-1)*beta*v(t-1));
    theta(t) = theta(t-1) + gamma(t)*v(t);
end