---
title: 'Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation'
title_zh: 领域归一化多教师在线策略蒸馏：突破教师分配的局限
authors:
- Xin Li
- Hao Jiang
- Xin Gao
- Annan Wang
- Yuchen Xie
- Jinghao Guo
- Xingwei Qu
- Yichi Zhang
- Chau Yuen
affiliations:
- Nanyang Technological University
- Yale University
- University of Manchester
arxiv_id: '2609.35347'
url: https://arxiv.org/abs/2609.35347
pdf_url: https://arxiv.org/pdf/2609.35347
published: '2026-09-27'
collected: '2026-09-29'
category: Training
direction: 大模型训练 · 多教师知识蒸馏
tags:
- Knowledge Distillation
- On-Policy Distillation
- Multi-Teacher Distillation
- LLM Post-Training
- RL
one_liner: 对多教师在线策略蒸馏的各领域反馈做尺度归一化，解决反馈失衡导致的弱技能迁移问题
practical_value: '- 训练多技能电商/推荐LLM Agent时，可复用DN-MOPD的领域反馈归一化思路：对不同任务（如推荐理由生成、搜索query理解、客服应答）的梯度/反馈按标准差做clip后加权，避免简单任务（如指令遵循）的梯度淹没复杂任务（如推理类需求）的优化信号

  - 做多任务推荐模型训练时，不需要手动调各任务损失权重，可直接用batch内各任务损失的标准差比值动态计算权重，clip在[0.25,4]区间防止极端值，工程实现简单几乎无额外开销

  - 多教师蒸馏整合垂直领域专家模型时，不需要改动路由逻辑，仅加一层反馈归一化即可提升弱领域技能的迁移效果，适配现有MOPD训练管线'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多教师在线策略蒸馏（MOPD）仅按领域分配教师，未考虑不同领域专家的反馈尺度差异，导致训练时反馈失衡：比如指令遵循类反馈的分散度是数学类的2.3-4.4倍，占4B模型初始梯度的94%，最终学生模型难以迁移数学等弱反馈领域的技能，效果甚至不如单最优教师蒸馏的模型。

### 方法关键点
- 保留MOPD的领域路由逻辑，无额外教师调用、无额外可学习参数，仅新增反馈归一化操作
- 每batch统计所有领域的teacher-student对数似然差的全局标准差σ_all，以及各领域单独的标准差σ_d
- 计算各领域的反馈权重w_d = clip(σ_all/σ_d, 0.25, 4)，对该领域所有token的蒸馏优势乘w_d后再更新学生模型，保留优势的正负号不变

### 关键实验
基于Qwen3.5的2B、4B、9B三个尺寸模型，分别训练数学、代码、指令遵循三个领域专家做蒸馏，对比Label-routed MOPD等基线：
- 6个公共基准平均得分，DN-MOPD比MOPD在8K评估时提升2.47~3.08个百分点，16K评估时提升1.17~2.36个百分点，恢复了MOPD丢失的80%以上数学技能增益，所有尺寸下效果均超过单最优教师蒸馏的模型
- 固定权重实验显示增益主要来自抑制过强的指令遵循反馈，而非放大数学反馈，9B/4B尺寸下固定为DN-MOPD统计得到的权重（数学×2、代码×1、指令×0.25）效果和动态计算相当

### 核心结论
多教师知识蒸馏整合跨域技能时，选对谁来教只是第一步，校准每个教师的反馈权重才能真正避免弱技能被淹没。
