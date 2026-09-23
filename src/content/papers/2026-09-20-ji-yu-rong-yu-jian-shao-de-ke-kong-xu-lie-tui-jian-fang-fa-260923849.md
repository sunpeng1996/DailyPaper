---
title: A Redundancy Reduction Approach for Controllable Sequential Recommendations
title_zh: 基于冗余减少的可控序列推荐方法
authors:
- Veronika Ivanova
- Marina Munkhoeva
- Ivan Razvorotnev
- Evgeny Frolov
affiliations:
- Yandex
- Applied AI Institute
- Lomonosov MSU
- HSE University
arxiv_id: '2609.23849'
url: https://arxiv.org/abs/2609.23849
pdf_url: https://arxiv.org/pdf/2609.23849
published: '2026-09-20'
collected: '2026-09-23'
category: RecSys
direction: 序列推荐 · 非对比学习正则化
tags:
- SequentialRecommendation
- BarlowTwins
- SelfSupervisedLearning
- PopularityDebiasing
- RepresentationLearning
one_liner: 将非对比学习Barlow Twins作为正则项加入序列推荐，通过可调参数实现精度-长尾曝光的可控权衡
practical_value: '- 可直接将BT-SR正则框架套用到现有Transformer序列推荐（如SASRec、BERT4Rec）上，无需复杂负采样，仅增加少量训练开销即可获得NDCG@10
  2.7%~7.9%的精度提升

  - 超参数α可直接作为业务调控旋钮：α调小可优先保障头部爆款推荐精度，α调大可提升中长尾商品曝光，适配不同业务目标（如大促推爆品/日常提多样性）

  - 构造正样本对时不用依赖随机mask/crop等破坏用户意图的增强方式，改用「共享相同下一跳交互item的不同用户序列」作为正对，标签一致且效果更稳定

  - 可复用论文提出的Alignment Concentration（AC）指标，量化模型对头部商品的倾向性，无需线上AB实验即可预判推荐结果的流行度分布'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Transformer序列推荐受长尾交互分布影响，头部item天然获得全局得分优势，传统对比学习正则依赖复杂负采样与随机数据增强，易进一步强化头部bias，且难以精准控制推荐精度与长尾曝光的权衡，缺乏轻量、可解释的调控手段。
### 方法关键点
- 提出BT-SR训练框架，在标准next-item预测损失基础上叠加Barlow Twins冗余减少正则项，总损失为 `L_pred + α*L_BT`，α为可调正则强度
- 正样本对构造无需随机mask/裁剪等破坏用户意图的增强方式，直接采样共享相同下一跳目标item的不同用户历史序列作为正对，标签一致性更高
- 提出Alignment Concentration（AC）指标，通过item embedding在用户表征空间主成分的投影能量，量化模型对头部item的倾向性
### 关键结果
在ML-1M、Yelp、Gowalla、Beauty、Kindle Store 5个公开基准数据集上，对比SASRec、CL4SRec、DuoRec等7个SOTA基线，BT-SR在NDCG@10上最高提升7.9%，HR@1最高提升12.7%；在Kindle Store等3个数据集上覆盖度最高提升13.9%，仅通过调整α即可在头部精度优先、长尾覆盖优先两个业务场景下灵活切换。
> 最值得记住：非对比冗余减少正则不仅能提升序列推荐精度，还能通过重塑表征空间几何结构，用单一超参数实现推荐结果流行度分布的可控调节
