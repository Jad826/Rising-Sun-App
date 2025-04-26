SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

CREATE TABLE `account` (
  `id` int(3) NOT NULL,
  `password` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `created_at` date NOT NULL,
  `contact_num` int(8) NOT NULL,
  `region` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `attribute` (
  `id` int(3) NOT NULL,
  `atturibute_na` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `city` (
  `id` int(3) NOT NULL,
  `city_name` text NOT NULL,
  `city_longitude` varchar(255) NOT NULL,
  `city_lattidute` varchar(255) NOT NULL,
  `zip` int(3) NOT NULL,
  `country_id` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `country` (
  `id` int(3) NOT NULL,
  `country_na` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `measuring_units` (
  `id` int(3) NOT NULL,
  `unit_name` varchar(50) NOT NULL,
  `unit_descripti` varchar(50) NOT NULL,
  `attribute_id` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `users_city` (
  `users_id` int(3) NOT NULL,
  `city_id` int(3) NOT NULL,
  `added_on` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `users_prefrences` (
  `users_id` int(3) NOT NULL,
  `meassuring_units_i` int(3) NOT NULL,
  `atturbute_id` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `weather_status` (
  `id` int(3) NOT NULL,
  `weather_st` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

ALTER TABLE `account`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `attribute`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `city`
  ADD PRIMARY KEY (`id`),
  ADD KEY `country_id` (`country_id`);

ALTER TABLE `country`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `measuring_units`
  ADD PRIMARY KEY (`id`),
  ADD KEY `attribute_id` (`attribute_id`);

ALTER TABLE `users_city`
  ADD PRIMARY KEY (`users_id`,`city_id`),
  ADD KEY `CITYID` (`city_id`);

ALTER TABLE `users_prefrences`
  ADD PRIMARY KEY (`users_id`,`atturbute_id`),
  ADD KEY `meassuring_units_i` (`meassuring_units_i`);

ALTER TABLE `weather_status`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `account`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT;

ALTER TABLE `city`
  ADD CONSTRAINT `COUNTRY` FOREIGN KEY (`country_id`) REFERENCES `account` (`id`) ON DELETE CASCADE;

ALTER TABLE `measuring_units`
  ADD CONSTRAINT `attiid` FOREIGN KEY (`attribute_id`) REFERENCES `attribute` (`id`) ON DELETE CASCADE;

ALTER TABLE `users_city`
  ADD CONSTRAINT `CITYID` FOREIGN KEY (`city_id`) REFERENCES `city` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `users_id` FOREIGN KEY (`users_id`) REFERENCES `account` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
