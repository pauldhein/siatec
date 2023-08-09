import pytest


@pytest.fixture
def elbow_dataset():
    return [(1, 1), (2, 2), (3, 2), (4, 1), (5, 2), (6, 2)]


@pytest.fixture
def v_dataset():
    return [(1, 1), (2, 2), (3, 1), (4, 3), (5, 2), (6, 3)]


@pytest.fixture
def inv_elbow_dataset():
    return [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 4),
        (6, 4),
        (7, 3),
        (8, 2),
        (9, 1),
        (10, 1),
    ]


@pytest.fixture
def retro_inv_dataset():
    return [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 3),
        (5, 3),
        (6, 1),
        (7, 1),
        (8, 1),
        (9, 2),
        (10, 3),
    ]


@pytest.fixture
def mid_inv_elbow_dataset():
    return [
        (1, 5),
        (2, 6),
        (3, 5),
        (4, 1),
        (5, 2),
        (6, 3),
        (7, 4),
        (8, 4),
        (9, 8),
        (10, 7),
        (11, 6),
        (12, 5),
        (13, 5),
        (14, 5),
        (15, 6),
        (16, 5),
    ]


@pytest.fixture
def regular_dataset():
    return [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 4),
        (6, 1),
        (7, 2),
        (8, 3),
        (9, 4),
        (10, 4),
    ]


@pytest.fixture
def retro_dataset():
    return [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 4),
        (6, 4),
        (7, 4),
        (8, 3),
        (9, 2),
        (10, 1),
    ]


@pytest.fixture
def repeated_retro_dataset():
    return [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 4),
        (6, 4),
        (7, 4),
        (8, 3),
        (9, 2),
        (10, 1),
        (11, 1),
        (12, 2),
        (13, 3),
        (14, 4),
        (15, 4),
        (16, 4),
        (17, 4),
        (18, 3),
        (19, 2),
        (20, 1),
    ]


@pytest.fixture
def odd_retro_dataset():
    return [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 4),
        (6, 4),
        (7, 4),
        (8, 4),
        (9, 3),
        (10, 2),
        (11, 1),
    ]


@pytest.fixture
def separated_retro_dataset():
    return [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 4),
        (6, 6),
        (7, 5),
        (8, 2),
        (9, 4),
        (10, 4),
        (11, 3),
        (12, 2),
        (13, 1),
    ]


@pytest.fixture
def middle_retro_dataset():
    return [
        (1, 3),
        (2, 2),
        (3, 3),
        (4, 1),
        (5, 2),
        (6, 3),
        (7, 4),
        (8, 4),
        (9, 4),
        (10, 4),
        (11, 3),
        (12, 2),
        (13, 1),
        (14, 2),
        (15, 3),
        (16, 2),
    ]


@pytest.fixture
def shifted_retro_dataset():
    return [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 4),
        (7, 6),
        (8, 6),
        (9, 5),
        (10, 4),
        (11, 3),
    ]


@pytest.fixture
def big_shifted_retro_dataset():
    return [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 4),
        (7, 6),
        (8, 6),
        (9, 5),
        (10, 4),
        (11, 3),
        (12, 5),
        (13, 5),
        (14, 4),
        (15, 3),
        (16, 2),
        (17, 0),
        (18, 1),
        (19, 2),
        (20, 3),
        (21, 3),
    ]


@pytest.fixture
def geometric_data():
    return [(1, 1), (2, 1), (2, 2), (3, 2), (1, 3), (2, 3)]
