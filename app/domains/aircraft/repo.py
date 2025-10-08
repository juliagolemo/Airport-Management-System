from typing import Dict, List, Optional

# simple in-memory "tables" container: table name -> list of rows
IN_MEMORY_DB: Dict[str, List[Dict]] = {"aircraft": []}


class AircraftRepo:
	def __init__(self, db: Dict[str, List[Dict]] = IN_MEMORY_DB):
		self.db = db

	def list(self) -> List[Dict]:
		return list(self.db.setdefault("aircraft", []))

	def get(self, aircraft_id: int) -> Optional[Dict]:
		for a in self.db.get("aircraft", []):
			if a["id"] == aircraft_id:
				return a
		return None

	def create(self, obj: Dict) -> Dict:
		rows = self.db.setdefault("aircraft", [])
		next_id = (max((r["id"] for r in rows), default=0) + 1) if rows else 1
		record = {"id": next_id, **obj}
		rows.append(record)
		return record

	def update(self, aircraft_id: int, changes: Dict) -> Optional[Dict]:
		for i, a in enumerate(self.db.get("aircraft", [])):
			if a["id"] == aircraft_id:
				updated = {**a, **{k: v for k, v in changes.items() if v is not None}}
				self.db["aircraft"][i] = updated
				return updated
		return None

	def delete(self, aircraft_id: int) -> bool:
		rows = self.db.get("aircraft", [])
		for i, a in enumerate(rows):
			if a["id"] == aircraft_id:
				rows.pop(i)
				return True
		return False

