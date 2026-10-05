---
title: 'Spatial Memory Intelligence: Endowing World Models with Understanding-Driven
  Long-Term Memory'
title_zh: 空间记忆智能：为世界模型赋予理解驱动的长期记忆能力
authors:
- Ying Yang
- Guiyu Zhang
- Lianghua Huang
- Chang Nie
- Chenyang Si
- Haofan Wang
- Shaoshuai Shi
- Li Jiang
affiliations:
- 香港中文大学（深圳）
- 阿里巴巴集团
- 南京大学
- Lovart AI
- 滴滴出行Voyager Research
arxiv_id: '2610.02521'
url: https://arxiv.org/abs/2610.02521
pdf_url: https://arxiv.org/pdf/2610.02521
published: '2026-09-30'
collected: '2026-10-05'
category: Agent
direction: 具身Agent · 世界模型记忆管理
tags:
- World Model
- MLLM
- Spatial Memory
- Memory Management
- Long Video Generation
one_liner: 基于MLLM的四原子操作空间记忆管理框架，提升长视频世界模型效率与一致性
practical_value: '- 可复用四原子操作（空间聚类、簇内稀疏化、动作感知检索、可靠性过滤）框架优化电商用户长周期交互记忆管理，既降低KV cache存储开销，又避免高价值兴趣信号丢失

  - 可借鉴「少量人工标注+大模型半自动打标+人工校验」的专用任务数据集构建流程，低成本微调轻量MLLM适配业务场景的记忆管理逻辑

  - 可靠性过滤机制可直接迁移到生成式推荐的内容校验环节，阻止存在漂移、错误的生成内容进入用户交互历史，避免后续推荐的兴趣偏移问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长视频世界模型在交互式生成过程中，观测序列随交互不断增长，现有压缩、检索类记忆管理方法存在明显缺陷：压缩类方法易丢失维持长序列一致性所需的细粒度空间证据，几何检索受遮挡、几何误差影响大，语义检索无法区分不同空间位置的相似内容，无法同时满足内存稀疏性、空间一致性、生成稳定性的核心需求。
### 方法关键点
- 首次引入MLLM作为专用空间记忆管理器，将记忆管理拆解为4种协同原子操作：空间聚类按空间 proximity 分组记忆块解决时序相邻但空间不相邻的记忆混乱问题，簇内稀疏化动态移除同簇冗余观测降低存储开销，动作感知检索结合当前动作与近期上下文精准召回相关历史记忆，可靠性感知过滤阻止存在视觉漂移的生成块进入记忆避免错误传播
- 构建操作导向的专用监督数据集，采用「少量人工标注→教师MLLM批量打标→人工校验清洗」的流水线生成训练数据，微调轻量MLLM适配记忆管理任务
### 关键结果
在HY1.5、Wan2.2两个主流世界模型骨干上对比6种现有记忆管理基线：HY1.5上实现83.68%的内存稀疏率，同时美学质量提升5.38%、GPT评估的空间一致性提升29.87%、PSNR提升0.83dB；Wan2.2上实现82.21%的内存稀疏率，全维度生成质量指标优于所有基线。
### 核心结论
将理解模型作为生成过程的核心管控组件而非事后辅助能力，是解决长序列生成一致性与效率矛盾的可行路径。
