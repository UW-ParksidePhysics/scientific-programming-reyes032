%simulation of a rc circuit with three different values of capacitors
% three different values of resistors
% three different values of capacitors



data = readcell('capandrestable.csv');

res_values = data(2,2:end);
cap_values = data(1,2:end);

number_of_resistors = length(res_values);
number_of_capacitors = length(cap_values);


%formulas across resistor
%resistance = resisance_in_ohms;
%current_across_resistor = peak_voltage/resistance;

%Charging of a capacitor
%
peak_voltage = 120;
frequency = 60;
omega = 2.*pi* frequency;                                                                 
ac_periods = 10/frequency;
times = linspace(0,ac_periods,1000);
source_voltage = peak_voltage .* sin(omega.*times);

for c = 1:number_of_capacitors
  for r = 1:number_of_resistors
    cap = cap_values{c};
    res = res_values{r};
    tau = res*cap;
    solution = solve_solution(peak_voltage,omega,tau);
   
    
    capacitor_voltage = solution(times);
    resistor_voltage = source_voltage - capacitor_voltage;


    hold on
    
    plot(times, capacitor_voltage)
    plot(times, resistor_voltage)
    ylim([-1*peak_voltage,1*peak_voltage])
  end    
end
plot(times, source_voltage)
hold off



%function peak_voltage = calculate_resistor_voltage(current, res_values)
    %peak_voltage = current * res_values;
%end

function solution = solve_solution(peak_voltage,omega,tau)
    syms capacitor_voltage(t);
    eqn = diff(capacitor_voltage,t) == (-capacitor_voltage + peak_voltage * sin(omega*t))/tau;
    cond = capacitor_voltage(0)  ==  0;
    solution(t) = dsolve(eqn,cond);
end    


