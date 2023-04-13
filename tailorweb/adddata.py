import sqlite3

conn = sqlite3.connect('site.db')
c = conn.cursor()
types = ['sh','sL','n','b']

names_sh = ['Straight bus and waist dart woven','Straight Armhole Princess','Very Flared Armhole Princess']
names_sl = ['Sleeveless','Full Fitted sleeves','Bracelet full sleeves']
names_n = ['Round neck','Sweetheart Neck','Keyhole Neck','Scoop Neck','Rounded Standup Neck']
names_n2 = ['Round neck','Scoop Neck','Rounded Standup Neck']
names_b = ['Full Zipper','No seam No zipper','Back Buttoned Zipper 22']


for x in range(1,4):
    query = c.execute('INSERT INTO design (code,name,type,image) VALUES(?,?,?,?) ',(types[0]+ str(x),names_sh[x-1],types[0],types[0]+str(x)+'.svg'))
    conn.commit()
    for i in range(1, 4):
        query = c.execute('INSERT INTO design (code,name,type,image) VALUES(?,?,?,?) ',
                          (types[0]+str(x)+'_'+types[1]+str(i), names_sl[i-1], types[1], types[1] + str(i)+'.svg'))
        conn.commit()
    if x==2:
        for j in range(1, 4):
            if j==1:
                query = c.execute('INSERT INTO design (code,name,type,image) VALUES(?,?,?,?) ',
                                  (types[0]+str(x)+'_'+types[2]+str(j), names_n2[j-1], types[2], types[2] + str(j)+'.svg'))
            else:
                query = c.execute('INSERT INTO design (code,name,type,image) VALUES(?,?,?,?) ',
                                  (types[0] + str(x) + '_' + types[2] + str(j+2), names_n2[j-1], types[2],
                                   types[2] + str(j+2) + '.svg'))
            conn.commit()
    else:
        for j in range(1, 4):
            query = c.execute('INSERT INTO design (code,name,type,image) VALUES(?,?,?,?) ',
                              (types[0]+str(x)+'_'+types[2]+str(j), names_n[j-1], types[2], types[2] + str(j)+'.svg'))
            conn.commit()
    for k in range(1, 3):
        query = c.execute('INSERT INTO design (code,name,type,image) VALUES(?,?,?,?) ',
                          (types[0] + str(x) + '_' + types[3] + str(k), names_b[k-1], types[3],
                           types[3] + str(k) + '.svg'))
        conn.commit()