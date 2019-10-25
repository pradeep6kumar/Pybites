<<<<<<< HEAD
from pcc_stats import diehard_pybites, Stats


def test_diehard_pybites():
    res = diehard_pybites()
=======
from pcc_stats import diehard_pybites, Stats


def test_diehard_pybites():
    res = diehard_pybites()
>>>>>>> 444b9e3e3c354fb4194c9052127c30f4ae496852
    assert res == Stats(user='clamytoe', challenge=('01', 7))