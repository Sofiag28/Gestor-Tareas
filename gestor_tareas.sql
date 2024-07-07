-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-06-2024 a las 20:37:35
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestor_tareas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tareas`
--

CREATE TABLE `tareas` (
  `id_Tareas` int(11) NOT NULL,
  `Nombre` varchar(200) NOT NULL,
  `Fecha_Inicio` datetime DEFAULT NULL,
  `Fecha_final` datetime DEFAULT NULL,
  `Estado` varchar(200) DEFAULT NULL,
  `id_usuarios` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tareas`
--

INSERT INTO `tareas` (`id_Tareas`, `Nombre`, `Fecha_Inicio`, `Fecha_final`, `Estado`, `id_usuarios`) VALUES
(14, 'dormir', '2024-05-13 20:13:00', '2024-06-08 20:13:00', 'asignado', 1),
(15, 'estudiar portugues', '2024-05-21 21:39:00', '2024-06-08 21:40:00', 'asignado', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `Id_Usuarios` int(11) NOT NULL,
  `Nombre_usuario` varchar(20) NOT NULL,
  `Apellidos_usuario` varchar(20) NOT NULL,
  `Email_usuario` varchar(50) NOT NULL,
  `Genero` varchar(20) NOT NULL,
  `Usuario_name` varchar(200) NOT NULL,
  `Contraseña_Usuario` varchar(255) NOT NULL,
  `Rol` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`Id_Usuarios`, `Nombre_usuario`, `Apellidos_usuario`, `Email_usuario`, `Genero`, `Usuario_name`, `Contraseña_Usuario`, `Rol`) VALUES
(1, 'Jeon', 'Kook', 'lausof@gmail.com', 'Masculino', 'jk', 'scrypt:32768:8:1$gR5Axk34OSfwJvhM$42b332fbfaae31bbd2cd5ab0301ae7564bb9e1c3d12a636a60413eca1cb9c96d25d8f582e8e5b6acc9d9b6ee597abd18f72430e93e38d0d752ca6878c62e7feb', 'Administrador'),
(3, 'rodolfo', 'polo', 'rod.@gmail.com', 'Femenino', 'reno', 'scrypt:32768:8:1$0MamYnjf1666fB1v$a399eabb5d26a05feb7ffb59ab2853c1f2c7c59ccfad4e7515f0555db0cefc02f1e64418f6074b772ec3cba4b2bb0f47db8d7bfd9bcb4c7fa9d38e9776cc6bc5', 'Usuario');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tareas`
--
ALTER TABLE `tareas`
  ADD PRIMARY KEY (`id_Tareas`),
  ADD KEY `fk_id1` (`id_usuarios`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`Id_Usuarios`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tareas`
--
ALTER TABLE `tareas`
  MODIFY `id_Tareas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `Id_Usuarios` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
