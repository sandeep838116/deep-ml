import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    # Your code here
    probabilities =[]

    for feature_vec in features:
        a = sum(f *w for f,w in zip(feature_vec,weights))+ bias
        a = 1/(1+math.exp(-a))
        probabilities.append(round(a,4))

    mse = sum((prob - labels)**2 for prob,labels in zip(probabilities,labels))/len(labels)
    
    return probabilities, round(mse,4)