from SQLManager import SQLManager
sql=SQLManager("kahoot.db")
sql.create_tables()

sql.add_quizz("УКРАЇНА","КВІЗ ПРО УКРАЇНУ")