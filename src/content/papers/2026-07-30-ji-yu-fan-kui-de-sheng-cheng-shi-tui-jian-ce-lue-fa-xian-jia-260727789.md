---
title: 'From Understanding to Action: Feedback-Grounded Policy Discovery for Generative
  Recommendation'
title_zh: 基于反馈的生成式推荐策略发现框架：弥合理解与行动的鸿沟
authors:
- Zhi Chen
- Minmao Wang
- Xingchen Liu
- Haoqiang Liang
- Huihuang Lin
- Likang Wu
- Hongke Zhao
- Yulong Wang
- Shijie Yi
- Fei Pan
affiliations:
- Huazhong Agricultural University
- Fudan University
- Kuaishou Technology
- Tianjin University
arxiv_id: '2607.27789'
url: https://arxiv.org/abs/2607.27789
pdf_url: https://arxiv.org/pdf/2607.27789
published: '2026-07-30'
collected: '2026-07-31'
category: GenRec
direction: 生成式推荐 · 反馈驱动策略蒸馏
tags:
- Generative Recommendation
- Semantic ID
- Knowledge Distillation
- LLM Agent
- Policy Optimization
one_liner: 区分用户意图与验证型推荐策略，蒸馏LLM知识到轻量SID模型，工业场景收入涨超4.5%
practical_value: '- 可复用「离线LLM挖掘意图/策略知识 + 蒸馏到轻量生成式推荐模型」的部署范式，完全避免在线调用LLM，兼顾语义能力与推理时延，适配电商/广告的高吞吐低延迟要求

  - 策略筛选可复用「增量优势」评估方法：仅保留效果超过仅用意图基线的策略，过滤LLM生成的语义合理但无实际增益的无效策略

  - 跨异构空间的知识迁移优先选择一阶+高阶关系蒸馏，而非直接MSE对齐embedding，适配LLM语义空间与推荐行为空间的异构特性，效果更稳定

  - 工业部署可采用「日级LLM知识更新 + 小时级流式训练更新学生模型」的多时间尺度架构，平衡知识新鲜度与线上稳定性，快手的落地架构可直接复用'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
基于Semantic ID的生成式推荐普遍仅依赖行为共现监督，无法区分需求理解与决策逻辑；LLM虽能推理用户意图，但未经过推荐业务效果校验，语义合理的推理不一定能带来好的推荐效果，存在「理解-行动鸿沟」：仅靠意图只能圈定推荐的语义范围，无法完成细粒度的候选排序决策。
### 方法关键点
- 拆分两类知识：意图知识定义用户当前需求，策略知识定义该需求下的推荐优先级与过滤边界，仅当策略能带来超过仅用意图基线的增量增益时才被保留
- 反馈驱动双Agent策略发现：策略Agent生成多份候选策略，执行器分别评估仅用意图、加策略的推荐效果，反馈Agent基于增量优势迭代优化策略，最多2轮即可收敛
- 双空间关系蒸馏：在轻量SID生成器中新增<Intent>、<Policy>两个隐Token，不硬对齐LLM与学生模型的embedding，而是对齐用户间的一阶相似度、高阶邻域结构，适配异构空间特性
### 关键结果
离线在Amazon Beauty/Toys/Sports三个公开数据集上，比TIGER、LETTER等SOTA基线的Recall@10最高提升19.8%；快手本地生活广告场景7天A/B测试覆盖1325万用户，Revenue提升4.506%，ADVV提升4.621%，线上推理时延仅从0.023s升至0.032s，远低于直接调用LLM的4.437s。
### 核心结论
LLM输出的语义合理内容无法直接作为推荐决策依据，经过业务效果验证的策略知识才能有效弥合意图理解到推荐行动的鸿沟。
