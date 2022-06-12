from models import Videos
from start_database import Session
import random


class Function:
    def __init__(self):
        Videos.metadata.create_all()
        self.session = Session()
        self.session.begin()

    def insert_id(self, video_id: str, username: str, search_title: str) -> None:
        metadata = Videos(video_id=video_id, username=username, search_title=search_title)
        self.session.add(metadata)
        self.session.commit()

    def retrieve_link(self) -> str:
        lst = self.session.query(Videos).all()
        random_id = random.randint(1, len(lst))
        print(random_id)
        return self.session.query(Videos.video_id).filter(Videos.id == random_id).first()[0]
