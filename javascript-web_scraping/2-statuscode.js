#!/usr/bin/node

const axios = require('axios').default;
axios.get(process.argv[2])
  .then(response => {
    console.log('code:', response.status);
  })
  .catch(res => {
    console.log('code:', res.response.status);
  });

