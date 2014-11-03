START TRANSACTION;
	INSERT INTO `guitar_schema`.`guitar` (`name`) VALUES ('test');
	select * from guitar;
COMMIT;