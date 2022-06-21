
CREATE TABLE `zz_rec_receiving_fruits` (
  `Receive_ID` int NOT NULL AUTO_INCREMENT,
  `Peak_year` int DEFAULT NULL,
  `ReceiveDate` date NOT NULL,
  `Grower_ID` int NOT NULL,
  `Rec_Delivey_Num` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `PlotName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `FruitType` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `DealName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `Pack_Type` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Pack_Qty` int NOT NULL,
  `TotalWeight_Bruto` decimal(18,2) NOT NULL,
  `Create_Date` date NOT NULL DEFAULT (curdate()),
  `Create_Time` time DEFAULT (curtime()),
  PRIMARY KEY (`Receive_ID`)
) 