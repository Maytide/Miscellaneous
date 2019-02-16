clear; close all; clc
% https://math.stackexchange.com/questions/214948/whats-the-algorithm-of-finding-the-convex-combination-of-permutation-matrices-f?rq=1

A = [.5 .2 .3;
     .1 .6 .3;
     .4 .2 .4];
b = reshape(A', [9 1]);
b = [b; 1];

id = eye(3);
v = perms([1 2 3]);
P = ones(9,6);

% Generate all permutation matrices
for i=1:6
    p = v(i,:);
    Pi = id(p,:)
    P(:,i) = reshape(Pi',[9 1]);
end
% Last row: sum of values = 1
P = [P; ones(1,6)];

% 0 <= xi <= 1
lb = zeros(6,1); 
ub = ones(6,1);

% It's a constraint satisfaction problem: no objective function
% no inequalities
x = linprog([],[],[],P,b,lb,ub)
sum(x)

% Verify solution
X = zeros(3,3);
for i=1:6
    p = v(i,:);
    Pi = id(p,:);
    X = X + x(i)*Pi
end

X