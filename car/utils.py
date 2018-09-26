import xlrd #excel读工具
from car.models import Car,CarType,CarBrand,CarSpecialArea,CarImage

# 此方法用于将车辆信息插入数据库中
def import_data(self, request, obj, change):
    data = xlrd.open_workbook(obj.file.path)
    table = data.sheet_by_index(0) #获取工作表
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(0)
    WorkList = []
    x = y = z = 0
    for i in range(1,nrows):
        row = table.row_values(i) #获取每行值
        print (row)
        for j in range(0,ncols):
            if type(row[j]) == float: #如果值为float则转换为int,避免出现1输出为1.0的情况
                row[j] = int(row[j])
        if row[0]!='': #查看行值是否为空,car_brand=row[14]
            if Car.objects.filter(car_name = row[0]).exists():#判断该行值是否在数据库中重复
                print ("1")
                x = x + 1 #重复值计数
            else:
                y = y + 1 #非重复计数
                print ("2")
                car_type1 = CarType.objects.filter(type_name=row[14])[0]
                car_brand1 = CarBrand.objects.filter(barnd_name=row[13])[0]
                car_spec_area1 = CarSpecialArea.objects.filter(spec_area_name=row[15])[0]
                print (car_type1)
                Car.objects.create(car_name=row[0], car_price=row[1], car_body_work=row[2], car_l_w_h=row[3], car_engine=row[4], car_gear_box=row[5],
                                                 car_drive_way=row[6], car_fuel_type=row[7], car_oil_cons=row[8], car_color=row[9], car_href_pic=row[10],
                                                 car_ld_pic=row[11],car_is_active=True, car_type=car_type1,car_brand=car_brand1 ,car_spec_area=car_spec_area1)
        else:
            z = z + 1     #空行值计
    # Car.objects.bulk_create(WorkList)
    print ('数据导入成功,导入'+str(x)+'条,重复'+str(y)+'条,有'+str(z)+'行为空!')
 
def import_images(self, request, obj, change):
    data = xlrd.open_workbook(obj.file.path)
    table = data.sheet_by_index(0) #获取工作表
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(0)
    WorkList = []
    x = y = z = k = 0
    for i in range(1,nrows):
        row = table.row_values(i) #获取每行值
        print (row)
        for j in range(0,ncols):
            if type(row[j]) == float: #如果值为float则转换为int,避免出现1输出为1.0的情况
                row[j] = int(row[j])
        if row[0]!='': #查看行值是否为空,car_brand=row[14]
            # if CarImage.objects.filter(car = row[0]).exists():#判断该行值是否在数据库中重复
                # print ("1")
                # x = x + 1 #重复值计数
            # else:
            # y = y + 1 #非重复计数
            # print ("2")
            # car_type1 = CarType.objects.filter(type_name=row[14])[0]
            # car_brand1 = CarBrand.objects.filter(barnd_name=row[13])[0]
            # car_spec_area1 = CarSpecialArea.objects.filter(spec_area_name=row[15])[0]
            car1 = Car.objects.filter(car_name = row[0])[0]
            # car_image = CarImage.objects.filter(car_name=row[0])
            print (car1)
            for k in range(1,ncols):
                if row[k]:
                    CarImage.objects.create(car_img=row[k],car=car1)
                else:
                    z = z+1
            # Car.objects.create(car_name=row[0], car_price=row[1], car_body_work=row[2], car_l_w_h=row[3], car_engine=row[4], car_gear_box=row[5],
            #                                  car_drive_way=row[6], car_fuel_type=row[7], car_oil_cons=row[8], car_color=row[9], car_href_pic=row[10],
            #                                  car_ld_pic=row[11],car_is_active=True, car_type=car_type1,car_brand=car_brand1 ,car_spec_area=car_spec_area1)
        else:
            z = z + 1     #空行值计
    # Car.objects.bulk_create(WorkList)
    print ('数据导入成功,导入'+str(x)+'条,重复'+str(y)+'条,有'+str(z)+'行为空!' +str(k))


# 此方法用于将车辆外键插入数据库中
def import_data_fro(self, request, obj, change):
    data = xlrd.open_workbook(obj.file.path) #打开文件
    table = data.sheet_by_index(0) #获取工作表
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(0)
    WorkList = []
    x = y = z = 0
    for i in range(1,nrows):
        row = table.row_values(i) #获取每行值
        print (row)
        for j in range(0,ncols):
            if type(row[j]) == float: #如果值为float则转换为int,避免出现1输出为1.0的情况
                row[j] = int(row[j])
        if row[0]!='': #查看行值是否为空
            if CarType.objects.filter(type_name = row[1]).exists():#判断该行值是否在数据库中重复
                x = x + 1 #重复值计数
            else:
                y = y + 1 #非重复计数type_name type_desc
                CarType.objects.create(type_name = row[1])

            if CarBrand.objects.filter(barnd_name = row[0]).exists():#判断该行值是否在数据库中重复
                x = x + 1 #重复值计数
            else:
                y = y + 1 #非重复计数type_name type_desc
                CarBrand.objects.create(barnd_name = row[0])

            if CarSpecialArea.objects.filter(spec_area_name = row[2]).exists():#判断该行值是否在数据库中重复
                x = x + 1 #重复值计数
            else:
                y = y + 1 #非重复计数type_name type_desc
                CarSpecialArea.objects.create(spec_area_name = row[2])
        else:
            z = z + 1     #空行值计数
    # CarType.objects.bulk_create(WorkList)
    print ('数据导入成功,导入'+str(y)+'条,重复'+str(x)+'条,有'+str(z)+'行为空!')
