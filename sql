CREATE DATABASE `work` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

-- `work`.account definition

CREATE TABLE `account` (
  `userId` int NOT NULL AUTO_INCREMENT,
  `userName` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `userTel` varchar(13) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `pic` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;



-- `work`.telnote definition

CREATE TABLE `telnote` (
  `noteId` int NOT NULL AUTO_INCREMENT,
  `sendName` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `requestName` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sendTel` varchar(13) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `requestTel` varchar(13) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`noteId`)
) ENGINE=InnoDB AUTO_INCREMENT=435 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;




INSERT INTO `work`.account (userName,userTel,pic) VALUES
	 ('たろう','11111111111','http://localhost:8888/work/upload/cc475cb4-e717-4916-9221-ebfa2f4dbfa0.PNG'),
	 ('孫','12345678901','https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png');
   


INSERT INTO `work`.telnote (sendName,requestName,sendTel,requestTel) VALUES
	 ('1','1','1','123'),
	 ('admin','孫','12312341234','12345678901'),
	 ('admin','孫','12312341234','12345678901'),
	 ('admin','孫','12312341234','12345678901'),
	 ('admin','孫','12312341234','12345678901'),
	 ('admin','孫','12312341234','12345678901'),
	 ('admin','たろう','12312341234','11111111111');
   

