import exrex
names = ['ZHANGSAN','Zhangsan','zhangsan','Zhangsan','Zhangs','ZS','zs','Zsan','zsan','zSan']
birthday = ['19880210','1988210','880210','88210','0210','210']
for name in names:
	for birth in birthday:
		dics = list(exrex.generate('(|{name})(|[!@$&*#.])(|[!@#$&*])( |{birth})'.format(name=name,birth=birth)))
		for dic in dics:
			if len(dic) >= 6:
				f_dic = open('D:\\namedic.txt','a')
				f_dic.write(dic+'\n')
				f_dic.close()
