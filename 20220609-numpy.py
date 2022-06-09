from pyecharts import options as opts
from pyecharts.charts import Pie, WordCloud
from pyecharts.faker import Faker
from pyecharts.render import make_snapshot
from selenium import webdriver


# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
#     .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
#     .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
# )
# bar.render()


# x = np.linspace(-np.pi, np.pi, 256)
#
# cos = np.cos(x)
# sin = np.sin(x)
#
# pyplot.plot(x, cos, '--', linewidth=2)
# pyplot.plot(x, sin)
#
# pyplot.show()
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
#
# fig1, ax1 = pyplot.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
# pyplot.show()
# np.random.seed(0)
#
# mu = 200
# sigma = 25
# x = np.random.normal(mu, sigma, size=100)
#
# fig, (ax0, ax1) = pyplot.subplots(ncols=2, figsize=(8, 4))
#
# ax0.hist(x, 20, density=True, histtype='stepfilled', facecolor='g', alpha=0.75)
# ax0.set_title('stepfilled')
#
# # Create a histogram by providing the bin edges (unequally spaced).
# bins = [100, 150, 180, 195, 205, 220, 250, 300]
# ax1.hist(x, bins, density=True, histtype='bar', rwidth=0.8)
# ax1.set_title('unequal bins')
#
# fig.tight_layout()
# pyplot.show()
# seaborn.set(style="darkgrid")
#
# tips = seaborn.load_dataset("tips")
# seaborn.relplot(x="total_bill", y="tip", data=tips);
# pyplot.show()
# fmri = seaborn.load_dataset("fmri")
# seaborn.relplot(x="timepoint", y="signal", hue="event", kind="line", data=fmri)
# pyplot.show()
# titanic = seaborn.load_dataset("titanic")
# seaborn.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)
# pyplot.show()
from webdriver_manager.core import driver


# def pie_base() -> Pie:
#     c = (
#         Pie()
#         .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
#         .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
#         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#     )
#     return c
#
# # 需要安装 snapshot_selenium
# make_snapshot(driver, pie_base().render(), "pie.png")



# words = [
#     ("Sam S Club", 10000),
#     ("Macys", 6181),
#     ("Amy Schumer", 4386),
#     ("Jurassic World", 4055),
#     ("Charter Communications", 2467),
#     ("Chick Fil A", 2244),
#     ("Planet Fitness", 1868),
#     ("Pitch Perfect", 1484),
#     ("Express", 1112),
#     ("Home", 865),
#     ("Johnny Depp", 847),
#     ("Lena Dunham", 582),
#     ("Lewis Hamilton", 555),
#     ("KXAN", 550),
#     ("Mary Ellen Mark", 462),
#     ("Farrah Abraham", 366),
#     ("Rita Ora", 360),
#     ("Serena Williams", 282),
#     ("NCAA baseball tournament", 273),
#     ("Point Break", 265),
# ]
#
#
# def wordcloud_base() -> WordCloud:
#     c = (
#         WordCloud()
#         .add("", words, word_size_range=[20, 100])
#         .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-基本示例"))
#     )
#     return c
#
# # 需要安装 snapshot_selenium
# make_snapshot(driver, wordcloud_base().render(), "WordCloud.png")

