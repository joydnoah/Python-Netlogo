def OnOfController(time, actual_model):
    model = actual_model
    if time > 100:
        model = "pot-fields"
    return model