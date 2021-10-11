/*
  History is the class which is responsible for storing and manipulating all the actions
  it has mainly 3 functions
  execute 
  undo
  redo
*/


class History{
    constructor(){
        this.history = [] //place where all commands gets stored for reusable actions (undo/redo)
        this.pointer = -1; //set current index = -1
        this.isUndoEnabled = false; //used to enable or disable undo button
        this.isRedoEnabled = false; //used to enable or disable redo button
    }

    //this is the funtion where we implement our code to do something via a command as argument
    execute(command){
        command.execute();
        if(this.pointer === (this.history.length -1)){
            this.history.push(command);
        }else{
            this._removeRedos();
            this.history.push(command);  
        }
        this.isUndoEnabled = true;
        this.isRedoEnabled = false;
        this.pointer++;
    }

    //this is where we undo the target action
    undo(){
        if(this.isUndoEnabled){
            this.history[this.pointer].undo();
            this.pointer--;
            this.isRedoEnabled = true;
            this.isUndoEnabled = (this.pointer > -1) ? true : false;
        }
    }

    //this is used to redo the undoed action
    redo(){
        if(this.isRedoEnabled){
            this.pointer++;
            this.history[this.pointer].redo(); //gets the command at the current index and apply its redo function
            this.isRedoEnabled = (this.pointer !== (this.history.length -1)) ? true : false;
            this.isUndoEnabled = true;
        }
    }

    _removeRedos(){
        while(this.pointer !== (this.history.length -1)){
            this.history.pop();
        }
        this.isRedoEnabled = false;
    }
}

export default History;