class Titular():
   # Init method to create an object
   def __init__(self, nome, sobrenome, cpf):
       self.nome = nome;
       self.sobrenome = sobrenome;
       self.cpf = cpf;


   #get and set methods in relation to the name
   def get_nome(self):
       return self.nome;
   def set_nome(self, novo_nome):
       self.nome = novo_nome;
       return;


   #get and set methods in relation to the surename
   def get_sobrenome(self):
       return self.sobrenome;
   def set_sobrenome(self, novo_sobrenome):
       self.sobrenome = novo_sobrenome;


   #method to get the person's full name
   def get_nome_completo(self):
       nome_completo = f'''{self.nome} {self.sobrenome}''';
       return nome_completo;


   # get and set methods in relation to the CPF (similar to de Social security number)
   def get_cpf(self):
       return self.cpf;


   def __str__(self):
       classe = f'''Nome: {self.nome},\nSobrenome: {self.sobrenome},\nCPF: {self.cpf},\n'''
       return classe


class Conta_Corrente():
   #Init method to create an object
   def __init__(self, n_conta, saldo, titular, limite):
       self.n_conta = n_conta;
       self.saldo = saldo;
       self.titular = titular;
       self.limite = limite;

   def get_n_conta(self):
       return self.n_conta;

   #Methods in reference to the value in ones account
   def get_saldo(self):
       return self.saldo

   #'Deposita' (deposit) adds to the account value
   def deposita(self, valor):
       if self.saldo+valor > self.limite:
           print("valor não é válido");
       else:
           self.saldo += valor;

   #'Saque' (withdraw) subtracts from ones account value if the number is not greater than the current account's value
   def saque(self, valor):
       if valor > self.saldo:
           print("Saque não autorizado, valor não é valido, por favor tente novamente");
       else:
           self.saldo-=valor;
           print("Saque realizado, por favor aguarde enquanto suas cédulas são liberadas");


   def transferencia(self, conta_destino, valor):
       if valor > self.saldo or conta_destino.saldo+valor> conta_destino.limite:
           print("Transferência não autorizada, valor não é valido, por favor tente novamente");
       else:
           self.saldo -= valor;
           conta_destino.saldo += valor;
           print("Transferencia realizada, aguarde o comprovante");

   #Account limit methods
   def get_limite (self):
       return self.limite;
   def set_limite(self,novo_limite):
       self.limite = novo_limite;

   def extrato_reduzido(self):
       exred = f'''Número: {self.n_conta},\nSaldo: {self.saldo}.''';
       return exred;
   def extrato_completo(self):
       extrato = f'''Nome: {self.titular.get_nome_completo()},\nNúmero{self.n_conta},\nCPF: {self.titular.get_cpf()},\nSaldo {self.saldo}'''
       return extrato;
   def __str__(self):
       conta = f'Número: {self.n_conta},\nSaldo: {self.saldo},\n{self.titular}Limite: {self.limite}.';
       return conta;

if __name__ == '__main__':
   Titular1 = Titular("Gustavo", "Ferreira", '888698232-87');
   Conta1 = Conta_Corrente(0001.01, 500.00, Titular1, 2000.00);

   print(Conta1.extrato_reduzido())
