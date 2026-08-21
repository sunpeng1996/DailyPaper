---
title: 'SSR-GRPO: Integrating Supervision and Semantic IDs into Reinforcement Learning
  for Dense Retrieval in E-commerce'
title_zh: SSR-GRPO：融合监督与语义ID的电商稠密检索强化学习框架
authors:
- Guangxin Song
- Xing Fang
- Mingmin Jin
- Jing Wang
- Bokang Wang
- Zhentao Song
- Junjie Bai
- Jianbo Zhu
affiliations:
- Alibaba Group
arxiv_id: '2608.19595'
url: https://arxiv.org/abs/2608.19595
pdf_url: https://arxiv.org/pdf/2608.19595
published: '2026-08-20'
collected: '2026-08-21'
category: RecSys
direction: 电商稠密检索 · GRPO优化
tags:
- Dense Retrieval
- GRPO
- Semantic ID
- Hard Negative Mining
- RLHF
one_liner: 融合分层Semantic ID与双视角奖励的GRPO稠密检索框架，在阿里电商场景落地提效
practical_value: '- 可复用双视角奖励设计：用RQ-VAE生成的分层Semantic ID做稀疏相关性信号，融合稠密embedding相似度，替换大模型奖励judge降本30%以上，同时消除同架构RL奖励偏见，尤其适配电商多属性语义匹配场景

  - 可直接落地的硬负样本挖掘方案：基于Semantic ID分层匹配规则（前两层一致第三层不同）挖掘细粒度语义硬负样本，结合高召回低转化的商业属性负样本做双维度构造，无需人工标注即可大幅提升模型细粒度语义区分能力

  - 训练框架可迁移：RL训练阶段融合R-DPO损失+GRPO，用不确定性动态加权平衡两个任务梯度，避免RL训练不稳定问题，适合所有稠密检索模型的RL优化流程

  - 工程trick：GRPO训练时加入硬负样本基准的masking机制，过滤top-K中的简单负样本噪声，提升训练效率20%同时减少Reward Hacking问题'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于RL的稠密检索框架R-GRPO存在两大核心痛点：一是batch内采样候选池有限，top-K结果混入大量噪声样本，导致训练偏离最优方向；二是奖励计算依赖同架构RL训练的大模型judge，存在评估偏见且算力成本极高，同时传统LLM微调范式难以捕获电商场景复杂细粒度的用户语义意图，长尾query效果差。

### 方法关键点
- 双视角奖励计算：融合稠密embedding相似度与RQ-VAE生成的分层Semantic ID匹配得分，替换原有大模型奖励judge，α=0.8时取得稠密/稀疏信号最优trade-off
- 双维度硬负样本挖掘：一类是召回高但转化低的商业属性负样本，一类是Semantic ID前两层匹配、第三层不匹配的细粒度语义负样本
- 联合训练架构：在GRPO基础上加入R-DPO损失学习正负对语义差异，设计基于硬负样本的masking函数过滤训练噪声，用不确定性动态加权平衡两个损失避免梯度冲突

### 关键结果
基于阿里0.3亿Tmall交互数据训练，离线对比SFT+R-GRPO基线，通用测试集HR@4k提升0.6%，长尾query HR@4k提升0.86%，GR@100提升0.69%；线上A/B测试对比R-GRPO，UCTCVR提升0.61%，GMV提升0.39%，目前已全量部署在天猫搜索。

### 核心结论
将Semantic ID的分层语义特性融入RL训练的奖励计算、负采样、噪声过滤全流程，可低成本解决电商稠密检索RL训练不稳定、效果天花板低的问题。
