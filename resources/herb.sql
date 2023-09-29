-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Sep 29, 2023 at 08:13 AM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `herb`
--

-- --------------------------------------------------------

--
-- Table structure for table `blacklist`
--

DROP TABLE IF EXISTS `blacklist`;
CREATE TABLE IF NOT EXISTS `blacklist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` varchar(255) NOT NULL,
  `blacklisted_on` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `blacklist`
--

INSERT INTO `blacklist` (`id`, `token`, `blacklisted_on`) VALUES
(2, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlcjEiLCJleHAiOjE2OTU2Mzg2NzF9.Y0Me9kHkxCDKzWNrb78baXnhPdfhQxkQ2GYRk7wvzCY', '2023-09-24 10:15:47'),
(3, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlcjIiLCJleHAiOjE2OTU2ODE3MjV9.f7X-xveJaFSVtClWvWVF-vVd0_Wza3xcOVTEYF0pE68', '2023-09-24 22:12:38'),
(4, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlcjIiLCJleHAiOjE2OTU2ODE3MjV9.f7X-xveJaFSVtClWvWVF-vVd0_Wza3xcOVTEYF0pE68', '2023-09-25 08:32:54'),
(5, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlcjIiLCJleHAiOjE2OTU2ODE3MjV9.f7X-xveJaFSVtClWvWVF-vVd0_Wza3xcOVTEYF0pE68', '2023-09-25 08:38:18'),
(6, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlcjIiLCJleHAiOjE2OTU3MTkyNTd9.nsjtDwbbfsX_tk3OqiMTodhwb8ZRN3DEa0jsILuYj7E', '2023-09-25 08:39:26'),
(7, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlcjQiLCJleHAiOjE2OTU5Mzc1NzJ9.n_TbwTAaCD2Q5kJ8hDGcQ2SL8wbQid-xWBDHohluivg', '2023-09-27 21:16:59'),
(8, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlcjQiLCJleHAiOjE2OTU5Mzc1NzJ9.n_TbwTAaCD2Q5kJ8hDGcQ2SL8wbQid-xWBDHohluivg', '2023-09-27 21:18:46');

-- --------------------------------------------------------

--
-- Table structure for table `disease`
--

DROP TABLE IF EXISTS `disease`;
CREATE TABLE IF NOT EXISTS `disease` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `disease` varchar(20) NOT NULL,
  `symptoms` text NOT NULL,
  `treatment` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `disease`
--

INSERT INTO `disease` (`id`, `disease`, `symptoms`, `treatment`) VALUES
(1, 'semgedi', 'difficulty_swallowing, pain_in_thorax_and_ear, sore_thorat, change_in_voice', 'kaluduru grind pottani and put it in the throat to turn phlegm, '),
(2, 'pain_in_heart', 'tiredness, abnormal_heart_rhythm, shortness_of_breath, cough', 'drink one teaspoon of kubuk powder with raw milk, tippili is fried in a pan, crushed and mixed with honey and rubbed on the tongue'),
(3, 'normal_fever', 'abnormal_body_temparature, trembling, tiredness, appette', 'ginger boiled with coriander and drink with sugar, ginger and pathpadagam boiled well and drink'),
(4, 'bade_kakkuma', 'bade_wedanawa, bada_korawima', 'grind pottani and put it in the throat to turn phlegm, ginger puree, lime puree and salt mixed well and drink'),
(5, 'gastric', 'gastric_burning, bloating, regurgitation, loss_of_appitite, headache', 'beli leaves boiled well and drink, vishnukanthi leaves boiled well and drink'),
(6, 'constipation', 'abnormal_bloating, decreased_appetite, stools_are_dry_and_hard', 'aralu leaves boiled well and drink with sukiri, vishnukanthi leaves boiled well and drink'),
(7, 'hemorrhoids', 'pain_or_discomfort, swelling_around_your_anus, bleeding', 'mukunuwanna and mung bean boiled and drink'),
(8, 'worm_diseases', 'tiredness, weakness, abnormal_pain, weight_loss', 'bata dalu mallum, elabudu leaves mallum'),
(9, 'cystitis', 'pain_and_burning_or_stining_when_you_pee, urine_that_dark_and_cloudy_or_strong_smelling, pain_low_down_in_your_tummy', 'drinking akkapana leaves juice, the leaves of the penala are cropped,squeezed, and the drink'),
(10, 'uninary_stones', 'vomiting, urine_that_smells_bad', 'kekiri seeds and akkapana boiled water with honey and drink'),
(11, 'test', 'test', 'test'),
(12, 'test disease', 'test symptom 1, test symptom 2', 'test treatment');

-- --------------------------------------------------------

--
-- Table structure for table `herbs`
--

DROP TABLE IF EXISTS `herbs`;
CREATE TABLE IF NOT EXISTS `herbs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `disease` varchar(20) NOT NULL,
  `herb` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `herbs`
--

INSERT INTO `herbs` (`id`, `disease`, `herb`) VALUES
(1, 'semgedi', 'kaluduru'),
(2, 'pain_in_heart', 'kubuk'),
(3, 'pain_in_heart', 'tippili'),
(4, 'normal_fever', 'ginger'),
(5, 'normal_fever', 'coriander'),
(6, 'normal_fever', 'pathpadagam'),
(7, 'bade_kakkuma', 'ginger'),
(8, 'gastric', 'beli'),
(9, 'gastric', 'vishnukanthi'),
(10, 'constipation', 'aralu'),
(11, 'constipation', 'vishnukanthi'),
(12, 'hemorrhoids', 'mukunuwanna'),
(13, 'worm_diseases', 'bata '),
(14, 'worm_diseases', 'elabudu'),
(15, 'cystitis', 'akkapana'),
(16, 'cystitis', 'penala'),
(17, 'uninary_stones', 'kekiri'),
(18, 'uninary_stones', 'akkapana');

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
CREATE TABLE IF NOT EXISTS `location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lon` varchar(20) NOT NULL,
  `lat` varchar(20) NOT NULL,
  `herb` varchar(20) NOT NULL,
  `added_user` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `added_user` (`added_user`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `location`
--

INSERT INTO `location` (`id`, `lon`, `lat`, `herb`, `added_user`) VALUES
(15, '6.6564655542656', '74.2111455151464', 'ginger', 'testuser3'),
(14, '6.6564655542656', '74.2111455151464', 'ginger', 'testuser3'),
(16, '6.6564655542656', '74.256456464564', 'vishnukanthi', 'testuser3'),
(17, '6.6525554265633', '74.256452344564', 'ginger', 'testuser4');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  `hashed_password` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `is_admin`, `hashed_password`) VALUES
(1, 'testuser1', 'testuser1@abc.com', NULL, '$2b$12$OIQXGYLYGST.u/8o0oF2tuAi6RnMmZtKpDO7qPEP3/yl0WVyZcpEG'),
(2, 'testuser2', 'testuser2@abc.com', 0, '$2b$12$Vg30fkUbUSMzVou35Nhfn.WjQsKgFrSFnmAf4/z1wz3zyDUy0gb.K'),
(3, 'testuser3', 'testuser3@abc.com', 0, '$2b$12$TDKYAVmBRZbuwjHb6CPX7OfsxcDitsE1lbX1y2YKaN4MFPRlOsLB2'),
(4, 'testuser4', 'testuser4@abc.com', 0, '$2b$12$NcDOVaxLL5p.38z2OmZNFOyueJxYZLvlsgaDRyzeoexfgPioHl41.');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
