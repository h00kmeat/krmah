try:
    def decorator(boost):
        def wrapper():
            boost_a = boost()
            distance = v0 * t - (boost_a * t ** 2) / 2
            print('Ускорение - ', boost_a, ' расстояние - ', distance)

        return wrapper()


    @decorator
    def boost():
        global v0, t
        v0, v, t = map(float, input().split())
        a = (v - v0) / t
        return a
except ZeroDivisionError:
    print('нельзя делить на ноль')
