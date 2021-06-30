-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-06-2021 a las 03:20:21
-- Versión del servidor: 10.1.31-MariaDB
-- Versión de PHP: 7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `flask_2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `authors`
--

CREATE TABLE `authors` (
  `id` smallint(4) UNSIGNED NOT NULL,
  `last_name` varchar(40) COLLATE utf8_spanish_ci NOT NULL,
  `name` varchar(40) COLLATE utf8_spanish_ci NOT NULL,
  `date_born` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `authors`
--

INSERT INTO `authors` (`id`, `last_name`, `name`, `date_born`) VALUES
(1, 'Vallejo Mendoza', 'César Abraham', '1892-03-16'),
(2, 'Vargas Llosa', 'Jorge Mario Pedro', '1936-03-28'),
(3, 'Alegría Bazán', 'Ciro', '1909-11-04'),
(4, 'García Márquez', 'Gabriel José de la Concordia', '1927-03-06');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `books`
--

CREATE TABLE `books` (
  `isbn` char(12) COLLATE utf8_spanish_ci NOT NULL,
  `title` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `author_id` smallint(4) UNSIGNED NOT NULL,
  `year_published` year(4) NOT NULL,
  `price` decimal(3,0) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `books`
--

INSERT INTO `books` (`isbn`, `title`, `author_id`, `year_published`, `price`) VALUES
('238874100138', 'Conversación en La Catedral', 2, 1951, '70'),
('383370912281', 'El mundo es ancho y ajeno', 3, 1941, '65'),
('480129403571', 'La ciudad y los perros', 2, 1963, '81'),
('483240184226', 'La serpiente de oro', 3, 1935, '85'),
('589120131047', 'Los perros hambrientos', 3, 1939, '31'),
('591338770183', 'Paco Yunque', 1, 1951, '55'),
('661984010128', 'El general en su laberinto', 4, 1989, '110'),
('683425019133', 'El coronel no tiene quien le escriba', 4, 1961, '42'),
('762841019387', 'Cien años de soledad', 4, 1967, '75'),
('890366138239', 'La fiesta del Chivo', 2, 2000, '30'),
('892014771852', 'Poemas humanos', 1, 1939, '120'),
('930281938211', 'El amor en los tiempos del cólera', 4, 1985, '38'),
('978318472263', 'Los heraldos negros', 1, 1919, '48'),
('981402938251', 'La casa verde', 2, 1966, '105');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `purchases`
--

CREATE TABLE `purchases` (
  `uuid` char(36) COLLATE utf8_spanish_ci NOT NULL,
  `isbn_book` char(12) COLLATE utf8_spanish_ci NOT NULL,
  `user_id` smallint(3) UNSIGNED NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `type_user`
--

CREATE TABLE `type_user` (
  `id` tinyint(1) UNSIGNED NOT NULL,
  `name` varchar(15) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `type_user`
--

INSERT INTO `type_user` (`id`, `name`) VALUES
(1, 'admin'),
(2, 'customer');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` smallint(3) UNSIGNED NOT NULL,
  `user` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `password` char(150) COLLATE utf8_spanish_ci NOT NULL,
  `type_user_id` tinyint(1) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `authors`
--
ALTER TABLE `authors`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`isbn`),
  ADD KEY `FK_book_author` (`author_id`);

--
-- Indices de la tabla `purchases`
--
ALTER TABLE `purchases`
  ADD PRIMARY KEY (`uuid`),
  ADD KEY `FK_buyed_book` (`isbn_book`),
  ADD KEY `FK_buyed_user` (`user_id`);

--
-- Indices de la tabla `type_user`
--
ALTER TABLE `type_user`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_users_type_user` (`type_user_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `authors`
--
ALTER TABLE `authors`
  MODIFY `id` smallint(4) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `type_user`
--
ALTER TABLE `type_user`
  MODIFY `id` tinyint(1) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` smallint(3) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `FK_book_author` FOREIGN KEY (`author_id`) REFERENCES `authors` (`id`);

--
-- Filtros para la tabla `purchases`
--
ALTER TABLE `purchases`
  ADD CONSTRAINT `FK_buyed_book` FOREIGN KEY (`isbn_book`) REFERENCES `books` (`isbn`),
  ADD CONSTRAINT `FK_buyed_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Filtros para la tabla `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `FK_users_type_user` FOREIGN KEY (`type_user_id`) REFERENCES `type_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
