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
-- Table structure for table `basic_fixed`
--

DROP TABLE IF EXISTS `basic_fixed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `basic_fixed` (
  `CODE` char(6) NOT NULL,
  `Name` char(32) NOT NULL,
  `NIY2` varchar(10) NOT NULL,
  `NIY1` varchar(10) NOT NULL,
  `NIY0` varchar(10) NOT NULL,
  `SALEY2` float NOT NULL,
  `SALEY1` float NOT NULL,
  `SALEY0` float NOT NULL,
  `AST` varchar(10) NOT NULL,
  `CAP` varchar(10) NOT NULL,
  `DPT` varchar(10) NOT NULL,
  `Numb` varchar(6) NOT NULL,
  PRIMARY KEY (`Numb`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `basic_fixed`
--

LOCK TABLES `basic_fixed` WRITE;
/*!40000 ALTER TABLE `basic_fixed` DISABLE KEYS */;
INSERT INTO `basic_fixed` VALUES ('123456','HOPE','5','11','20',14,555,5552,'50','18','32','1'),('123457','GOPE','500','700','300',412,5251,2512,'40','35','5','2'),('123458','HYNWOO','120','100','80',555,112,5251,'20','15','5','3'),('123459','SULGI','90','800','670',2525,1255,2555,'80','48','32','4');
/*!40000 ALTER TABLE `basic_fixed` ENABLE KEYS */;
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
