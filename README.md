## LINKEDIN LEARNING 
<h1>Criação de repositório no github </h1>
{Link - >}[https://github.com/fjdslimajunior/linkedin-learn.git]

### Ambiente virtual com venv e pip
* Criação do ambiente virtual
```
python -m venv "nome-sugerido-por-convenção (.venv)"
```
* Ativação do ambiente
```
.venv/scripts/activate
```

> Obs.: Caso tenha dificuldades em ativar o ambiente verifique se existe restrição no sistema. O comando a seguir pode ser usado em um terminal, aberto como administrador e executado para desabilitar o bloqueio que vem ativo no SO por padrão: 
```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
* Desativação do ambiente virtual
```
deactivate
```
### Instalação de Bibliotecas
```
> pip install "biblioteca-do-seu-interesse"
```