from __future__ import print_function
from builtins import str
from builtins import range
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import urllib.parse
from h2o.estimators.glm import H2OGeneralizedLinearEstimator

# DISCLAMINER
#
# The main function of API tests is to make sure that changes to the API are captured
# before the customers do.  This is to prevent breaking the customer code.  If the
# changes are necessary, we will have the chance to warn them about the changes.
#
# All API tests should be short and fast to run.  The main purposes of API tests are to
# make sure that the command in its most popular forms run correctly when user types in
# correct input arguments.  Light weight checking will be provided on the command output
# to make sure that we are getting the correct responses.
#
# For exhaustive tests using all possible combination of input arguments, making sure all
# responses of the API commands are correct, or if in error, the correct error messages
# are sent should be done elsewhere.

def h2oframes():
    """
    h2o.frames()

    Testing the h2o.api() command here.

    :return: none if test passes or error message otherwise
    """
    try:
        training_data = h2o.import_file(pyunit_utils.locate("smalldata/logreg/benign.csv"))
        Y = 3
        X = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10]

        model = H2OGeneralizedLinearEstimator(family="binomial", alpha=0, Lambda=1e-5)
        model.train(x=X, y=Y, training_frame=training_data)
        hf_col_summary = h2o.api("GET /3/Frames/%s/summary" % urllib.parse.quote(training_data.frame_id))["frames"][0]
        assert hf_col_summary["row_count"]==100, "row count is incorrect.  Fix h2o.api()."
        assert hf_col_summary["column_count"]==14, "column count is incorrect.  Fix h2o.api()."
        model_coefficients = \
            h2o.api("GET /3/GetGLMRegPath", data={"model": model._model_json["model_id"]["name"]})["coefficients"][0]
        assert len(model_coefficients)==11, "Number of coefficients is wrong.  h2o.api() command not working"
    except Exception as e:
        assert False, "h2o.api() command not working"


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oframes)
else:
    h2oframes()
