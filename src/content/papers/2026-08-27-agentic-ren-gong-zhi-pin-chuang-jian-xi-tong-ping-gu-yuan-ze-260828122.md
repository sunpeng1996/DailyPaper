---
title: 'Agentic Artifact Creation: Systems, Evaluation, Principles, and Opportunities'
title_zh: Agentic 人工制品创建：系统、评估、原则与机遇
authors:
- Tianfu Wang
- Zhezheng Hao
- Xilin Xia
- Lixin Liu
- Mengkang Hu
- Hongzhang Liu
- Xi Chen
- Ziyan Liu
- Xiankun Lin
- Weijia Zhang
affiliations:
- 香港科技大学（广州）
- 浙江大学
- 中国科学技术大学
- 清华大学
- 香港大学
arxiv_id: '2608.28122'
url: https://arxiv.org/abs/2608.28122
pdf_url: https://arxiv.org/pdf/2608.28122
published: '2026-08-27'
collected: '2026-08-31'
category: Agent
direction: Agent 智能体制品生成综述
tags:
- Agentic Creation
- Generative Agent
- Artifact Generation
- Evaluation Framework
- Design Principles
one_liner: 梳理259篇Agentic制品创建工作，提出统一功能架构、跨领域设计原则与落地机遇
practical_value: '- 搭建电商营销物料（海报、短视频、商品文案）Agent生成系统时，可直接复用三组件架构：用Operational Representation存储可编辑物料状态（SVG源文件、视频时间线、文案大纲）、Construction
  Policy做动作决策、Runtime Verification做规则校验（品牌规范、内容合规），解决直接生成物料改不动、不合规的问题

  - 生成多模块耦合物料（商详页、促销海报）时，优先采用细粒度Unit Edit+Relation Edit接口，避免全量重生成，可大幅降低迭代成本，同时保留已通过校验的内容

  - 评估Agent生成系统时，除最终产出质量外，需加入轨迹级、修复效率指标（问题修复时长、单次修改波及范围），更贴合业务落地的实际需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有生成模型仅能生成独立内容片段，无法交付满足多约束、高耦合要求的完整可用制品（如符合品牌规范的电商海报、逻辑自洽的研报），单向直接生成模式存在错误难定位、修改成本高的问题；过往Agent相关研究分散在不同模态和领域，缺乏统一分析框架与落地指导。

### 方法关键点
- 明确定义Agentic制品创建为有状态迭代构建流程，核心特征是中间观测结果可指导后续修改，区别于无反馈的单向生成
- 提出通用三组件功能架构：Operational Representation存储制品中间状态（支持实例、结构化模型、可执行程序三类形式）、Construction Policy基于任务要求与反馈决策下一步动作（支持单智能体、集中/分布式多智能体拓扑）、Runtime Verification输出可落地反馈（含状态校验、故障诊断、修改指导）
- 梳理2023-2026年8月的259篇符合定义的工作（含230个系统、29个基准），覆盖文本、2D视觉、音频、视频、空间、行为六大制品家族，提炼跨领域设计原则

### 关键结果数字
累计收录259篇严格符合定义的工作，其中230个落地系统、29个评测基准；六大制品家族中行为类（软件、仿真系统等）相关工作最多达73篇，2D视觉类次之达61篇；验证两个核心结论：任务分解会降低局部复杂度但提升协调与重装配成本，与生成器同源的学习式裁判几乎无法提供独立评估证据。

### 核心结论
Agentic制品创建的核心价值不是生成能力更强，而是通过对齐可编辑状态、细粒度操作、可观测反馈三者的粒度，实现可追溯、可局部修改的可控生成，大幅降低复杂制品的迭代成本。
