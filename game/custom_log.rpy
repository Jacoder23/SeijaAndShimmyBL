init python:
    dev_log_history = []

    def dev_log(text):
        if config.log is not None:
            renpy.log(text)
        dev_log_history.append(str(text))

    def export_log():
        return "\n".join(dev_log_history)

    def FormatHistoryEntry(entry):
        who = entry.who + ": " if entry.who is not None else ""
        return who + entry.what

    def export_history():
        return "\n".join([FormatHistoryEntry(x) for x in _history_list])