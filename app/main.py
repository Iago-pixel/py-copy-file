def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "cp":
        return None

    file_name = command_parts[1]
    new_file_name = command_parts[2]

    if file_name == new_file_name:
        return None

    try:
        with open(file_name, "r") as file_in:
            with open(new_file_name, "a") as file_out:
                file_out.write(file_in.read())
    except FileNotFoundError:
        return None
