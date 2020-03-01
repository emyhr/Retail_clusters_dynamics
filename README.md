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

## Building the model
We have a set of customers(receipts) P with elements p<sub>i</sub>, i=1, ..., N, where N - number of customers(receipts). For each p<sub>i</sub>, there is a vector of numbers p<sub>i</sub> = {p<sup>1</sup>, p<sup>1</sup>, p<sup>1</sup>, ..., p<sup>r</sup>}, where r - number of categories(equals 21). Btw, in vector p's coordinates, superscripts don't signify powers but indices (as it is the case in maths sometimes). Values p<sub>i</sub> are the numbers of product items customer purchased from the corresponding category. In this model, euclidean metrics is used for distance calculations.

## Time points
Provided files contained list of receipts of one year. To increase the volume of the sample in a time point, three days were merged into a single time point. The code is [here](https://github.com/emyhr/Retail_clusters_dynamics/blob/master/time_period.ipynb)

## Vector initialisation
1. Consider one receipt. Extract list of product ids;
2. Extract list of product ids of the first category;
3. Count number of product ids of that category contained in the list of product ids in the receipt. Assign the result to the first coordinate of the vector;
4. Repeat step 3 for all of the categories;
5. Repeat the whole process for each receipt.

Code of vector initialisation is given [here](https://github.com/emyhr/Retail_clusters_dynamics/blob/master/init_coord.ipynb)

## Clustering

For clustering, [KMeans](https://en.wikipedia.org/wiki/K-means_clustering) algorithm was used. I think, everyone knows how it works, if someone doesn't, just follow the given link. The implementation code of this and all of the others methods and algorithms used in this work is given in this [module](https://github.com/emyhr/Retail_clusters_dynamics/blob/master/coursework.py).  
Here, it is applied on the sample of one of the time points with k=3.
![kmeans](/img/kmeans.png)
![kmeans_](/img/kmeans_.png)
But the question is how do we know what k to choose? What number of clusters will optimal? [Elbow method](https://en.wikipedia.org/wiki/Elbow_method_(clustering)) is your friend here. Since not so many people know about the Elbow method, let me explain it right here. So, the main idea is to choose such number of clusters, that adding one more cluster will not improve the model. In the Elbow method, different criteria can be used for determining the optimal k. I used two: average distance from points to cluster centroid and variance explained.

### Average distance criterion

First, we need to calculate the distances between each point and the centroid of the cluster the point belongs to. Then, the average of those distance is computed. Now, we plot the graph with the number of clusters k as X-axis and the average distance as Y-axis. Let's plot this graph for the dataset of one day.
![elbow](/img/elbow.png)
At some value of k=k<sub>optimal</sub>, we can see significant drop of the average distance, after which the slope becomes more smooth, uniform. Exactly this values k is considered optimal. In this case, it is k=6. The logic behind is that if we divide the sample into 6 clusters, those clusters will be more closely grouped. However, this value should not be very big or small(one cluster - the biggest avg distance, as many clusters as points - avg distance is 0). 


##1. Data cleaning and preprocessing



[Detailed description of the thesis](https://medium.com/p/3b1aa6f15c8e/edit)
 
