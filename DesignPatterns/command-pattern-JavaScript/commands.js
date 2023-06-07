/*
 a command is something in which we define what action to do.
 Loosely coupled coding style can be built using this technique
 A command class consists of mainly three methods
 execute
 undo
 redo

 these methods are called inside history class.

 ______Basic structure of a command is______

class Command{
    constructor(){

    }

    execute(args){ //args optional

    }

    undo(){

    }

    redo(){

    }
}

*/