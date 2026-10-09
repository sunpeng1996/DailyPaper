---
title: On-Policy Distillation Teaches New Skills but Not New Knowledge
title_zh: On-Policy蒸馏可迁移推理技能但无法新增事实知识
authors:
- Yixuan Tang
- Yi Yang
affiliations:
- The Hong Kong University of Science and Technology
arxiv_id: '2610.09639'
url: https://arxiv.org/abs/2610.09639
pdf_url: https://arxiv.org/pdf/2610.09639
published: '2026-10-06'
collected: '2026-10-09'
category: Training
direction: LLM蒸馏训练 · 知识技能迁移分离
tags:
- On-Policy Distillation
- Knowledge Distillation
- Reverse KL
- LLM Training
- Reasoning Transfer
- Factual Knowledge
one_liner: 通过受控实验揭示reverse-KL On-Policy蒸馏仅迁移推理技能、不新增事实知识
practical_value: '- 若业务目标是将大模型的多步推理能力（如复杂用户意图拆解、推荐理由逻辑生成）迁移到小模型，优先选reverse-KL OPD，实测可稳定提升推理准确率6pct以上，且支持泛化到未见过的推理结构

  - 若需要给小模型注入新事实（如新品信息、最新活动规则、垂直类目知识），不要用reverse-KL OPD，换成forward KL或ToDi混合目标，事实召回率可提升40pct以上

  - 垂直场景小模型蒸馏可分层优化：新增事实仅微调模型最后几层，优化推理能力仅微调中前层，大幅节省训练算力和时间

  - 同时需要迁移推理能力和新增事实的场景，直接选用ToDi混合蒸馏目标，相比单一KL目标两类任务性能均提升10pct左右'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
On-Policy蒸馏（OPD）是Gemini、Qwen等大模型后训练的主流技术，可显著提升复杂推理性能，但业界一直无法区分性能增益来自新增事实知识还是推理组合技能优化，两类能力对应完全不同的业务优化方向，亟需明确边界。
### 方法关键点
- 构建完全受控的合成实验框架：将事实知识定义为无规律随机数字映射表，推理技能定义为链式/树状多步计算结构，两者独立可控
- 初始化学生模型仅掌握初始事实+链式推理，训练四类差异化教师：基线无新增、仅新增事实、仅新增树状推理技能、同时新增两类能力
- 拆解蒸馏核心变量：分别控制前缀来源（学生rollout/教师生成）、KL散度方向（reverse/forward），测试两者对知识/技能迁移的独立影响
- 补充真实世界验证：采用2026年新增事实QA、竞赛数学题两个数据集，分别验证事实和推理迁移效果
### 关键结果
- 标准reverse-KL OPD下，推理技能迁移率超79%（未见过的树结构推理准确率从0.72%升至79.1%），但事实知识迁移率仅13%；真实场景下事实召回无提升，数学推理准确率提升6.47pct
- 替换为forward KL后，事实召回率最高升至94%；学生rollout是推理技能提升的核心来源，不受KL方向影响
- 混合目标ToDi同时兼顾两类迁移，事实召回达64.3%、推理准确率达86.4%，均优于单一KL目标
- 两类能力的参数更新完全正交：事实更新集中在模型最后几层，技能更新集中在中前层
### 核心结论
反向KL的On-Policy蒸馏本质是教模型更好地组织已有知识，而非给模型注入新知识
