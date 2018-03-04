from app import store
from app import dummy_data
from app import views

member_store = store.MemberStore()
post_store = store.PostStore()
if __name__  == "__main__":
    dummy_data.seed_stores(member_store,post_store)
