import sys
import datetime
import pickle


class Todo:
    data = {
        "stack": [],
        "kpending": 0,
        "kdone": 0,
    }

    def __init__(self):
        self.date = datetime.datetime.now()
        self.data = pickle.load(open("todo.pickle", "rb"))

    """
       __            __      ___      __ 
      / /_____  ____/ /___  / (_)____/ /_
     / __/ __ \/ __  / __ \/ / / ___/ __/
    / /_/ /_/ / /_/ / /_/ / / (__  ) /_  
    \__/\____/\__,_/\____/_/_/____/\__/    
                                         
    """

    @staticmethod
    def help():
        print("Usage :-")
        print("$ ./todo add \"todo item\"  # Add a new todo")
        print("$ ./todo ls               # Show remaining todos")
        print("$ ./todo del NUMBER       # Delete a todo")
        print("$ ./todo done NUMBER      # Complete a todo")
        print("$ ./todo help             # Show usage")
        print("$ ./todo report           # Statistics", end='')

    def add(self, todo):
        self.data['stack'].append(todo)
        print("Added todo: "'"' + todo + '"')
        self.data['kpending'] += 1
        pickle.dump(self.data, open("todo.pickle", "wb"))

    def delete(self, index):
        try:
            y = (int(index) - 1)
            del self.data['stack'][y]
            self.data['kpending'] -= 1
            print("Deleted todo #" + index)
            pickle.dump(self.data, open("todo.pickle", "wb"))
        except IndexError:
            print("Error: todo #" + index + " does not exist. Nothing deleted.")

    def list(self):
        if len(self.data['stack']) > 0:
            for i, e in reversed(list(enumerate(self.data['stack']))):
                print('[' + str(i + 1) + ']', e)
        else:
            print("There are no pending todos!")

    def report(self):
        print(self.date.strftime("%Y-%m-%d"), "Pending :", self.data['kpending'], "Completed :", self.data['kdone'])

    def done(self, index):
        try:
            if len(self.data['stack']) > 0:
                print("Marked todo #" + index + " as done.")
                del self.data['stack'][int(index) - 1]
                self.data['kpending'] -= 1
                self.data['kdone'] += 1
                pickle.dump(self.data, open("todo.pickle", "wb"))
            else:
                print("List is empty.")
        except IndexError:
            print("Error: todo #" + index + " does not exist.")

    def clearall(self):
        self.data['stack'].clear()
        self.data['kpending'] = 0
        self.data['kdone'] = 0
        pickle.dump(self.data, open("todo.pickle", "wb"))


if __name__ == '__main__':

    obj = Todo()
    try:
        if len(sys.argv) == 1 or sys.argv[1] == "help":
            obj.help()
        elif sys.argv[1] == "ls":
            obj.list()
        elif sys.argv[1] == "add":
            try:
                if len(sys.argv) == 3:
                    obj.add(sys.argv[2])
                else:
                    print("Error: Missing todo string. Nothing added!")
            except SyntaxError:
                obj.help()
        elif sys.argv[1] == "del":
            try:
                if len(sys.argv) == 3:
                    obj.delete(sys.argv[2])
                else:
                    print("Error: Missing NUMBER for deleting todo.")
            except IndexError:
                print("Error: todo #" + sys.argv[2] + " does not exist. Nothing deleted.")
        elif sys.argv[1] == "report":
            obj.report()
        elif sys.argv[1] == "done":
            try:
                if len(sys.argv) == 3:
                    obj.done(sys.argv[2])
                else:
                    print("Error: Missing NUMBER for marking todo as done.")
            except IndexError:
                print("Error: todo #" + sys.argv[2] + " does not exist.")
        elif sys.argv[1] == "clr":
            obj.clearall()
    except SyntaxError as err:
        print(err)
        obj.help()
