---
title: 'EAGER: Enrich-and-Align Generative Query Recommendation from Clicked Items
  in E-commerce Search'
title_zh: EAGER：电商场景下基于点击商品的生成式查询推荐框架
authors:
- Shuwei Yuan
- Mingqian Ding
- Luxin Liu
- Rong Xiao
- Xiaoyi Zeng
affiliations:
- Alibaba International Digital Commerce Group
arxiv_id: '2609.07143'
url: https://arxiv.org/abs/2609.07143
pdf_url: https://arxiv.org/pdf/2609.07143
published: '2026-09-07'
collected: '2026-09-09'
category: QueryRec
direction: 生成式查询推荐 · 点击商品转查询场景
tags:
- QueryRecommendation
- GenerativeQuery
- SFT
- GRPO
- EcommerceSearch
one_liner: 提出两阶段生成式I2Q查询推荐框架，兼顾多样性与业务对齐，已在头部电商生产部署
practical_value: '- 数据构造可复用：采用「点击query+后搜query+LLM生成query+PARM排序」的多源监督标签方案，零额外标注成本解决I2Q任务标注稀疏问题

  - 训练流程可迁移：两阶段范式（SFT做多样性扩充+GRPO做业务对齐）先扩召回空间再做规则/偏好约束，适配各类生成式推荐场景

  - 奖励设计可直接复用：混合奖励（8项可落地规则奖励+PARM偏好奖励）统一离线标注筛选和在线RL优化信号，避免目标不一致

  - 上线架构可复用：生成式结果作为额外召回通道与现有日志/稠密检索结果混合排序，无需替换现有线上链路，落地风险极低'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商用户点击商品返回feed时的场景化query推荐（I2Q）是衔接推荐与搜索的核心高价值触点，传统基于日志共现的方法无法覆盖长尾/新商品的个性化意图，通用LLM生成的query流畅但脱离平台业务规则和真实用户点击偏好，同时需要兼顾多样性、合规性、点击转化多目标，传统单阶段训练难以满足。

### 方法关键点
- 第一阶段SFT查询扩充：1）多源监督标签构造，按优先级拼接用户点击query、后搜query、LLM生成query，用PARM（基于Qwen-4B训练的点击偏好模型）对生成query排序过滤噪音；2）四阶段课程学习，从仅商品输入的I2Q→带CoT的增强I2Q→加用户特征的UI2Q→带CoT的增强UI2Q，逐步提升推理深度和个性化程度；3）增加多样性正则损失+自蒸馏策略，提升输出query差异度，扩充生成空间。
- 第二阶段GRPO对齐：用混合奖励做RL优化，规则奖励覆盖合规、长度、多样性、无敏感词等8项可验证业务约束，PARM模型奖励拟合用户点击偏好，两阶段共享PARM信号保证训练目标一致。

### 关键结果
离线对比GPT-5.2、Gemini3.1、不同参数Qwen等基线，基于Qwen3-1.7B的EAGER Soft HR@all达93.82%，Distinct-2达83.04，规则得分9.16，均优于所有基线；9天线上A/B测试显示，UCTR提升0.83%，PCTR提升1.28%，支付订单量提升3.49%，L2P提升2.38%。

最值得记住的一句话：生成式推荐落地核心是先通过SFT做意图覆盖扩大召回空间，再通过RL对齐业务约束和用户偏好，两者互补才能兼顾效果和合规性。
