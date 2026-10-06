from pathlib import Path
from database.db import Database
from gui.app import InventoryApp
BASE=Path(__file__).resolve().parent
if __name__=="__main__":
    db=Database(BASE/"inventory.db");db.initialize();InventoryApp(db,BASE).mainloop()
