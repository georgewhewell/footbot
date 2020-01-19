with (import <nixpkgs> { });
  
let
  ecos  = python3.pkgs.callPackage ./nix/ecos.nix  { };
  osqp  = python3.pkgs.callPackage ./nix/osqp.nix  { };
  scs   = python3.pkgs.callPackage ./nix/scs.nix   { };
  cvxpy = python3.pkgs.callPackage ./nix/cvxpy.nix { inherit ecos osqp scs; };
  interpreter = (python3.withPackages (ps: with ps; [
      setuptools
      numpy
      pandas
      tables
      requests
      flask
      unidecode
      cvxpy
  ]));
in pkgs.mkShell {
  buildInputs = [
    interpreter
  ];

}
