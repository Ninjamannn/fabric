from fabric import Connection
from fabric. import append, exists


c = Connection(
    host='52.59.248.255',
    user='ubuntu',
    port=22,
    connect_kwargs={
        "key_filename": "/home/ninja/aws/zlata_aws/zlata_aws.pem",
    },
)

result = c.run('w')
print(result)
print(c.user)


def deploy(c):
    site_folder = '/home/{user}/test_fabric/'.format(user=c.user)
    c.run('mkdir -p {site_folder}'.format(site_folder=site_folder))
    with c.cd(site_folder):
        _get_latest_source(c)


def _get_latest_source(c):
    repo_url = 'https://github.com/Ninjamannn/testme.git',
    branch = 'develop',  # git branch

    if c.exists('.git'):
        c.run('git fetch')
    else:
        c.run('git clone {REPO_URL} . -b {BRANCH}'.format(REPO_URL=repo_url, BRANCH=branch))
    current_commit = c.local("git log -n 1 --format=%H", capture=True)
    c.run('git reset --hard {current_commit}'.format(current_commit=current_commit))


deploy(c)
