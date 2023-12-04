clear all
clc
clf
x = [0 0.0625 0.125 0.25 0.5 0.75 1 1.25 1.5 1.75 2 2.25 2.375 2.5];
y = 4*[1.59 1.5 1.43 1.4 1.34 1.3 1.27 1.24 1.22 1.18 1.14 1.04 0.94 0.82];

pINV = polyfit(y,x,3);
y_values = linspace(max(y), min(y), 100); % Generating x values for plotting the polynomial
x_fit = polyval(pINV, y_values); % Evaluating the polynomial at x_values

%YNEW = pINV(1)*y_values.^10+pINV(2)*y_values.^9+pINV(3)*y_values.^8+pINV(4)*y_values.^7+pINV(5)*y_values.^6+pINV(6)*y_values.^5+pINV(7)*y_values.^4+pINV(8)*y_values.^3+pINV(9)*y_values.^2+pINV(10)*y_values.^1+pINV(11); %10
%YNEW = pINV(1)*y_values.^7+pINV(2)*y_values.^6+pINV(3)*y_values.^5+pINV(4)*y_values.^4+pINV(5)*y_values.^3+pINV(6)*y_values.^2+pINV(7)*y_values.^1+pINV(8); %7
%YNEW = pINV(1)*y_values.^5+pINV(2)*y_values.^4+pINV(3)*y_values.^3+pINV(4)*y_values.^2+pINV(5)*y_values.^1+pINV(6); %5
%YNEW = pINV(1)*y_values.^4+pINV(2)*y_values.^3+pINV(3)*y_values.^2+pINV(4)*y_values+pINV(5); %4
%YNEW = pINV(1)*y_values.^3+pINV(2)*y_values.^2+pINV(3)*y_values+pINV(4); %3
YNEW = -0.6198*y_values.^3+2.183*y_values.^2-2.725*y_values+6.199; %3
%YNEW = pINV(1)*y_values.^2+pINV(2)*y_values+pINV(3); %3


%1/0.01+e^-1.4x

YPlot=100*(((2.5-YNEW)/2.5));
XPlot=100*(((2.5-x)/2.5));
BatteryPercentage = (y-3.28)/.0308; % Vmax-Vmin/100=0.0308

%Vmax=4*1.59=6.36 Vmin=0.9*4=3.6 0.0276=(Vmax-VMin)/100 	LINEAR.. :(
figure (1);
plot(y_values,YPlot,y,XPlot,'o',y,BatteryPercentage);
%set (gca,'XDir','reverse');
%legend('Original Data','Polyfit','Lin');
grid on

figure(2);
plot(y,XPlot,'o',y_values,YPlot,y,BatteryPercentage)


figure(3);
plot(x,y,'o')