from flask import Markup, url_for, session
from flask_appbuilder.security.sqla.models import User
from flask_appbuilder.models.decorators import renders
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref, query
from flask_appbuilder import Model

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
class Trida(Model):
    name = Column(String(50), primary_key=True)

    def __repr__(self):
        return self.name

class TimeGroup(Model):
    __tablename__ = "timegroup"
    id = Column(Integer, primary_key=True)
    timegroup = Column(String(150), unique=True, nullable=False)

    def __repr__(self):
        return self.timegroup

class ConectUser(Model):
    __tablename__ = "conectuser"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    time_group = Column(Integer, ForeignKey("timegroup.timegroup"), nullable=False)

    def __repr__(self):
        return self.name
    

    def __repr__(self):
        return self.name
