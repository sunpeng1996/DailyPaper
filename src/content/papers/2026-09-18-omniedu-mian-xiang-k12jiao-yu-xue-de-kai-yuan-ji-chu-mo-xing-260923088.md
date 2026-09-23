---
title: 'OmniEdu: Open Foundation Models for Learning and Teaching'
title_zh: OmniEdu：面向K12教与学的开源基础模型系列
authors:
- Hao Liang
- Qihan Lin
- Meiyi Qiang
- Linzhuang Sun
- Hengyi Feng
- Mingrui Chen
- Sizhe Qiu
- Wentao Zhang
affiliations:
- Peking University
- University of the Chinese Academy of Sciences
- Zhongguancun Academy
arxiv_id: '2609.23088'
url: https://arxiv.org/abs/2609.23088
pdf_url: https://arxiv.org/pdf/2609.23088
published: '2026-09-18'
collected: '2026-09-23'
category: LLM
direction: 教育领域大模型 · 能力对齐微调
tags:
- LLM
- Instruction Tuning
- Domain Adaptation
- Educational LLM
- Model Alignment
one_liner: 围绕四大教育能力构建对齐语料，训练的多尺度开源K12教与学基础模型系列
practical_value: '- 垂直领域大模型微调可借鉴「按核心能力维度组织训练语料」的思路，替代按任务/来源分组的方式，平衡多任务能力表现，例如电商导购大模型可拆分为商品理解、用户需求诊断、话术生成等能力维度组织语料

  - 指令微调语料构建的多阶段pipeline可直接复用：确定性清洗→语义审核改写→任务特定质量打分→token预算约束的多样性选择→领域指令分配，可大幅提升垂直领域微调语料质量

  - 业务落地选型可参考多尺度训练验证思路，根据时延、算力要求选择不同参数量版本，小参数模型经高质量领域微调也可获得可观的能力提升'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有教育大模型多聚焦解题或 tutoring 单一能力，训练语料按来源/任务组织，未做能力维度的平衡，无法覆盖教与学全场景需求。

### 方法关键点
提出OmniEdu开源模型系列，围绕学科能力、课纲对齐、诊断推理、教学支撑四大核心能力组织微调语料，整合100+教育资源与通用指令源，经过多阶段语料处理pipeline，最终得到69999条样本、15.96M监督响应token（其中教育专属样本60951条），完成4B/9B/27B三个尺度模型的微调。

### 关键结果数字
OmniEdu-27B在K12-Bench上达到63.12% EM、76.69% F1，MathFish 85.89%，EDUMATH 86.95%，MathTutorBench Scaffold设置78.74%，LongTutor教学平均分3.02（参测模型最高），全尺度模型经教育定向微调后三类教育基准表现均有稳定提升。
