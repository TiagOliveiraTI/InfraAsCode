from diagrams import Diagram
from diagrams.onprem.client import User
from diagrams.generic.compute import Rack
from diagrams.onprem.iac import Terraform
from diagrams.oci.storage import DataTransfer

with Diagram("Fluxo", show=False):
    user = User("User")
    estadoDesejado = Rack("Estado Desejado")
    estadoAtual = Rack("Estado Atual")
    terraform = Terraform("Terraform")
    infraCloud = DataTransfer("Infraestrutura")

    user >> estadoDesejado >> terraform >> estadoAtual >> terraform >> infraCloud