-- Crear la tabla task_management
CREATE TABLE task_management (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    is_completed BOOLEAN DEFAULT FALSE,
    date_deadline DATE,
    create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar algunas tareas de ejemplo
INSERT INTO task_management (name, description, is_completed, date_deadline)
VALUES ('Tarea 1', 'Descripción de la tarea 1', FALSE, '2024-08-15');

INSERT INTO task_management (name, description, is_completed, date_deadline)
VALUES ('Tarea 2', 'Descripción de la tarea 2', TRUE, '2024-08-16');

INSERT INTO task_management (name, description, is_completed, date_deadline)
VALUES ('Tarea 3', 'Descripción de la tarea 3', FALSE, '2024-08-17');
