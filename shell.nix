# shell.nix
##Este archivo es para automatizar mi entorno de desarrollo en nixOS
#--Diego--
# python.nix
with (import <nixpkgs> {});
let
  my-python-packages = python-packages: with python-packages; [
    pandas
    requests
    django
    cx_oracle
    pillow
    djangorestframework
    # other python packages you want
  ];
  python-with-my-packages = python3.withPackages my-python-packages;
in
mkShell {
  buildInputs = [
    python-with-my-packages
    pkgs.microsoft-edge
  ];
}

