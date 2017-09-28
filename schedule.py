import random

# randint(a, b) : a <= N <= b
# for i in range(10):
# 	print random.randint(4, 7)
def check_null(name_dict):
	if len(name_dict) == 0:
		return True
	else:
		return False

def check_full(topic_id, topic_dict):
	if topic_id == 4:
		if len(topic_dict[topic_id]) == 3:
			return True
	elif topic_id == 5:
		if len(topic_dict[topic_id]) == 6:
			return True
	elif topic_id == 6:
		if len(topic_dict[topic_id]) == 3:
			return True
	elif topic_id == 7:
		if len(topic_dict[topic_id]) == 6:
			return True
	else:
		return False

def check_name_not_repeated(topic_dict, topic_id, name):
	if name in topic_dict[topic_id]:
		return False
	else:
		return True

def pick_a_topic(topic_dict):
	topic_id = random.randint(4, 7)
	while check_full(topic_id, topic_dict):
		topic_id = random.randint(4, 7)
	return topic_id

def pick_a_name(name_dict, topic_dict, topic_id):
	
	length = len(name_dict)
	idx = random.randint(0, length - 1)
	# print 'idx', idx

	name = list(name_dict.iterkeys())[idx]

	while check_name_not_repeated(topic_dict, topic_id, name) is not True:
		idx = random.randint(0, length - 1)
		# print 'idx', idx
		name = list(name_dict.iterkeys())[idx]
	
	name_dict[name] -= 1
	if name_dict[name] == 0:
		del name_dict[name]
	return name

def generate_topic_dict(name_dict, topic_dict):

	while check_null(name_dict) is not True:
		# print 'in generate_topic_dict while...'
		topic_id = pick_a_topic(topic_dict)
		name = pick_a_name(name_dict, topic_dict, topic_id)
		topic_dict[topic_id] += [name]

	return topic_dict

if __name__ == '__main__':

	name_strs = ['Bai', 'Li', 'Ma', 'Wu', 'Tian', 'Gong', 'Hou', 'Chen', 'Bao', 'Wangyy', 'Hu', 'Zhao', 'Wanghw', 'Zhang']
	name_count_2 = ['Li', 'Ma', 'Zhang', 'Chen']
	
	topic_name = {4:{}, 5:{}, 6:{}, 7:{}}
	for topic in range(4, 8):
		for name in name_strs:
			topic_name[topic][name] = 0

	for i in range(1):
		name_dict = {}
		
		# initialize
		for name in name_strs:
			if name in name_count_2:
				name_dict[name] = 2
			else:
				name_dict[name] = 1

		topic_dict = {4:[], 5:[], 6:[], 7:[]}

		topic_dict = generate_topic_dict(name_dict, topic_dict)
		
		print topic_dict
		for topic, names in topic_dict.iteritems():
			for name in names:
				topic_name[topic][name] += 1

		print topic_name

	