def flat_generator(some_list):
    for item in some_list:
        if isinstance(item, list):
            for i in item:
                yield i