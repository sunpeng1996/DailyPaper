---
title: 'Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for
  Multi-Domain LLMs'
title_zh: 基于答案验证的多教师蒸馏方法实现多领域LLM能力整合
authors:
- Xixiang He
- Xingming Li
- Baiqi Wu
- Qiyao Sun
- Xuanyu Ji
- Ao Cheng
- Qingyong Hu
affiliations:
- National University of Defense Technology
- Zhejiang University
- Intelligent Game and Decision Lab
arxiv_id: '2609.02548'
url: https://arxiv.org/abs/2609.02548
pdf_url: https://arxiv.org/pdf/2609.02548
published: '2026-09-02'
collected: '2026-09-03'
category: Training
direction: 多域LLM · 多教师知识蒸馏训练
tags:
- Knowledge Distillation
- Multi-Domain LLM
- Policy Optimization
- On-Policy Training
- Model Distillation
one_liner: 通过逐样本答案验证筛选合格教师，将多领域教师能力蒸馏为单部署模型
practical_value: '- 做电商多域垂类Agent、商品问答LLM时，可抛弃按域路由教师的逻辑，改为逐样本验证教师答案正确性后筛选监督源，避免匹配域教师答错误导学生，显著提升弱域表现

  - 电商文案生成、多域推荐LLM重排模块的小模型蒸馏，可复用self-anchor+验证合格教师反馈合并为特权上下文的蒸馏框架，推理侧仅保留学生模型，无额外部署开销

  - 多域模型训练前先评估初始域性能差距，仅弱域有充足提升空间时使用该方法，初始域表现已均衡的模型无需做在线蒸馏，可节省训练算力'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多域LLM整合独立训练的多领域教师能力时，普遍依赖样本域标签匹配对应教师，但域匹配是平均属性，单样本下匹配域教师未必正确，跨域教师反而可能答对。统计显示匹配教师正确率仅52.9%，逐样本筛选正确教师的覆盖率可达65.7%，传统方法浪费了大量跨域正确教师的监督信号，且部署多教师路由方案推理开销高，亟需将多教师能力蒸馏为单个可部署模型。
### 方法关键点
- 离线预跑所有教师的样本答案，用程序验证器筛选单样本下答案正确的教师组成合格集合，完全抛弃域标签限制
- 在线训练时学生对每个prompt采样G个rollout，同组内的正确rollout作为self-anchor监督错误样本，错误样本再调用所有合格教师的反馈，经过答案泄漏过滤后合并为特权上下文
- 仅EMA自教师能读取特权上下文，将自教师的token分布蒸馏到学生模型，训练全程仅更新学生参数，部署侧仅保留学生模型，无额外组件开销
### 关键实验
在SciKnowEval的化学、材料、物理三领域科学问答数据集上测试，对比SDPO、域路由蒸馏等baseline：Qwen3-8B上Macro准确率较多域后训练基线提升4.64pp，最弱域准确率提升14.79pp，域性能差距缩小74.7%，效果优于部署三个匹配域教师的路由方案；初始域性能已均衡的Llama-3.1-8B-Instruct无额外增益。
### 核心结论
不是域归属，而是验证后的可靠性，决定谁可以成为教师。
