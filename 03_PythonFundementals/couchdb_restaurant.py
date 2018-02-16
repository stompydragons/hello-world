import couchdb

couch = couchdb.Server()

dbname = "restaurant"

if dbname in couch:
    db = couch[dbname]
else:
    db = couch.create(dbname)

summary = '_design/summary/_view/menu-count'
pages = '/_design/pages/_view/without-hours'

for item in db.view(summary, group=True):
    print(item.key, item.value)

# doc_id, doc_rev = db.save({'category': 'Dessert', 'name': 'Chocolate cheesecake'})

# print(doc_id)

for doc_id in db:
    doc = db[doc_id]
    print(type(doc))
    # doc['type']
    print(doc)
    # print(db.get(doc_id))