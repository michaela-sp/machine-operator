from models import machines


def validated_template(template: machines.Template) -> machines.Template:
    return machines.Template.MAC_OS if template == machines.Template.LINUX else template
