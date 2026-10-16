---
title: 'From Failures to Learnable Worlds: Policy-Conditioned Environment Generation
  for Navigation Agents'
title_zh: 基于策略失败模式挖掘的导航Agent训练环境生成框架WEDGE
authors:
- Yue Zhang
- Han Lin
- Zun Wang
- Yidong Huang
- Zaid Khan
- Mohit Bansal
affiliations:
- UNC Chapel Hill
arxiv_id: '2610.19420'
url: https://arxiv.org/abs/2610.19420
pdf_url: https://arxiv.org/pdf/2610.19420
published: '2026-10-13'
collected: '2026-10-16'
category: Agent
direction: 具身Agent · 自适应训练环境生成
tags:
- Embodied Agent
- Environment Generation
- LLM-based Diagnosis
- Policy Adaptation
- Navigation
one_liner: 通过LLM挖掘导航Agent失败模式，针对性生成训练环境实现性能与跨域迁移提升
practical_value: '- 模型bad case定向优化范式可复用：先对比正负样本用LLM提取可量化的弱点特征，经统计验证后定向构造训练样本，比通用难例挖掘效果更显著，适合推荐/广告模型的短板补全、冷启动优化场景

  - 训练样本难度校准技巧可直接落地：生成符合弱点特征的候选后，先跑小批量预测筛选成功率在20%~60%区间的样本，避免过易无增益、过难学不会的问题，大幅提升fine-tune效率

  - 跨域迁移训练逻辑可借鉴：针对源域诊断的弱点生成训练数据，优化后可直接迁移到目标域，比通用数据增广的跨域适配效果更稳定，适合多场景跨域的推荐/搜索模型优化'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有具身Agent训练环境生成仅关注真实度、多样性或任务匹配，忽略不同预训练策略的差异化失败模式，通用难例挖掘易出现样本冗余或过难问题，无法针对性补全模型能力短板，训练效率低且跨域迁移效果差。

### 方法关键点
- 弱点挖掘：对比15条成功+15条失败轨迹，用LLM从场景、目标、路径、Agent四类可量化原语中生成可执行的弱点特征（如target visibility、blind path ratio），经覆盖率、非冗余、预测性、增量价值四层验证后保留有效弱点
- 环境生成：针对Top1弱点对应可调节参数（如目标位置、初始状态、场景布局）生成候选环境，筛选特征值落在失败关联区间的样本
- 难度校准：每个候选环境跑5次策略rollout，仅保留成功2-3次的中等难度样本用于训练，避免过易无增益、过难无学习信号的问题
- 多适配支持：兼容RL参数训练、LoRA fine-tune、闭源模型in-context learning三类适配方式，迭代重诊断弱点支撑多轮优化

### 关键结果
在ProcTHOR模拟器上完成诊断与训练，跨域迁移到HM3D数据集，对比随机环境、通用难例挖掘两类基线：
- DD-PPO：ProcTHOR上Success Rate（SR）从82.1提升至85.6，超基线3pct以上
- Uni-NaVid：ProcTHOR SR从51.6提升至55.7，HM3D SR从69.2提升至73.4，跨域增益4.2pct
- Gemini-3.8-flash：ProcTHOR SR从41.0提升至44.3，HM3D SR从57.9提升至64.2，跨域增益6.3pct

> 最值得记住：Agent的失败不仅是诊断信号，更是构造针对性训练环境的可执行指导，比通用增广能带来更稳定的性能与跨域迁移收益
