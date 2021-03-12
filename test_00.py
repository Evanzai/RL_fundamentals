import tensorflow as tf 

a = tf.constant([1,2])
b = tf.constant([3,4])

c = a+b

d = a * b

print(c)
print(tf.config.list_physical_devices('GPU'))

print(d)