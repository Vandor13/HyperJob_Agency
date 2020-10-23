def get_cleaned_data(raw_data):
    promocode_form = PromoCodeForm(raw_data)
    if promocode_form.is_valid():
        return promocode_form.cleaned_data
    else:
        return {}
