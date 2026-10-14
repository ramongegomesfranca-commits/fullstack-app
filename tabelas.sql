create table empresas (
    id_empresa INT IDENTITY(1,1) PRIMARY KEY,
    nome_empresa VARCHAR(100) NOT NULL,
    cnpj CHAR(14),
    tipo_relacionamento VARCHAR(100) NOT NULL
);

create table representantes(
    id_representante INT IDENTITY(1,1) PRIMARY KEY, 
    id_empresa INT NOT NULL FOREIGN KEY REFERENCES empresas(id_empresa),
    nome_representante VARCHAR (100) NOT NULL,
    telefone VARCHAR (100),
    email VARCHAR(100)
);

create table projetos(
    id_projeto INT IDENTITY(1,1) PRIMARY KEY,
    id_empresa INT NOT NULL FOREIGN KEY REFERENCES empresas(id_empresa),
    nome_evento VARCHAR (100) NOT NULL,
    data_montagem DATE,
    data_evento_inicio DATE,
    data_evento_termino DATE,
    data_desmontagem DATE,
    status_funil VARCHAR(100)
);
