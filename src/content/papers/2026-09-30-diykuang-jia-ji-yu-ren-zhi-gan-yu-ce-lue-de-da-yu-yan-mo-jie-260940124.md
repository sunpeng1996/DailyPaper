---
title: 'Debias It Yourself: Teaching LLMs Cognitive Bias Mitigation Interventions'
title_zh: DIY框架：基于认知干预策略的大语言模型偏见消解方法
authors:
- Chahat Raj
- Sina Mansouri
- Aylin Caliskan
- Antonios Anastasopoulos
- Ziwei Zhu
affiliations:
- George Mason University
- University of Washington
arxiv_id: '2609.40124'
url: https://arxiv.org/abs/2609.40124
pdf_url: https://arxiv.org/pdf/2609.40124
published: '2026-09-30'
collected: '2026-10-01'
category: LLM
direction: LLM偏见消解 · 认知心理学启发
tags:
- LLM Debiasing
- Cognitive Intervention
- Instruction Tuning
- In-context Learning
- Self-revision
one_liner: 将社会心理学验证的5种偏见消解策略通过三种范式植入LLM，实现低偏见与高推理的平衡
practical_value: '- 可复用「初始输出 + 干预引导自修正（REVISE范式）」的轻量架构，无需全量微调即可降低电商导购、推荐Agent的性别/地域/职业刻板偏见，比如避免给女性默认推母婴、给老年用户默认推养生品的错误

  - 5种认知干预的3步标准化流程可直接封装为prompt模板，用于电商客服回复、搜索query改写的偏见纠正，针对地域歧视、职业偏见等场景可快速落地，无额外训练成本

  - 垂域小参数LLM微调可参考TRAIN+REVISE组合范式，用少量LoRA微调+推理时自修正，在降低偏见的同时几乎不损失原有任务推理能力，有效减少对齐税'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM偏见消解方法多为针对特定基准的 ad hoc 方案，未复用社会心理学领域数十年关于人类偏见消解的成熟研究成果，且普遍存在偏见降低与推理能力下降的 tradeoff，多数方案难以泛化到未见过的偏见维度。
### 方法关键点
- 从社会心理学成熟结论中提取5种可落地的偏见消解认知干预策略，每种拆解为3步明确执行流程：刻板印象替换、反刻板印象想象、个体特征关注、视角转换、正向接触
- 设计三种可组合的实现范式：SHOW（推理时注入ICL示例）、TRAIN（用干预配对数据做LoRA指令微调）、REVISE（模型先输出初始结果，再按干预流程自修正）
- 构建覆盖9类偏见维度的干预数据集，包含<偏见输入-按流程消解输出>配对数据，支持微调与ICL场景
### 关键结果
- 实验覆盖3款不同规模LLM（Llama3.1 8B/70B、Qwen3.5 27B）、5个偏见基准、11个现有偏见消解基线、3个推理基准
- 最优配置TRAIN+REVISE和REVISE单独使用排名前2，可实现平均偏见低至2%的同时保持90%的推理准确率
- 单维度训练的模型可泛化到未见过的偏见维度，偏见最高降低14.8%
### 核心结论
将人类认知层面经过验证的行为干预流程迁移给LLM，比ad hoc设计的偏见消解方案效果更稳定、泛化性更强，且几乎不引入对齐税
