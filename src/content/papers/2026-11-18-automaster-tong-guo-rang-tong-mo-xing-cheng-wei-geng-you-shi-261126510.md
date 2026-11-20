---
title: 'AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher'
title_zh: AutoMaster：通过让同模型成为更优教师的自主后训练框架
authors:
- Guoxin Chen
- Shuang Sun
- Fanzhe Meng
- Xinyu Tang
- Ruihua Song
- Wayne Xin Zhao
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
arxiv_id: '2611.26510'
url: https://arxiv.org/abs/2611.26510
pdf_url: https://arxiv.org/pdf/2611.26510
published: '2026-11-18'
collected: '2026-11-20'
category: Training
direction: LLM 自主后训练 · 行为塑形
tags:
- SFT
- Post-Training
- LLM Agent
- Behavioral Shaping
- Skill Guidance
one_liner: 提出Skill-FT与AutoMaster自主后训练框架，固定教师下较普通SFT提升1.42~8.99pp
practical_value: '- 业务Agent（电商导购、搜索、推荐解释Agent）微调时，可先针对业务痛点设计自然语言skill（如搜索Agent加「先验证query意图再召回」、文案生成Agent加「先核对商品属性再写文案」）引导教师生成轨迹，比仅筛选成功轨迹的普通SFT效果更高

  - 微调Trick：引导教师用的skill指令不要从训练样本里移除，哪怕推理时完全不用skill，也能稳定带来2.15~4.01pp的性能提升，无额外成本

  - 可复用AutoMaster的双循环架构做业务Agent的自动化迭代：内层用Agent自动分析bad case、优化skill、生成训练数据，外层做微调+效果反馈迭代，降低人工标注和调参成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于成功教师轨迹的SFT存在明显缺陷：成功轨迹中依然会残留无依据假设、无效重复、浅层验证等不良行为，会被学生一并学习；同时高价值的有效行为在成功轨迹中占比极低，仅靠筛选轨迹无法充分挖掘固定教师的潜力，自主后训练需要主动对教师行为进行塑形。
### 方法关键点
- 提出Skill-FT：针对任务痛点设计自然语言skill，追加到教师的系统prompt中，引导教师在rollout时抑制不良习惯、激活低占比的有效行为；微调时保留训练样本中引导教师的skill指令（推理阶段不添加任何skill）。
- 提出AutoMaster双循环自主后训练框架：内层由LLM Agent负责轨迹行为分析、skill设计、试点rollout验证skill有效性、批量rollout、筛选优质轨迹构建训练集；外层基于生成的训练集做SFT，根据学生模型的评估效果反馈迭代skill设计和数据筛选策略，全程固定教师模型、任务池、训练数据量、SFT超参数配方。
### 关键结果
在Terminal命令行、网页搜索、软件工程3类任务上测试Qwen3.5-4B和9B模型，对比普通SFT基线，AutoMaster带来1.42~8.99pp的性能提升，其中9B模型增益更显著；消融实验证实，保留skill指令的训练效果比移除平均高2.15~4.01pp，skill引导和数据筛选两个模块缺一不可。
**最值得记住的结论**：固定教师模型也可以通过行为塑形成为更优的教师，仅使用成功轨迹的普通SFT远未榨干固定教师的价值。
