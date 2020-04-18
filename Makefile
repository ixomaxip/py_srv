include .env
include ci/main.make

main: down rt up log | ccze -A