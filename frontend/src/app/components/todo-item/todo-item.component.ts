import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-todo-item',
  imports: [],
  templateUrl: './todo-item.component.html',
  styleUrl: './todo-item.component.scss'
})
export class TodoItemComponent {
  @Input() todo: any;
  @Output() delete = new EventEmitter<number>();

  onDelete(): void {
    this.delete.emit(this.todo.id);
  }
}
