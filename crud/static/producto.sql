create table Producto (
    claveProducto int primary key auto_increment not null,
    descripcion varchar(255) not null,
    precio decimal(10,2) not null
);