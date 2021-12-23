from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(constructor=None)


class BaseModel(Base):
    __abstract__ = True
    """Base class for all the Python data models"""

    def __init__(self, **kwargs):
        """
        Custom initializer that allows nested children initialization.
        Only keys that are present as instance's class attributes are allowed.
        These could be, for example, any mapped columns or relationships.

        Code inspired from GitHub.
        Ref: https://github.com/tiangolo/fastapi/issues/2194
        """

        cls = self.__class__
        model_columns = self.__mapper__.columns
        relationships = self.__mapper__.relationships

        for key, val in kwargs.items():

            if not hasattr(cls, key):
                raise TypeError(f"Invalid keyword argument: {key}")

            if key in model_columns:
                setattr(self, key, val)
                continue

            if key in relationships:
                relation_cls = relationships[key].mapper.entity

                if isinstance(val, list):
                    instances = [relation_cls(**elem) for elem in val]
                    setattr(self, key, instances)

                elif isinstance(val, dict):
                    instance = relation_cls(**val)
                    setattr(self, key, instance)
