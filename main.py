from bs4 import BeautifulSoup as BS
import requests



def scrapePage(link):
        page = requests.get(link)
        soup = BS(page.content, 'html.parser')
        job_info = soup.findAll("div", {"class": "col-md-2 col-xs-12 job-title job-title-text-wrap col-md-push-2"})
        job_details = [job.string.strip() for job in job_info]
        filtered_job_details = []
        for i in range(0,len(job_details),4):
            filtered_job_details.append((job_details[i: i+4]))
        allLinks = soup.findAll('a')
        joblist = []
        for link in allLinks:
            if link.string:
                joblist.append(link.string)


        job_filter = list()
        for i in range(9, len(joblist)-2):
            if joblist[i] not in ('View Details', 'Bookmark', 'Next', '1', '2','Skip to Main Content', 'Home',
                                  'Search Jobs', 'Log In /Create Account', 'Help', '2', 'Next', 'Posting Number',
                                  'Location', 'Position Type', 'Job Close Date', 'Contact Information', 'msu.edu'):
                job_filter.append(joblist[i])
        jobs_withInfo = dict()
        for info in filtered_job_details:
                jobs_withInfo[info[0]] = info[1:]

        for key, value in zip(jobs_withInfo, job_filter):
            jobs_withInfo[key].append(value)

        for key, values in jobs_withInfo.items():
            if 'Non-Student' in jobs_withInfo[key]:
                print(f'{key} | {values[0]} | {values[1]} | {values[2]}) | {values[3]}')

        return jobs_withInfo



def main():
        scrapePage('https://rhs-msu.peopleadmin.com/postings/search?page=1')


if __name__ == '__main__':
    main()


