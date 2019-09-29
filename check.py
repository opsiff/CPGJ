
import os
import json
import shutil
import sys
import chgPy

def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def findPy(id,path):
    # 先找到id.py文件
    try:
        dir_list=[]
        file_list=os.listdir(path)
        for filename in file_list:
            if os.path.isdir(filename):
                dir_list.append(path+'/'+filename)
            else:
                if filename==id+'.py':
                    return path+'/'+filename,path
        for dir in dir_list:
            str=findPy(id,dir)
            if str!='':
                return str,dir
        return '',path

    except Exception as e:
        print('check.py',e)

def correct(outTxt,answerTxt,cl):
    sum=0
    try:
        try:
            with open(outTxt,'r',encoding='utf-8') as f:
                outss=f.readlines()
            outs=[]
            for line in outss:
                print(line)
                line=line.replace('\n','',10)
                line=line.replace('\'','"',100)
                outs.append(json.loads(line,encoding='utf-8'))
        except Exception as e:
            print('读入output出错',e)
        try:
            with open(answerTxt,'r',encoding='utf-8') as f:
                answser=f.readlines()
            ans=[]
            for line in answser:
                line=line.replace('\n','',10)
                ans.append(json.loads(line))
        except Exception as e:
            print('读ans出错',e)
        for i in range(len(ans)):
            out=outs[i]
            an=ans[i]
            print('Your Out:',out)
            try:
                if out["姓名"]==an["姓名"]:
                    sum+=0.2
                else:
                    print('第{0}条数据,可能出错 错误提示:'.format(i))
            except Exception as e:
                print('第{0}条数据,可能出错 错误提示:'.format(i),e)
            try:
                if out["手机"] == an["手机"]:
                    sum += 0.2
                else:
                    print('第{0}条数据,可能出错 错误提示:'.format(i))
            except Exception as e:
               print('第{0}条数据,可能出错 错误提示'.format(i),e)
            try:
                if out["地址"]==an["地址"]:
                    sum+=0.6
                else:
                    print('第{0}条数据,可能出错 错误提示:'.format(i))
            except Exception as e:
                 print('第{0}条数据,可能出错 错误提示'.format(i),e)
    except Exception as e:
         print('测评BUG',e)
    return sum

def quickEva(id,cl,filedir,filepath,answerTxt,Repo_id):
    sum=0
    try:
        print('开始运行程序')
        os.system('cd ' + filedir + '&&' + 'python ' + filepath)
    except:
        print('程序运行错误,代码存在若干BUG!')
        return 0
    try:
        cl.printText('开始比对答案')
        sum = correct('./evaluation/' + Repo_id+ '/output.txt', answerTxt, cl)
    except Exception as e:  #
        print('错误提示: ', e)
        print('计分函数异常，可能情况如下:')
        print('1.代码问题?\n2.文本输出问题?\n具体请看上面英文的错误')
        return 0
    return sum

def slowEva(id,cl,filedir,filepath,answerTxt,Repo_id):
    sum=0
    inputTxt='./evaluation/'+Repo_id+'/input.txt'
    try:
        with open(inputTxt,'r',encoding='utf-8') as f:
            inputs=f.readlines()
        with open(answerTxt,'r',encoding='utf-8') as f:
            ans=f.readlines()
    except Exception as e:
        print('mode 1 ',e)
    try:
        for inItem in inputs[:-1]:
            #print(inItem)
            try:
                inItem=inItem.replace('\'','"',100)
                #print(json.loads(inItem))
                with open(inputTxt,'w',encoding='utf-8') as f:
                    f.write(inItem)
                    f.write('END')
            except Exception as e:
                print('加载Input异常',e)
                continue
            try:
                try:
                    os.system('cd ' + filedir + '&&' + 'python ' + filepath)
                except Exception as e:
                    print(id+'.py error',e)
                    continue
                try:
                    with open('./evaluation/' + Repo_id + '/output.txt', 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    line = lines[0].replace('\n', '', 10)
                    uOut =line.replace('\'','"',100)
                    uOut = json.loads(uOut)
                except Exception as e:
                    print('Item{0}'.format(inputs.index(inItem))+' Error:',e)
                    continue
                #print(uOut)
                try:
                    if uOut=='END':
                        break
                    an=json.loads(ans[inputs.index(inItem)].replace('\n','',10))
                    print('Your Out:',uOut)
                    try:
                        if uOut["姓名"] == an["姓名"]:
                            sum += 0.2
                    except Exception as e:
                        print('第{0}条数据,可能出错 错误提示:'.format(inputs.index(inItem)), e)
                    try:
                        if uOut["手机"] == an["手机"]:
                            sum += 0.2
                    except Exception as e:
                        print('第{0}条数据,可能出错 错误提示'.format(inputs.index(inItem)), e)
                    try:
                        if uOut["地址"] == an["地址"]:
                            sum += 0.6
                    except Exception as e:
                        print('第{0}条数据,可能出错 错误提示'.format(inputs.index(inItem)), e)
                    print('Item{0}'.format(inputs.index(inItem)) + ' done')
                except:
                    print('Item{0}'.format(inputs.index(inItem)) + ' Error:', e)
                    continue
            except:
                print('Item{0}'.format(inputs.index(inItem))+' Error:',e)
                continue
    except Exception as e:
        print('mode 1','测评异常',e)
    return sum

def evaluateProcess(id,cl,mode,Repo_id):
    sum=0
    try:
        #outputTxt=resource_path('./evaluation/'+id+'/output.txt')
        #inputTxt = resource_path('./input.txt')
        #answerTxt = resource_path('./answer.txt')
        inputTxt='./input.txt'
        answerTxt='./answer.txt'
        filepath,filedir=findPy(id,path='./evaluation/'+Repo_id)
        if filepath=='':
            cl.printText('错误提示: 找不到以学号命名的py文件')
            return
        filepath=os.getcwd()+filepath[1:]
        filedir=os.getcwd()+filedir[1:]
        print(filepath, filedir)
        try:
            shutil.copy(inputTxt,'./evaluation/'+Repo_id)
        except Exception as e:
            cl.printText('复制文件错误 错误提示'+e)

        try:
            print('尝试修改你的代码')
            chgPy.ChangeYourPy(filepath,mode)
        except:
            print('代码修改失败，检查代码编码格式是否是utf-8',e)
            return 0

        if mode==0:
            print('执行mode 0')
            sum=quickEva(id,cl,filedir,filepath,answerTxt,Repo_id)
        else:
            print('执行mode 1')
            sum=slowEva(id,cl,filedir,filepath,answerTxt,Repo_id)
    except Exception as e:
        print(e,'运行异常')
        return 0

    try:
        # os.remove(filedir+'/output.txt')
        os.remove(filedir+'./input.txt')
    except:
        cl.printText('删除文件失败')
    return sum

if __name__=='__main__':
    id = '031701129'
    print(evaluateProcess(id='021700125'))