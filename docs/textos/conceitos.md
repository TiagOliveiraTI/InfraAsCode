# Conceitos de Infraestrutura por código

1. [Old Way](#oldway)
1. [Problemas e desafios](#problemas)
1. [Infraestrutura como solução](#iac)
1. [IaC: Conceitos](#conceitos)
1. [IaC: Principais ferramentas](#ferramentas)
1. [IaC: Casos de Uso](#casos)
1. [IaC: Dicas de Boa vizinhança](#dicas)

<a id="oldway"></a>
## OldWay
A forma como era feita, e ainda é em muitos lugares, pensamentos na infra como sendo um datacenter, com vários servidores, num esquema de infra by premises

> Solicitar para data center -> Instalar SO -> Instalar Pacotes -> Configurar Serviços -> Refinar Segurança -> Publicar serviços

<a id="problemas"></a>
### Problemas
- Processo demorado
- Muito passos manuais
- Alto custo técnico
- Repetição
- Atualização
- Escalabilidade
- Resiliencia
- Manter a alta disponibilidade

<a id="conceitos"></a>
## IaC: Conceitos
- Infraestrutura como código
- Automação do processo de criação e gerenciamento da infraestrutura
- Permite aplicação de práticas de desenvolvimento
- agilidade, repetibilidade, reutilização, manter estado, dinamismo, testes

### Temos dois focos principais
- Infrastructure
    - Tudo que envolve a infra, como databases, máquinas, enfim...
    - Provisionamento da Infra


- Configuration manager
    - Instalação da aplicação
    - Configuração da aplicação
    - Remoção da aplicação

<a id="ferramentas"></a>
## IaC: Principais ferramentas
- Ferramentas que gerenciam a infra através de códigos de sintaxe própria ou linguagem de programação
    - Terraform
    - AWS Cloud Formation
    - Pulumi
    - Vagrant
- Ferramentas que gerenciam a configuração de servidores ou ambientes através de declarações pré-definidas ou variáveis
    - Ansible
    - Saltstack
    - Puppet
    - Chef

<a id="casos"></a>
## IaC: Casos de Uso
- Criação de infraestrutura para aplicação (máquina, redes, subredes, acesso a internet, banco de dados, storage, cdn...)
- Criação de ambientes de testes
- Atualização zero downtime de aplicação
- Escalabilidade e Elasticidade
- Desastre e Recuperação
- Desativação de infraestruturas

<a id="dicas"></a>
## IaC: Dicas de Boa vizinhança
- Código Limpo
- Comentários explicativos
- README E USEME atualizados
- KISS (Keep it simple, stupid)