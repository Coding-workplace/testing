import locale
# Set to user default safely 
# Use this early and avoid further setlocale calls in multi-threaded apps.
locale.setlocale(locale.LC_ALL)


# Query current locale and conventions
print(locale.getlocale())                      # e.g. ('en_US', 'UTF-8')
print(locale.localeconv())                     # dict: decimal_point, thousands_sep, currency_symbol...

print(locale.format_string('%f', 12345.67))
print(locale.format_string('%.2f', 12345.67, grouping=True))

# currency
print(locale.currency(1234.56))       
print(locale.currency(1234.56, grouping=True))

# parsing numbers
locale.atof('12.345,67')   # -> 12345.67
locale.atoi('1.234.567')   # -> 1234567