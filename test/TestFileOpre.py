import os
import shutil




def delDir(dir):
    for parent, dirnames, filenames in os.walk(dir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        if filenames.__len__() < 1 and dirnames.__len__() < 1:
            if os.path.isdir:
                print("删除目录：" + dir)
                os.rmdir(dir)
        else:
            for dirname in dirnames:
                delDir(parent +os.sep + dirname)
if __name__ == '__main__':
    rootdir = "F:\image\煎蛋"  # 指明被遍历的文件夹
    # delDir(rootdir)
    # print(os.path.isdir(rootdir))

    for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

        for dirname in dirnames:  # 输出文件夹信息
            # print("parent is：" + parent)
            # print("dirname is：" + dirname)
            continue
        parents = parent.split('\\')
        parent1 = parents[len(parents) - 1]  #
        for filename in filenames:  # 输出文件信息
            if len(str(parent1)) == 5:

                # print("filename：%s" % (filename))
                # dir_name = filename[0: 1]
                goal_dir = parent[:len(parent) - 5] + parent1[:4]
                if not os.path.exists(goal_dir):
                    os.makedirs(goal_dir)
                print("move : %s to %s" % (parent + os.sep +filename, goal_dir + os.sep + filename))
                shutil.move(parent + os.sep +filename, goal_dir + os.sep + filename)