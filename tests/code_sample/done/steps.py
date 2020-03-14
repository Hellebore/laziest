def function_with_args_modifications(arg_1):
    arg_1 *= 10
    return str(arg_1) + ' was incremented'


def function_with_args_modifications_with_function(arg_1):
    return arg_1.split()


def function_with_args_modifications_with_function_and_one_more_step(arg_1):
    arg_1 = arg_1.split()
    arg_1 *= 10
    return arg_1


def multiple_assigment_per_line_attr_calls_one_return(key, val):
    key, new_var = key.strip(), val.strip()
    new_var *= 4
    return new_var


def vars_intersections_steps(key, val):
    key, new_var = key.strip(), val.strip()
    new_var *= 4
    return key + new_var

# TODO: add steps with ifs statements
