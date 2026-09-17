---
title: 'FRAUDSkill: Structured Frozen-Weight Skill Optimization for Audio Anti-Fraud
  Detection'
title_zh: FRAUDSkill：面向音频反欺诈检测的结构化冻权技能优化框架
authors:
- Chengxian Hu
- Zhiming Ma
- Mingjun Pan
- Yifan Wang
- Shun Zhang
- Qifan Wang
- Zhilei Zhao
- Yijin Zhou
- Yuxi Zhao
- Huiyuan Liu
affiliations:
- People's Public Security University of China
- JD Technology
- Meta
- University of Science and Technology of China
- Northeastern University
arxiv_id: '2609.18766'
url: https://arxiv.org/abs/2609.18766
pdf_url: https://arxiv.org/pdf/2609.18766
published: '2026-09-16'
collected: '2026-09-17'
category: Other
direction: 音语模型适配 · 结构化反欺诈决策
tags:
- Audio-LLM
- Frozen-Weight Adaptation
- Anti-Fraud Detection
- Structured Inference
- Skill Optimization
one_liner: 提出结构化冻权适配框架FRAUDSkill，无需修改基座音语模型即可实现高性能音频反欺诈检测
practical_value: '- 可复用「基座模型全冻结+外部独立优化技能/路由/规则层」的适配范式，适配电商风控、内容审核等规则迭代频繁的场景，避免反复微调基座的算力和时间成本

  - 结构化输出控制+校验引导多路推理的方案可直接迁移到所有要求输出符合固定协议的大模型落地场景，大幅降低无效输出率

  - 多步串行决策类任务（如场景识别→风险判定→分类定级）优先用外部独立路由策略替代硬编码prompt，规则迭代时仅需调整外部层，适配效率更高'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有音频语言模型落地反欺诈场景时，输出需符合预定义标签空间和「场景识别→欺诈判定→类型分类」的结构化决策协议，传统微调、手动prompt方案将知识、规则编码到模型参数或prompt中，欺诈模式、标签政策迭代时适配成本极高。
### 方法关键点
1. 提出FRAUDSkill冻权适配框架，完全冻结基座音频语言模型参数，仅优化外部独立的技能程序、路由策略、决策规则层
2. 新增结构化输出控制+校验引导的多路推理逻辑，强制输出符合预设决策协议
### 关键结果
在TeleAntiFraud基准测试集上Macro-F1达73.50%，较共享冻权基线提升31.96%，无效输出占比降至1.94%，规则迭代时无需调整基座，适配效率显著提升
