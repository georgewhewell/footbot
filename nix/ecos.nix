{ stdenv
, lib
, buildPythonPackage
, fetchPypi
, python
, numpy
, scipy
, nose
}:

buildPythonPackage rec {
  pname = "ecos";
  version = "2.0.7.post1";

  src = fetchPypi {
    inherit pname version;
    sha256 = "0n67plhclbsxqi23is8rj62vv3d75nnwzhsmya9jlbpknd10zsc3";
  };

  propagatedBuildInputs = [
    numpy
    scipy
  ];

  checkInputs = [
    nose
  ];
}
