from django.core.validators import RegexValidator

def is_valid_pincode():
    return RegexValidator(
        regex=r'^\+?1?\d{6}$', message='Please enter 6 digit pincode.'
    )
    
def is_valid_mobile_number():
    return RegexValidator(
        regex=r'^\+?1?\d{6}$', message='Please enter 6 digit pincode.'
    )