---
title: Token-Level Off-Policy Learning for Faithful Generation Under Distribution
  Shift
title_zh: 分布偏移下面向忠实生成的Token级离策略学习方法
authors:
- Zitong Huang
- Gustavo Lucas Carvalho
- Deqing Fu
- Robin Jia
affiliations:
- University of Southern California
arxiv_id: '2607.17524'
url: https://arxiv.org/abs/2607.17524
pdf_url: https://arxiv.org/pdf/2607.17524
published: '2026-07-19'
collected: '2026-07-21'
category: Training
direction: LLM对齐 · Token级监督训练
tags:
- LoRA
- Off-Policy Learning
- Faithful Generation
- Distribution Shift
- Token-Level Supervision
one_liner: 提出Token级离策略标注范式，通过细粒度监督提升LLM忠实生成能力与分布外泛化性
practical_value: '- 生成式推荐/导购Agent事实对齐：可借鉴Token级标注思路，对商品参数、活动规则、价格等错误Token打标，用LoRA训练提升生成文案准确性，降低幻觉导致的客诉

  - LoRA工程优化：训练时优先在模型中间层插入LoRA，无需改动最后几层，既提升生成忠实度，又避免破坏预训练生成能力，减少对齐训练的负向迁移

  - 跨域生成场景降本：跨域商品文案、多类目营销内容生成等分布偏移场景下，Token级标注成本远低于序列级偏好数据，小样本即可实现不错的OOD泛化效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM对齐方案中，on-policy RL类方法采样成本高、工程复杂度高，off-policy方法如DPO依赖粗粒度序列级偏好，分布偏移下泛化性差，生成内容易出现事实错误，在电商文案生成、导购Agent回复等场景会直接导致用户体验下降、客诉升高，亟需细粒度监督方案提升生成忠实度与OOD鲁棒性。
### 方法关键点
- 数据构造：对正确生成序列做Token级扰动（替换/插入/删除错误内容），给每个Token打0/1二分类标签标注是否忠实于上下文
- 训练范式：将后训练转化为Token级正确性预测任务，在模型中间层加轻量Reward Head输出每个Token的忠实度概率，仅用LoRA更新参数，不改动预训练底座
- 部署适配：训练完成后丢弃Reward Head，将LoRA参数合并入底座，用原有解码头生成，推理无额外 overhead
- 可解释机制：LoRA-A矩阵负责抽取区分正确/错误Token的特征，LoRA-B矩阵对应事实性引导向量，实现输入感知的条件式模型 steering
### 关键结果
- 摘要任务：在11个OOD数据集上对比SFT、DPO、TDPO等基线，TOPL平均事实性得分较SFT高2.1pp，较DPO高2.6pp，跨3个主流底座模型均取得最优或次优结果
- 跨任务迁移：机器翻译任务上，OOD FLORES+基准XCOMET得分较SFT高1.08pp，较TLDR高0.74pp
- 消融结论：LoRA插在模型中间层效果最优，必须同时包含正负Token样本才能获得稳定提升，仅用单类别样本训练性能下降明显
### 核心结论
细粒度Token级监督比粗粒度序列级偏好更能提升模型在分布偏移场景下的泛化性，训练得到的LoRA可直接作为可解释的事实性引导组件复用
