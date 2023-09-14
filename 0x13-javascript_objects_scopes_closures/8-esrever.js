#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {

  let result = [];
  while (list.length > 0) {
    result.push(list.pop());
  }
  return result;
};
