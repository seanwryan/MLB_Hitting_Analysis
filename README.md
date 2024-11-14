# MLB Project: Diamondbacks Player Analysis

## Project Overview
This project analyzes MLB hitters to identify player archetypes, key performance metrics, and standout players, with a specific focus on the Arizona Diamondbacks' roster. Using data-driven clustering methods, we categorize players into archetypes (e.g., Balanced Hitter, Contact Hitter, Power Hitter) and assess key attributes like on-base percentage (OBP), slugging percentage (SLG), and speed metrics to inform player evaluation and decision-making.

The project is built upon MLB hitting data, enriched with feature engineering, and visualized to highlight insights pertinent to player performance and team building. Future plans include extending this analysis to pitching data, which has been cleaned and pre-processed but not yet analyzed in depth.

## Key Steps and Structure

1. **Data Cleaning**: 
   - Initial cleaning was performed on hitting and pitching datasets to address missing values, standardize player names, and prepare the data for analysis.

2. **Feature Engineering**: 
   - Calculated additional metrics, such as isolated power (ISO), extra-base hit percentage (XBH%), and walk-to-strikeout ratio (BB/SO), to enhance the predictive power of clustering models.

3. **Clustering Analysis**: 
   - Applied k-means clustering to categorize players into archetypes based on refined features. The optimal number of clusters was determined using the Elbow Method and Silhouette Score.

4. **Visualization**: 
   - Created a series of visualizations to highlight the distribution of hitter types, performance comparison, and Diamondbacks-specific player insights. These visualizations assist in identifying key players and archetypes within the Diamondbacks roster.

5. **Extending to Pitching Data (Planned)**: 
   - The process will be replicated on the pitching dataset, utilizing similar clustering techniques to categorize pitcher archetypes and evaluate key metrics such as ERA, WHIP, and strikeout rate.

## Project Directory
The project is structured as follows:

- `data/`: Contains raw and processed data files, organized by hitting and pitching.
- `scripts/`: Organized into `clustering`, `data_processing`, and `visuals` directories for clustering models, data cleaning, and visualization generation.
- `figures/`: Stores visual outputs, with `archive` for older versions and `visuals` for final images used in reporting.

## Relevant Techniques and Data Engineering Considerations
To align with data engineering practices and support reproducibility, this project incorporates:

- **Automated Data Processing Pipelines**: 
   - Scripts are modularized and can be scheduled to run sequentially for streamlined updates to processed datasets. A future implementation could involve setting up scheduled ETL (Extract, Transform, Load) processes to update datasets regularly.

- **Scalable Data Transformation**: 
   - Feature engineering methods were applied to enhance analysis, and similar approaches will be extended to pitching data, enabling scalable analysis across multiple player types.

- **Efficient Data Storage and Retrieval**: 
   - Processed datasets and intermediate files are organized within structured folders, allowing easy access and adaptability to new data sources. The project can be adapted for integration with a cloud-based data storage solution, like AWS S3, for scalable data access.

- **Version Control and Archiving**: 
   - Visuals and data files are archived, enabling tracking of changes over time and maintaining previous versions for analysis comparison.

## Tools and Libraries Used

- **Python**: Primary programming language for data processing and analysis.
- **pandas, scikit-learn**: For data manipulation and clustering.
- **matplotlib, seaborn**: For visualization.
- **Git and GitHub**: For version control and project management.

## Future Directions

- **Expansion to Pitching Data**: 
   - In addition to hitters, we will apply clustering and performance analysis techniques on the pitching dataset. This extension will provide a comprehensive view of the team’s roster.

- **Enhanced Data Pipelines**: 
   - Integrating data engineering best practices, such as automated data pipelines and scalable cloud storage, to support the Diamondbacks’ data analysis and decision-making needs.

- **Advanced Model Integration**: 
   - Future iterations could incorporate predictive models to assess player performance trajectories, tailored to meet the analytical needs of MLB teams.

## Citations

- **ChatGPT-4 (OpenAI)**: Used for drafting, code assistance, and project structuring.
- **Baseball-Reference**: MLB data source for player statistics.
