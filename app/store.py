import copy
import itertools

class BaseStore():
    def __init__(self,data_provider,last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def get_all(self):
        return self._data_provider

    def add(self,item_instance):
        item_instance.id = self._last_id
        self._data_provider.append(item_instance)
        self._last_id += 1

    def get_by_id(self, id):
        all_item_instances = self.get_all()
        result = None
        for item_instance in all_item_instances:
            if item_instance.id == id:
                result = item_instance
                break
        return  result

    def update(self,item_instance):
        all_item_instances = self.get_all()
        result = item_instance

        for index,current_item_instance in enumerate(all_item_instances):
            if current_item_instance.id == item_instance.id :
                all_item_instances[index] = item_instance
                break
        return result

    def delete(self,id):
        item_instance = self.get_by_id(id)
        if item_instance is not None :
            self._data_provider.remove(item_instance)

    def entity_exists(self,item_instance):
        result = True
        if self.get_by_id(item_instance.id)is None:
            result = False
        return result

class MemberStore(BaseStore):
    members = []
    last_id = 1

    def __init__(self):
        super().__init__(MemberStore.members , MemberStore.last_id)

    def get_by_name(self, member_name):
        all_members = self.get_all()

        for member in all_members:
            if member.name == member_name:
                yield member

    def get_members_with_posts(self, all_posts):
        all_members = copy.deepcopy(self.get_all())

        for member, post in itertools.product(all_members, all_posts):
            if member.id is post.member_id:
                member.posts.append(post)
        for member in all_members :
            yield member


    def get_top_two(self, all_posts):
        member_with_posts = list(self.get_members_with_posts(all_posts))
        member_with_posts.sort(key=lambda member: len(member.posts), reverse=True)

        yield member_with_posts[0]
        yield member_with_posts[1]

class PostStore(BaseStore):
    posts = []
    last_id = 1

    def __init__(self):
        super().__init__(PostStore.posts, PostStore.last_id)

    def get_posts_by_date(self):
        all_posts = self.get_all()
        all_posts.sort(key = lambda post: post.date , reverse = True)

        for post in all_posts :
            yield all_posts


