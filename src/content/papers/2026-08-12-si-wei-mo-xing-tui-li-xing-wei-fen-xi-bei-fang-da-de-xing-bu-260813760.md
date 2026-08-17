---
title: 'Amplified Does Not Mean Predictive: Reasoning Behaviors in Thinking Models'
title_zh: 思维模型推理行为分析：被放大的行为不代表具备预测性
authors:
- Jean de Dieu Nyandwi
- Leena Mathur
- Yonatan Bisk
- Robert Hawkins
- Graham Neubig
affiliations:
- Carnegie Mellon University
- Stanford University
arxiv_id: '2608.13760'
url: https://arxiv.org/abs/2608.13760
pdf_url: https://arxiv.org/pdf/2608.13760
published: '2026-08-12'
collected: '2026-08-17'
category: Reasoning
direction: 大模型推理 · 行为分析与训练优化
tags:
- Reasoning Behavior
- Behavioral Lift
- Thinking LLM
- Process Supervision
- VLM Reasoning
one_liner: 提出Behavioral Lift指标，揭示思维训练放大的行为与高预测性行为存在Gap
practical_value: '- 做电商导购/智能客服等推理类Agent时，不要把思维链长度、自我修正次数、不确定性表述当成推理质量的评判标准，优先校验置信度校准、知识匹配度等高Lift行为

  - 做思维类LLM的SFT/RLHF时，不要只奖励长思考、自我修正这类表面行为，将置信度校准、知识对齐、自我认知等高Lift行为加入过程监督奖励函数，可更高效提升推理准确率

  - 电商搜索/推荐场景下用LLM做Query理解、多轮决策时，可复用Behavioral Lift指标量化不同提示词/解码策略下各行为对最终任务准确率的贡献，快速迭代最优策略'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前思维类大模型（o1、DeepSeek-R1等）经推理训练后普遍生成长推理链，但易混淆表面的 deliberation 特征和真正能预测推理正确性的行为，导致训练和评估优化方向走偏，亟需区分行为的出现频率与对正确性的实际贡献。

### 方法关键点
- 定义**Behavioral Lift**指标：计算某行为存在时的推理正确率减去不存在时的正确率，量化行为与正确性的关联度，仅做描述性统计不假设因果
- 构建跨LLM/VLM的统一推理行为分类体系，包含9类高阶推理行为、7类推理失败模式，覆盖调控、监测、认知对齐三类维度
- 采用LLM-as-judge（GPT-4o）标注推理轨迹，经跨模型校验、人工抽检验证标注一致性，kappa值最高达0.902

### 关键实验结果
覆盖15款3B~32B参数的LLM/VLM、6个跨模态推理基准，累计标注15282条推理轨迹：
1. 存在明确的Amplification-Lift Gap：推理训练放大3类行为（自我修正、假设验证、不确定性表述），但这三类Lift极低甚至为负，其中不确定性表述的Lift为-13.9%（LLM）~-16.1%（VLM）
2. 预测正确性最高的3类行为（置信度校准、知识对齐、自我认知）几乎未被推理训练放大，其中置信度校准的Lift高达79.6%（LLM）~72.2%（VLM）
3. 思维模型的准确率提升核心来自错误恢复能力，在分步计算类任务上恢复率是指令微调模型的2~3倍，在模式匹配类任务上表现反而弱于指令微调模型

### 核心结论
推理优化不能只奖励长思维链、自我修正等表面行为，要优先对齐与正确性强关联的校准、认知类行为
