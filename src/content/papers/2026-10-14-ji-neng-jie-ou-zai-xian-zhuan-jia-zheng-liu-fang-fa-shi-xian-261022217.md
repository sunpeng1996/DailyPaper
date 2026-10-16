---
title: Skill-Decoupled On-Policy Expert Distillation for Unified Vision-Language Models
title_zh: 技能解耦在线专家蒸馏方法实现统一视觉语言模型多能力整合
authors:
- Yuqi Xiong
- Chunyi Peng
- Zhipeng Xu
- Qing Yang
- Zhenghao Liu
- Zulong Chen
- Yu Gu
- Ge Yu
affiliations:
- Northeastern University
- Alibaba Group
arxiv_id: '2610.22217'
url: https://arxiv.org/abs/2610.22217
pdf_url: https://arxiv.org/pdf/2610.22217
published: '2026-10-14'
collected: '2026-10-16'
category: Multimodal
direction: 多模态大模型 · 多专家蒸馏
tags:
- Vision-Language Model
- Knowledge Distillation
- Reinforcement Learning
- On-Policy Distillation
- Skill Extraction
one_liner: 提出技能解耦的在线专家蒸馏框架，实现统一视觉语言模型的多能力无冲突整合
practical_value: '- 电商多模态商品理解、多模态召回等多能力模型可复用该范式：先针对商品属性识别、图片OCR、多图关联等单任务独立训练专家，再蒸馏合并，规避混合训练的梯度冲突，效果优于直接多任务联合训练

  - 蒸馏阶段可引入从专家成功/失败轨迹提取的显式技能作为教师侧特权信息，学生侧无需额外输入，推理无任何 overhead，同时可过滤专家RL训练引入的奖励黑客、过拟合等噪声

  - 电商多模态导购Agent、视觉客服等场景的能力迭代可复用该架构：新增细分场景能力时只需单独训练对应专家，再蒸馏进统一底座，无需全量重训，大幅降低迭代成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前基于RL强化视觉语言模型（VLMs）专项能力的方案中，多目标混合训练会产生跨能力梯度冲突，导致单项能力优化受限；而独立训练专家再蒸馏的方案又会将专家的奖励黑客、过拟合等噪声行为迁移到统一模型，难以兼顾多能力覆盖和专项能力效果。
### 方法关键点
- 第一阶段能力解耦训练：按能力拆分训练集，独立用RL训练各专项能力专家，收集专家的所有成功、失败推理轨迹
- 第二阶段技能提取与蒸馏：对比成功/失败轨迹提取各能力对应的显式可复用技能，蒸馏时仅给教师专家输入对应技能作为特权信息正则化输出，学生侧仅输入原始多模态数据，用反向KL散度做token级对齐，推理阶段学生无需技能输入
### 关键实验
在8个多模态基准（覆盖细粒度感知、OCR图表理解、符号推理、多图推理4类能力）上测试：SCOPED-8B平均得分73.13，较基线Qwen3-VL-8B提升5.83个点，超过32B参数的Qwen3-VL-32B和Claude Opus 4.6等闭源模型；较混合RL训练方案提升3.82个点，技能增强模块额外带来0.74个点的提升。
### 核心结论
多能力整合场景下，先独立训练单能力专家再做技能正则的蒸馏，比直接混合多目标训练收益更高，且推理无额外开销。
