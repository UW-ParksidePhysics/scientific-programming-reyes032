% Simulation parameters
resistance = 100*10^3;  % (in Ω) 
capacitance = 1*10^-9;  % (in F)
frequency = 60; % AC source frequency (in Hz)
peak_voltage = 110;  % AC source peak voltage (in V)

% Calculated parameters
tau = resistance * capacitance;  % RC time constant
omega = 2*pi*frequency; % AC source angular frequency (in rad/s)

% Solve differential equation for v_C
syms capacitor_voltage(t)  % v_C(t) for differential equation solver
% dv_C / dt = (-v_C + V0 sin(ωt)) / RC
eqn = diff(capacitor_voltage,t) == (-capacitor_voltage + peak_voltage * sin(omega*t))/tau
% Initial condition: v_C(0)
% cond = capacitor_voltage(0) == peak_voltage;  % capacitor charged to 110V
cond = capacitor_voltage(0) == sqrt(2)*peak_voltage/2;  % capaciator charged to rms V
% cond = capacitor_voltage(0) == 0;  % capacitor uncharged at start
% v_C(t) from differential equation solver
voltage_solution(t)= dsolve(eqn, cond)

% Plot solutions
simulation_stop_time = 10/frequency  % Stop after 10 source AC periods
% simulation_stop_time = 10*tau  % Stop after 10 RC constants
times = linspace(0,simulation_stop_time,1000)  % times to plot
source_voltages = peak_voltage .* sin(omega.*times)  % v_s(t)
capacitor_voltages = voltage_solution(times)  % v_C(t)
resistor_voltages = source_voltages - capacitor_voltages  %v_R(t)
hold on
plot(times, source_voltages)  % v_s(t) vs t
plot(times, capacitor_voltages)  % v_C(t) vs t
plot(times, resistor_voltages)  % v_R(t) vs t
ylim([-1.5*peak_voltage, 1.5*peak_voltage])  % set voltage plot range
