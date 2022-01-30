class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            clean = []
            for c in email:
                if c == '+' or c == '@':
                    break

                if c != '.':
                    clean.append(c)

            domain = []
            for c in reversed(email):
                domain.append(c)
                if c == '@':
                    break

            domain = ''.join(domain[::-1])
            clean = ''.join(clean)

            unique_emails.add(clean + domain)

        return len(unique_emails)
                    
