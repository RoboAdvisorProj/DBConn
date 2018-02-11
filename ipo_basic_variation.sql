-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: ipo
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

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
-- Table structure for table `basic_variation`
--

DROP TABLE IF EXISTS `basic_variation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `basic_variation` (
  `CODE` char(6) NOT NULL,
  `Name` char(32) NOT NULL,
  `Price` varchar(10) NOT NULL,
  `D_PRH` varchar(10) NOT NULL,
  `D_PRL` varchar(10) NOT NULL,
  `Y_PRH` varchar(10) NOT NULL,
  `Y_PRL` varchar(10) NOT NULL,
  `D_IV` varchar(4) NOT NULL,
  `Numb` int(11) NOT NULL AUTO_INCREMENT,
  `VOL` varchar(10) NOT NULL,
  PRIMARY KEY (`Numb`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `basic_variation`
--

LOCK TABLES `basic_variation` WRITE;
/*!40000 ALTER TABLE `basic_variation` DISABLE KEYS */;
INSERT INTO `basic_variation` VALUES ('123456','gaybar','5000','8800','6700','9000','4300','YES',1,'0.31343284'),('123476','shobar','1500','1800','1700','1900','300','YES',2,'0.05882353'),('123156','gaybar','50500','88500','65700','95000','43500','No',3,'0.34703196'),('127156','jrybar','8500','8850','6570','9500','4350','No',4,'0.34703196'),('543267','Hyuo','95000','88000','86000','83000','80000','YES',5,'0.02325581');
/*!40000 ALTER TABLE `basic_variation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-10 16:23:02
