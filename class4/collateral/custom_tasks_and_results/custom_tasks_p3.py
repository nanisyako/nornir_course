from nornir import InitNornir
from nornir.core.task import Result
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import networking


def my_task(task):
    if task.host.groups[0] == "ios":
        cmd = "show run"
        task.run(task=networking.netmiko_send_command, command_string=cmd)
    elif task.host.groups[0] == "junos":
        cmd = "show configuration"
        task.run(task=networking.netmiko_send_command, command_string=cmd)


def new_task(task):
    result = "this task succeeded"
    return Result(host=task.host, result=result, failed=True, changed=True)


def main():
    nr = InitNornir(config_file="config.yaml", logging={"enabled": False})
    # result = nr.run(task=my_task)
    # print_result(result)
    nr = nr.filter(name="arista1")
    result = nr.run(task=new_task)
    import ipdb

    ipdb.set_trace()
    print_result(result)


if __name__ == "__main__":
    main()
