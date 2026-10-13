CXX ?= g++
CXXFLAGS ?= -std=c++14 -O2 -Wall -Wextra -pedantic -pthread
all: stability_monitor
stability_monitor: stability_monitor.cpp
	$(CXX) $(CXXFLAGS) $< -o $@
clean:
	rm -f stability_monitor
.PHONY: all clean
