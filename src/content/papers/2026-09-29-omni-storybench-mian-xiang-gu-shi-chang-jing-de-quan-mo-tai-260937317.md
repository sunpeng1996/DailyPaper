---
title: What Comes Next? Omni-StoryBench for Evaluating Story-Grounded Omnimodal Generation
title_zh: 《Omni-StoryBench：面向故事场景的全模态连贯生成评估基准》
authors:
- Sieun Hyeon
- Yejoon Lee
- Mintaek Lim
- Woojin Kim
- Jaeik Kim
- Jaeyoung Do
affiliations:
- Seoul National University
- AIDAS Laboratory
- ECE
- IPAI
arxiv_id: '2609.37317'
url: https://arxiv.org/abs/2609.37317
pdf_url: https://arxiv.org/pdf/2609.37317
published: '2026-09-29'
collected: '2026-10-04'
category: Eval
direction: 全模态生成 · 系统级评估基准
tags:
- Omnimodal Generation
- Benchmark
- LLM-as-judge
- Multimodal Evaluation
- VLM Orchestration
one_liner: 构建故事场景全模态生成评估基准，验证带VLM规划的编排式生成框架效果最优
practical_value: '- 电商多模态商品内容（主图、详情文案、语音介绍）生成可复用带VLM规划的编排式架构，比原生全模态模型可控性更高，适配业务强约束场景

  - 多模态生成效果评估可复用LLM-as-judge的一致性校验框架，覆盖上下文保留、跨模态对齐、约束遵循三个核心维度，比单模态独立评估更贴合真实业务体验

  - 内容生成类业务可优先优化文本侧生成质量，验证表明文本表现与图像、语音生成质量正相关，可快速提升全链路生成效果'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有全模态生成评估仅对单模态输出独立校验，忽略跨模态内容的连贯性与事件一致性，无法衡量系统级生成能力。
### 方法关键点
构建Omni-StoryBench基准，包含900条经过严格校验的开源儿童绘本故事跳转样本，给定当前页内容与下页结构化约束，要求模型生成下页插图、旁白、角色语音三类输出；评估体系同时覆盖单模态专属指标，以及基于LLM-as-judge的上下文保留、约束遵循、参考一致性、跨模态对齐4类一致性指标，共测试32种基线配置。
### 关键结果数字
带强VLM规划的编排式架构表现最优，原生全模态模型在输出完整性、可控性上表现较差；文本侧表现与图像、语音质量正相关，图像生成与视觉连续性是当前最大性能瓶颈。
