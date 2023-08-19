import { Component } from '@angular/core';
import { USERS } from '../mock-users';
import { User  } from '../user';




@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})




export class UsersComponent {
    // user: User = {
    //   id: 1,
    //   name: 'Dave'
    // };
    // create a users property to expose the USERS array for binding
    users = USERS;

    selectedUser?: User;

    onSelect(user: User): void{
      this.selectedUser = user;
    }
}

