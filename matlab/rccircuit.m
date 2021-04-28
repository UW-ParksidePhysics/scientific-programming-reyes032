






%input values
voltage = 120;

capacitance_in_mufarads =132.6e-6;

resistance_in_ohms = 4;

frequency_in_hz = 60;

%ohms law fromula
%voltage = current * resistance_in_ohms;
resistance_in_ohms = voltage/current;
current = voltage/resistance_in_ohms;
power = voltage*current;
% rms 
v_rms = voltage / sqrt(2);

%Circuit totals
total_impedence = (resistor_in_ohms*capacitive_reactance)/sqrt(resistance_in_ohms^2 + capacitive_reactance^2);
total_current = sqrt(current_across_resistor^2 + current_across_capacitor);
%formulas capacitor
capacitive_reactance = 1/ (2*pi*frequency_in_hz*capacitance_in_mufarads);
current_across_capacitor = voltage/capacitive_reactance;
voltage_across_capacitor = voltage;

%formulas across resistor
resistance = resisance_in_ohms;
current_across_resistor = voltage/resistance;

%Charging of a capacitor
%
voltage = 120;
frequency_in_hz = 60;
capacitance_in_mufarads =132.6e-6;
resistance_in_ohms = 4;
T = 2 * pi /omega;
t = 

tau = resistance_in_ohms * capacitance_in_mufarads;
omega = 2.* pi.* frequency_in_hz;
y = voltage/tau.*(sin(omega.*t));
plot(t, y, 'b-')
title('capacitor charging anlaysis')
xlabel('time (s)')
ylabel('Voltage across capacitor (v)')


function voltage = calculate_resistor_voltage(current, resistance)
    voltage = current * resistance;
end    
