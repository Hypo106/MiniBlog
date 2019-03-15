#!/usr/bin/env python
# -*- coding:utf-8 -*-
# File Name is manage.py
# Created by Hypo.Wang at 2017/9/26 10:24

from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import ArticleType, article_types, Source, \
    Comment, Article, User, Menu, ArticleTypeSetting, BlogInfo, \
    Plugin, BlogView

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# Global variables to jiajia2 environment:
app.jinja_env.globals['ArticleType'] = ArticleType
app.jinja_env.globals['article_types'] = article_types
app.jinja_env.globals['Menu'] = Menu
app.jinja_env.globals['BlogInfo'] = BlogInfo
app.jinja_env.globals['Plugin'] = Plugin
app.jinja_env.globals['Source'] = Source
app.jinja_env.globals['Article'] = Article
app.jinja_env.globals['Comment'] = Comment
app.jinja_env.globals['BlogView'] = BlogView

def make_shell_context():
    return dict(db=db, ArticleType=ArticleType, Source=Source,
                Comment=Comment,Article=Article,User=User,Menu=Menu,
                ArticleTypeSetting=ArticleTypeSetting,BlogInfo=BlogInfo,
                Plugin=Plugin,BlogView=BlogView)

manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def deploy(deploy_type):
    from flask.ext.migrate import upgrade
    from app.models import BlogInfo, User, ArticleTypeSetting, Source, \
        ArticleType, Plugin, BlogView, Comment

    # upgrade database to the latest version
    upgrade()

    if deploy_type == 'product':
        BlogInfo.insert_blog_info()
        User.insert_admin(email='w_haibo106@126.com', username='Hypo', password='123456')
        ArticleTypeSetting.insert_system_setting()
        Source.insert_sources()
        ArticleType.insert_system_articleType()
        Plugin.insert_system_plugin()
        BlogView.insert_view()

        # You must run `python manage.py deploy(product)` before run `python manage.py deploy(test_data)`
    if deploy_type == 'test_data':
        Menu.insert_menus()
        ArticleType.insert_articleTypes()
        #Article.generate_fake(100)
        #Comment.generate_fake(300)
        #Comment.generate_fake_replies(100)
        #Comment.generate_fake(300)

if __name__ == '__main__':
    manager.run()