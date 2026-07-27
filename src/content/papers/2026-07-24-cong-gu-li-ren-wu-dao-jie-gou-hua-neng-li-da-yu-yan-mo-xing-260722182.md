---
title: 'From Isolated Tasks to Structured Capabilities: A Multilayer Taxonomy for
  Large Language Models'
title_zh: 从孤立任务到结构化能力：大语言模型多层能力分类体系
authors:
- Shixin Fang
- Jiachen Wo
- Wenjuan Qin
- Sihang Jiang
- Yanghua Xiao
affiliations:
- Fudan University
arxiv_id: '2607.22182'
url: https://arxiv.org/abs/2607.22182
pdf_url: https://arxiv.org/pdf/2607.22182
published: '2026-07-24'
collected: '2026-07-27'
category: Eval
direction: 大语言模型 · 能力分类与评估
tags:
- LLM
- Evaluation
- Capability Taxonomy
- Cognitive Science
- Benchmark
one_liner: 基于认知科学构建LLM三层14领域91子技能分类体系，完成1.5万余篇顶会LLM论文能力分布标注
practical_value: '- 自研Agent/LLM4Rec能力评估可复用该三层分类框架，避免评估任务零散无体系，快速定位能力覆盖盲区

  - 电商场景定制LLM训练目标时，可参考高协同lift的能力对（如语义+推理）设计组合训练任务，提升能力迁移效率

  - Agent版本迭代对比时，可基于该分类的子技能粒度做能力增益/退化的细粒度诊断，准确定位迭代问题'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM评估围绕孤立任务组织，碎片化问题导致跨研究对比困难、能力映射模糊、覆盖缺口难以识别。
### 方法关键点
以人类认知科学为指导（不依赖LLM架构），构建包含基础层、建构层、整合层的三层能力分类体系，覆盖14个能力域、91项子技能；通过多模型标注、共识仲裁流程，完成2023-2025年ACL/AAAI/ICML/NeurIPS共3.15万余篇论文筛选，映射1.59万篇LLM相关论文的能力分布。
### 关键结果
22.3%研究聚焦语言语义能力、21.3%聚焦推理能力，6个能力域占比不足2%；域内Top子技能中位数占比97.9%，10个域的Top子技能覆盖率≥90%；语言语义+推理是最高频能力组合（占比11.7%，lift=2.47），心理理论+社交推理交互是协同提升最高的能力对（lift=30.84）。
