

import os, __main__

from sys import argv
from json import loads, dumps


from lib.ApexProject import ApexProject
from lib.ApiGatewayDeployer import ApiGatewayDeployer
from lib.SwaggerGenerator import SwaggerGenerator
from lib.SwaggerBaseConfig import config

def pretty(json):
    return dumps(json, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    project = ApexProject(argv[1])

    path = os.path.dirname(os.path.realpath(__file__))

    generator = SwaggerGenerator(project=project)
    print generator.generate()
    deployer = ApiGatewayDeployer(swagger=generator.generate(), project=project)

    deployer.deploy()
