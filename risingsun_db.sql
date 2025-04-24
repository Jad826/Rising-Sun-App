-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 23, 2025 at 02:21 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `risingsun_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `id` int(3) NOT NULL,
  `password` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `created_at` date NOT NULL,
  `contact_num` int(8) NOT NULL,
  `region` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `attribute`
--

CREATE TABLE `attribute` (
  `id` int(3) NOT NULL,
  `atturibute_na` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

CREATE TABLE `city` (
  `id` int(3) NOT NULL,
  `city_name` text NOT NULL,
  `city_longitude` varchar(255) NOT NULL,
  `city_lattidute` varchar(255) NOT NULL,
  `zip` int(3) NOT NULL,
  `country_id` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `country`
--

CREATE TABLE `country` (
  `id` int(3) NOT NULL,
  `country_na` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `measuring_units`
--

CREATE TABLE `measuring_units` (
  `id` int(3) NOT NULL,
  `unit_name` varchar(50) NOT NULL,
  `unit_descripti` varchar(50) NOT NULL,
  `attribute_id` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_city`
--

CREATE TABLE `users_city` (
  `users_id` int(3) NOT NULL,
  `city_id` int(3) NOT NULL,
  `added_on` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_prefrences`
--

CREATE TABLE `users_prefrences` (
  `users_id` int(3) NOT NULL,
  `meassuring_units_i` int(3) NOT NULL,
  `atturbute_id` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `weather_status`
--

CREATE TABLE `weather_status` (
  `id` int(3) NOT NULL,
  `weather_st` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `attribute`
--
ALTER TABLE `attribute`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`id`),
  ADD KEY `country_id` (`country_id`);

--
-- Indexes for table `country`
--
ALTER TABLE `country`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `measuring_units`
--
ALTER TABLE `measuring_units`
  ADD PRIMARY KEY (`id`),
  ADD KEY `attribute_id` (`attribute_id`);

--
-- Indexes for table `users_city`
--
ALTER TABLE `users_city`
  ADD PRIMARY KEY (`users_id`,`city_id`),
  ADD KEY `CITYID` (`city_id`);

--
-- Indexes for table `users_prefrences`
--
ALTER TABLE `users_prefrences`
  ADD PRIMARY KEY (`users_id`,`atturbute_id`),
  ADD KEY `meassuring_units_i` (`meassuring_units_i`);

--
-- Indexes for table `weather_status`
--
ALTER TABLE `weather_status`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `city`
--
ALTER TABLE `city`
  ADD CONSTRAINT `COUNTRY` FOREIGN KEY (`country_id`) REFERENCES `account` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `measuring_units`
--
ALTER TABLE `measuring_units`
  ADD CONSTRAINT `attiid` FOREIGN KEY (`attribute_id`) REFERENCES `attribute` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `users_city`
--
ALTER TABLE `users_city`
  ADD CONSTRAINT `CITYID` FOREIGN KEY (`city_id`) REFERENCES `city` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `users_id` FOREIGN KEY (`users_id`) REFERENCES `account` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
