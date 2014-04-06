import requests
from subprocess import call
from local_config import GITHUB_USERNAME, GITHUB_PASSWORD


def make_auth_req(request):
    return requests.get(request, auth=(GITHUB_USERNAME, GITHUB_PASSWORD))


def get_repositories_url(user):
    request = "https://api.github.com/users/{0}".format(user)
    r = make_auth_req(request)
    repositories_url = r.json()["repos_url"]
    return repositories_url


def get_repositories(user):
    repositories_url = get_repositories_url(user)
    r = make_auth_req(repositories_url)
    repositories = r.json()
    repositories_list = []
    for repo in repositories:
        repositories_list.append(repo["name"])
    return repositories_list


def extract_data(user, request, repository):
    file = open("{0}/{1}.zip".format(user, repository), "wb")
    for part in request.iter_content():
        file.write(part)
    file.close()


def download_repos(user):
    repositories = get_repositories(user)
    command = "mkdir {0}".format(user)
    call(command, shell=True)

    url = "https://github.com/%s/{}/archive/master.zip" % (user)
    for repo in repositories:
        r = make_auth_req(url.format(repo))
        extract_data(user, r, repo)


def main():
    download_repos("SvetlaGeorgieva")


if __name__ == '__main__':
    main()
