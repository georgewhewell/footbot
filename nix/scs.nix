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
  pname = "scs";
  version = "2.1.0";

  src = fetchPypi {
    inherit pname version;
    sha256 = "1m45366lfkv71mhdmr10ch7wgn16n79rg75jxqizqcgg6r5s6rqx";
  };

  propagatedBuildInputs = [
    numpy
    scipy
    future
  ];

  doCheck = false;
}
