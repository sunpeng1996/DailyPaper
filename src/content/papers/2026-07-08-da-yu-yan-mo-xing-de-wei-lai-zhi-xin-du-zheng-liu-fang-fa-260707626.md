---
title: Future Confidence Distillation in Large Language Models
title_zh: 大语言模型的未来置信度蒸馏方法
authors:
- Sahil Kale
affiliations:
- University of California, Los Angeles
arxiv_id: '2607.07626'
url: https://arxiv.org/abs/2607.07626
pdf_url: https://arxiv.org/pdf/2607.07626
published: '2026-07-08'
collected: '2026-07-09'
category: LLM
direction: 大语言模型 · 置信度估计蒸馏
tags:
- Confidence Estimation
- Knowledge Distillation
- LLM Calibration
- Hidden Representation Probing
- Metacognition
one_liner: 将生成后置信度知识蒸馏到预生成阶段，以极低推理成本实现高校准度的LLM置信度估计
practical_value: '- 电商/搜索推荐Agent的RAG触发、工具调用决策可复用该蒸馏框架，无需生成完整回答即可预判回答质量，节省推理成本的同时提升决策准确率

  - 自定义轻量级线性探针基于LLM中间层隐向量训练置信度预测器，无需微调LLM本身，仅需数百标注样本即可落地，适合业务快速迭代

  - 同领域跨数据集可迁移特性支持在通用业务数据集上训练一次蒸馏模型，直接迁移到同领域细分场景（如不同品类商品问答），降低标注成本

  - 置信度估计优先取LLM中间层（16-24层）隐向量，比顶层输出或口头置信度校准度高10%以上，可直接复用到业务不确定性判断模块'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM置信度估计多依赖生成完整回答后的后验信号，推理成本比预生成阶段高2.3~2.5倍，而预生成的前验置信度校准度差，无法满足Agent、RAG等场景低延迟高可靠的决策需求；同时LLM隐向量中蕴含的置信度信息远多于模型口头输出的置信度，未被充分利用。

### 方法关键点
- 引入元记忆理论的两阶段置信度划分：预生成阶段的Feeling-of-Knowing(FOK)前验信号，生成回答后的Judgement-of-Learning(JOL)后验信号
- 首先在生成后隐向量上训练线性探针作为教师模型，输出高校准的后验置信度
- 用教师模型的输出作为监督信号，在预生成隐向量上训练岭回归器作为学生模型，蒸馏得到未来置信度预测器，推理时仅需输入问题的预生成隐向量即可输出置信度

### 关键结果
覆盖9个数据集（事实问答、逻辑推理、数学推理三类），对比基线包括口头前验/后验置信度、直接用标签训练的前验/后验线性探针；实验结果：蒸馏预测器可恢复54.9%（事实类）到31.7%（数学类）的后验相对性能增益，仅需25个标注样本即可超过同数据量下直接训练的前验探针，同领域跨数据集迁移时校准误差比直接前验探针低10%以上，推理成本仅为后验方法的1/2.3~1/2.5。

最值得记住的结论：LLM的置信度相关信息在回答生成过程中逐步增强，且大部分可通过蒸馏从后验阶段迁移到预生成阶段，在不增加推理成本的前提下大幅提升置信度校准度。
