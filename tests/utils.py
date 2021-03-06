from yaat.models import Column


def generate_columns(user=None):
    retval = [
        Column(resource='test_resource', key='first', value='First', is_shown=True, ordering=Column.ASC),
        Column(resource='test_resource', key='second', value='Second', is_shown=True, ordering=Column.ASC),
        Column(resource='test_resource', key='third', value='Third', is_shown=True, ordering=Column.ASC)
    ]

    if user:
        for i in range(0, len(retval)):
            retval[i].user = user

    return retval
