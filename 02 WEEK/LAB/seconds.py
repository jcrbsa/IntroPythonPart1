secons_input = int(input("Por favor, entre com o número de segundos que deseja converter:"))

day = secons_input // 86400
rest_day = secons_input % 86400
hour = rest_day // 3600
rest_hour = rest_day % 3600
minute = rest_hour // 60
rest_minute = rest_hour % 60
seconds = rest_minute


print (day , "dias," , hour  , "horas," , minute , "minutos e" , seconds , "segundos.")

 
