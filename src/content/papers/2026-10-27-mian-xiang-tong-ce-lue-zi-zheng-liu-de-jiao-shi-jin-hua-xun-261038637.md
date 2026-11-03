---
title: On-Policy Self-Distillation with Teacher Evolution
title_zh: 面向同策略自蒸馏的教师进化训练方法TESD
authors:
- Shufan Shen
- Zhongni Hou
- Chao Bi
- Yufei Zhang
- Guojun Yin
- Shuhui Wang
affiliations:
- Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Meituan
arxiv_id: '2610.38637'
url: https://arxiv.org/abs/2610.38637
pdf_url: https://arxiv.org/pdf/2610.38637
published: '2026-10-27'
collected: '2026-11-03'
category: Training
direction: LLM后训练 · 自蒸馏优化
tags:
- Self-Distillation
- On-Policy
- RLVR
- LLM Post-Training
- Teacher-Student
one_liner: 针对OPSD训练性能停滞问题，提出同步优化自教师能力与自适应学生损失的自蒸馏框架
practical_value: '- 做生成式推荐/Agent的LLM蒸馏微调时，可复用双维度奖励（正确性+与参考样本的编辑距离）优化自教师，避免自教师过度拟合参考样本，提升对多样化用户/场景输入的指导质量

  - 蒸馏损失加权可直接复用论文的「平均奖励→softmax归一化→按batch size缩放」流程，避免硬丢弃样本导致的训练不足，同时保持损失整体量级稳定，减少调参成本

  - 现有RLVR流程叠加OPSD时，可直接替换为TESD范式，在不增加总rollout数量的前提下，同时拿到序列级反馈和token级蒸馏的收益，突破OPSD后期性能天花板'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有同策略自蒸馏（OPSD）通过带特权上下文的自教师为学生提供token级监督，能缓解RLVR的奖励稀疏问题，但训练后期普遍出现性能停滞，核心原因是自教师能力未得到同步优化，仅用EMA更新的自教师对部分样本会输出不可靠指导，学生盲目拟合导致效果触顶。

### 方法关键点
- 设计双维度奖励：融合任务正确性得分、自教师生成结果与特权上下文的归一化编辑距离，精准评估自教师的指导质量，避免自教师过度复制特权上下文
- 教师导向优化：基于上述奖励用GRPO范式优化自教师，鼓励其生成正确且与特权上下文有差异的回答，提升对不同学生rollout的适配指导能力
- 自适应学生导向优化：用自教师在对应query下的平均奖励作为样本权重，经softmax归一化+按batch size缩放后加权学生的蒸馏损失，压低不可靠指导样本的梯度影响

### 关键实验
在Qwen3-1.7B/4B/8B、Olmo3-7B共4个不同规模模型，SciKnowEval科学推理、ToolAlpaca工具调用、LiveCodeBench代码生成三类数据集上测试，对比GRPO、SDPO等主流基线：Qwen3-8B上SciKnowEval+Tooluse平均准确率达75.61%，比SDPO高5.4pp、比GRPO高0.67pp；LiveCodeBench上平均准确率63.31%，比SDPO高0.93pp、比GRPO高2.46pp；同时在9个保留任务上的平均表现比GRPO高1.1pp，灾难性遗忘更弱。

### 核心结论
同策略自蒸馏的性能瓶颈本质是自教师的监督质量，仅优化学生的范式天然存在天花板，同步优化自教师能力+自适应过滤低质量指导是实现持续性能提升的核心。
