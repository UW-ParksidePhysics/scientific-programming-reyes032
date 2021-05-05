dia_1 = ones(1,5);

twos = 2 * dia_1;
dia_2 = diag(twos);

dia_neg_ones = -1 * ones(1,4);
negitive_ones = diag(dia_neg_ones);
zeros = [[zeros(1,4) ; negitive_ones] zeros(5,1)];
zeros_opp = zeros';
x5 = zeros + zero_opp + dia_2;

v = (1/(2*(1/(5+1))^2)) * x5;

e = eig(v);
[V,D] = eig(v);
fift_eigenvector = V(:,5);
fifth_eigenvalue = D(5,5);



x = [0.1667, 0.3333, 0.5000, 0.6667, 0.8333];
x2 = [0:.1:1];
y = sqrt(2) * sin(x3 * pi);

plot(x, fift_eigenvector, '-',x3,y, ':')
xlabel('x')
ylabel('eigenvectors')

