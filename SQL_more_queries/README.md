SQL - More queries        

Project Overview     
This project has a collection of SQL tasks aimed at enhancing proficiency in MySQL, focusing on advanced queries, database design, and user management. The tasks involve creating and modifying databases and tables, working with privileges, and executing complex queries.     
  
Tasks Description     
Below is a summary of each task included in this project:        

Task 0: My privileges!               
Description: Script to list all privileges of the MySQL users `user_0d_1` and `user_0d_2` on the server.       
File: `0-privileges.sql`           

Task 1: Root user      
Description: Script to create the user `user_0d_1` with all privileges on the MySQL server. The user password is `user_0d_1_pwd`.        
File: `1-create_user.sql`          

Task 2: Read user      
Description: Script to create the database `hbtn_0d_2` and a user `user_0d_2` with only SELECT privileges. The user password is `user_0d_2_pwd`.         
File: `2-create_read_user.sql`       

Task 3: Always a name      
Description: Script to create a table `force_name` with columns `id` (INT) and `name` (VARCHAR(256)), enforcing that `name` cannot be null.      
File: `3-force_name.sql`        

Task 4: ID can't be null      
Description: Script to create a table `id_not_null` where `id` defaults to 1 and cannot be null, and `name` is a VARCHAR(256) column.     
File: `4-never_empty.sql`      

Task 5: Unique ID       
Description: Script to create a table `unique_id` with a unique `id` column that defaults to 1 and a `name` column (VARCHAR(256)).      
File: `5-unique_id.sql`                

Task 6: States table           
Description: Script to create the database `hbtn_0d_usa` and a table `states` with an `id` column as the primary key and a `name` column (VARCHAR(256)).   
File: `6-states.sql`        

Task 7: Cities table        
Description: Script to add a `cities` table to `hbtn_0d_usa` with `id` (primary key), `state_id` (foreign key referencing `states.id`), and `name` columns.   
File: `7-cities.sql`              
  
Task 8: Cities of California           
Description: Script to list all cities of California from the `hbtn_0d_usa` database, ordered by `cities.id`. Only subqueries are used.       
File: `8-cities_of_california_subquery.sql`          
  
Task 9: Cities by States               
Description: Script to list all cities with their corresponding state names, sorted by `cities.id` in ascending order.        
File: `9-cities_by_state_join.sql`                 
     
Task 10: Genre ID by show            
Description: Script to list all TV shows from `hbtn_0d_tvshows` that have at least one genre linked. Outputs include the show titles and genre IDs, sorted by `tv_shows.title` and `tv_show_genres.genre_id`.         
File: `10-genre_id_by_show.sql`             

Task 11: Genre ID for all shows         
Description: Script to list all TV shows, and include genre IDs for those shows that have them. If a show doesn't have a genre, it should still be listed.     
File: `11-genre_id_all_shows.sql`      

Task 12: No Genre     
Description: Script to list all TV shows without any genre assigned to them. The result should show the title of the TV shows, ordered by `tv_shows.title`.    
File: `12-no_genre.sql`      

Task 13: Number of shows by genre           
Description: Script to display the number of TV shows in each genre, ordered by the number of shows in descending order.      
File: `13-count_shows_by_genre.sql`       

Task 14: My genres        
Description: Script to list all genres of shows that a specific user (e.g., "viewer_1") likes. The result should display the genre name, sorted by the genre name.         
File: `14-my_genres.sql`        

Task 15: Only Comedy          
Description: Script to list all shows that fall under the "Comedy" genre, ordered by the title of the TV shows.        
File: `15-comedy_only.sql`          

Task 16: List shows and genres      
Description: Script to display all TV shows along with their genres. If a show has multiple genres, each should be shown on a separate line.     
File: `16-shows_genres_list.sql`        
