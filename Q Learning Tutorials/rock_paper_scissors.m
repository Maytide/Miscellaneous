% Linear programming to optimize minimax zero-sum game
% https://www.princeton.edu/~rvdb/542/lectures/lec8.pdf
% or rps-lp.pdf in same folder
clear; close all; clc

T = [0 1 -1; -1 0 1; 1 -1 0];
% T = [0 1 -1; -1 0 1; 1.01 -1 0];
% T = [0 0 -1; -1 0 0; 1 -1 0];
% T = [1 1 1; 0 0 0; 0 0 0];
e1 = [1 0 0]';
e2 = [0 1 0]';
e3 = [0 0 1]';
e = e1+e2+e3;

f = [0 0 0 1];
A = [-T' e]
b = zeros(3,1);
Aeq = [e' 0];
beq = [1];
lb = [0 0 0 -1000];
ub = [];

xv = linprog(-f,A,b,Aeq,beq,lb,ub);