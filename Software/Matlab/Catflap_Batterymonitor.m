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
y_range = linspace(6.36,3.6,100);

x_lin = linspace(0,2.5,11);
y_lin = 4*linspace(1.59,0.9,11);

BatteryVoltage = y_lin

BatteryPercentage = (BatteryVoltage-3.6)/.0276
BatteryPercentage2 = (y-3.6)/.0276



y_per = (y_fit-3.6)/0.0276

x_per = 100*(1-((6.36-y_lin)/2.5))

x_perdata = 100*(((2.5-x)/2.5))

plot(x, y, 'o', x_lin, y_lin,'x',x_values, y_fit);
legend('Original Data','Lin','Polyfit');
grid on

figure (2);
plot(x,BatteryPercentage2,'o' ,x,BatteryPercentage,'x',x_values, y_per)
legend('Original Data','Linear');
grid on

figure (3);
plot(y_lin, x_per, 'o', y, x_perdata, 'x')
set (gca,'XDir','reverse'); 
legend('Original Data');
grid on

