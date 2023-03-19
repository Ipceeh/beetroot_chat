BEGIN TRANSACTION;

INSERT INTO auth_user VALUES(1,'pbkdf2_sha256$390000$OhiOH6SUafmD5fP7lTFcjB$hMh8PEU+CRoxw7MA+jW1lVT5HcayyyZQMuQ3WfTEbtc=','2023-03-19 09:34:32.806851',True,'admin','','admin@admin.com',True,True,'2023-03-19 09:33:31.612196','');
INSERT INTO auth_user VALUES(2,'pbkdf2_sha256$390000$WauTvvu5Y33orVMLZDryjj$hFcN9o8myvdYPhq9aw7X2200GrZPxq0JTdm1cf7+bqs=',NULL,False,'Oksana','','',False,True,'2023-03-19 10:42:59.745420','');

INSERT INTO django_admin_log VALUES(1,'1251840b-b3ca-4104-9e14-ad1b27b84d55','Message object (1251840b-b3ca-4104-9e14-ad1b27b84d55)',1,'[{"added": {}}]',7,1,'2023-03-19 10:06:38.576787');
INSERT INTO django_admin_log VALUES(2,'14888b4f-6cca-4303-9a31-15949a97e704','admin                : Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ul',1,'[{"added": {}}]',7,1,'2023-03-19 10:12:52.847707');
INSERT INTO django_admin_log VALUES(3,'f427a931-06c9-4340-b8e1-580fdefd3d28','admin : Hi!',1,'[{"added": {}}]',7,1,'2023-03-19 10:34:16.948174');
INSERT INTO django_admin_log VALUES(4,'2','Oksana',1,'[{"added": {}}]',4,1,'2023-03-19 10:43:00.129950');
INSERT INTO django_admin_log VALUES(5,'8c094049-08e7-4aa1-b4d3-b03f2944f6b2','Oksana : Hi, I''m Oksana!',1,'[{"added": {}}]',7,1,'2023-03-19 10:44:24.353547');


INSERT INTO django_session VALUES('vc7bncf3uk5060zr4ahv5ghqtnr1ka7j','.eJxVjDsOwjAQBe_iGln-JbYp6TmDtetd4wBypDipEHeHSCmgfTPzXiLBtta0dV7SROIstDj9bgj5wW0HdId2m2We27pMKHdFHrTL60z8vBzu30GFXr91jAqNdzYH4xGhoIpjMTZiIT1EPTrlQWmvCRjRGNYGAB3RQByCZSveH9x3OB8:1pdpQu:znwIUFfNHGkwCsIJH7fdWlRF1gQer8KyKTUVZn0QnM8','2023-04-02 09:34:32.816795');

INSERT INTO chat_message VALUES('2023-03-19 10:06:03','1251840bb3ca41049e14ad1b27b84d55','Hello, everybody!',1);
INSERT INTO chat_message VALUES('2023-03-19 10:11:37','14888b4f6cca43039a3115949a97e704','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',1);
INSERT INTO chat_message VALUES('2023-03-19 10:34:06','f427a93106c94340b8e1580fdefd3d28','Hi!',1);
INSERT INTO chat_message VALUES('2023-03-19 10:44:12','8c09404908e74aa1b4d3b03f2944f6b2','Hi, I''m Oksana!',2);

COMMIT;
