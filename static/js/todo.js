var app = angular.module('toDo', []);

app.controller('toDoController', function($scope, $http){
    $scope.todoList = []
    
    $scope.todoAdd = function(){            
        $http.post('http://localhost:8000/todoapp/add/', { 'todo_text': $scope.todoInput, 'done': false })
        .then(function(response) {
            console.log(response.data);
            $scope.todoList.push({ 'todo_text':$scope.todoInput, 'done': false }); 
            $scope.todoInput = '';
        });
    }

    $scope.todo_list = function(){
        $http.get('http://localhost:8000/todoapp/list/').then(function(response){
            console.log(response.data);
            $scope.todoList = response.data;
        });
    }

    $scope.remove = function(id, idx){
        
        $http.delete('http://localhost:8000/todoapp/delete/'+id+'/')
        .then(function(response){            
            $scope.todoList.splice(idx, 1);
        });
            
    }

});