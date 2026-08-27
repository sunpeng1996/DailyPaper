---
title: 'Unsupervised Post-Training of Foundation Models: A Survey'
title_zh: 基础模型无监督后训练（UPT）综述：分类框架与落地选型指南
authors:
- Yijie Xu
- Qianyi Cai
- Huizai Yao
- Yili Wang
- Tianfu Wang
- Cehao Yang
- Xingbo Yao
- Zhiyu Guo
- Aiwei Liu
- Xuming Hu
affiliations:
- HKUST(GZ)
- Xiaohongshu Inc.
- WeChat, Tencent
- CUHK
- AI2 Robotics
arxiv_id: '2608.24982'
url: https://arxiv.org/abs/2608.24982
pdf_url: https://arxiv.org/pdf/2608.24982
published: '2026-08-25'
collected: '2026-08-27'
category: Training
direction: 大模型训练 · 无监督后训练综述
tags:
- Unsupervised Post-Training
- Foundation Model
- Self-Improvement
- Model Adaptation
- Survey
one_liner: 系统梳理80种严格无监督后训练方法，提出双维度分类框架与落地选型指引
practical_value: '- 电商/推荐垂域大模型适配优先选择Prediction-Statistic Optimization类UPT方法，基于域内未标注语料做CPT即可降低域偏移，可直接复用LANGADAPTCPT等成熟方案，小语种适配场景下可将perplexity从23.64降至3.34

  - 导购Agent、多步推理类大模型优化可复用Sample-Relation Supervision类方法，基于多采样majority vote生成伪标签做GRPO训练，无需标注即可将MATH-500基准得分从46.7提升至83.4

  - 落地时可匹配Input Visibility×Update Persistence时序框架选型：离线域适配选离线语料UPT，线上实时请求优化选Test-Time
  Instance Adaptation，仅更新LoRA/steering vector等小参数，不影响全局模型稳定性'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

## 动机
当前大模型后训练依赖人工标注、偏好数据、外部验证器等监督信号，在垂类域适配、开放生成任务等无标注/无验证器场景下难以落地，现有相关综述未严格界定无监督后训练边界，也缺乏统一分类框架指导方法选型。

## 方法关键点
- 明确严格UPT的4条边界规则：必须更新模型参数/适配器/记忆等状态、仅用未标注输入与同源模型产物做更新信号、无外部监督、评估器与基模型同谱系
- 按更新信号来源将80种严格UPT方法分为4大类：预测统计优化（直接用NLL、熵、置信度等单样本统计量做优化目标）、样本关系监督（用多样本投票、聚类、一致性等关系做信号）、自生成目标Bootstrapping（生成伪标签、推理链、偏好对等训练目标再做SFT/DPO）、内部评估器Bootstrapping（自举生成同谱系奖励模型/评估器输出信号）
- 提出Input Visibility×Update Persistence双维度时序框架，覆盖从离线预部署到单样本推理时的6种适配时序场景，明确不同场景的选型规则

## 关键结果
- 预测统计优化类的LANGADAPTCPT将巴斯克语perplexity从23.64降到3.34，下游任务准确率从27.43提升到34.14
- 样本关系监督类的TTRL将AIME 2024得分从12.9提升到40.2，MATH-500得分从46.7提升到83.4
- 自生成目标类的QUIET-STAR将零样本GSM8K得分从5.9提升到10.9，CommonsenseQA从36.3提升到47.2
- 内部评估器类的CONL将AIME 2024得分从60.0提升到76.5，DeepMath从70.5提升到87.1

## 核心结论
无监督后训练的核心权衡是：语义表达能力越强的信号适配开放场景效果越好，但反馈路径越长越容易出现递归误差放大，选型时需要匹配任务结构与部署时序，在信号接入环节添加校验机制阻断误差累积
