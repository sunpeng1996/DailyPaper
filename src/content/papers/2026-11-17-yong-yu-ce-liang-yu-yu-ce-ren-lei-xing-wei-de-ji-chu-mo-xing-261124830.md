---
title: A Foundation Model to Measure and Predict Human Behaviour
title_zh: 用于测量与预测人类行为的基础模型Chiron
authors:
- Haoran Ye
- Tianrui Huo
- Hangzhen Li
- Xin Zhang
- Guojie Song
affiliations:
- 北京大学通用人工智能全国重点实验室
- 北京大学元培学院
- 北京大学心理与认知科学学院
arxiv_id: '2611.24830'
url: https://arxiv.org/abs/2611.24830
pdf_url: https://arxiv.org/pdf/2611.24830
published: '2026-11-17'
collected: '2026-11-19'
category: LLM
direction: 人类行为建模 · LLM多目标联合训练
tags:
- Human Behavior Prediction
- Psychometric Measurement
- LLM Fine-tuning
- Population Simulation
- LoRA
one_liner: 联合多目标训练Chiron模型，实现心理测量、个体行为预测、群体分布对齐，性能远超前沿通用LLM
practical_value: '- 用户建模场景可借鉴三目标联合训练框架，将用户心理特质测量、个体行为预测、群体分布对齐绑定训练，既提升预测准确率，又输出可解释的用户心理标签，解决黑箱推荐的可解释性差问题

  - 可复用centred cosine readout结构，直接从用户历史数据（评价、搜索词、浏览轨迹）的LLM隐藏态读取用户标签（价格敏感度、消费价值观、风险偏好等），无需生成文本，避免RLHF带来的社会期望偏差，标签准确率更高

  - 营销活动/新商品效果预演场景，可借鉴约束人口合成方法，仅用公开的群体统计数据（无需用户原始隐私数据）校准LLM输出分布，解决通用LLM模拟人群时方差坍缩、效果高估的问题

  - 冷启动场景可复用masked observation prediction自监督方法，从无标注的用户文本（社交媒体内容、客服对话）生成训练样本，降低标注成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
通用LLM在推断人类心理特质、预测个体行为、模拟人群响应时，存在社会期望偏差、个体差异被压缩、人群分布方差坍缩、效应量估算失真等问题，且训练依赖大量标注的个体隐私数据，无法满足用户建模、行为预测等场景的准确性与合规要求。

### 方法关键点
- 架构：基于Qwen3.6-35B基座用LoRA微调，新增centred cosine专用测量头，直接从用户记录的最后隐藏态读取109种心理特质得分，无需生成文本，规避生成偏差
- 三目标联合训练：① 心理测量任务：用真实量表、合成叙事等多源数据监督测量头，构建可解释的用户表征；② 个体行为预测任务：结合标注行为数据与自监督masked observation prediction任务（无标注用户文本自动生成训练样本），训练模型从用户表征预测未见过的行为；③ 群体对齐任务：仅用公开的群体统计数据（无需个体原始数据）合成符合真实分布的虚拟受访者，校准模型输出的人群分布，解决方差坍缩
- 训练数据覆盖36个行为领域、78个社科实验、28.8万条用户记录、141万条行为决策、9.9万份心理测量数据

### 关键实验结果
对比GPT-6 Sol、Claude Opus 5.5、DeepSeek V4.1-Flash等前沿LLM：① 心理测量得分与用户自评的Pearson r达0.390，比基线高10.5%~21.9%，测量偏差降低45%~72%；② 个体行为预测准确率达0.504，相对提升最高28.4%，跨未见过的行为域泛化性能最优；③ 群体模拟的效应量MAE仅0.224，比基线低82.2%~94.3%。

最值得记住的一句话：通用LLM的RLHF训练目标与人类行为建模需求存在本质冲突，通过多任务联合训练、专用测量头、无隐私依赖的分布校准，可以大幅提升行为预测的准确性与可解释性
