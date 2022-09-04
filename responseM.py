import time
timeday = time.asctime(time.localtime(time.time()))
responseD = {'what is your name':[
    'My name is AdeBOT',
    'Hi you can call me AdeBot.',
    'My owner named me AdeBot call me that.',
    ],
            'what is the time?':[
                'The time is'+ timeday,
                ],
            'what is the time':[
                'The time is:'+ timeday,
                ],
             'tell me a riddle':[
                 'I am something with four legs, under something with four legs, eating something with four legs.. what are we?',
                 ],
             'who is bill gates':[
                 'He is the owner of the company Microsoft',
                 ],
             'bill gates':[
                 'He is the owner of the company Microsoft',
                 ],
             'who created you':[
                 'I was created by Coco :0',
                 ],
             'gender':[
                 'I am an AI Bot i have no gender',
                 'I currently dont specify :)',
                 ],     
    }
