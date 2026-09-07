---
title: Inventory-Grounded Policy-Level Optimization for Training-Free AI Search
title_zh: 面向免训练AI搜索的库存感知策略级优化框架IGPO
authors:
- Wei Zhou
- Tiandeng Wu
- Jiandong Ding
- Zhufeng Fan
- Yi Cao
affiliations:
- Huawei Technologies Co., Ltd.
arxiv_id: '2609.04813'
url: https://arxiv.org/abs/2609.04813
pdf_url: https://arxiv.org/pdf/2609.04813
published: '2026-09-04'
collected: '2026-09-07'
category: RecSys
direction: 电商搜索优化 · 免训练动态库存适配
tags:
- Training-Free
- Dynamic Inventory
- AI Search
- Prompt Optimization
- E-commerce
one_liner: 提出库存感知的免训练AI搜索优化框架IGPO，适配动态商品库，线上CTR相对提升3.17% bad case降38.9%
practical_value: '- 动态库存场景下可复用「策略规则 + runtime库存画像」的解耦设计，避免将瞬时库存状态固化到prompt/模型中，适配电商商品库频繁更新的场景

  - 离线优化阶段可借鉴「同query多轨迹分组对比 + 库存引导探索」的思路，无需标注数据即可自动区分“真无货”和“检索漏召”，大幅降低bad case

  - Policy Guidelines的更新可复用论文的分层校验逻辑：先单补丁回放验证，再组合回放校验回归，完全自动更新无需人工审核，降低运维成本

  - 线上serving可参考规则规模设计：单阶段最多注入3条规则，p95新增prompt长度568token，p95延迟增加185ms，符合生产级性能要求'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
早期部署的AI搜索系统普遍面临商品库存频繁更新的问题，商品上下架、属性变更、元数据质量波动快，无法将库存信息固化到prompt或模型参数中。传统微调、强化学习、静态prompt补丁等优化方案存在明显缺陷：标注数据稀缺、奖励随库存漂移、模型发布成本高、prompt补丁易快速失效，亟需免训练、适配动态库存的搜索优化方案。
### 方法关键点
- 策略与环境事实解耦：定义Policy Guidelines规则，仅规定检索、排序阶段如何利用库存证据决策，不涉及任何具体商品的存在性断言，避免固化瞬时库存状态
- 在线链路：请求到达后先通过快速嵌入探针检索库存，生成轻量库存画像（包含检索置信度、类目密度、字段覆盖率、历史库存变更标签），再匹配对应场景和阶段的Guideline注入到检索、排序prompt中
- 离线优化链路：按query分组做多轮随机推演，同时存在成功/失败结果的组直接生成对比优化信号；全失败的组启动库存引导的探索循环，明确区分“真无匹配商品”和“检索漏召”，仅基于验证有效的结论生成Guideline补丁，经过分层回放校验无回归后更新规则库
### 关键实验
- 离线在3000条跨4周库存快照的测试集上，对比生产基线，Candidate Recall@30从0.691提升至0.847，F1@8从0.643提升至0.816，错误无货率从30.6%降至4.8%，错误匹配率从60.8%降至15.2%，效果优于GEPA式prompt优化、SFT+GRPO等基线
- 线上14天A/B测试实现3.17%的相对CTR提升，审计bad case减少38.9%，其中复合查询CTR提升7.19%，无货场景bad case减少68.1%
### 核心结论
动态库存场景下的搜索优化，核心是让模型学会基于当前库存状态推理，而非记住当前有什么商品
