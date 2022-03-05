# Author: Abo
# Date: 2022/3/4 12:47


def get_target_count(blog):
    old_len = len(blog)
    new_len = len(blog.replace('#', ''))
    return old_len - new_len


def get_super_topic(target_blog):
    count = get_target_count(target_blog)
    if count < 2:
        return None

    topic_lst = []
    while True:
        if get_target_count(target_blog) >= 2:
            topic_lst.append(target_blog[target_blog.index('#') + 1:target_blog.index('#', target_blog.index('#') + 1)])
            target_blog = target_blog[target_blog.index('#', target_blog.index('#') + 1) + 1:]
        else:
            break
    for item in topic_lst:
        if item.isspace() or item == '':
            topic_lst.remove(item)

    return topic_lst


# blog = 'asdasd#话题一#ggggasdewee#话题二#aaaaggge##gggaa#话题三#gasdf#话题四#Sghjssdss'
if __name__ == '__main__':
    while True:
        blog = input('请将微博文本复制至此处：' + '\n')
        res_list = get_super_topic(blog)
        if not res_list or len(res_list) == 0:
            print('该微博不存在超话')
        else:
            res = '\n'.join(res_list)
            print(f'该微博存在的超话有：\n{res}')

        answer = input('输入任意内容即可退出程序')
        if True:
            break
