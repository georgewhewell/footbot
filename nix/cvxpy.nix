{ stdenv
, lib
, buildPythonPackage
, fetchPypi
, python
, cvxopt
, numpy
, scipy
, ecos
, osqp
, scs
}:

buildPythonPackage rec {
  pname = "cvxpy";
  version = "1.1.0a2";

  src = fetchPypi {
    inherit pname version;
    sha256 = "1c170y0gif3hraja0bbzp7v1yhg5xgmk73sn3dh47073cyr872fl";
  };

  propagatedBuildInputs = [
    cvxopt
    numpy
    scipy
    ecos
    osqp
    scs
  ];

  doCheck = false;
}
