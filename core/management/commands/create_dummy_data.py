import random
from django.core.management.base import BaseCommand
# from django.utils.text import slugify
from model_mommy import mommy
from faker import Faker
from faker.providers import lorem, person, internet
from ...models import Human, Child, Parent, Sibling, Avatar, User

fake = Faker()
fake.add_provider(lorem)
fake.add_provider(internet)


def random_pick(collection):
    return random.choice(collection)

class Command(BaseCommand):
    help = 'Create Dummy Data.'

    def handle(self, *args, **kwargs):
        parents = []
        siblings = []
        users = []
        humans = []

        for i in range(3):
            user = mommy.make(User, username=fake.user_name(), email=fake.email(), password=fake.sentence(nb_words=2) )
            users.append(user)

        for i in range(5):
            parent = mommy.make(Parent, user=random_pick(users), name=fake.word(), description=fake.sentence())
            sibling = mommy.make(Sibling, user=random_pick(users), name= fake.word(), description=fake.sentence())
            parents.append(parent)
            siblings.append(sibling)

        for i in range(10):
            human = mommy.make(Human,
                               user=random_pick(users),
                               name= fake.sentence(nb_words=3),
                               content= fake.text(max_nb_chars=200, ext_word_list=None),
                               parent=random_pick(parents),
                               siblings=random.sample(siblings, 2)
                               )
            humans.append(human)

        for i in range(20):
            mommy.make(Child,
                       user=random_pick(users),
                       name = fake.sentence(nb_words=3),
                       content = fake.text(max_nb_chars=200, ext_word_list=None),
                       human = random_pick(humans)
                       )

