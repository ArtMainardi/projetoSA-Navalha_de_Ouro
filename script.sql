CREATE DATABASE IF NOT EXISTS barbearia;
USE barbearia;

-- Criar a tabela 'agendamentos'
CREATE TABLE IF NOT EXISTS agendamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    servico VARCHAR(100),
    preco DECIMAL(10,2),
    barbeiro VARCHAR(50),
    data DATE NOT NULL,
    horario VARCHAR(5),
    status VARCHAR(20) DEFAULT 'Agendado' CHECK (status IN ('Agendado', 'Concluído', 'Cancelado'))
);

-- Inserir 8 agendamentos com dados variados
INSERT INTO agendamentos (cliente, telefone, servico, preco, barbeiro, data, horario, status) VALUES
('Carlos Silva', '(11) 98765-4321', 'Corte de Cabelo', 45.00, 'Lucas', '2026-09-10', '09:00', 'Agendado'),
('Ana Beatriz', '(11) 97654-3210', 'Barba Completa', 35.00, 'Mateus', '2026-09-08', '10:30', 'Concluído'),
('João Pedro', '(11) 96543-2109', 'Corte + Barba', 70.00, 'Lucas', '2026-09-09', '14:00', 'Concluído'),
('Mariana Costa', '(11) 95432-1098', 'Coloração', 90.00, 'Gabriel', '2026-09-11', '11:00', 'Cancelado'),
('Felipe Rocha', '(11) 94321-0987', 'Corte Infantil', 40.00, 'Mateus', '2026-09-12', '15:30', 'Agendado'),
('Lucas Almeida', '(11) 93210-9876', 'Sobrancelha', 20.00, 'Gabriel', '2026-09-12', '16:00', 'Agendado'),
('Roberto Souza', '(11) 92109-8765', 'Corte de Cabelo', 45.00, 'Lucas', '2026-09-07', '17:00', 'Concluído'),
('Thiago Martins', '(11) 91098-7654', 'Corte + Barba', 70.00, 'Mateus', '2026-09-13', '18:00', 'Agendado');