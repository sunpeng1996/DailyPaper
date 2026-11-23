---
title: 'ORION: Exact Canonical-State Supervision for Systematic Generalization in
  Transformers'
title_zh: ORION：基于精确规范态监督的Transformer系统泛化框架
authors:
- Sibi Gokul
- Jyoti Prakash Meher
affiliations:
- National Institute of Technology Warangal, India
arxiv_id: '2611.27087'
url: https://arxiv.org/abs/2611.27087
pdf_url: https://arxiv.org/pdf/2611.27087
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: Transformer训练优化 · OOD推理泛化
tags:
- Transformer
- OOD Generalization
- RoPE
- Intermediate Supervision
- Length Extrapolation
- Depth Extrapolation
one_liner: 通过规范态监督与RoPE的互补组合，解决Transformer深度与长度外推的正交失效问题，提升OOD推理性能
practical_value: '- 多步推理类Agent（如电商智能导购、订单履约路径规划）可复用ORION+RoPE的正交优化思路：用RoPE解决长上下文位置混乱问题，用ORION中间态监督解决多步执行的状态漂移问题，显著提升OOD场景下的推理准确率

  - 对于有明确中间执行状态的业务任务，可添加轻量化投影头做辅助监督，仅需稀疏标注（甚至单任务仅1个中间态）即可稳定推理轨迹，训练 overhead 极低

  - 大模型微调遇到多步推理OOD性能差问题时，可先拆分失效原因：是长度外推失效还是深度漂移，分别针对性优化，避免盲目调参'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
自回归Transformer在OOD推理任务上普遍失效，过往研究无法明确区分失效根因是长序列的位置corruption，还是深层执行步骤的结构态漂移，两类问题的优化方案独立，缺乏正交验证与组合方案，导致OOD泛化提升效果有限。
### 方法关键点
- 提出ORION框架，在Transformer指定层添加轻量化2层MLP投影头，将中间隐状态映射到预定义的规范态空间，用余弦距离损失约束隐状态轨迹与真实计算流严格对齐
- 采用预注册2×2因子实验设计，正交验证位置编码（绝对PE/RoPE）和状态监督（无/ORION）两类优化的作用边界
- 联合训练损失为原生任务损失加λ加权的ORION辅助损失，无需改动主模型结构，可快速接入现有训练流程
### 关键结果
- 测试域：Folding、GridShift两个精确可解算法推理域，CLRS-30算法基准
- 核心数字：RoPE单独优化长度外推准确率到59.8%，ORION+RoPE组合优化深度外推准确率到66.7%；二者联合在Folding、GridShift的长度-深度联合外推任务上分别比基线提升1.8pp、18.0pp；26M参数量下ORION+RoPE比RoPE单独方案深度外推准确率高8.2pp；跨域迁移时ORION预训练比普通Transformer预训练最高提升8.5pp准确率。
### 核心结论
Transformer OOD推理失效可拆分为长度外推、深度外推两个正交问题，RoPE解决位置混乱、规范态监督解决状态漂移，二者组合才能实现最优的多步长序列推理泛化。
