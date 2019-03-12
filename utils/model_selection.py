def model_selection(default_model=None):
    phrase = 'select applied model' + (' [default=' + default_model + ']:' ) if default_model else ':'
    model = input(phrase)
    if model == "" and default_model:
        return default_model
    return model