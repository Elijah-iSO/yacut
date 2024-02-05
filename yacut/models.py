from datetime import datetime

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(6), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            id=self.id,
            original=self.original,
            short=self.short,
            timestamp=self.timestamp,
        )

    def from_dict(self, data):
        dict = {'url': 'original', 'custom_id': 'short'}
        for field, value in dict.items():
            if field in data:
                setattr(self, value, data[field])