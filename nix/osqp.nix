{ stdenv
, lib
, buildPythonPackage
, fetchPypi
, python
, cmake
, numpy
, scipy
, future
}:

buildPythonPackage rec {
  pname = "osqp";
  version = "0.6.1";

  src = fetchPypi {
    inherit pname version;
    sha256 = "130frig5bznfacqp9jwbshmbqd2xw3ixdspsbkrwsvkdaab7kca7";
  };

  dontUseCmakeConfigure = true;
  nativeBuildInputs = [
    cmake
  ];

  propagatedBuildInputs = [
    numpy
    scipy
    future
  ];

  doCheck = false;
}
