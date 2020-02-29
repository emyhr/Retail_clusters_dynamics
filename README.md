# Modelling dynamics of retail customer clusters
## Intro

This was my bachelor thesis at Bauman Moscow State Technical University (BMSTU). The idea behind is to clusterise customers and to model their behaviour throughout a given period of time. The data used in this project was provided to the department by a Russian network of grocery shops. 

Source files: 15 csv-files containing anonimised receipts of customers. Each of the files had around 1 million rows.
## Data preparation
### Data cleaning
Excerpt from one of the files  
![receipt](/img/receipt_example.png)

Columns:
- shop id;
- receipt date; 
- receipt id;
- product id;
- product name;
- quantity;
- price;

The table looks fine and seems like no data cleaning is needed. However, if values are printed, the opposite is evident.
![whitespaces](/img/whitespaces.png)
![whitespaces2](/img/whitespaces2.png)

The notebook which contains data cleaning part is [here](https://github.com/emyhr/Retail_clusters_dynamics/blob/master/file_refiner.ipynb)  
After cleaning the data file sizes decreased 1.5 times.
|File|Size before cleaning(kb)|Size after cleaning(kb)|  
|:---:|:---:|:---:|
|1|1 005 926|630 639| 
|2|1 239 462|787 221|  
|3|594 244|375 117|  
|4|1 920 671|1 218 908|  
|5|383 151|240 953|
|6|681 931|434 843|  
|7|636 644|409 472|  
|8|452 536|285 073|  
|9|852 451|538 738|  
|10|890 994|562 112|  
|11|847 766|536 733|  
|12|1 522 345|972 821|  
|13|502 756|319 804|  
|14|2 061 362|1 315 503|  
|15|1 840 329|1 175 503|

### Splitting products into sections
Next step, is splitting products into sections(categories). The following categories have been chosen:
- alcohol;
- pet products;
- bakery;
- non-alcoholic beverages;
- cheese and sausages;
- tobacco;
- condiments;
- confectionery;
- semi-finished products;
- seafood;
- frozen products;
- fruits and vegetables;
- groceries;
- household;
- products for children;
- dairy products;
- meat;
- salads;
- snacks;
- detergents;
- others;

For sorting, I used 're' Python library. The algorithm is the following:
1. For each section, two lists were created: one contained keywords of the category, another one contained keywords that definitely didn't belong to the category;
2. Product name and product id are read;
3. Product name is tested for containment of keywords from the first list and for absence of values from the second list;
4. If the previous condition is satisfied, the product id is written to the file of that category.
The code can be found [here](https://github.com/emyhr/Retail_clusters_dynamics/blob/master/sorting_products.ipynb)

|Category|Number of products|
|:---:|:---:|
|alcohol|1495|
|pet products|141|
|bakery|828|
|non-alcoholic beverages|1430|
|cheese and sausages|363|
|tobacco|128|
|condiments|412|
|confectionery|1193|
|semi-finished products|223|
|seafood|273|
|frozen products|204|
|fruits and vegetables|722|
|groceries|454|
|household|252|
|products for children|92|
|meat|308|
|dairy products|1297|
|salads|2820|
|snacks|189|
|detergents|642|
|others|204|

##Building the model


##Phases of work:

1. Data cleaning and preprocessing;

2. Sorting products into categories;
3. Initialising coordinates for each receipt;
4. Clustering;
5. Visualisation;

##1. Data cleaning and preprocessing



[Detailed description of the thesis](https://medium.com/p/3b1aa6f15c8e/edit)
 
