# Instructions
# In this exercise, we'll develop a simple control system for a nuclear reactor.

# For a reactor to produce the power it must be in a state of criticality. 
# If the reactor is in a state less than criticality, it can become damaged. 
# If the reactor state goes beyond criticality, it can overload and result in a meltdown. 
# We want to mitigate the chances of meltdown and correctly manage reactor state.

"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    if temperature < 800 and neutrons_emitted > 500:
        return (temperature * neutrons_emitted) < 500000
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:
    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
        
    percentage_value = ((voltage * current) / theoretical_max_power) * 100
    if percentage_value >= 80:
        return "green"
    elif percentage_value >= 60:
        return "orange"
    elif percentage_value >= 30:
        return "red"
    elif percentage_value < 30:
        return "black"
    
        
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    if temperature * neutrons_produced_per_second < (threshold * .90):
        return 'LOW'
    elif threshold * .90 <= temperature * neutrons_produced_per_second <= threshold * 1.10:
        return 'NORMAL'
    else:
        return 'DANGER'
