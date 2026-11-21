---
title: 'Overlooked and Underutilized: Prototypes are the Missing Piece in Tabular
  XAI'
title_zh: 被忽视且未充分利用：原型是表格可解释AI的缺失拼图
authors:
- Jacek Karolczak
- Jerzy Stefanowski
affiliations:
- Institute of Computing Science, Poznan University of Technology
arxiv_id: '2611.24831'
url: https://arxiv.org/abs/2611.24831
pdf_url: https://arxiv.org/pdf/2611.24831
published: '2026-11-18'
collected: '2026-11-21'
category: Other
direction: 表格可解释AI · 原型式解释方法优化
tags:
- XAI
- Tabular Data
- Prototype Explanation
- Feature Attribution
- Cognitive Load
one_liner: 提出将原型纳入表格XAI解释体系，结合认知理论与几何验证降低非专家用户认知负担
practical_value: '- 推荐系统排序/召回模型的特征归因解释可引入原型分组方法，将关联用户/物品特征聚合成语义单元，大幅降低运营/产品侧的解释理解成本

  - 高风险业务场景（如电商信贷授信、广告投放准入）的模型审计流程，可叠加原型相似性推理+特征级校验的复合解释pipeline，平衡易用性与严谨性

  - 面向业务方的模型效果解释报告可参考认知理论适配System 1思考模式，优先输出典型样本级结论再下钻特征细节，提升跨角色沟通效率'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前表格场景XAI高度依赖特征归因方法，孤立特征的解释结果需要非专家用户（如运营、业务方）付出极高认知成本，现有方案缺乏兼顾严谨性与易用性的直观解释入口。

### 方法关键点
1. 将原型尤其是原型片段作为特征归因的补充解释方案，把关联特征分组为有界子空间内的语义单元，替代孤立特征输出解释
2. 认知层面契合Rosch分类理论与Kahneman系统1快思考逻辑，自然降低用户理解成本
3. 引入几何有效性三元组框架，从数据流形验证维度保障原型解释的可靠性
4. 倡导采用「直观相似性推理+严格特征级审计」的复合解释pipeline

### 结论
该方案为表格XAI的易用性优化提供了明确研究方向，同时梳理了原型方法落地的开放挑战与潜在解决路径。
