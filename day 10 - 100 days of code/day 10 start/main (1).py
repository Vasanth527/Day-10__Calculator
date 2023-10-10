# Functions with inputs

def format_name(f_name , l_name):
  """this will take f_name and l_name as inputs and converts into title case words"""
  return f"{f_name.title()} {l_name.title()}"
  # formated_f_name = f_name.title()
  # formated_l_name = l_name.title()
  # return f"{formated_f_name} {formated_l_name}"

first_name = input("Entr your first name : ")
last_name = input("Entr your last name : ")
final_name = format_name(first_name,last_name)
print(final_name)