import numpy
import datetime
import random

# generator for looping through time periods
def daterange(start_date, end_date):
    """
    Generator for looping through time periods
    """
    if start_date < end_date:
        for day in range((end_date - start_date).days):
            yield start_date + datetime.timedelta(day)
    else:
        print('start_date exceeds end_date')


# Means by coordinates
def Mean(a):
    """
    Return means by coordinates
    """
    sums = numpy.zeros(len(a[0]))
    for i in a:
        sums += i
    mean = sums / len(a)
    return mean


# Variance
def var(a,b):
    return (a-b)**2


# Principal Component Analysis
def pca(matrix, n):
    """
    Implementation of the Principal Component Analysis.
    Reduces number of dimensions of the dataset.
    matrix: dataset
    n: number of dimensions to keep
    """
    
    means = numpy.mean(matrix, axis=0) # means of matrix
    stds = numpy.std(matrix, axis=0) # standard deviation of matrix
    
    s_matrix = (matrix - means) # centred matrix
    cov = numpy.cov(s_matrix, rowvar=False) # covariation matrix of centred matrix
    
    evals, evecs = numpy.linalg.eig(cov) # eig vals
    fvec = evecs.T[0:n] # feature vector
    
    result = numpy.dot(fvec, s_matrix.T)
    
    return result.T


#distance between two points 
def distance(a, b):
	if (len(a) != len(b)):
		print('error!')
		print(a)
		print(b)
	a = numpy.array(a)
	b = numpy.array(b)
	dist = numpy.sqrt(sum((a-b)**2))
	return dist


#returns random element of container
def rand_element(data_list, k):
	cent_idx = random.sample(range(0, len(data_list)), k)
	data_list = numpy.array(data_list)
	return data_list[cent_idx]


# new the right kmeans method
def new_kmeans(sample, k):
    
    epsilon = 0.001 # accuracy
    centres_dist = 1 # distance between new and old centres
    centres = list(rand_element(sample, k)) # choosing first random centres
    counter = 0
    
    # keep clustering until the distance between centre's 
    # current and previous positions < epsilon
    while centres_dist > epsilon:

        clusters = []
        for i in range(k):
            clusters.append([]) # creating a cell for each cluster

        distances = []
        # calculating the distance between point and each cluster
        for point in sample:
            distances.append([distance(point, centre) for centre in centres])
        
        # putting point into the cluster with the nearest centre
        for idx in range(len(distances)):
            clusters[numpy.argmin(distances[idx])].append(sample[idx])
        

        old_centres = centres.copy() # store current position of centres
        centres.clear()
        for i in range(k):
            if not clusters[i]:
                centres.append(old_centres[i]) # if some centre is farther than 
                                               # others from all points, we keep it  
            else:
                centres.append(sum(numpy.array(clusters[i])) / len(clusters[i])) # recalculating new centre
                
        centres_dist = 0
        # sum up the distances between centres' current and previous positions
        centres_dist = sum([distance(centres[i], old_centres[i]) for i in range(k)])
            
        counter += 1
        print(f'\r{counter}', end='')
        
    return (clusters, centres)


#elbow method
def elbow(ds, n, mode='distance'):
    """
    Implementation of the elbow method.
    Used to define k in KMeans clustering.
    Parameters:
    ds: dataset.
    n: top limit for k (number of clusters),
    mode: 'distance', 'variance'
    """
    
    if mode == 'distance':
        
        sums = numpy.zeros(n) # average distance between the cluster centre 
                              #  and the element of the cluster
            
        for k in range(1, n+1):
            clusters, centres = new_kmeans(ds, k)
            for i in range(k):
                sums[k-1] += sum(list(map(lambda x: distance(centres[i], x), clusters[i])))        

        return sums / len(ds)
    
    elif mode == 'variance':
        
        gm = Mean(numpy.array(ds)) #grand mean
        SST = sum([(numpy.array(x) - numpy.array(gm))**2 for x in ds]) # sum of squares total (21 of them)
        SSB = 0 # sum of squares between groups
        SSB_list = [] # variance explained

        # for all k in [1, n]
        for k in range(1, n+1):
            clusters, centres = new_kmeans(ds, k)
            SSB = 0
            for i in range(k):
                cm = Mean(clusters[i]) # mean of cluster
                n = len(clusters[i]) # number of elements in cluster
                SSB += n * (cm - gm)**2 # calculating SSB
            SSB_list.append(SSB)
        
        variance = numpy.array(SSB_list) / numpy.array(SST)
        var_avr = Mean(variance.T)
        
        return var_avr
    
    else: raise ValueError('no such mode')


def Silhouette(sample, k, mode=None):
    """
    Implementation of Silhouette
    """
    
    if k < 2:
        raise ValueError('k cannot be less than 2')
    
    clusters, centres = new_kmeans(sample, k) 
    
    a = []
    for i in range(k):
        a.append([])
        
    b = []
    for i in range(k):
        b.append([])
        
    s = []
        
    for idx, clust in enumerate(clusters):
        
        for point_i in clust:
            a[idx].append(sum([distance(point_i, point_j) for point_j in clust]) / (len(clust)-1))
        
            clusters_ = clusters.copy()
            clusters_.remove(clust)
            b[idx].append(min([sum([distance(point_i, point_j) for point_j in clust_]) / len(clust_) for clust_ in clusters_]))
                
        s.append((numpy.array(b[idx])-numpy.array(a[idx])) / max(b[idx], a[idx]))
    
    if mode == 'average':
        s_list = []
        for elem in s:
            s_list += list(elem)
    else:
        s_list = list(s)
        
    return s_list
