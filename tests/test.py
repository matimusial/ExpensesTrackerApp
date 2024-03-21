from app.database.database import Database
from app.services.encryption import Encryption
from app.services.validation import FormValidation
from app.auth.login import Login
from app.auth.register import Register

import string

from PyQt5.QtCore import QDate, QDateTime, Qt

# Pobierz aktualną datę
aktualna_data = QDate.currentDate()
print(type(aktualna_data))
print("Aktualna data:", aktualna_data.toString("dd-MM-yyyy"))
