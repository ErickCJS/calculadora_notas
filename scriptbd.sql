CREATE TABLE semestre (
    id_semestre INT AUTO_INCREMENT PRIMARY KEY,
    nombre_semestre VARCHAR(6) NOT NULL
);

CREATE TABLE curso (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(70) NOT NULL,
    id_semestre INT NOT NULL,
    nota_final DECIMAL(4,2) DEFAULT 0,
    FOREIGN KEY (id_semestre) REFERENCES semestre(id_semestre) ON DELETE CASCADE
);

CREATE TABLE unidad (
    id_unidad INT AUTO_INCREMENT PRIMARY KEY,
    nombre_unidad VARCHAR(5) NOT NULL,
    nota DECIMAL(4,2) DEFAULT 0,
    peso INT NOT NULL,
    id_curso INT NOT NULL,
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso) ON DELETE CASCADE
);

CREATE TABLE subunidad (
    id_subunidad INT AUTO_INCREMENT PRIMARY KEY,
    nombre_subunidad VARCHAR(8) NOT NULL,
    nota DECIMAL(4,2) DEFAULT 0,
    peso INT NOT NULL,
    id_unidad INT NOT NULL,
    FOREIGN KEY (id_unidad) REFERENCES unidad(id_unidad) ON DELETE CASCADE
);

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_apellido VARCHAR(50) NOT NULL,
    tipo_usuario BOOLEAN NOT NULL,
    correo VARCHAR(80) NOT NULL UNIQUE,
    contraseña VARCHAR(50) NOT NULL,
    token VARCHAR(60),
    enlace_imagen VARCHAR(50),
    veces INT DEFAULT 0
);
