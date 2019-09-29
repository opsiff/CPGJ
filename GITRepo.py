
import git
import re
import os
import shutil
import win32api
import stat
def rmdirs(path):
    print(path)
    for filename in os.listdir(path):
        if os.path.isdir(filename):
            rmdirs(path+'/'+filename)
            os.rmdir(path+'/'+filename)
        else:
            os.remove(path+'/'+filename)
    os.remove(path)


def rm_read_only(fn, tmp, info):
    if os.path.isfile(tmp):
        os.chmod(tmp, stat.S_IWRITE)
        os.remove(tmp)
    elif os.path.isdir(tmp):
        os.chmod(tmp, stat.S_IWRITE)
        shutil.rmtree(tmp)

def find_Id(path):
    try:
        dir_list = []
        file_list = os.listdir(path)
        for filename in file_list:
            if os.path.isdir(filename):
                dir_list.append(path + '/' + filename)
            else:
                if re.findall(r'\d{9}',filename):
                    id=re.findall(r'\d{9}',filename)[0]
                    return id
        for dir in dir_list:
            id = find_Id(dir)
            if str != '':
                return id
        return id

    except Exception as e:
        print('找学号出错?', e)
    return ''

def git_clone(url,cl,path='./evaluation/'):
    try:
        if not os.path.exists(path[:-1]):
            os.mkdir(path[:-1])

        Repo_id = url.split('/')[-1]
        print('仓库id:',Repo_id)
        if os.path.exists(path+Repo_id):
            try:
                shutil.rmtree(path+Repo_id, onerror=rm_read_only)
            except Exception as e:
               print(e)
        path=path+Repo_id #更新文件夹
        os.mkdir(path)
        try:
            cl.printText('git clone Repo ... '+url)
            clone=git.Repo.clone_from(url,path)
            id=find_Id(path)
            return 'clone done',id,Repo_id
        except Exception as e:
            print(e)
            return e,''
    except Exception as e:
        print(e)
        return e, ''

if __name__=='__main__':
    git_clone(url='https://github.com/CerberusX/031701129')







