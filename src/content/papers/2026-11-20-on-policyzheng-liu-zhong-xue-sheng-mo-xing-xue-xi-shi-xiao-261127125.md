---
title: 'When Students Fail to Learn from Teachers: Learning Dynamics of On-Policy
  Distillation'
title_zh: On-Policy蒸馏中学生模型学习失效的动力学机制与优化方法
authors:
- Xinnan Zhang
- Zeyi Liao
- Siliang Zeng
- Zhongruo Wang
- Jiaxiang Li
- Xinyan Zhao
- Huan Sun
- Mingyi Hong
affiliations:
- University of Minnesota
- The Ohio State University
- Amazon
- Virginia Tech
arxiv_id: '2611.27125'
url: https://arxiv.org/abs/2611.27125
pdf_url: https://arxiv.org/pdf/2611.27125
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: LLM训练 · On-Policy蒸馏优化
tags:
- On-Policy Distillation
- Knowledge Distillation
- LLM Training
- Learning Dynamics
- KL Divergence
one_liner: 揭示On-Policy蒸馏训练失效的三层动力学机制，提出状态依赖KL路由策略提升蒸馏性能
practical_value: '- 做生成式推荐/Agent小模型蒸馏时，先做SFT将学生分布对齐教师再跑OPD，可大幅降低训练崩溃概率，避免生成重复、过长的低质量内容，收益远高于训练中加修复trick

  - 原OPD效果差时，可用「学生对教师top-p集合覆盖率」「教师概率低估比例」两个指标做路由，低覆盖率场景切换forward KL，比仅看教师熵、advantage的策略效果更好，额外耗时仅2.5%-6.8%

  - 若蒸馏后出现师生token重叠率高但整体生成质量差的「伪一致」问题，优先检查EOS、分隔符等格式token的师生匹配度，这类token不匹配会触发跨位置梯度干扰，导致重复生成'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
On-Policy蒸馏（OPD）是当前LLM后训练的核心技术，可通过token级稠密监督将大模型能力迁移到小模型，算力效率高于RL类方法，但训练极不稳定，易出现响应过长、重复生成、性能骤降问题，甚至出现师生token重叠率高但生成质量极差的「伪一致」现象，现有方案多为经验性修复，缺乏底层机制解释，无法系统性解决失效问题。

### 方法关键点
- 三层动力学解析失效机制：本地分布层面，学生对教师偏好token概率极低时，采样token更新几乎无法修正分布偏差；跨位置层面，师生不匹配位置的梯度会通过共享参数干扰其他位置的更新方向；采样轨迹层面，持续在不匹配状态训练会抑制学生原有模式，让学生进入教师也无法提供有效反馈的不可靠状态
- 提出状态依赖KL路由：用学生对教师top-p集合的覆盖率、教师概率质量低估比例两个指标触发路由，当覆盖率过低或低估比例过高时，切换为top-K forward KL优化，其余场景保留原有采样token OPD

### 关键实验
在Qwen3 1.7B/4B/8B三个尺度模型上测试，数学推理任务相比基准OPD，平均Avg@8提升1.38~2.50个百分点，Best@8提升1.01~6.24个百分点；代码生成任务平均Avg@8提升2.92~3.44个百分点，Best@8提升1.27~2.88个百分点，训练步耗时仅增加2.5%~6.8%，无额外显存开销。

### 核心结论
OPD训练前先通过SFT拉近师生分布，比在训练中叠加各种修复trick的收益更高、稳定性更好
