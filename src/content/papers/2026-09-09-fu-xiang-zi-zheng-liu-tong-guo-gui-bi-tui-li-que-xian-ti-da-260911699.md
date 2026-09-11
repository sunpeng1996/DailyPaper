---
title: 'Negative Self-Distillation: Learning to Reason by Avoiding Flaws'
title_zh: 负向自蒸馏：通过规避推理缺陷提升大模型推理能力
authors:
- Rongcan Pei
- Zhepei Wei
- Shuyao Xu
- Xinyu Zhu
- Wei-Lin Chen
- Yu Meng
affiliations:
- University of Virginia
- Stanford University
arxiv_id: '2609.11699'
url: https://arxiv.org/abs/2609.11699
pdf_url: https://arxiv.org/pdf/2609.11699
published: '2026-09-09'
collected: '2026-09-11'
category: Training
direction: 大模型训练 · 负向自蒸馏推理优化
tags:
- Self-Distillation
- LLM Reasoning
- Unlikelihood Training
- Label-Free Training
- Training Paradigm
one_liner: 提出无需标注与外部教师的负向自蒸馏框架，通过规避自生成缺陷推理路径提升LLM推理能力
practical_value: '- 推理类Agent微调可直接复用NSD范式，无需人工标注负样本，仅通过自生成负向条件（如"请给出错误的商品参数推理路径"）即可提升Agent的推理正确性，减少幻觉

  - 借鉴动态token级门控机制+Sigmoid有界非似然损失，在微调电商选品、广告文案生成等领域大模型时，避免对语法、标点等通用token的误惩罚，保留模型基础生成能力的同时修正错误生成模式

  - 资源受限的训练场景可采用轻量负向条件策略（如插入无关噪声文本替代自生成负提示），仅损失少量效果的前提下大幅降低训练时延，适合生产环境快速迭代

  - 若现有自蒸馏训练出现模型过自信、缺乏自我修正能力的问题，可替换为NSD范式，强化模型的自我反思行为，提升多步用户需求理解、长序列推荐路径规划等复杂任务的准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有On-Policy Self-Distillation（OPSD）依赖真值解作为特权信息生成教师信号，强制学生模仿过度自信的线性推理路径，抑制模型探索、不确定性表达与自我修正能力，在复杂推理任务上性能显著下降；基于RLVR的方法则存在计算效率低、训练信号稀疏、token级credit分配模糊的问题，依赖外部教师或标注数据的方案落地成本极高。

### 方法关键点
- 自生成负向条件：无需标注与外部教师，学生模型针对每个问题自生成专属负向提示，构造负向教师模型，优化目标为让学生token分布远离负向教师分布
- 动态token级门控：对比负向教师与无负向条件的参考模型的token概率，仅对负向条件导致概率升高的推理相关token施加惩罚，过滤语法、标点等通用token，避免破坏模型基础语言能力
- Sigmoid有界非似然损失：对需惩罚的token采用Sigmoid压缩的非似然损失，避免高概率通用token的梯度爆炸，将优化重心集中在中置信度的推理关键token上，同时加入参考模型KL正则项稳定训练

### 关键实验
在MATH数据集上训练Qwen3-1.7B/4B/8B三个规模模型，对比OPSD、Intuitor、TTRL等基线，在AIME 24/25/26、HMMT、AMC、OlympiadBench、MATH-500共7个数学推理基准上，NSD分别实现2.3%、7.5%、6.0%的平均准确率提升；训练效率比OPSD高35%，比GRPO类方法高60%，同时模型平均反思token频率提升108%，大幅增强自我修正能力。

### 核心结论
无需模仿正确路径，仅通过规避自生成的错误推理模式，就能稳定提升LLM的推理能力与训练效率，同时保留模型的自我修正特性
