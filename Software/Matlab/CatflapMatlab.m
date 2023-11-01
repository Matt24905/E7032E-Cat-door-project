clc
file = (['cate' ...
    '.csv']);
catdata = readtable(file);
T = readtable(file,'NumHeaderLines',43);
x = T.Var1;
y = T.Var2;
figure;
plot(x,y);
set(gca, 'XDir','reverse')
%axis([catdata{12,2} catdata{13,2} catdata{19,2} catdata{20,2}])
axis([0.08 0.12 0 84])
xlabel('Time [S]')
ylabel('Voltage [V]')
