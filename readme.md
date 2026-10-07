aloha

hello world

### 本次实践学会的东西

1. 在 GitHub 上创建一个 repo

2. 下载 GitHub CLI，实际上之前只下载了 Git，用 ChatGPT 检查电脑之后发现没有 gh

3. 学会用 git clone 将 GitHub 上的远程仓库克隆到本地。由于网络问题出现了延迟（失败是因为电脑连接 GitHub 的 HTTPS 端口（443）时超时了，约 21 秒内没能建立连接。随后单独检查 GitHub 连通性时也发生了超时，说明当时存在网络连接问题。—— ChatGPT），用 Agent 辅助克隆了一下，然后发现节点的稳定性会影响 git clone，后来也发现还会影响 git push

4. 掌握了提交修改的步骤。先打开 powershell，cd 到文件地址，然后用 git status 来查看文件的修改情况，随后用 git add readme.md 来把需要提交的文件存入暂存区，用 git commit -m "Add readme" 来在本地创建一次提交，最后 git push -u origin main 来将 main 分支推送到 GitHub，并设置后续推送的默认目标

5. 了解了 git add . 和 git add *文件* 的区别。前者是暂存当前目录及其子目录中的所有修改，包括新增、修改和删除的文件，但不包含被忽略的文件；后者只推送当前分支中尚未上传的提交，不会上传未提交的文件修改

6. 学会用 git switch 来转换分支，用 git switch -c for_fun 来创建并切换分支，用 git branch 来检查当前所处的分支

7. 用 git diff -- readme.md 来确认修改内容

8. 合并分支不一定会产生冲突。如果 main 已经包含另一分支的全部提交，Git 会显示 Already up to date.——实际上我发现好多操作都会显示这个，可能是我最开始做了很多不必要的操作

9. 学会了通过 .gitignore 排除虚拟环境、数据集和缓存文件，避免将它们提交到仓库（这是 ChatGPT 教的）

10. 了解到预训练模型的输入尺寸、通道数和输出类别需要与任务匹配。ImageNet 的类别编号不能直接当作 MNIST 的数字标签

11. 学会如何删除一个仓库。因为第一次做的时候不合格，出现了很多问题，用 SUBMISSION 里面的评分标准自评了一遍之后发现只能得 60 分，遂删除原 repo 重新建了一个

12. 学会恢复误删的 branch，用 git branch *name* *提交编号* 可以恢复被误删的分支