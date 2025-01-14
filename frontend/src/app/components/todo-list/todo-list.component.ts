import { Component, OnInit } from '@angular/core';
import { TodoService } from '../../services/todo.service';
import { NgFor } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-todo-list',
  standalone: true,
  imports: [NgFor, FormsModule],
  templateUrl: './todo-list.component.html',
  styleUrl: './todo-list.component.scss'
})
export class TodoListComponent implements OnInit {
  todos: any[] = [];
  newTask: string = '';

  constructor(private todoService: TodoService) {}

  ngOnInit(): void {
    this.loadTodos();
  }

  loadTodos(): void {
    this.todoService.getTodos().subscribe({
      next: (data) => {
        this.todos = data;
      },
      error: (err) => {
        console.error('Fail to load TODOs:', err);
      }
    });
  }

  addTodo(): void {
    if (!this.newTask.trim()) return

    const newTodo = { task: this.newTask, completed: false};
    this.todoService.addTodo(newTodo).subscribe({
      next: (addedTodo) => {
        this.todos.push(addedTodo);
        this.newTask = ''; // フォームリセット
      },
      error: (err) => {
        console.error('Failed to add TODO:', err);
      }
    });
  }

  deleteTodo(id: number): void {
    this.todoService.deleteTodo(id).subscribe({
      next: () => {
        this.todos = this.todos.filter((todo) => todo.id !== id);
      },
      error: (err) => {
        console.error('Failed to delete TODO:', err);
      }
    });
  }
}
