#input - mga data nimo or mga relevant features sa imong dataset nga maka affect sa imong target output or i-predict
inputs = [1, 2, 3, 2.5] #features or data that help us come up with a result


#weights are values related to the input could be an intensity of how much likely relevant or can affect the output 
#weights - mga value nga makatabang sa imong input kung unsa sya karelevant sa mahimong output nga imo ipredict
#from the word itself unsa sya kabug-at or karelevant sa imong input para maka-come up sa imong desired believable output
weights1 = [0.2,0.8,-0.5, 1.0]
weights2 = [0.5,-0.91,0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

#bias - gamit para pang shift sa sigmoid activation function towards left or right
#kay kung i-plot man gali nato ang function same raman ang center sa function if dili nato i-increas ang bias or b
# source : https://towardsdatascience.com/whats-the-role-of-weights-and-bias-in-a-neural-network-4cf7e9888a0f
bias1 = 2
bias2 = 3
bias3 = 0.5

output = [inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] +bias1,
		  inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] +bias2,	  
		  inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] +bias3]

print(output)