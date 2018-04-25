import numpy as np
import skfuzzy as fuzz
import operator

def OnOffController(autonomy, actual_model, set_point, range):
    model = actual_model
    if autonomy < set_point - range:
        model = "pot-fields"
    elif autonomy >= set_point - range and autonomy <= set_point + range:
        model = "bio"
    elif autonomy > set_point + range:
        model = "rules"
    return model

def FuzzyController(autonomy, MSD, time):
    # Generate universe variables
    #   * Quality and service on subjective ranges [0, 10]
    #   * Tip has a range of [0, 25] in units of percentage points
    x_MSD = np.arange(0, 400, 1)
    x_autonomy = np.arange(0, 400, 1)
    x_time = np.arange(0, 1000, 1)
    x_method = np.arange(0, 1, 0.01)

    # Generate fuzzy membership functions
    MSD_lo = fuzz.zmf(x_MSD, 0, 200)
    MSD_md = fuzz.pimf(x_MSD, 100, 150, 250, 300)
    MSD_hi = fuzz.smf(x_MSD, 200, 400)
    autonomy_lo = fuzz.zmf(x_autonomy, 0, 200)
    autonomy_md = fuzz.pimf(x_autonomy, 100, 150, 250, 300)
    autonomy_hi = fuzz.smf(x_autonomy, 200, 400)
    time_lo = fuzz.zmf(x_time, 0, 500)
    time_md = fuzz.pimf(x_time, 250, 400, 600, 750)
    time_hi = fuzz.smf(x_time, 500, 1000)
    method_lo = fuzz.zmf(x_method, 0, 0.5)
    method_md = fuzz.pimf(x_method, 0.25, 0.4, 0.6, 0.75)
    method_hi = fuzz.smf(x_method, 0.5, 1)

    # We need the activation of our fuzzy membership functions at these values.
    # The exact values 6.5 and 9.8 do not exist on our universes...
    # This is what fuzz.interp_membership exists for!
    autonomy = 100
    MSD = 50
    time = 800

    MSD_level_lo = fuzz.interp_membership(x_MSD, MSD_lo, MSD)
    MSD_level_md = fuzz.interp_membership(x_MSD, MSD_md, MSD)
    MSD_level_hi = fuzz.interp_membership(x_MSD, MSD_hi, MSD)

    autonomy_level_lo = fuzz.interp_membership(x_autonomy, autonomy_lo, autonomy)
    autonomy_level_md = fuzz.interp_membership(x_autonomy, autonomy_md, autonomy)
    autonomy_level_hi = fuzz.interp_membership(x_autonomy, autonomy_hi, autonomy)

    time_level_lo = fuzz.interp_membership(x_time, time_lo, time)
    time_level_md = fuzz.interp_membership(x_time, time_md, time)
    time_level_hi = fuzz.interp_membership(x_time, time_hi, time)

    # Rules
    active_rule11 = np.fmin(MSD_level_lo, autonomy_level_lo)
    active_rule12 = np.fmax(np.fmin(time_level_lo, autonomy_level_lo), active_rule11)
    method_activation_lo = np.fmin(active_rule12, method_lo)

    active_rule21 = np.fmin(MSD_level_md, autonomy_level_md)
    active_rule22 = np.fmax(np.fmin(time_level_md, autonomy_level_md), active_rule21)
    method_activation_md = np.fmin(active_rule22, method_md)

    active_rule31 = np.fmin(MSD_level_hi, autonomy_level_hi)
    active_rule32 = np.fmax(np.fmin(time_level_hi, autonomy_level_hi), active_rule31)
    method_activation_hi = np.fmin(active_rule32, method_hi)

    method0 = np.zeros_like(x_method)

    # Aggregate all three output membership functions together
    aggregated = np.fmax(method_activation_lo,
                         np.fmax(method_activation_md, method_activation_hi))

    # Calculate defuzzified result
    method = fuzz.defuzz(x_method, aggregated, 'centroid')
    method_activation = fuzz.interp_membership(x_method, aggregated, method)  # for plot

    method1 = np.arange(method, method + 1, 1)
    method_lo1 = fuzz.zmf(method1, 0, 0.5)
    method_md1 = fuzz.pimf(method1, 0.25, 0.4, 0.6, 0.75)
    method_hi1 = fuzz.smf(method1, 0.5, 1)

    stats = {"pot-fields": method_lo1[0], "bio": method_md1[0], "rules": method_hi1[0]}
    method = max(stats.items(), key=operator.itemgetter(1))[0]
    return method