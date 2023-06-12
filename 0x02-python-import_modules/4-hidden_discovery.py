#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    def_nms = dir(hidden_4)

    for k in range(len(def_nms)):
        if def_nms[k][:2] != '__':
            print(def_nms[k])
