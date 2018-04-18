def OnOfController(autonomy, actual_model, set_point, range):
    model = actual_model
    if autonomy < set_point - range:
        model = "pot-fields"
    elif autonomy >= set_point - range and autonomy <= set_point + range:
        model = "bio"
    elif autonomy > set_point + range:
        model = "rules"
    return model