from random import randint


def init_boxs(box_num, win_width, win_height, life_num):
    # 初始化一个方块容器
    life_coordinate = get_life_coordinate(box_num, life_num)
    boxs = []
    for x in range(0, box_num):
        tmp = []
        for y in range(0, box_num):
            if (x, y) in life_coordinate:
                value = 1
            else:
                value = 0
            tmp.append({
                'value': value,
                'x': x * (win_width / box_num),
                'y': y * (win_height / box_num),
                'width': win_width / box_num,
                'height': win_height / box_num
            })
        boxs.append(tmp)
    return boxs


def get_life_coordinate(box_num, life_num):
    ret = []
    for n in range(0, life_num):
        ret.append((randint(0, box_num), randint(0, box_num)))
    return ret


def change_boxs(boxs):
    # 进行一次细胞变换
    # 如果一个细胞周围有3个细胞为生，则将细胞转换为生
    # 如果一个细胞周围有2个细胞为生，则状态保持不变
    # 在其他情况下，细胞都会转为死
    x_len = len(boxs)
    for x, v1 in enumerate(boxs):
        y_len = len(v1)
        for y, v2 in enumerate(v1):
            count = 0
            # 超过上限
            if x == x_len-1 and y == y_len-1:
                if boxs[x-1][y-1]['value'] == 1:
                    count += 1
                if boxs[x-1][y]['value'] == 1:
                    count += 1
                if boxs[x][y-1]['value'] == 1:
                    count += 1
                if boxs[0][y]['value'] == 1:
                    count += 1
                if boxs[0][y]['value'] == 1:
                    count += 1
                if boxs[0][0]['value'] == 1:
                    count += 1
                if boxs[x][0]['value'] == 1:
                    count += 1
                if boxs[x-1][0]['value'] == 1:
                    count += 1
            elif x == x_len-1:
                if boxs[x-1][y-1]['value'] == 1:
                    count += 1
                if boxs[x-1][y]['value'] == 1:
                    count += 1
                if boxs[x-1][y+1]['value'] == 1:
                    count += 1
                if boxs[x][y-1]['value'] == 1:
                    count += 1
                if boxs[x][y+1]['value'] == 1:
                    count += 1
                if boxs[0][y-1]['value'] == 1:
                    count += 1
                if boxs[0][y]['value'] == 1:
                    count += 1
                if boxs[0][y+1]['value'] == 1:
                    count += 1
                pass
            elif y == y_len-1:
                if boxs[x-1][y-1]['value'] == 1:
                    count += 1
                if boxs[x][y-1]['value'] == 1:
                    count += 1
                if boxs[x+1][y-1]['value'] == 1:
                    count += 1
                if boxs[x-1][y]['value'] == 1:
                    count += 1
                if boxs[x+1][y]['value'] == 1:
                    count += 1
                if boxs[x-1][0]['value'] == 1:
                    count += 1
                if boxs[x][0]['value'] == 1:
                    count += 1
                if boxs[x+1][0]['value'] == 1:
                    count += 1
            else:
                if boxs[x-1][y-1]['value'] == 1:
                    count += 1
                if boxs[x-1][y]['value'] == 1:
                    count += 1
                if boxs[x-1][y+1]['value'] == 1:
                    count += 1
                if boxs[x][y-1]['value'] == 1:
                    count += 1
                if boxs[x][y+1]['value'] == 1:
                    count += 1
                if boxs[x+1][y-1]['value'] == 1:
                    count += 1
                if boxs[x+1][y]['value'] == 1:
                    count += 1
                if boxs[x+1][y+1]['value'] == 1:
                    count += 1

            if count == 3:
                boxs[x][y]['value'] = 1
            elif count == 2:
                pass
            else:
                boxs[x][y]['value'] = 0

if __name__ == '__main__':
    boxs = init_boxs(20, 400, 400, 10)
    change_boxs(boxs)

