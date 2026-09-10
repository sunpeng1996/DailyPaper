---
title: 'IdeaAMBIG: Benchmarking Implementation-Critical Gaps in Research-Idea Specifications'
title_zh: IdeaAMBIG：研究思路规范中实现关键缺口的基准测试
authors:
- Yiling Ma
- Yilun Zhao
- Sihong Wu
- Manasi Patwardhan
- Arman Cohan
affiliations:
- Yale University
- TCS Research
arxiv_id: '2609.10539'
url: https://arxiv.org/abs/2609.10539
pdf_url: https://arxiv.org/pdf/2609.10539
published: '2026-09-09'
collected: '2026-09-10'
category: Eval
direction: LLM能力评估 · 实现缺口基准测试
tags:
- Benchmark
- LLM Evaluation
- Reproducibility
- Coding Agent
- Ambiguity Detection
one_liner: 构建含660个实例的IdeaAMBIG基准，评估LLM对研究方法规范的可编码性检测、缺陷定位与澄清生成能力
practical_value: '- 做Agent辅助算法落地时，可跳过缺陷定位瓶颈，优先基于人工标注的歧义点生成澄清方案，大幅提升编码实现效率

  - 复现推荐/LLM领域新算法时，可参考本基准的三类评估流程（就绪检测→缺陷定位→澄清），减少复现踩坑

  - 团队内部算法文档规范可参考本基准的缺口标注逻辑，明确参数、流程定义，降低跨角色协作的信息差'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
大量研究方法描述信息不足，实现者/编码Agent需引入无依据假设才能复现，行业缺少标准化的实现缺口评估基准。
### 方法关键点
从论文、代码库、Issue、复现物料中构建实证支撑的规范与解决方案，推出含660个实例的IdeaAMBIG基准：163个真实缺口来自复现报告与GitHub Issue，497个为向可编码规范注入的可控合成缺口，覆盖三类评估任务：可编码就绪度检测、无提示缺陷定位、给定缺陷的澄清动作生成。
### 关键结果
13款LLM测试中，最优模型真实场景Macro Defect Recovery Rate仅9.6%，给定缺陷后Macro Clarification Action Success Rate达80.6%；oracle测试中提供金标解决方案可将下游可编码率从14%提升至98%，缺陷定位是当前核心瓶颈。
