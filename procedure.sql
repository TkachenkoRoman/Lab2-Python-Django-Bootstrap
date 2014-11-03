use guitar_schema;

delimiter //
DROP PROCEDURE IF EXISTS statistics//
CREATE PROCEDURE statistics()
BEGIN
	CREATE TEMPORARY TABLE IF NOT EXISTS res(
		`id` INT NOT NULL AUTO_INCREMENT,
		`name` VARCHAR(45) NOT NULL,
		`count` TINYINT(1) NOT NULL DEFAULT 0,
		PRIMARY KEY (`id`));
	
	INSERT INTO res(`name`, `count`) VALUES('Guitars', (SELECT COUNT(*) FROM Guitar));
	INSERT INTO res(`name`, `count`) VALUES('Pickups', (SELECT COUNT(*) FROM Pickups));
	INSERT INTO res(`name`, `count`) VALUES('Bridges', (SELECT COUNT(*) FROM Bridge));
	INSERT INTO res(`name`, `count`) VALUES('Bodies', (SELECT COUNT(*) FROM Body));
	INSERT INTO res(`name`, `count`) VALUES('Types', (SELECT COUNT(*) FROM Guitar_types));
	INSERT INTO res(`name`, `count`) VALUES('Produsers', (SELECT COUNT(*) FROM Produser));
	INSERT INTO res(`name`, `count`) VALUES('History', (SELECT COUNT(*) FROM History));

	SELECT * FROM res;
	DROP TABLE res;
END//

delimiter ;

CALL statistics();
