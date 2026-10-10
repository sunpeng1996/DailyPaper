---
title: 'GeoReform: Reflective Formalization Evolution for Multimodal Geometry Problem
  Solving'
title_zh: GeoReform：面向多模态几何题求解的反思式形式化演化框架
authors:
- Jialu Wang
- Ruichen Zhang
- Xiaoou Liu
- Hua Wei
- Tianlong Chen
affiliations:
- Tongji University
- University of North Carolina at Chapel Hill
- Arizona State University
arxiv_id: '2610.12391'
url: https://arxiv.org/abs/2610.12391
pdf_url: https://arxiv.org/pdf/2610.12391
published: '2026-10-08'
collected: '2026-10-10'
category: Reasoning
direction: 多模态几何推理 · 反思式优化框架
tags:
- MLLM
- Multimodal Reasoning
- Reflective Learning
- Geometry Reasoning
- Formalization Optimization
one_liner: 提出反思式形式化演化框架GeoReform，大幅提升多模态大模型几何推理准确率
practical_value: '- 可复用反思式优化思路：把RAG/多模态输入的结构化表示从固定输出改为可优化策略，通过失败case诊断迭代优化抽取规则，降低冗余信息干扰、提升推理准确率

  - 多模态内容理解场景可迁移：电商商品图属性抽取、广告素材语义解析场景，可通过全链路推理失败case回标，优化实体/关系的选择、分组、呈现规则，减少歧义

  - 小参数MLLM落地优化参考：无需全量微调，仅通过优化输入的结构化表示策略即可显著提升小模型任务准确率，降低推理部署成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
MLLM在几何题求解场景下难以准确识别、使用图表中的几何关系，现有将几何实体/关系转换为文本表示的方法易引入冗余、歧义问题，既会修复部分错误也会新增错误，核心痛点并非提取事实不足，而是结构化表示的组织方式无法支撑下游推理。
### 方法关键点
提出GeoReform反思式形式化演化框架，将结构化表示定义为可优化策略而非固定解析输出，通过执行全推理链路、收集失败rollout、诊断当前表示缺陷、迭代突变策略，优化几何实体/关系/约束的选择、grounding、分组和呈现方式。
### 关键结果
在Geometry3K数据集上，将Qwen3VL-2B的准确率从42.0%提升至56.0%，多个几何推理基准实验验证了有效形式化对多模态几何推理的关键作用。
