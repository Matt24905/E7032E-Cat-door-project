% clear all
% clc
% clf
y = [0 0.0625 0.125 0.25 0.5 0.75 1 1.25 1.5 1.75 2 2.25 2.375 2.5];
x = 4 * [1.59 1.5 1.43 1.4 1.34 1.3 1.27 1.24 1.22 1.18 1.14 1.04 0.94 0.82];

% Fit an exponential curve
%f = fit(x',y','rat33');

%val =  GOOD VALUES!!

     % General model Rat33:
     % val(x) = (p1*x^3 + p2*x^2 + p3*x + p4) /
     %           (x^3 + q1*x^2 + q2*x + q3)
     % Coefficients (with 95% confidence bounds):
     %   p1 =       259.3  (-1.088e+05, 1.094e+05)
     %   p2 =       -4844  (-2.044e+06, 2.034e+06)
     %   p3 =   3.026e+04  (-1.272e+07, 1.278e+07)
     %   p4 =  -6.324e+04  (-2.671e+07, 2.659e+07)
     %   q1 =      -732.4  (-3.043e+05, 3.029e+05)
     %   q2 =        7336  (-3.065e+06, 3.08e+06)
     %   q3 =  -1.902e+04  (-8.014e+06, 7.976e+06)



Voltage = linspace(3.28,6.36,100);
Rat33 =f(Voltage);
Yresult = (f.p1*Voltage.^3 + f.p2*Voltage.^2 + f.p3.*Voltage + f.p4) ./ (Voltage.^3 + f.q1*Voltage.^2 + f.q2.*Voltage + f.q3); 

YLinear = linspace(0,2.5,100);
YPercent=100*(((2.5-Yresult)/2.5));
YPercentLINEAR=100*(((2.5-y)/2.5));
BatteryPercentage = (Voltage-3.28)/.0308; % Vmax-Vmin/100=0.0308


figure(1);
plot(x,YPercentLINEAR,'o',Voltage,BatteryPercentage,Voltage,YPercent)
set (gca,'XDir','reverse');
legend('Original Data','Linear','Rat33',Location='best');
grid on
xlabel('Voltage [V]')
ylabel('Battery Percentage [%]')
xlim([3.28 6.36])
ylim([0 100])





