import numpy as np


def generate_cell_data(ncells, ngenes, nclusters, xmus, xsds, ymus, ysds, prop, ref_cols):
    """
    Generate synthetic cell data with clusters.

    Parameters:
        ncells (int): Number of cells.
        ngenes (int): Number of genes.
        nclusters (int): Number of clusters for cell types.
        xmus (list): List of mean values for the x-axis for each category.
        xsds (list): List of standard deviations for the x-axis for each category.
        ymus (list): List of mean values for the y-axis for each category.
        ysds (list): List of standard deviations for the y-axis for each category.
        prop (list): Proportions of each category in the cell population.
        ref_cols (list): List of colors corresponding to each category.

    Returns:
        samples (ndarray): Generated cell data with x and y coordinates.
        clust_cell (list): List of color assignments for each cell based on its category.
    """
    # Generate cell type assignments for each cell based on given proportions.
    comp = np.random.choice(range(1, len(nclusters) + 1), p=prop, size=ncells, replace=True)

    # Generate x and y coordinates for each cell based on the assigned cell type.
    samples = np.column_stack((np.random.normal(loc=np.array(xmus)[comp-1], scale=np.array(xsds)[comp-1], size=ncells),
                               np.random.normal(loc=np.array(ymus)[comp-1], scale=np.array(ysds)[comp-1], size=ncells)))

    # Assign colors to each cell based on its category.
    clust_cell = [ref_cols[i-1] for i in comp]

    return samples, clust_cell



def generate_gene_data(ncells, ngenes, nclusters, xmus, xsds, ymus, ysds, prop, ref_cols):
    """
    Generate synthetic gene data with clusters.

    Parameters:
        ncells (int): Number of cells.
        ngenes (int): Number of genes.
        nclusters (int): Number of clusters for gene types.
        xmus (list): List of mean values for the x-axis for each cluster.
        xsds (list): List of standard deviations for the x-axis for each cluster.
        ymus (list): List of mean values for the y-axis for each cluster.
        ysds (list): List of standard deviations for the y-axis for each cluster.
        prop (list): Proportions of each cluster in the gene population.
        ref_cols (list): List of colors corresponding to each cluster.

    Returns:
        samples (ndarray): Generated gene data with x and y coordinates.
        clust_gene (list): List of color assignments for each gene based on its cluster.
    """
    # Generate gene type assignments for each gene based on given proportions.
    comp = np.random.choice(range(1, len(nclusters) + 1), p=prop, size=ngenes, replace=True)

    # Generate x and y coordinates for each gene based on the assigned gene type.
    samples = np.column_stack((np.random.normal(loc=np.array(xmus)[comp-1], scale=np.array(xsds)[comp-1], size=ngenes),
                               np.random.normal(loc=np.array(ymus)[comp-1], scale=np.array(ysds)[comp-1], size=ngenes)))

    # Assign colors to each gene based on its cluster.
    clust_gene = [ref_cols[i-1] for i in comp]

    return samples, clust_gene
