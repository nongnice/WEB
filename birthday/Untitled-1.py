CREATE TABLE "friends" 
("id" INTEGER NOT NULL,
  "first_name" TEXT NOT NULL, 
  "last_name" TEXT NOT NULL, PRIMARY KEY("id"));

INSERT INTO friends (first_name,last_name) VALUES ("Carter","Zenke")



create table 'songs'
('id' integer not null,
 'name' text not null,
 'tempo' integer not null,
 'duration' integer not null,
 'artist_id' integer not null);

insert into songs (id,name,tempo,duration,artist_id) values (1,'something comforting',144,282,23);
insert into songs (id,name,tempo,duration,artist_id) values (2,'Drive',142,196,45);

create table 'artists'
('id' integer not nu
 'name' text not null,
 'birthyear' integer not null,
 'label' text not null);

insert into artists (id,name,birthyear,label) values (23,'porter robinson',1992,'mom+pop');
insert into artists (id,name,birthyear,label) values (45,'oh wonder',1990,'republic');

