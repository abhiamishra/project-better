const express = require('express'); //installing the library
const graphqlHTTP = require('express-graphql');
const schema = require('./schema/schema');
const app = express();

app.use("/graphql", graphqlHTTP({
    schema
}));

app.listen(4000, () => {
    console.log("now listening for requests on Port 4000")
});