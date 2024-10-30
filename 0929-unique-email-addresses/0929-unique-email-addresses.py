class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        unique_emails = set()

        for email in emails:
            local_name, domain_name = email.split('@')

            local_name = local_name.split('+')[0]
            local_name = local_name.replace('.', '')


            unique_name = local_name + "@" + domain_name
            unique_emails.add(unique_name)

        return len(unique_emails)







        