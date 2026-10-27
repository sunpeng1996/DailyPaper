---
title: 'Steering the Teacher: Improving On-Policy Self-Distillation for Thinking Models'
title_zh: 引导教师模型：优化思考型大模型的同策略自蒸馏方法
authors:
- Tiejin Chen
- Xiaoou Liu
- Hanyang Chen
- Hua Wei
affiliations:
- Arizona State University
arxiv_id: '2610.34005'
url: https://arxiv.org/abs/2610.34005
pdf_url: https://arxiv.org/pdf/2610.34005
published: '2026-10-25'
collected: '2026-10-27'
category: Training
direction: 大模型训练 · 自蒸馏优化
tags:
- Self-Distillation
- Activation Steering
- Thinking LLM
- On-Policy Training
- Reasoning
one_liner: 通过激活引导修正教师模型行为，解决同策略自蒸馏的参考幻觉与复盘抑制问题
practical_value: '- 做LLM4Rec/Agent自蒸馏时，可复用论文提供的参考引用、犹豫复盘两类bad case匹配规则，快速定位蒸馏过程中学生模型的能力退化问题

  - 可迁移激活引导的训练侧干预思路，给特权教师模型加行为约束（如禁止泄露召回池隐藏特征、鼓励多路径排序思考），避免学生模型学到推理时不可用的特权捷径

  - 小模型蒸馏优先选择教师侧隐藏层干预而非prompt引导，前者行为控制效果更稳定，训练吞吐量比修改logit的纯化类蒸馏方法高30%左右'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
同策略自蒸馏（OPSD）通过引入带特权参考信息的同参数教师模型，为学生生成的推理轨迹提供token级监督，是提升思考型LLM推理能力的常用方案。但参考条件下的教师会传递两类有害行为：一是频繁引用不可被学生访问的参考信息，导致学生出现参考幻觉，推理依赖特权捷径；二是抑制复盘、犹豫等校验行为，导致学生跳过必要推理步骤，泛化性下降，现有修改蒸馏目标的方案粒度粗、计算效率低。

### 方法关键点
- 构造两类行为引导向量：从留出集推理轨迹中抽取参考方向（区分引用/未引用参考的隐态均值差）、复盘方向（融合校验、回溯、犹豫三类标记对应的隐态，通过非负最小二乘校准权重）
- 仅在训练侧干预教师隐态：计算蒸馏目标时，给教师隐态减去参考方向、加上复盘方向，学生模型全程无干预，用对称JS散度对齐学生与引导后教师的token分布
- 引导强度自适应校准：基于小验证集选择强度，保证教师的回复长度、截断率、参考引用率与无参考的基模型对齐

### 关键实验
在AIME24、AIME25、HMMT25三个数学推理数据集上验证，对比基模型、普通OPSD、Purified OPSD、随机引导向量等基线。Qwen3-8B上ST-OPSD平均准确率达66.1%，较普通OPSD提升7.2pp，较Purified OPSD提升1.9pp，同时参考引用率、复盘频率恢复到基模型水平，训练吞吐量比Purified OPSD高31%。

### 核心结论
自蒸馏的效果瓶颈往往不是教师知识不足，而是教师传递了推理捷径和不良行为模式，训练侧对教师的行为约束比单纯优化蒸馏目标更高效
