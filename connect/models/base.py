from marshmallow import Schema, fields, post_load


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id')
        if kwargs:
            for attr, val in kwargs.items():
                setattr(self, attr, val)


class BaseSchema(Schema):
    id = fields.Str()

    @post_load
    def make_object(self, data):
        return BaseModel(**data)
