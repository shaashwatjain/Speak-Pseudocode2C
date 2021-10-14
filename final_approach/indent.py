    def while_loop(self, content):
        """
        while loop construct
        content: string
        """
        content.pop(0)
        rel_op = ["!=", "==", "<", "<=", ">", ">="]
        bin_op = {"and": "&&", "or": "||"}

        string = "while("
        # used to initialize only 1 uninitialized variable
        flag = 1
        for i, word in enumerate(content):
            if word in rel_op:
                string += " " + word + " "

            elif word.isdigit() or word in ["true", "false"]:
                string += word

            elif word in bin_op.keys():
                string += " " + bin_op[word] + " "

            else:
                if self.variable_obj.check_variable_in_scope(word, self._current_indent):
                    string += word
                else:
                    if flag:
                        self.initialize_variable(["", word, "0"])
                        string += word
                        flag = 0
                    else:
                        raise VariableNotDeclared

        self.insert_line(string + ")")
        self.insert_line("{")
        self.increase_indent()


    #################################
    # Helper functions for for loop #
    #################################
    def helper_oper_(self, val, sign):
        if int(val) > 1:
            oper = "{0}=".format(sign)
        else:
            oper = "{0}{0}".format(sign)
            val = ""
        return oper, val


    def helper_greater_(self, x, y):
        if x > y:
            oper = "--"
        else:
            oper = "++"
        return oper


    #######################
    # For loop constructs #
    #######################
    def for_loop(self, content):
        """
        For loop construct
        content: String
        """
        content.pop(0)
        init = update = ""
        variable_exist = 0
        iterator = content[0]
        pos = content.index("till")

        # For range starting
        range_start = content[pos - 1]
        type_ = "int "

        # Required if value of pre initialized iterator is changed
        is_init = 1
        if not range_start.isdigit():
            if range_start in ["a", "z"]:
                type_ = "char "
                range_start_val = ord(range_start)

            elif range_start != "range" and self.variable_obj.get_variable(
                range_start, self._current_indent
            ):
                obj = self.variable_obj.get_variable(range_start, self._current_indent)
                type_ = str(obj.var_type.name) + " "
                range_start_val = obj.var_value

            else:
                #  elif range_start == "range":
                # checking if range_start==range and iter is declared before
                if self.variable_obj.check_variable_in_scope(
                    iterator, self._current_indent
                ):
                    obj = self.variable_obj.get_variable(iterator, self._current_indent)
                    type_ = str(obj.var_type.name) + " "
                    range_start_val = obj.var_value

                else:
                    range_start = "1"
                    range_start_val = 1
            is_init = 0

        else:
            range_start_val = int(range_start)

        # For range ending
        range_end = content[pos + 1]
        if not range_end.isdigit():
            if range_end in ["z", "a"]:
                type_ = "char "
                range_end_val = ord(range_end)

            else:
                variable_exist = self.variable_obj.check_variable_in_scope(
                    content[pos + 1], self._current_indent
                )
                if variable_exist:
                    type_ = (
                        str(
                            self.variable_obj.get_variable(
                                content[pos + 1], self._current_indent
                            ).var_type.name
                        )
                        + " "
                    )
                    range_end_val = int(
                        self.variable_obj.get_variable(
                            content[pos + 1], self._current_indent
                        ).var_value
                    )
                else:
                    raise VariableNotDeclared
        else:
            range_end_val = int(range_end)

        # if iterator is not defined
        if not self.variable_obj.check_variable_in_scope(iterator, self._current_indent):
            init = "{0}{1} = {2}".format(type_, iterator, range_start)
        else:
            if is_init:
                init = "{0} = {1}".format(iterator, range_start)

            range_start = int(
                self.variable_obj.get_variable(content[0], self._current_indent).var_value
            )

        # evaluate the condition of for loop
        cond_oper = "<=" if range_start_val < range_end_val else ">="
        condition = "{0} {1} {2}".format(iterator, cond_oper, range_end)

        last = content[-1]
        if not all(x in content for x in ["no", "update"]):

            if any(x in content for x in ["increment", "increase"]):
                oper, last = self.helper_oper_(last, "+")

            elif any(x in content for x in ["decrement", "decrease"]):
                oper, last = self.helper_oper_(last, "-")

            else:
                last = ""
                oper = self.helper_greater_(range_start_val, range_end_val)

            update = "{0}{1}{2}".format(iterator, oper, last)

        self.insert_line("for({0}; {1}; {2})".format(init, condition, update))
        self.insert_line("{")
        self.increase_indent()
