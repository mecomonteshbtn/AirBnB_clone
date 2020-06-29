#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 07:56:17 2020

@author: Robinson Montes
         Carlos Murcia
"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """aclass that contains the entry point of the command interpreter.
    """
    prompt = '(hbnb) '
    class_list = ['BaseModel']

    def do_EOF(self, args):
        """EOF command to exit the program.
        """
        return True

    def do_quit(self, args):
        """ Quit command to exit the program.
        """
        return True

    def emptyline(self):
        """method to do nothing when an empty line is inputed.
        """
        pass

    def postloop(self):
        """method to do nothing after each console loop.
        """
        pass

    def do_create(self, args):
        """Create command to create a new instance of BaseModel, save it in a
        JSON file and prints the id.

        Attributes:
            args (str): inputted line in command prompt.
        """
        line = args.split()
        if not self.verify_class(line):
            return
        instance = eval(str(line[0]) + '()')
        if isinstance(instance, BaseModel):
            instance.save()
            print(instance.id)
        return

    def do_show(self, args):
        """Show command that prints the string representation of an instance
        based on the class name and id.

        Attributes:
           args (str): inputted line in command prompt.
        """
        line = args.split()
        if not self.verify_class(line):
            return
        if not self.verify_id(line):
            return

    def do_destroy(self, args):
        """Destroy command that deletes an instance based on the class name
        and id. Save the change in JSON file.

        Attributes:
            args (str): inputted line in command prompt.
        """
        line = args.split()
        if not self.verify_class(line):
            return
        if not self.verify_id(line):
            return
        key = line[0] + '.' + line[1]
        objects = models.storage.all()
        models.storage.delete(objects[key])
        models.storage.save()

    @classmethod
    def verify_class(cls, line):
        """Static method to verify inputed class"""
        if len(line) == 0:
            print('** class namer missing **')
            return False
        elif line[0] not in HBNBCommand.class_list:
            print('** class doesn exist **')
            return False
        return True

    @staticmethod
    def verify_id(line):
        """Static method to ferify the id.
        """
        if len(line) < 2:
            print('** instance id missing **')
            return False
        objects = models.storage.all()
        key = line[0] + '.' + line[1]
        if key not in objects.keys():
            print('** no instance found **')
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
