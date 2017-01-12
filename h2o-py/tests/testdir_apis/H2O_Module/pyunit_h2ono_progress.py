from __future__ import print_function
from builtins import str
from builtins import range
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import urllib.parse
from h2o.estimators.glm import H2OGeneralizedLinearEstimator


def h2ono_progress():
    """
    h2o.no_progress()

    Testing the h2o.no_progress() command here.  Not sure if the clients should be using this command ....
    Command is verified by eyeballing the pyunit test output file and make sure the no progress bars are there.
    Here, we will assume the command runs well if there is no error message.

    :return: none if test passes or error message otherwise
    """
    try:
        h2o.no_progress()
        training_data = h2o.import_file(pyunit_utils.locate("smalldata/logreg/benign.csv"))
        Y = 3
        X = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10]
        model = H2OGeneralizedLinearEstimator(family="binomial", alpha=0, Lambda=1e-5)
        model.train(x=X, y=Y, training_frame=training_data)
    except Exception as e:
        assert False, "h2o.no_progress() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2ono_progress)
else:
    h2ono_progress()
