# This program defines an rc circuit and the charging of three capacitor and using three resistors
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint


def import_data(filename):
    file = open(filename)
    content = file.readlines()[1:]
    output = {'capacitor_values': [], 'resistor_values': []}
    for line in content:
        element = line.split(",")
        # print(element)
        output['capacitor_values'].append(float(element[0]))
        output['resistor_values'].append(float(element[1]))
    return output


def parameter_setup():
    peak_voltage = 120
    frequency = 60
    omega = 2. * np.pi * frequency
    ac_periods = 10 / frequency
    times = np.linspace(0, ac_periods, 1000)
    return peak_voltage, omega, times


# def source_voltage(peak_voltage , np.sin(omega*times)

def capacitor_voltage(solve_solution, times):
    return solve_solution * times


def resistor_voltage(source_voltage, capacitor_voltage):
    return source_voltage - capacitor_voltage


# def solve_solution(peak_voltage,omega,tau):
# y0 = capacitor_voltage(0) = 0
# y = odeint(solve_solution(),y0.times)
# return (-capacitor_voltage + peak_voltage * np.sin(omega*t))/tau


def plot_solution(times, source_voltage, resistor_voltage, peak_voltage, capacitor_voltage):
    # plt.plot(times, source_voltage)
    plt.plot(times, capacitor_voltage)
    plt.plot(times, resistor_voltage)
    plt.xlabel('time')
    plt.ylabel('voltage')
    plt.ylim(-1 * peak_voltage, 1 * peak_voltage)


if __name__ == '__main__':
    import_values = import_data('../matlab/capandrestable.csv')
    for resistance, capacitance in zip(import_values['resistor_values'], import_values['capacitor_values']):
     print(resistance,capacitance)
