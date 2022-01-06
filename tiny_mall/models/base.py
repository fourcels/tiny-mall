

from sqlalchemy.ext.declarative import declarative_base


def _declarative_constructor(self, **kwargs):
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
                instances = [elem if isinstance(
                    elem, relation_cls) else relation_cls(**elem) for elem in val]
                setattr(self, key, instances)

            elif isinstance(val, dict):
                instance = relation_cls(**val)
                setattr(self, key, instance)
            else:
                setattr(self, key, val)


Base = declarative_base(constructor=_declarative_constructor)
