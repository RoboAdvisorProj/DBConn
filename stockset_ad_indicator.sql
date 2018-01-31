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
  `CODE` char(10) NOT NULL,
  `Name` char(32) NOT NULL,
  `Price` varchar(10) NULL,
  `Value` varchar(10) NULL,
  `PER` decimal(7,3) NULL,
  `EPS` decimal(10,2) NULL,
  `ROA` decimal(6,3) NULL,
  `ROE` decimal(6,3) NULL,
  `BETA` decimal(6,3) NULL,
  `PBR` decimal(5,2) NULL,
  `NIY0` decimal(7,2) NULL,
  `NI3Y` decimal(7,2) NULL,
  `SALE3Y` decimal(7,2) NULL,
  `DEPRT` decimal(7,2) NULL,
  `D_IV` char(5) NULL,
  `VOL_D` decimal(5,4) NULL,
  `VOL_Y` decimal(5,4) NULL,
  `Chan` decimal(4,2) NULL,
  `Numb` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Numb`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ad_indicator`
--

LOCK TABLES `ad_indicator` WRITE;
/*!40000 ALTER TABLE `ad_indicator` DISABLE KEYS */;
INSERT INTO `ad_indicator` VALUES ('123456','HOPE','333','333',1.000,'1',0.400,0.250,1.000,1.00,'20',0.6931,2.9914,0.640,'NO',0.2710,0.7068,5.00,'1'),('123457','GOPE','111','111',2.000,'2',7.500,3.750,2.000,2.00,'300',-0.2554,0.9039,0.125,'YES',0.0571,1.4545,3.00,'2'),('123458','HYNWOO','100','500',1.000,'1',4.000,1.000,1.000,1.00,'1',-0.2027,1.1236,0.250,'NO',0.2957,0.7437,1.00,'3'),('123459','SULGI','500','1',1.000,'1',8.375,8.375,1.000,1.00,'1',1.0037,0.0059,0.400,'YES',0.2957,0.7437,1.00,'4');
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

-- Dump completed on 2018-01-28 16:14:24
