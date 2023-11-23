const graphql = require('graphql');
// define schema and describes the object types and relations between those
const _ = require('lodash');

const { GraphQLObjectType, GraphQLString, GraphQLSchema } = graphql;
//takes that function from package so that we can use it

var books = [
    {name: "Abhi", genre:"AKDJMA" id:'1'},
    {name: "Alzia", genre:"AMA" id:'2'},
    {name: "Aritiaza", genre:"AA" id:'3'},

];
//defines our new entity
const BookType = new GraphQLObjectType({
    name: 'Book',
    //fields of the entity
    fields: () => ({
        id: { type: GraphQLString }, //name of field: type of field
        name: { type: GraphQLString},
        genre: { type: GraphQLString}
    })
});

//Define root queries that are the basic queries
const RootQuery = new GraphQLObjectType({
    name: 'RootQueryType',
    fields: {
        book: {
            type: BookType,
            args: { id: {type: GraphQLString}}, //argument for what we are expecting
            resolve(parent, args){
                //code to get data from database/otherwise
                
            }
        }
    }
});

module.exports = new GraphQLSchema({
    query: RootQuery
});