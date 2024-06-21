# README

## Gestão Verde - Park and Garden Management System

This project aims to develop a management system for Gestão Verde, a company that manages various parks and gardens. The system allows the registration of information about plants, species, and parks to optimize management practices and make the spaces greener and more efficient.

### Features

1. **Plant Species (Class `Species`)**
    - Attributes:
        - `name`: Name of the species.
        - `foliage_type`: Type of foliage (persistent, deciduous, or semi-deciduous).
        - `produces_fruit`: Indicates if the species produces fruit (True/False).
        - `plant_type`: Type of plant (tree or shrub).
        - `max_radius`: Maximum radius occupied by a plant of this species (in meters).
        - `average_lifespan`: Average lifespan of a plant of this species (in years).
    - Functionalities:
        - Retrieve any attribute.
        - Calculate the area occupied by a plant of this species (in square meters).
        - Convert a species to a string to display its details.
        - Compare species using the `==` operator (species are equal if their names are the same).

2. **Plants (Class `Plant`)**
    - Attributes:
        - `species`: The species of the plant (an object of type `Species`).
        - `location`: GPS location of the plant (a pair of decimal values).
        - `plantation_year`: Year the plant was planted (a positive integer).
    - Functionalities:
        - Retrieve any attribute.
        - Calculate the area occupied by the plant based on its species.
        - Calculate the age of the plant in a given year.
        - Determine if a given location falls within the area occupied by the plant.
        - Convert a plant to a string to display its details.

3. **Parks (Class `Park`)**
    - Attributes:
        - `name`: Name of the park.
        - `plantation_area`: Plantation area of the park (width and length in meters).
        - `plants`: A list of plants in the park.
    - Functionalities:
        - Add plants to the park (ensure no plants are added in already occupied locations).
        - Remove a plant from the park given its GPS location.
        - Check if there is a plant at a given GPS location.
        - Calculate the total occupied area.
        - Calculate the available plantation area.
        - Check if there is space for a given plant in the park.
        - Calculate the average age of the plants in a given year.
        - Count the number of different species.
        - List all species in the park (no duplicates).
        - Display existing plants ordered by species.
        - Display existing plants ordered by year of plantation.
        - List plants whose age is equal to or greater than the average lifespan of their species.

4. **File Management**
    - Load species from a file:
        - File format: `species_name,foliage_type,produces_fruit,plant_type,max_radius,average_lifespan`
        - Example:
          ```
          castanheiro,caduca,True,tree,8.1,100
          cedro,persistent,False,tree,1.5,80
          pinheiro manso,persistent,True,tree,3.1,100
          loureiro,persistent,False,shrub,3.0,40
          ```
    - Save park information to a file:
        - File format:
          ```
          park_name,plantation_area
          species_name,plant_location,plantation_year
          ```

5. **Park Management Menu**
    - Options:
        1. Add plant
        2. Remove plant
        3. List existing plants
        4. Show occupied area
        5. Show available plantation area
        6. Show park map
        7. Statistics and information
        8. Save park to file
        9. Exit

6. **Statistics and Information Menu**
    - Options:
        - Show average age of plants in the park.
        - Show the number of different species.
        - List existing species in the park.
        - List all plants organized by species.
        - List all plants organized by year of plantation.
        - List plants that have exceeded the average lifespan of their species.
        - Histogram of plant ages.
        - Histogram of plants by species.

### Graphical Representation
- Generate histograms based on plant ages and species for better visualization.

### Installation and Usage

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Run the system:**
    ```bash
    python main.py
    ```

3. **Follow the menu instructions to manage parks and plants.**

### Contribution
- Contributions are welcome! Please fork the repository and create a pull request with your changes.

### Contact
- For any inquiries, please contact [danilosmussa@gmail.com].
