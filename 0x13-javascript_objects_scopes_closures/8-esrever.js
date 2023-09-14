#!/usr/bin/node

exports.esrever = function (list) {

  let result = [];
  while (list.length > 0) {
    result.push(list.pop());
  }
  return result;
};
