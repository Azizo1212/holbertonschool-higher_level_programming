#!/usr/bin/node

exports.esrever = function (list) {
  const aux = [];
  for (let i = list.length - 1; i > -1; i--) {
    aux.push(list.pop());
  }
  return aux;
};
