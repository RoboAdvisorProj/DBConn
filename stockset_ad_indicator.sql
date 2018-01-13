-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: stockset
-- ------------------------------------------------------
-- Server version	5.7.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ad_indicator`
--

DROP TABLE IF EXISTS `ad_indicator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ad_indicator` (
  `CODE` char(6) NOT NULL,
  `Name` char(32) NOT NULL,
  `Price` varchar(10) NOT NULL,
  `Value` varchar(10) NOT NULL,
  `PER` decimal(6,3) DEFAULT NULL,
  `EPS` varchar(8) NOT NULL,
  `ROA` decimal(6,3) DEFAULT NULL,
  `ROE` decimal(6,3) DEFAULT NULL,
  `BETA` decimal(6,3) DEFAULT NULL,
  `PBR` decimal(5,2) DEFAULT NULL,
  `NIY` varchar(10) NOT NULL,
  `NI3Y` float NOT NULL,
  `SALE3Y` float DEFAULT NULL,
  `DEPTR` decimal(6,3) DEFAULT NULL,
  `D_IV` char(5) NOT NULL,
  `VOL_D` decimal(5,4) DEFAULT NULL,
  `VOL_Y` decimal(5,4) DEFAULT NULL,
  `Chan` decimal(4,2) NOT NULL,
  `Numb` varchar(7) NOT NULL,
  PRIMARY KEY (`Numb`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ad_indicator`
--

LOCK TABLES `ad_indicator` WRITE;
/*!40000 ALTER TABLE `ad_indicator` DISABLE KEYS */;
INSERT INTO `ad_indicator` VALUES ('123456','KELLOG','50','800',0.000,'0',0.000,0.000,0.000,0.00,'0',0.774597,0,0.000,'YES',0.0000,0.0000,0.00,'1'),('123476','PERLABYSS','500','8000',0.000,'0',0.000,0.000,0.000,0.00,'0',0.693134,0,0.000,'YES',0.0000,0.0000,0.00,'2'),('123422','Hospok','300','2500',0.000,'0',0.000,0.000,0.000,0.00,'0',-0.0327913,0,0.000,'YES',0.0000,0.0000,0.00,'3');
/*!40000 ALTER TABLE `ad_indicator` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-14  7:31:30
