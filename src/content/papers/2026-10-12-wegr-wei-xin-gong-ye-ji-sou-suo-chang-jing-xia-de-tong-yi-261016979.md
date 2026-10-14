---
title: 'WeGR: Unified Generative Retrieval for Industrial Search Systems in WeChat'
title_zh: WeGR：微信工业级搜索场景下的统一生成式检索框架
authors:
- Jiajun Han
- Guoxin Ma
- Felix
- Liangsheng Xu
- Ruiqi Yu
- Yingdi Guo
- Zongbing Wang
- Xinhua Ye
- Chenyan Hua
- Xin Xie
affiliations:
- Tencent Penguin Island
arxiv_id: '2610.16979'
url: https://arxiv.org/abs/2610.16979
pdf_url: https://arxiv.org/pdf/2610.16979
published: '2026-10-12'
collected: '2026-10-14'
category: GenRec
direction: 生成式检索 · Semantic ID 工业落地
tags:
- Generative Retrieval
- Semantic ID
- RQ-VAE
- GRPO
- Industrial Deployment
- Reinforcement Learning
one_liner: 提出融合协同感知语义ID编码与动态RL优化的生成式检索框架，微信落地提效降本
practical_value: '- Semantic ID构造可直接复用CoCo-VAE的3个核心trick：加入Q2I/I2I协同正则优化表示、首层码本刷新复活死码、FAR正则防坍缩，比传统RQ-Kmeans/RQ-VAE的召回效果更优，适配电商搜索的协同信号需求

  - 生成式检索的RL偏好优化无需额外开发辅助奖励模型，采用DHPO的动态horizon课程学习方案，从前缀匹配到全SID匹配逐步优化，既解决奖励稀疏问题，又避免辅助模型带来的噪声和跨场景适配成本，可直接迁移到多搜索场景

  - 工业落地可参考渐进式替换路径：先将WeGR作为新增召回通路验证效果，再逐步裁剪传统通路的召回配额，最多可裁剪80%传统召回候选，反而进一步提升业务指标，同时减少下游预排阶段的算力消耗，适配存量系统平滑迭代

  - 针对新用户、长尾query等冷启动场景，WeGR的增益显著高于传统召回，可复用该结论优化冷启动流量的召回策略，无需单独搭建冷启动专属通路'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式检索落地面临两大核心痛点：一是Semantic ID（SID）编码范式要么无法有效融入用户交互协同信号，要么存在严重码本坍缩、利用率低问题，导致SID区分度不足，召回效果差；二是RL偏好优化依赖全SID精确匹配获取用户行为奖励，奖励稀疏问题突出，引入辅助奖励模型又会带来噪声、跨场景适配成本高，难以替代传统多通路召回的复杂架构。
### 方法关键点
- 协同无坍缩编码器CoCo-VAE：将Q2I、I2I协同信号融入连续表示学习，新增首层码本刷新机制复活低使用率码字，搭配FAR正则（样本级残差保真+码本级碰撞惩罚），同时保留协同语义和高码本利用率
- 动态视野策略优化DHPO：基于SID层级结构做课程学习，训练初期用短前缀匹配发放奖励，逐步拉长匹配长度到全SID，无需辅助奖励模型即可解决奖励稀疏问题，搭配多正样本SFT（MSFT）补充稳定学习信号
- 渐进式落地路径：从新增WeGR为额外召回通路，到逐步裁剪80%传统召回通路的候选量，降低下游算力消耗
### 关键实验
微信电商搜索2个月线上A/B测试显示，V1.2版本（裁剪80%传统召回候选）单量相对提升2.539%，CTR提升1.508%，CVR提升1.381%，CPU/GPU使用率分别下降25.5%/26.1%，视频号搜索、微信搜一搜latency分别降低21.7ms、15.4ms；独立直播搜索场景下DHPO可实现HR@6提升5.95%~7.07%，MRR@6提升6.12%~7.82%。
### 核心结论
生成式检索完全可以替代传统多通路召回架构，在提升业务指标的同时大幅降低系统复杂度和算力成本，是工业级搜索的可行演进方向
