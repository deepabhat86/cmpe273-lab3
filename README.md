# cmpe273-lab3

## Pre-requisites

* Install _Pipenv_

```
pip install pipenv
```

* Install _[Flask](https://palletsprojects.com/p/flask/)_

```
pipenv install flask==1.1.1
```
* Install _[Ariadne](https://ariadnegraphql.org/docs/flask-integration.html)_ for handling GraphQL schema and binding.

```
pipenv install ariadne==0.10.0
```

* Run your Flask application from a shell/terminal.

```sh
pipenv shell
$ env FLASK_APP=app.py flask run
```


* Open [this URL](http://127.0.0.1:5000/graphql) in a web browser or run this CLI to see the output.


## Queries:

Get class
```
{
classes(id:1){
    name
    students{
      id
      name
    }
  }
}
```

Get student
```
{
  students(id:4528){
    id
name
  }
}
```

Mutate Student
```
mutation{
  create_student(input:{
    name: "Girish"
  }){
    id
    name
  }
}
```

Mutate Class
```
mutation{
  create_class(input:{
    name: "CMPE-273"
  }){
    id
    name
  }
}
```

Mutate Class( Add student)
```
mutation{
  update_class(input:{
    id: "1"
studentid: "1"
  }){
    id
    name
  }
}
```
