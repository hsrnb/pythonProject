def get_predict(pil_im, model):
    #对图片进行缩放
    pil_im = pil_im.resize(200,200)
    #将格式转为numpy array 格式
    array_im = np_asarray(pil_im)
    #对图片进行预测
    result = model.predict([[array_im]])
    if result[0][0] > 0.5:
        print("预测结果是：狗")
    else:
        print("预测结果是：猫")