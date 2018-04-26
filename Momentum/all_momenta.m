clear; close all; clc


iters = 5000;
T = 1:iters;

h = 0.01;
df = @(x) 2*h*x;
f = @(x) h*x.^2;

theta1 = 10;
gamma1 = 0.99999;
gamma_damp = 1;
beta = 0.990;
epsilon = 1-beta;

thetaC = classical_momentum(df, iters, theta1, gamma1, gamma_damp, beta, epsilon);
thetaN = nesterov_momentum(df, iters, theta1, gamma1, gamma_damp, beta, epsilon);

beta = [0 0.9 0.99 0.999];
K = size(beta)
% epsilon = 1-beta;
epsilon = 1;

thetaA = aggregated_momentum(df, iters, K(2), theta1, gamma1, gamma_damp, beta, epsilon);

% f(theta(iters))
% theta(iters)
plot(T, thetaC);
hold on
plot(T, thetaN);
hold off
hold on
plot(T, thetaA);
hold off
title(['f(x)=' num2str(h) 'x^2'])
legend('theta Classical', 'theta Nesterov', 'theta AggMo')
ylim([-theta1 +theta1])