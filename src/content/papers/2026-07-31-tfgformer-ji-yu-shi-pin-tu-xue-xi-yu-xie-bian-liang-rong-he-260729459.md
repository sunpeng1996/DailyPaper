---
title: 'TFGformer: Multivariate Time Series Forecasting via Time-Frequency Graph Learning
  and Covariate Fusion'
title_zh: TFGformer：基于时频图学习与协变量融合的多变量时间序列预测
authors:
- Yu Sun
- Yuan Chang
- Xiaohou Shi
- Yan Sun
affiliations:
- Beijing University of Posts and Telecommunications
- China Telecom Research Institute
arxiv_id: '2607.29459'
url: https://arxiv.org/abs/2607.29459
pdf_url: https://arxiv.org/pdf/2607.29459
published: '2026-07-31'
collected: '2026-08-03'
category: Other
direction: 多变量时间序列预测 · 时频图建模
tags:
- Time Series Forecasting
- Transformer
- Graph Learning
- Covariate Fusion
- STFT
one_liner: 提出融合时频图学习与协变量融合的多变量时序预测框架TFGformer，效果优于现有SOTA Transformer基线
practical_value: '- 电商销量、流量、库存等时序预测场景可复用STFT+自适应时频图建模方法，捕捉变量间稀疏有效关联，抑制噪声干扰

  - 协变量融合思路可迁移到用户行为时序预测任务，将节假日、大促、平台活动等外部特征无缝融入主序列表征提升准确率

  - Gumbel-Softmax采样生成稀疏动态图的trick可复用在多变量关联建模场景，既降低计算量又避免冗余依赖引入的噪声'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
多变量时序预测需建模复杂时序动态与变量间依赖，但实际场景中噪声关联易引入干扰，日历特征、外部事件等关键上下文协变量常未被充分利用。
### 方法关键点
1. 提出TFGformer统一框架，融合时频图结构学习与协变量感知表征融合
2. 时频图模块基于STFT捕捉互补时频域模式，通过加权马氏距离学习自适应变量间关联，用Gumbel-Softmax采样生成稀疏动态图抑制无效依赖
3. 基于MLP的模块将历史与未来协变量融合入主序列表征，充分利用趋势先验与上下文信号
### 关键结果
在电力、交通、气象三类公开基准数据集上实验，性能持续优于现有SOTA Transformer类时序预测模型
