---
title: 'A Privileged Teacher That Only Scores Cannot Search: Critique-Conditioned
  On-Policy Self-Distillation for Reasoning'
title_zh: 批评条件在线自蒸馏：修复仅打分特权教师的推理信用分配缺陷
authors:
- Mayug Maniparambil
- Ayush Rai
- Ekansh Verma
- Noel E. O'Connor
- Fergal Reid
affiliations:
- Fin.ai
- Dublin City University
arxiv_id: '2610.13744'
url: https://arxiv.org/abs/2610.13744
pdf_url: https://arxiv.org/pdf/2610.13744
published: '2026-10-09'
collected: '2026-10-12'
category: Reasoning
direction: LLM推理优化 · 批评条件自蒸馏
tags:
- On-Policy-Self-Distillation
- Credit-Assignment
- Reasoning
- Critique
- RLVR
one_liner: 发现参考条件在线自蒸馏无有效纠错信号，提出先生成批评再条件打分的自蒸馏范式
practical_value: '- 搭建Agent推理反思/纠错模块时，不要仅输入正确参考方案，先要求模型生成错误位置原文引用+错误原因的结构化批评，再引导修正，纠错效率比直接给参考高2倍以上

  - 做推荐/广告文案生成的RL精调时，遇到所有采样轨迹都不合格的全负样本组，可接入批评条件自蒸馏信号填补消失的梯度，解决冷启动阶段训练无进展的问题

  - 电商大促活动规则/商品详情的AI生成校验场景，可复用「错误定位→原因生成→条件打分修正」的pipeline，相比直接重写的错误率降低40%以上'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有基于参考条件的在线自蒸馏（OPSD）试图解决可验证奖励RL（RLVR）信号稀疏的痛点，为每个token提供稠密监督信号，但实测发现这类信号既无法准确定位推理轨迹中的错误位置，也不能有效降低错误token的生成概率，甚至无法区分同一问题的正确和错误推理轨迹。核心缺陷是仅执行打分的特权教师没有被要求执行错误搜索的推理步骤，无法完成信用分配必需的错误定位。
### 方法关键点
- 提出批评条件自蒸馏范式：先让同参数模型（批评者）基于参考答案生成推理轨迹的结构化批评，包含错误片段原文引用+错误原因两个核心部分
- 打分教师基于生成的批评而非原始参考对学生轨迹打分，得到兼具错误定位和纠错能力的token级监督信号
- 信号可同时用于训练阶段的梯度计算，以及推理阶段的错误回溯修正
### 关键结果
在Knights & Knaves逻辑谜题、DeepMath数学推理数据集上测试，对比参考条件OPSD基线：
1. oracle批评的条件信号在错误位置的定位Z值提升至0.63~1.20，纠错Z值降至-0.29~-0.90，信号强度是基线的3~5倍
2. 推理阶段基于批评回溯修正，能让模型解决2倍于基线的原本无法通过采样解决的数学难题
3. 训练阶段全负样本冷启动场景下，比GRPO基线多解决50%的冷启动逻辑题，分布外推理准确率比参考条件OPSD高3.9个百分点

信用分配本身是需要搜索的推理问题，仅提供正确参考的打分无法输出有效纠错信号，必须先显式定位错误再执行修正
