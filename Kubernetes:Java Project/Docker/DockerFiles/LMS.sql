-- MySQL dump 10.18  Distrib 10.3.27-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: LMS
-- ------------------------------------------------------
-- Server version	10.3.27-MariaDB-0+deb10u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `LMS`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `LMS` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `LMS`;

--
-- Table structure for table `EMPLOYEE`
--

DROP TABLE IF EXISTS `EMPLOYEE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EMPLOYEE` (
  `username` varchar(250) DEFAULT NULL,
  `password` varchar(250) DEFAULT NULL,
  `phoneNo` varchar(20) DEFAULT NULL,
  `street` varchar(250) DEFAULT NULL,
  `postalCode` varchar(250) DEFAULT NULL,
  `city` varchar(250) DEFAULT NULL,
  `firstName` varchar(250) DEFAULT NULL,
  `lastName` varchar(250) DEFAULT NULL,
  `empID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`empID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EMPLOYEE`
--

LOCK TABLES `EMPLOYEE` WRITE;
/*!40000 ALTER TABLE `EMPLOYEE` DISABLE KEYS */;
INSERT INTO `EMPLOYEE` VALUES ('user1','pass1','321-654-0987','1 Elm St','54321','CityC','John','Doe',1),('user2','pass2','432-765-0192','2 Pine St','65432','CityD','Jane','Smith',2);
/*!40000 ALTER TABLE `EMPLOYEE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EMPLOYEE_WORKS_AT`
--

DROP TABLE IF EXISTS `EMPLOYEE_WORKS_AT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EMPLOYEE_WORKS_AT` (
  `empID` int(11) NOT NULL,
  `storeID` int(11) NOT NULL,
  PRIMARY KEY (`empID`,`storeID`),
  KEY `storeID` (`storeID`),
  CONSTRAINT `EMPLOYEE_WORKS_AT_ibfk_1` FOREIGN KEY (`empID`) REFERENCES `EMPLOYEE` (`empID`),
  CONSTRAINT `EMPLOYEE_WORKS_AT_ibfk_2` FOREIGN KEY (`storeID`) REFERENCES `STORE` (`storeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EMPLOYEE_WORKS_AT`
--

LOCK TABLES `EMPLOYEE_WORKS_AT` WRITE;
/*!40000 ALTER TABLE `EMPLOYEE_WORKS_AT` DISABLE KEYS */;
INSERT INTO `EMPLOYEE_WORKS_AT` VALUES (1,1),(2,2);
/*!40000 ALTER TABLE `EMPLOYEE_WORKS_AT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MANAGER`
--

DROP TABLE IF EXISTS `MANAGER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MANAGER` (
  `username` varchar(250) DEFAULT NULL,
  `password` varchar(250) DEFAULT NULL,
  `phoneNo` varchar(20) DEFAULT NULL,
  `street` varchar(250) DEFAULT NULL,
  `postalCode` varchar(250) DEFAULT NULL,
  `city` varchar(250) DEFAULT NULL,
  `firstName` varchar(250) DEFAULT NULL,
  `lastName` varchar(250) DEFAULT NULL,
  `managerID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`managerID`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MANAGER`
--

LOCK TABLES `MANAGER` WRITE;
/*!40000 ALTER TABLE `MANAGER` DISABLE KEYS */;
INSERT INTO `MANAGER` VALUES ('manager1','asjf','98897','kjhafkjhd','lkjasf8','Toronto','Arman','Grewal',1),('manager2','pass4','324-657-9012','4 Birch St','45678','CityF','Bob','Williams',2),('lkjhlkj','hlkjh','lkjh','hkljh','kjhkj','kjhhjk','testing','grewal',6),('kljh','kljhkl','kjh','kljh','kjh','khj','testA','kh',7),('hfjhgf','yfuigjkh','ugi67rtf','jhgy','jkjhlkjh98','toronto','arman','Grewal',9),('kjsahdfkljh','kjhksadhf','892h3498h','wall street','sadfh89','toronto','Arman','Grewal',10),('JLHKL','JHKLJHKJLHKJH','HK','KJHKJL','alskjdfkljKJH','brampton','macbook','pro',11),('kjlh','kljh','kjh','kljh','kljh','kjhkjhkjh','arman','test101010',12),('batman25','asdf','29304','arkham','asdfadf','GOTHAM','BATMAN','JOKER',13);
/*!40000 ALTER TABLE `MANAGER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MANAGER_MANAGES`
--

DROP TABLE IF EXISTS `MANAGER_MANAGES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MANAGER_MANAGES` (
  `managerID` int(11) NOT NULL,
  `storeID` int(11) NOT NULL,
  PRIMARY KEY (`managerID`,`storeID`),
  KEY `storeID` (`storeID`),
  CONSTRAINT `MANAGER_MANAGES_ibfk_1` FOREIGN KEY (`managerID`) REFERENCES `MANAGER` (`managerID`),
  CONSTRAINT `MANAGER_MANAGES_ibfk_2` FOREIGN KEY (`storeID`) REFERENCES `STORE` (`storeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MANAGER_MANAGES`
--

LOCK TABLES `MANAGER_MANAGES` WRITE;
/*!40000 ALTER TABLE `MANAGER_MANAGES` DISABLE KEYS */;
INSERT INTO `MANAGER_MANAGES` VALUES (1,1),(2,2);
/*!40000 ALTER TABLE `MANAGER_MANAGES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `REGIONAL_MANAGER`
--

DROP TABLE IF EXISTS `REGIONAL_MANAGER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `REGIONAL_MANAGER` (
  `username` varchar(250) DEFAULT NULL,
  `password` varchar(250) DEFAULT NULL,
  `phoneNo` varchar(20) DEFAULT NULL,
  `street` varchar(250) DEFAULT NULL,
  `postalCode` varchar(250) DEFAULT NULL,
  `city` varchar(250) DEFAULT NULL,
  `firstName` varchar(250) DEFAULT NULL,
  `lastName` varchar(250) DEFAULT NULL,
  `regionalManagerID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`regionalManagerID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `REGIONAL_MANAGER`
--

LOCK TABLES `REGIONAL_MANAGER` WRITE;
/*!40000 ALTER TABLE `REGIONAL_MANAGER` DISABLE KEYS */;
INSERT INTO `REGIONAL_MANAGER` VALUES ('regManager1','pass5','123-456-7890','5 Maple St','56789','CityG','Clara','Brown',1),('regManager2','pass6','234-567-8901','6 Aspen St','67890','CityH','Dave','Wilson',2);
/*!40000 ALTER TABLE `REGIONAL_MANAGER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `REGIONAL_MANAGER_OVERSEES`
--

DROP TABLE IF EXISTS `REGIONAL_MANAGER_OVERSEES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `REGIONAL_MANAGER_OVERSEES` (
  `regionalManagerID` int(11) NOT NULL,
  `storeID` int(11) NOT NULL,
  PRIMARY KEY (`regionalManagerID`,`storeID`),
  KEY `storeID` (`storeID`),
  CONSTRAINT `REGIONAL_MANAGER_OVERSEES_ibfk_1` FOREIGN KEY (`regionalManagerID`) REFERENCES `REGIONAL_MANAGER` (`regionalManagerID`),
  CONSTRAINT `REGIONAL_MANAGER_OVERSEES_ibfk_2` FOREIGN KEY (`storeID`) REFERENCES `STORE` (`storeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `REGIONAL_MANAGER_OVERSEES`
--

LOCK TABLES `REGIONAL_MANAGER_OVERSEES` WRITE;
/*!40000 ALTER TABLE `REGIONAL_MANAGER_OVERSEES` DISABLE KEYS */;
INSERT INTO `REGIONAL_MANAGER_OVERSEES` VALUES (1,1),(2,2);
/*!40000 ALTER TABLE `REGIONAL_MANAGER_OVERSEES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STORE`
--

DROP TABLE IF EXISTS `STORE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `STORE` (
  `storeName` varchar(250) DEFAULT NULL,
  `phoneNo` varchar(20) DEFAULT NULL,
  `street` varchar(250) DEFAULT NULL,
  `postalCode` varchar(250) DEFAULT NULL,
  `city` varchar(250) DEFAULT NULL,
  `storeID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`storeID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STORE`
--

LOCK TABLES `STORE` WRITE;
/*!40000 ALTER TABLE `STORE` DISABLE KEYS */;
INSERT INTO `STORE` VALUES ('Store A','123-456-7890','123 Main St','12345','CityA',1),('Store B','234-567-8901','234 Oak St','23456','CityB',2);
/*!40000 ALTER TABLE `STORE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inventory` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(255) NOT NULL,
  `supplier_name` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `quantity` int(11) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (1,'Product A','Supplier 1',10.99,100),(2,'Product B','Supplier 2',15.49,50),(3,'Product C','Supplier 1',5.99,200),(4,'Product D','Supplier 3',8.75,75);
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-11 16:53:42
