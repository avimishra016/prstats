'''reading pull requests from git repository'''
import yaml
from github import Github

def get_repo_and_tokens():
    '''reading the repos and access tokens from the yaml file'''
    repos_and_tokens = []
    repos = ""
    access_token = ""
    with open(r'C:/Users/aweso/Downloads/Visual Studio Coding/python/repo.yaml') as file:
        documents = yaml.full_load(file)
        repos = documents['repos']
        access_token = documents['accessToken']
    for url_num in range(len(repos)):
        repos[url_num] = repos[url_num].replace('https', 'git')
        repos_and_tokens.append([repos[url_num], access_token[url_num]])
    return repos_and_tokens

def get_pull_requests(repo_url, access_token):
    '''use the repo url and access token to get the pull requests from a repo'''
    pull_request_data = [["PR #", "Title", "Date Created"]]
    git = Github(access_token)
    for repo in git.get_user().get_repos():
        if repo.git_url==repo_url:
            pulls = repo.get_pulls(state='open', sort='created', base='main')
            for pull in pulls:
                time_string = pull.created_at.strftime("%m/%d/%Y @ %H:%M:%S")
                pull_request_data.append([pull.number, pull.title, time_string])
    return pull_request_data

def main():
    '''print out the data collected on each pull request for each repo'''
    repo_token = get_repo_and_tokens()
    print_text = "{number:>14}: {title:>20}, {date:>21}"
    for pair in repo_token:
        data = get_pull_requests(pair[0], pair[1])
        print("Repo_Url:", pair[0])
        for pull_request in data:
            print (print_text.format(number=pull_request[0], title=pull_request[1], date=pull_request[2]))
        print()
if __name__ == "__main__" :
    main()
