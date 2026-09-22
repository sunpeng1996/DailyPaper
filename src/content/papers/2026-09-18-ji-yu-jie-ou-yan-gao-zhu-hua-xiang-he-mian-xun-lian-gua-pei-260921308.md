---
title: Auto-Bidding with Disentangled Advertiser Profiles and Train-Free Adaptation
title_zh: 基于解耦广告主画像和免训练适配的自动出价框架ADAPT
authors:
- Songyue Cai
- Shan Gu
- Wei Chen
- Ziru Xu
- Lianyu Wang
- Jian Xu
- Xiaofeng Zhu
affiliations:
- University of Electronic Science and Technology of China
- Taobao & Tmall Group, Alibaba
- Hainan University
arxiv_id: '2609.21308'
url: https://arxiv.org/abs/2609.21308
pdf_url: https://arxiv.org/pdf/2609.21308
published: '2026-09-18'
collected: '2026-09-22'
category: RecSys
direction: 广告自动出价 · 广告主画像建模
tags:
- AutoBidding
- AdvertiserProfiling
- DisentangledRepresentation
- ContrastiveLearning
- TrainingFreeAdaptation
- DecisionTransformer
one_liner: 提出两阶段训练的ADAPT自动出价框架，通过解耦广告主画像实现免训练冷启动与策略更新
practical_value: '- 广告主/用户画像建模可借鉴「静态属性+动态行为解耦」思路，拆分公共策略与个性化策略，减少表示冗余提升下游任务效果

  - 冷启动场景可复用免训练适配逻辑：新用户用同品类公共画像+零私有画像初始化，老用户用EMA更新画像无需重训，降低线上运维成本

  - 两阶段训练范式可迁移到其他个性化序列决策任务：第一阶段用对比学习单独学习纯净主体画像，第二阶段用解耦画像引导决策，避免画像被任务标签过度偏移

  - Decision Transformer 前缀增强技巧可直接复用：将三类画像作为前缀拼接到轨迹序列前，无需修改模型结构即可注入个性化信息'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有自动出价方法大多缺乏广告主个性化建模，直接复用推荐域画像方案面临三大挑战：连续竞价轨迹难以提取纯净策略画像；数值型画像语义模糊，公共与个性化信息混杂利用率低；线上场景禁止频繁重训，新广告主冷启动、老广告主策略更新成本极高。

### 方法关键点
- 两阶段训练：第一阶段基于广告主记忆库做对比学习，拆分静态类目画像与动态个体画像，提取纯净策略表示；第二阶段用交叉注意力提取公共画像、MLP提取私有画像，加入相关性损失保证二者解耦，三类画像作为前缀输入Decision Transformer预测出价参数
- 免训练适配：新广告主用类目静态画像+全量广告主公共画像均值+零私有画像实现零样本冷启动；老广告主新周期的轨迹用冻结的第一阶段编码器编码后，通过EMA更新记忆库中个体画像，全程无需重训模型

### 关键实验
在阿里公开AuctionNet基准（稠密、稀疏两个版本）上对比IQL、DT、GAS等9个SOTA基线：稠密场景100%预算下得分比最强基线GAS高2.23%，稀疏场景75%预算下提升达7.27%；新广告主零样本冷启动得分比原生DT高26.42%，老广告主新周期免训练更新比不更新得分高5.39%。

### 核心结论
个性化序列决策任务中，先单独学习纯净的主体画像再解耦利用，比直接端到端融合任务标签训练的效果更好、适配成本更低。
