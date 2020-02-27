type Query {
    students(id: ID!): Student
    classes(id: ID!): Class
}

type Student {
    id: ID!
    name: String!
}

type Class{
    id: ID!
    name: String!
    students: [Student]
}

type Mutation {
    create_student(input: StudentInput): Student
    create_class(input: ClassInput): Class
    update_class(input: UpdateClassInput!): Class
}

input StudentInput{
    name: String!
}

input ClassInput{
    name: String!
}

input UpdateClassInput{
    id: ID!
    studentid: ID!
}
