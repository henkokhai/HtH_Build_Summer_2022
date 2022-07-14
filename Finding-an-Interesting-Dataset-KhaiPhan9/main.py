import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

student_data = pandas.read_csv("{Student_Mental_Health.csv}")

print(student_data)