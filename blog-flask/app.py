# -*- codeing = utf-8 -*-
from flask import Flask

app = Flask(
    __name__,
    static_url_path='',
    static_folder='static',
    template_folder='.'
)

# 总入口
from main_view.index import _index
app.register_blueprint(_index)

# 概要和简历
from total.概要.guide import _guide
app.register_blueprint(_guide)
from total.简历.cv import _cv
app.register_blueprint(_cv)

# 特设网页区域
from total.特设网页.精神文明建设展.culture import _culture
app.register_blueprint(_culture)
from total.特设网页.大学毕业.graduation import _graduation
app.register_blueprint(_graduation)
from total.特设网页.战列舰编年史.bb import _bb
app.register_blueprint(_bb)
from total.特设网页.画廊.gallery import _gallery
app.register_blueprint(_gallery)

# 日志系统区域
from blog_view.diary import _diary
app.register_blueprint(_diary)
from blog_view.computer import _computer
app.register_blueprint(_computer)
from blog_view.important import _important
app.register_blueprint(_important)




# 发送页面标识
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('common/fav.ico')





if __name__ == '__main__':
    app.run(debug='on', port='8000')
