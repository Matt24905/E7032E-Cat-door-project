clc
catdata = ('Fdxb.csv');
%catdata = ('em410.csv');
T = readtable(catdata,'NumHeaderLines',43);
x = T.Var1;
y = T.Var2;

y_env = envelope(y,30,'peak');

plot(x,y);
figure;
plot(x,y,x,y_env);


%axis([catdata{12,2} catdata{13,2} catdata{19,2} catdata{20,2}])
axis([0.00 0.005 6 11.5])
xlabel('Time [ms]')
ylabel('Voltage [V]')

activation_field_cyclesFDX = 32;
activation_field_cyclesEM = 64;

fc1 = 125e3;
fc2 = 134.2e3;
bit_time =  activation_field_cyclesFDX/fc1;
grid on

% Set the x-axis grid lines
xticks(0.00008:bit_time:0.1);

% Set the y-axis grid lines at intervals of 0.5
%yticks(-1:0.5:1);

figure;
%plot(x,y);
plot(x,y_env);


itterations = 100;
bit = zeros(1,itterations);
for i = 1:itterations
    start = 44100;
    length= 2048;
    NewChunkY = y_env((start+length*(i-1)):start+length*i);
    avgYLEFT =mean(NewChunkY(1:(length)/2));
    avgYRIGHT =mean(NewChunkY(length/2:length));
    if abs(avgYLEFT - avgYRIGHT) < 3
        bit(i) = 1;
    else
        bit(i) = 0;
    end
end
    newX=x(start:start+length);
    plot(newX,NewChunkY)