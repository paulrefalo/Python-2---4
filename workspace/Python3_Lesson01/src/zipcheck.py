'''
zipcheck.py: validation function for US zip codes
'''

def zip_errors(z):
    """
    Validate z as either NNNNN or NNNNN-NNNN.
    """
    if len(z) not in (5, 10):
        return "Zip codes should be 5 or 10 chars long"
    if (not z[:5].isdigit() or 
        len(z) == 10 and not z[6:].isdigit()):
        return "Zip code contains non-numeric chars"
    if len(z) == 10 and z[5] != "-":
        return "Ten-digit zips must have a dash between the parts"
    return

