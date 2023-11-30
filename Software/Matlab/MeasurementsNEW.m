clc
file = (['em410.csv']);
catdata = readtable(file);
T = readtable(file,'NumHeaderLines',43);
x = T.Var1;
y = T.Var2;
%[up,lo] = envelope(y);
y_env = envelope(y,30,'peak');
%y_env = up;
%figure;
plot(x,y);
figure;
plot(x,y,x,y_env);

%set(gca, 'XDir','reverse')
%axis([catdata{12,2} catdata{13,2} catdata{19,2} catdata{20,2}])
axis([0.00 0.005 6 11.5])
xlabel('Time [ms]')
ylabel('Voltage [V]')

activation_field_cyclesFDX = 32;
activation_field_cyclesEM = 64;

fc1 = 125e3;
fc2 = 134.2e3;
bit_time =  activation_field_cyclesEM/fc1;
grid on

% Set the x-axis grid lines at intervals of pi/2
xticks(0.00001:bit_time:0.1);

% Set the y-axis grid lines at intervals of 0.5
%yticks(-1:0.5:1);

figure;
%plot(x,y);
plot(x,y_env);
