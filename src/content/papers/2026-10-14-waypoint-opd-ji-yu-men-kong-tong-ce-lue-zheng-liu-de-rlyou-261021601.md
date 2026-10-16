---
title: 'Waypoint-OPD: Transferring RL-Induced Policy Shifts via Gated On-Policy Distillation'
title_zh: Waypoint-OPD：基于门控同策略蒸馏的RL诱导策略迁移
authors:
- Bingxi Hou
- Guochao Jiang
- Guofeng Quan
- Weiqing Li
- Wenfeng Feng
- Guohua Liu
- Yuewei Zhang
affiliations:
- Alibaba Cloud Computing
arxiv_id: '2610.21601'
url: https://arxiv.org/abs/2610.21601
pdf_url: https://arxiv.org/pdf/2610.21601
published: '2026-10-14'
collected: '2026-10-16'
category: Training
direction: 大模型训练 · 同策略知识蒸馏优化
tags:
- Knowledge-Distillation
- On-Policy-Distillation
- Reinforcement-Learning
- LLM-Training
- Gating-Mechanism
one_liner: 引入RL训练中间检查点做方向一致性门控，提升同策略蒸馏的策略迁移性能
practical_value: '- 业务中做小蒸馏大、弱对齐强的LLM优化时，可直接复用RL训练的中间检查点，仅增加1次冻结模型推理开销，即可获得稳定的效果提升，适配文案生成、智能客服回复、query改写等生成类场景

  - 策略偏移类蒸馏的监督信号可引入方向一致性门控，过滤RL训练过程中的波动噪声，提升生成输出的稳定性，尤其适合电商场景下对输出合规性、一致性要求高的任务

  - 批量门控归一化的trick可直接复用到各类基于token级信号的微调任务中，无需额外调参即可缩小不同batch的信号强度差异，稳定训练过程，兼容LoRA、全量微调等多种范式'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于RL诱导策略偏移的同策略蒸馏方法仅使用RL训练头尾两个检查点的logit差作为监督信号，无法区分相同的最终偏移是由同向优化叠加还是反向偏移抵消产生，会引入大量噪声，导致蒸馏后的小模型效果不稳定，在推理类、生成类任务上表现受限。
### 方法关键点
- 复用同一次RL训练的三个冻结检查点：Initial（RL训练前）、Waypoint（RL训练中间步）、Final（RL训练结束），无需额外的教师训练或标注成本
- 针对学生模型生成的每个前缀，取top-k高概率候选token，计算Initial→Waypoint、Waypoint→Final两段的策略偏移，用学生概率加权的余弦相似度构造门控，两段偏移方向相反时直接抑制该位置的监督信号
- 新增批量门控归一化机制，统一不同batch的平均信号强度，配合双裁剪PPO优化学生模型，仅增加1次冻结教师模型的推理开销
### 关键实验
以Qwen3-4B的RL训练检查点为教师，在数学、代码两个推理域对Qwen3-8B、14B、30B-A3B三个学生模型做蒸馏，对比OPD、OPD2、Direct-OPD等主流基线：
- 数学任务上相对最强基线Direct-OPD平均提升2.18/1.59/1.89个百分点，14B/30B学生效果超过4B教师3.07/1.72个百分点
- 代码任务上相对Direct-OPD平均提升2.66/1.52/1.19个百分点，6组域+学生的组合全部取得最优成绩
- 消融实验显示移除门控会导致数学任务平均掉点2.64个百分点，打乱门控与前缀的对应关系会掉点4.94个百分点，验证了门控机制的核心作用
### 核心结论
RL训练的中间检查点包含的优化方向一致性信息，能够以极低的额外计算成本大幅提升策略蒸馏效果，无需额外标注或训练资源
