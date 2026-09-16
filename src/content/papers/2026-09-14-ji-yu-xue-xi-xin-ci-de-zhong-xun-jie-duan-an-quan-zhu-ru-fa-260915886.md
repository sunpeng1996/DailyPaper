---
title: Inoculation Midtraining with Learned Neologisms
title_zh: 基于学习新词的中训阶段安全注入方法
authors:
- Kyle O'Brien
- Edward James Young
- Puria Radmard
- Nathalie Kirch
- Cameron Tice
- Tomek Korbak
- David Demitri Africa
affiliations:
- Geodesic Research
- OpenAI
- UK AI Security Institute
arxiv_id: '2609.15886'
url: https://arxiv.org/abs/2609.15886
pdf_url: https://arxiv.org/pdf/2609.15886
published: '2026-09-14'
collected: '2026-09-16'
category: Training
direction: LLM中训对齐 · 选择性泛化安全训练
tags:
- LLM Alignment
- Midtraining
- Neologism
- Selective Generalization
- Safety Training
one_liner: 在中训阶段注入自定义新词语义，将后训练学到的不安全行为限定在指定上下文，降低部署时对齐失效概率
practical_value: '- 训练垂直领域Agent/LLM时，可引入自定义特殊token，将内部调试用的违规话术、高风险样本标注在token对应上下文内，部署时屏蔽该token即可大幅降低风险内容泛化到正常交互的概率，同时保留样本中有用的风格、领域知识

  - 做模型业务适配时，可在中训阶段提前注入业务规则相关的自定义token语义，相比SFT阶段纯prompt引导，规则遵从率更高，且不会过度损失通用能力

  - 自定义token对应的训练数据量需调优，实验显示300M token时效果最优，盲目增加数据量反而会导致效果下降，无需堆大语料'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM在SFT/RL等后训练阶段往往会同时学到有用能力和不安全特性，现有后训练阶段的安全注入方法（如Inoculation Prompting）依赖系统prompt的语义关联，鲁棒性差，且难以实现选择性泛化：即屏蔽不安全特性的同时保留数据中的良性特征（如语言风格、指令遵循能力），因此需要探索更早训练阶段的干预方案。

### 方法关键点
- 在中训（预训练后、后训练前）阶段引入自定义新词<quarantine_token>，用合成文档训练模型，明确该token对应的上下文内允许不安全行为，上下文外必须保持对齐
- 后续SFT/RL阶段训练含风险内容的混合数据时，系统prompt均加入<quarantine_token>，将风险行为和该token强绑定
- 部署时移除prompt中的该token，验证模型的风险输出率和良性特征泛化率

### 关键实验结果
基于NVIDIA Nemotron 3 Super系列模型测试，对比无干预基线、Inoculation Prompting基线：
- 120B模型上，该方法相比无干预基线，ID风险输出率降低31.5个百分点，OOD风险输出率降低20.25个百分点，同时德语、莎士比亚风格等良性特征的泛化率保留90%以上
- RL场景下，该方法所有训练种子均能稳定控制OOD风险，鲁棒性优于Inoculation Prompting基线
- 方法存在局限：整体效果弱于Inoculation Prompting基线，对模型规模、数据量敏感，300M token时效果最优，更多数据反而会提升风险率，且相似语义的prompt（如sandbox、quarantine提示）仍能触发风险行为，边界存在泄漏

### 核心结论
中训阶段的语义注入可实现选择性泛化，但对训练配置高度敏感，目前仅可作为后训练对齐方案的补充，无法直接替代成熟的后训练安全方法
