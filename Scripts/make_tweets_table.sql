USE Twitter;

create table Tweets
(
	id_num MEDIUMINT NOT NULL AUTO_INCREMENT,
    tweet VARCHAR(300) UNIQUE,
    PRIMARY KEY (id_num)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;
;

