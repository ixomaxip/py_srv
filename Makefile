include .env
include ci/main.make
-include .env.local

main: down rt up log | ccze -A