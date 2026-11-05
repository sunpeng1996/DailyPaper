---
title: Offline Learning of Reserve Prices from Censored Bids
title_zh: 基于删失出价数据的拍卖保留价离线学习方法
authors:
- Lavanya Marla
- Yunzong Xu
- Boxuan Zhou
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2611.06067'
url: https://arxiv.org/abs/2611.06067
pdf_url: https://arxiv.org/pdf/2611.06067
published: '2026-11-04'
collected: '2026-11-05'
category: RecSys
direction: 广告拍卖 · 保留价优化
tags:
- Reserve Price
- Censored Data
- Minimax Regret
- Second-price Auction
- Monotone Hazard Rate
one_liner: 提出删失出价下基于MHR假设的最小最大后悔保留价离线学习框架，规避分布误配损失
practical_value: '- 电商/搜索广告二价拍卖场景下，若仅能观测高于历史保留价的出价，无需假设出价分布参数，直接用删失比例、历史最低保留价处的右边界危险率两个可观测指标计算鲁棒保留价，可避免参数模型误配带来的持久收入损失

  - 可直接复用文中的auto-selector自适应框架，先判断收入是否在最低历史保留价处仍未下降，是则采用观测尾端的最优保留价，否则采用最小最大后悔保留价，无需人工判断场景归属

  - 上线新保留价前，可通过文中的两参数最坏case计算方法预估收入后悔上界，控制收入风险，eBay实验显示直接复用历史保留价最多可损失54%的最优收入，远高于鲁棒规则的后悔值'
score: 9
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
二价拍卖是电商、搜索广告的核心变现机制，保留价设置直接决定平台收入，但历史出价天然存在删失问题：所有低于历史最低保留价的出价完全不可观测，即便有无限数据也无法还原完整的出价分布，传统基于参数分布拟合的保留价计算方法容易因分布假设错误产生持续的收入后悔，亟需不需要强分布假设的鲁棒离线学习方案。

### 方法关键点
- 引入MHR（单调危险率）这一拍卖领域通用的需求形状约束，将问题划分为可识别、非识别两类 regime：可识别 regime 下最优保留价可直接从观测到的尾端出价得到，无需还原隐藏分布；
- 非识别 regime 下，通过理论推导证明最小最大后悔保留价仅依赖两个可观测指标：删失比例（低于历史最低保留价的出价占比）、历史最低保留价处的右边界危险率，将无限维的分布搜索问题降为二维优化；
- 提出auto-selector自适应规则，自动根据样本判断所属 regime 选择对应策略，无需预先知道分布特征，不同 regime 下的学习率分别达到O(N^{-1/2})、O(N^{-1})、匹配下界的O(N^{-2/5})。

### 关键实验
基于合成数据与真实eBay Palm Pilot拍卖数据，对比参数MLE、历史保留价复用等baseline：1. MHR约束下的鲁棒规则在7/8的常见起拍价场景下，留出集后悔低于Weibull分布拟合的MLE；2. 直接复用历史起拍价最多可损失54%的最优收入，远高于鲁棒规则的后悔值；3. MHR约束相比无约束的保留价策略，在所有合成场景下均降低了最坏case后悔。

**最值得记住的一句话**：删失出价场景下，鲁棒最优保留价不需要拟合完整的出价分布，仅靠删失比例和边界危险率两个可观测指标就能平衡不同分布下的最坏收入损失。
