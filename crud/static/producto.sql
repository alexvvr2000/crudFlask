create table Producto (
    claveProducto int primary key auto_increment,
    descripcion varchar(255) not null,
    precio decimal(10,2) not null
);
INSERT INTO Producto (descripcion, precio) VALUES ('Producto A', 10.99);
INSERT INTO Producto (descripcion, precio) VALUES ('Producto B', 20.50);
INSERT INTO Producto (descripcion, precio) VALUES ('Producto C', 5.75);
INSERT INTO Producto (descripcion, precio) VALUES ('Producto D', 15.25);
INSERT INTO Producto (descripcion, precio) VALUES ('Producto E', 8.50);