# shell.nix
##Este archivo es para automatizar mi entorno de desarrollo en nixOS
#--Diego--
{ pkgs ? import <nixpkgs> {} }:
let
  python-with-my-packages = pkgs.python3.withPackages (p: with p; [
    pandas
    requests
    django
    cx_oracle
    pillow
    # other python packages you want
  ]);
in
python-with-my-packages.env # replacement for pkgs.mkShell
