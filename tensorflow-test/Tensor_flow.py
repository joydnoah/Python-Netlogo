import tensorflow as tf

x1 = tf.constant([1,2,3,4])
x2 = tf.constant([3,4,5,6])

result = tf.multiply(x1, x2)

sess = tf.Session()

print(sess.run(result))
sess.close()

