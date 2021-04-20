x = 0:.5:10;
mu = 5;
e = 2.71828;
sigma_1 = .5;
sigma_2 = 1.0;
sigma_3 = 1.5;


y1 = (1 / ((sigma_1) * sqrt(2 * pi))) * e.^-((x-mu).^2) / (2 * (sigma_1).^2);
y2 = (1 / ((sigma_2) * sqrt(2 * pi))) * e.^-((x-mu).^2) / (2 * (sigma_2).^2);
y3 = (1 / ((sigma_3) * sqrt(2 * pi))) * e.^-((x-mu).^2) / (2 * (sigma_3).^2);

plot(x,y1,"y""-")
hold on
plot(x,y2,"b""--")
hold on
plot(x,y3,"r"":")



xlabel('x')
ylabel('phi(x-5,sigma)')
legend('sigma(.5)','sigma(1.0)','sigma(1.5)')
hold off