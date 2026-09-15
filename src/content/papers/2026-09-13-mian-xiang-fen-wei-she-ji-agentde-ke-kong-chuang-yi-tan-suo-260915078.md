---
title: Enabling Creative Exploration for Vibe Design Agents
title_zh: 面向氛围设计Agent的可控创意探索架构
authors:
- Yifan Zhang
- Nghi D. Q. Bui
- Georgios Evangelopoulos
- Arnaud Benard
affiliations:
- Google
arxiv_id: '2609.15078'
url: https://arxiv.org/abs/2609.15078
pdf_url: https://arxiv.org/pdf/2609.15078
published: '2026-09-13'
collected: '2026-09-15'
category: Agent
direction: 设计Agent · 可控创意探索
tags:
- Design Agent
- Controllable Generation
- Verbalized Sampling
- UI Generation
- Inference Optimization
one_liner: 提出显式设计规范中间层，解耦UI设计Agent的创意探索与代码生成环节
practical_value: '- 做生成式Agent（如电商装修、商品详情页生成Agent）时，可将风格/主题等创意属性封装为结构化中间规范，解耦创意探索与高精度代码/内容生成，避免调temperature同时破坏生成质量

  - 可复用Verbalized Sampling思路，让LLM先输出多个候选方案+典型性评分，再用温度采样选方案，兼顾多样性与生成质量，适配电商首页/活动页多风格生成场景

  - 评估创意类Agent不要仅看单一偏好分，需分开统计探索覆盖率、视觉差异度、用户反馈、操作行为多维度指标，例如电商装修Agent可统计不同风格的点击率、修改率调优

  - 线上部署时注意探索架构的延迟开销，该方案仅带来3%左右的60秒内完成率下降，实际业务可通过缓存常用主题候选进一步降低开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有UI设计Agent靠调整全局token temperature做创意探索，会同时打乱审美决策与语法敏感的代码生成，既无法精准控制设计方向，还容易生成无效代码；同时RLHF等对齐方法容易导致输出趋同，无法满足用户探索多元设计方向的需求。

### 方法关键点
- 基于Verbalized Sampling设计三阶段推理架构：预生成3类（安全、高级、实验）结构化设计规范，附带LLM自评估的典型性评分
- 外部选择器对评分做温度缩放后采样选中规范，下游生成器固定解码参数，基于原请求+选中规范生成最终UI与代码，完全解耦探索与生成环节
- 支持两类规范：主题规范（配色、字体、圆角、明暗模式等）、视觉资产提示词（配图主题、构图、风格）

### 关键结果
离线实验覆盖168个UI设计prompt，每个温度下每类干预完成1255组配对比较：主题采样在τ=2.0时选择覆盖率从基线1.0提升到2.87，截图相似度从0.6765降至0.5438，LLM评审胜负比1.10；资产采样在τ=1.0时胜负比达1.32。线上A/B测试覆盖30万+用户任务：负反馈减少31.51%，用户修正交互增加7.08%，60秒内任务完成率仅下降3.47%，代码导出提升8.23%但统计不显著。

**最值得记住的一句话**：评估创意类Agent时，探索广度、偏好得分、实际用户行为是完全独立的三类指标，不能用单一指标替代对设计探索效果的判断。
