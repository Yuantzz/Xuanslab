import scrapy
import matplotlib.pyplot as plt


class AgentsSpider(scrapy.Spider):
    name = 'agents'
    allowed_domains = ['tracker.gg']
    start_urls = ['https://tracker.gg/valorant/insights/agents?map=icebox']

    def parse(self, response):
        agent_names = response.css('div.st__item--sticky div.value::text').extract()
        win_rates = response.css('div.st-content__item-value--active div.value::text').extract()

        # 将 win rates 转换为浮点数
        win_rates = [float(rate.replace('%', '')) for rate in win_rates]

        # 绘制条形图
        plt.figure(figsize=(10, 6))
        bars = plt.bar(agent_names, win_rates, color='skyblue')
        plt.xlabel('Agent Name')
        plt.ylabel('Win Rate (%)')
        plt.title('Win Rate of Valorant Agents')
        plt.xticks(rotation=45, ha='right')  # 旋转 x 轴标签，使其更容易阅读
        plt.title('Custom Title: Win Rate of Valorant Agents in icebox(base on tier)', fontsize=16, fontweight='bold', color='blue')

        # 在每个条形上方显示具体数值
        for bar, win_rate in zip(bars, win_rates):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{win_rate:.2f}%',
                     ha='center', va='bottom', color='black', fontsize=8)

        plt.tight_layout()

        # 显示图形
        plt.show()

        self.log('Scraping complete.')
