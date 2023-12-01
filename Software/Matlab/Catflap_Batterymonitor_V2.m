% clc 
% x = [0 0.05 0.25 0.5 0.75 1 1.25 1.5 1.62 1.75 2 2.1 2.25 2.33 2.44 2.5 2.53];
% y = [1.59 1.5 1.4 1.34 1.3 1.28 1.24 1.22 1.2 1.18 1.13 1.1 1.04 1 0.9 0.82 0.7];
%  
% % 1.59    0
% % 1.5     0.05
% % 1.4     0.25
% % 1.34    0.5 
% % 1.3     0.75
% % 1.28    1
% % 1.24    1.25
% % 1.22    1.5
% % 1.2     1.62
% % 1.18    1.75
% % 1.13    2
% % 1.1     2.1
% % 1.04    2.25
% % 1       2.33
% % 0.9     2.44
% % 0.82    2.5
% % 0.7     2.53
% %xq = 0:pi/16:pi;
% intpol = interp1(x,y,'spline');
% plot(x,y,x,intpol)
clc
clf
%x = [0 0.05 0.25 0.5 0.75 1 1.25 1.5 1.62 1.75 2 2.1 2.25 2.33 2.44 2.5 2.53];
%y = [1.59 1.5 1.4 1.34 1.3 1.27 1.24 1.22 1.2 1.18 1.13 1.1 1.04 1 0.9 0.82 0.7];

x = [0 0.25 0.5 0.75 1 1.25 1.5 1.75 2 2.25 2.5];
y = 4*[1.59 1.4 1.34 1.3 1.27 1.24 1.22 1.18 1.14 1.04 0.82];

xq = 0:0.001:2.53; % Define the query points where you want to interpolate

intpol = interp1(x, y, xq, 'spline'); % Interpolate y values corresponding to xq



p = polyfit(x,y,7);
x_values = linspace(min(x), max(x), 100); % Generating x values for plotting the polynomial
y_fit = polyval(p, x_values); % Evaluating the polynomial at x_values



pINV = polyfit(y,x,4);
y_values = linspace(max(y), min(y), 100); % Generating x values for plotting the polynomial
x_fit = polyval(pINV, y_values); % Evaluating the polynomial at x_values

%0.1788   -3.0871   19.1757  -51.4369   53.1496
%   -0.0831   -0.1877    4.2356
yss = -0.0831*y_values.^2-0.1877*y_values+4.2356;
yss1 = 0.1788*y_values.^4-3.0871*y_values.^3+19.1757*y_values.^2-51.4369*y_values+53.1496;
%yss2=pINV(1)*y_values.^7+pINV(2)*y_values.^6+pINV(3)*y_values.^5+pINV(4)*y_values.^4+pINV(5)*y_values.^3+pINV(6)*y_values.^2+pINV(7)*y_values.^1+pINV(1)
yss2=-0.4576*y_values.^5+11.2783*y_values.^4-109.5197*y_values.^3+523.2503*y_values.^2-1229.7*y_values.^1+1139.8

% y_range = linspace(6.36,3.6,100);
% pinv = polyfit(y,x,7);
% y_fit_inv = polyval(pinv, y_range);


x_lin = linspace(0,2.5,11);
y_lin = 4*linspace(1.59,0.9,11);

BatteryVoltage = y

BatteryPercentage = (BatteryVoltage-3.6)/.0276
BatteryPercentage2 = (y-3.6)/.0276

y_per = (y_fit-3.6)/0.0276

x_per = 100*(1-((6.36-y_lin)/2.5))
x_per2 = 100*(1-((6.36-y_values)/2.5))


x_perdata = 100*(((2.5-x)/2.5))

x_perdata2 = 100*(((2.5-x_values)/2.5))

x_perdata3 = 100*(((2.5-y_values)/2.5))

plot(x, y, 'o', x_lin, y_lin,'x',x_values, y_fit);
legend('Original Data','Lin','Polyfit');
grid on

figure (2);
plot(x,BatteryPercentage2,'o' ,x,BatteryPercentage,'x',x_values, y_per)
legend('Original Data','Linear');
%set (gca,'XDir','reverse'); 
grid on

figure (3);
plot(y, x_perdata, 'o',y_lin, x_per, 'x', y_fit, x_perdata2 )
set (gca,'XDir','reverse'); 
legend('Original Data','Linear');
grid on


figure (4);
plot(y, x, 'o',y_values,yss1)
legend('Original Data');
%set (gca,'XDir','reverse'); 
grid on

yee=100*(((2.5-yss1)/2.5))
yeee=100*(1-((6.36-y)/2.5))
y_per = (x_fit-3.6)/0.0276
x_per = 100*(1-((6.36-y_values)/2.5))

yss1 = 0.1788*y_values.^4-3.0871*y_values.^3+19.1757*y_values.^2-51.4369*y_values+53.1496;
yee=100*(((2.5-yss1)/2.5))
yeeasdasd=100*(((2.5-x)/2.5))
asdasd = 100*(((2.5-y_lin)/2.5))
figure (5);
plot(y_values,yee,y,yeeasdasd,'o',y,BatteryPercentage);
%set (gca,'XDir','reverse');
legend('Original Data','Polyfit','Lin');
grid on
