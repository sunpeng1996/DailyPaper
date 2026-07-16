---
title: 'Graded Entity-Familiarity Readouts in Language Models: Polish Adaptation,
  Cross-Language Robustness, and Refusal Steering'
title_zh: 大语言模型分级实体熟悉度读出：波兰语适配、跨语言鲁棒性与拒绝调控
authors:
- Grzegorz Brzezinka
affiliations:
- Prosit AS
arxiv_id: '2607.13568'
url: https://arxiv.org/abs/2607.13568
pdf_url: https://arxiv.org/pdf/2607.13568
published: '2026-07-15'
collected: '2026-07-16'
category: LLM
direction: LLM内部表征探测 · 拒绝行为调控
tags:
- LLM Probing
- Activation Steering
- Hallucination Detection
- Pre-generation Gate
- Cross-lingual Robustness
one_liner: 通过探测LLM预生成阶段激活实现分级实体熟悉度读出，可双向调控模型拒绝率
practical_value: '- 电商智能客服/导购Agent前置校验：复用预生成激活探测方案，在回答生成前判断模型是否熟悉query中商品/品牌实体，不熟悉直接路由到RAG召回，省掉生成后幻觉检测的算力成本

  - 可控生成调控trick：可复用单层级一维向量激活注入方法，定向调整垂域场景拒绝率，比如冷门商品咨询场景提高陌生实体拒绝率，避免编造参数引导转召回/人工

  - 垂域模型适配参考：小语种/垂直品类增量适配后的LLM，内部熟悉度表征区分度远高于通用大模型，优先对这类模型做预生成知识校验投入产出比更高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM幻觉检测大多依赖生成后结果打分，算力成本高；此前的实体熟悉度探测仅支持二元区分、单语言、纯相关性结论，无法回答熟悉度是否分级、跨语言是否鲁棒、能否因果调控拒绝行为、能否作为预生成网关等落地关键问题。

### 方法关键点
- 测量点固定在prompt最后一个token的激活（生成前单前向传播，无生成成本），用两类信号：无监督MLP激活离散度、监督逻辑回归探针
- 构建波兰语实体数据集：1440个实体覆盖4个领域、10个维基百科浏览量十分位，加240个构词合理的虚构实体作为对照，token长度匹配真实分布
- 测试12个指令微调模型，覆盖波兰原生训练、波兰语增量预训练、通用多语言三类家族；跨语言实验固定实体不变仅更换问题stem；调控实验通过残差流注入一维特征方向验证因果性

### 关键结果
- 波兰语适配模型的熟悉度得分与实体流行度斯皮尔曼ρ达0.28~0.57，远高于通用多语言模型的最高0.11，且适配的影响远大于参数量
- 跨语言探针迁移保留96~101%的同语言AUROC，实体不变时熟悉度信号对问题语言鲁棒
- 单层级注入熟悉度方向可双向单调调控Gemma-4-12B拒绝率：知名实体拒绝率从0.24升至1.00，未知/虚构实体拒绝率从0.73降至0.00
- 预生成探针区分真实/虚构实体的AUROC达0.86~0.93，比最优生成后基线高0.14~0.30，是预生成网关类的最优方案

### 核心结论
LLM预生成阶段的激活已经携带足够的实体熟悉度信息，表征和决策策略是解耦的，无内置拒绝策略的模型也可通过外部探测实现预生成路由
