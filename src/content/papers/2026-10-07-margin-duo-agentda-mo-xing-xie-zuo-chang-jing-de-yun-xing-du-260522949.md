---
title: 'MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination'
title_zh: MARGIN：多Agent大模型协作场景的运行时置信度校准方法
authors:
- Joss Armstrong
affiliations:
- Ericsson, Athlone, Ireland
arxiv_id: '2605.22949'
url: https://arxiv.org/abs/2605.22949
pdf_url: https://arxiv.org/pdf/2605.22949
published: '2026-10-07'
collected: '2026-10-09'
category: MultiAgent
direction: 多智体协作 · 置信度校准
tags:
- Multi-Agent
- Confidence Calibration
- Online Learning
- Distribution Shift
- LLM Coordination
one_liner: 提出无需重训无需预留校准集的多Agent在线置信度校准方法，提升异构模型协作决策准确率
practical_value: '- 多LLM协作的业务场景（如商品文案生成选优、query改写排序、多召回源结果融合）可直接复用MARGIN校准逻辑：无需重训模型，仅通过历史正确性反馈校正各模型的置信度权重，即可提升选优准确率

  - 分布漂移频繁的业务场景可借鉴EWMA+稀疏带收缩的设计：用指数滑动平均跟踪近期准确率与置信度的比值，数据稀疏时向模型级估计融合，兼顾漂移适应性与估计稳定性

  - 多模型投票选优场景可替换原始置信度加权逻辑：解决异构模型置信度不可比、甚至置信度与准确率负相关的「置信度反转」问题，比直接用原始置信度投票更可靠

  - 若业务中仅能获得选中结果的反馈，需补充少量探索性校验：仅更新选中模型的校准状态会导致校准效果下降30pct左右，需定期校验未选中模型的输出正确性以维持校准精度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
异构多Agent协作时，不同大模型自报的置信度标准不统一，任务分布漂移后预训练的校准规则会快速失效；传统固定后验校准方法（如温度缩放）需要预留校准集且无法应对漂移，极端场景下甚至会出现高置信度模型准确率更低的「置信度反转」问题，直接用原始置信度加权投票的决策效果可能差于随机选择。

### 方法关键点
- 将0-1置信度划分为3个等宽区间，为每个（模型，置信度区间）对用EWMA分别跟踪历史准确率与平均上报置信度，二者比值作为区间级校准因子
- 样本稀疏的区间校准因子向模型级全局校准因子收缩，解决小样本下的估计方差问题
- 校准后的置信度作为多模型投票的权重，无需重训模型、无需预留校准集，仅靠后续的正确性反馈即可在线更新

### 关键结果
在代码生成、QA、数学三类任务，18模型池/9模型子集的分布漂移实验中验证：
- 分布漂移后ECE比5个在线基线低1.53~30.52pct，代码生成任务答案选择准确率比原始置信度加权高4.3~14.0pct
- BigCodeBench场景下原始置信度与准确率负相关（r=-0.692），成对选优准确率仅42.37%（低于随机50%），校准后提升至63.36%

> 最值得记住：异构多LLM协作时不要直接信任模型自报的置信度，仅靠历史正确性反馈做轻量在线校准即可大幅提升决策效果，且能自适应任务分布漂移
