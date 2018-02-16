def var_args(name, **kwargs):
    print(name)
    print(kwargs)


var_args('Mark', description='Loves Python', feedback=None, subscriber=True)
