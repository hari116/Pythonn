import os

abs_path = os.path.dirname(os.path.abspath(__file__))


def abs_path(file_name):
    return (abs_path + '/' + file_name)


if __name__ == '__main__':
    print(abs_path('helper.py'))
