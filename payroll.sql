-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Nov 28, 2022 at 03:14 PM
-- Server version: 5.5.27
-- PHP Version: 5.4.7

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `payroll`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE IF NOT EXISTS `admin`(
  `uid` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`uid`, `pass`) VALUES
('admin', '123');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE IF NOT EXISTS `employee` (
  `employeeno` int(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `qualification` varchar(50) NOT NULL,
  `experience` varchar(50) NOT NULL,
  `job` varchar(20) NOT NULL,
  `dateofjoin` varchar(50) NOT NULL,
  `contact` int(20) NOT NULL,
  `address` varchar(30) NOT NULL,
  `email` varchar(20) NOT NULL,
  `salary` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`employeeno`, `name`, `qualification`, `experience`, `job`, `dateofjoin`, `contact`, `address`, `email`, `salary`) VALUES
(1221, 'rahul', 'graduate', '1 yr', 'clerk', '20 october 2022', 2147483647, 'khanna', 'rahul@gmail.com', 12000),
(121, 'ragahv', 'graduate', '2 yrs', 'clerk', '21 nov 2022', 543435646, 'khanna', 'raghav@gmail.com', 15000),
(99, 'Kamal', 'MCA', '12', 'Accountant', '12-12-2021', 2147483647, 'khann', 'aa', 120000);

-- --------------------------------------------------------

--
-- Table structure for table `salary`
--

CREATE TABLE IF NOT EXISTS `salary` (
  `employeeno` int(10) NOT NULL,
  `name` varchar(30) NOT NULL,
  `month` varchar(30) NOT NULL,
  `noofdays` int(10) NOT NULL,
  `noofleaves` int(10) NOT NULL,
  `overtimeinhours` int(15) NOT NULL,
  `salary` int(10) NOT NULL,
  `salaryperday` int(10) NOT NULL,
  `deduction` int(10) NOT NULL,
  `extratime` int(10) NOT NULL,
  `grosspay` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `salary`
--

INSERT INTO `salary` (`employeeno`, `name`, `month`, `noofdays`, `noofleaves`, `overtimeinhours`, `salary`, `salaryperday`, `deduction`, `extratime`, `grosspay`) VALUES
(101, 'shivay', 'january', 28, 2, 20, 30000, 1000, 2000, 1000, 31000),
(22222, 'ghf', 'February', 22, 8, 12, 56000, 1867, 14933, 5600, 46667),
(99, 'Kamal', '', 30, 12, 12, 120000, 4000, 48000, 12000, 84000);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
