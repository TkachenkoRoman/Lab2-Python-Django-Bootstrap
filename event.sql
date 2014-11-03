use guitar_schema;
delimiter //

DROP EVENT IF EXISTS account//
CREATE EVENT account
    ON SCHEDULE EVERY 5 SECOND
    DO
      BEGIN
        INSERT INTO `guitar_schema`.`Accounting`(`date`, `Guitars`, `Pickups`, `Bridges`, `Bodies`, `Types`, `Produsers`, `History`)
		VALUES(NOW(),
			  (SELECT COUNT(*) FROM Guitar),
			  (SELECT COUNT(*) FROM Pickups),
			  (SELECT COUNT(*) FROM Bridge),
			  (SELECT COUNT(*) FROM Body),
			  (SELECT COUNT(*) FROM Guitar_types),
			  (SELECT COUNT(*) FROM Produser),
			  (SELECT COUNT(*) FROM History));
      END //

delimiter ;

SELECT * FROM Accounting;
SHOW EVENTS;
INSERT INTO Accounting(`date`, `Guitars`, `Pickups`, `Bridges`, `Bodies`, `Types`, `Produsers`, `History`)
		VALUES(NOW(),
			  (SELECT COUNT(*) FROM Guitar),
			  (SELECT COUNT(*) FROM Pickups),
			  (SELECT COUNT(*) FROM Bridge),
			  (SELECT COUNT(*) FROM Body),
			  (SELECT COUNT(*) FROM Guitar_types),
			  (SELECT COUNT(*) FROM Produser),
			  (SELECT COUNT(*) FROM History));