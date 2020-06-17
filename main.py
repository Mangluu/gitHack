import os

## Number of days you want to make commits
for i in range(1,366,7):
    d = str(i) + ' day ago'
    ## Open a text file and modify it
    with open('bot2.txt', 'a') as file:
        file.write(d)
    ## Add bot2.txt to staging area
    os.system('git add bot2.txt')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

    with open('bot2.txt', 'a') as file:
        file.write('Commit1')
    os.system('git add bot2.txt')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

    with open('bot2.txt', 'a') as file:
        file.write('Commit2')
    os.system('git add bot2.txt')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

    with open('bot2.txt', 'a') as file:
        file.write('Commit3')
    os.system('git add bot2.txt')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

    with open('bot2.txt', 'a') as file:
        file.write('Commit4')
    os.system('git add bot2.txt')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

    with open('bot2.txt', 'a') as file:
        file.write('Commit2')
    os.system('git add bot2.txt')
        ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

    with open('bot2.txt', 'a') as file:
        file.write('Commit3')
    os.system('git add bot2.txt')
        ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

    with open('bot2.txt', 'a') as file:
        file.write('Commit4')
    os.system('git add bot2.txt')
        ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')


## push the commit to github
os.system('git push -u origin master')
