
from sqlalchemy import String, Integer, Column
from sqlalchemy import select, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class PopCharts(Base):
    __tablename__ = "PopCharts"
    id = Column(Integer, primary_key=True)
    youtube_link = Column(String())
    name = Column(String())
    artist = Column(String())
    time_on_chart = Column(Integer)
    change = Column(Integer)
    total_views = Column(Integer)
    num_likes = Column(Integer)
    duration = Column(Integer)
    views_this_week = Column(Integer)


class PopChartsExploration:
    def __init__(self, filename):
        self.engine = create_engine(f'sqlite:///{filename}', echo=False)
        Session = sessionmaker(self.engine)
        self.session = Session()
    
    def save(self):
        self.session.commit()
            
    def get_longest_song(self):
        result = (
            self.session.query(PopCharts)
            .order_by(PopCharts.duration.desc())
            .first())
            
        print(f'Found: {result.artist} - {result.name} {result.duration}')
        

if __name__ == '__main__':
    popChartsExploration = PopChartsExploration('pop_charts_exploration.db')
    popChartsExploration.get_longest_song()
    