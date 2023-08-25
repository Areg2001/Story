import environ

env = environ.Env() 
environ.Env.read_env()
FRONTEND_URL = env('FRONTEND_URL')
token = get_random_string(length=32)

verify_link = FRONTEND_URL + '/email-verify/' + token
subject, from_email, to = 'Verify Your Email', 'from@fpn.com', email
html_content = render_to_string('verify_email.html', {'verify_link':verify_link, 'base_url': FRONTEND_URL, 'backend_url': BACKEND_URL}) 
text_content = strip_tags(html_content) 

msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
msg.attach_alternative(html_content, "text/html")
msg.send()