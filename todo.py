import sys
import datetime
import pickle


class Todo:

    stack = []

    def __init__(self):
        self.date = datetime.datetime.now()
        self.stack = pickle.load(open("todo.pickle", "rb"))
        self.kpending = len(self.stack)
        self.kdone = 0


    def help(self):
        print("Usage :-")
        print("$ ./todo add \"todo item\"  # Add a new todo")
        print("$ ./todo ls               # Show remaining todos")
        print("$ ./todo del NUMBER       # Delete a todo")
        print("$ ./todo done NUMBER      # Complete a todo")
        print("$ ./todo help             # Show usage", sep='')
        print("$ ./todo report           # Statistics", end='')


    def add(self, todo):
        self.stack.append(todo)
        print("Added todo: "'"'+todo+'"')
        self.kpending += 1
        # t = (self.stack, self.kpending, self.kdone)
        pickle.dump(self.stack, open("todo.pickle", "wb"))


    def delete(self, index):
        try:
            y = (int(index)-1)
            del self.stack[y]
            temp = self.stack
            print("Deleted todo #"+index)
            pickle.dump(temp, open("todo.pickle", "wb"))
        except:
            print("Error: todo #"+index+" does not exist. Nothing deleted.")


    def list(self):
        if len(self.stack) > 0:
            for i, e in reversed(list(enumerate(self.stack))):
                print('['+str(i+1)+']', e)
        else:
            print("There are no pending todos!")

    def report(self):
        print(self.date.strftime("%Y-%m-%d"), "Pending :", self.kpending, "Completed :", self.kdone)


    def done(self, index):
        try:
            print("Marked todo #"+index+" as done.")
            i=1
            while len(self.stack) > 0:
                del self.stack[int(i)-1]
                i+=1
            self.kdone += 1
            pickle.dump(self.stack, open("todo.pickle", "wb"))
        except:
            print("Error: todo #"+index+" does not exist.")

    def clearall(self):
        self.stack.clear()
        pickle.dump(self.stack, open("todo.pickle", "wb"))


        
if __name__ == '__main__':

    obj = Todo()
    main_arg = sys.argv[0]

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
        except:
            obj.help()
    elif sys.argv[1] == "del":
        try:
            if len(sys.argv) == 3:
                obj.delete(sys.argv[2])
            else:
                print("Error: Missing NUMBER for deleting todo.")
        except:
            print("Error: todo #" + sys.argv[2] + " does not exist. Nothing deleted.")
    elif sys.argv[1] == "report":
        obj.report()
    elif sys.argv[1] == "done":
        try:
            if len(sys.argv) == 3:
                obj.done(sys.argv[2])
            else:
                print("Error: Missing NUMBER for marking todo as done.")
        except:
            print("Error: todo #"+sys.argv[2]+" does not exist.")

    elif sys.argv[1] == "clr":
        obj.clearall()