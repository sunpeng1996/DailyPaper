---
title: Localize-Then-Decide Guarantees for LLM Judgments
title_zh: 面向大语言模型评判任务的先定位后决策一致性保证方法
authors:
- Xinyu Li
- Yi Zhou
- Guanqun Cao
- Zeyu Fu
- Tianjin Huang
- Gaojie Jin
affiliations:
- University of Exeter
- Cardiff University
- University of the West of England
- University of Macau
arxiv_id: '2608.25824'
url: https://arxiv.org/abs/2608.25824
pdf_url: https://arxiv.org/pdf/2608.25824
published: '2026-08-26'
collected: '2026-08-27'
category: Eval
direction: LLM评估 · 评判一致性保证
tags:
- LLM-as-Judge
- Conformal Prediction
- Calibration
- Preference Alignment
- Confidence Estimation
one_liner: 提出两阶段Localize-Then-Decide框架，解决多候选场景LLM评判置信度失真问题，实现高概率人类对齐保证
practical_value: '- 多候选生成排序场景（如AIGC文案选优、推荐候选truncation）可复用先定位后决策的两阶段结构，先用轻量规则筛出topN短名单再做精细置信度校验，避免多候选下置信度失真。

  - 线上LLM自动评估链路（如生成式推荐结果质量校验、Agent决策结果抽检）可引入共形预测做候选集范围兜底，保证高概率覆盖人类偏好结果，降低bad case漏判风险。

  - 可借鉴校准后的置信度弃权规则，在置信度不足时触发人工审核，平衡自动评审的效率和准确率，适合电商评论moderation、广告素材合规校验等场景。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有基于置信度阈值的LLM评判一致性保证方案仅适配两两比较场景，当候选响应数量增多时，概率质量分散在多个选项会导致置信度估计失真，置信度与错判风险的单调关系失效，无法提供可靠的人类判断对齐保证。

### 方法关键点
提出Localize-Then-Decide两阶段框架：1. 第一阶段基于共形预测生成小规模候选短名单，以高概率覆盖人类偏好的响应；2. 第二阶段基于校准后的置信度规则，从短名单中选择最优响应或选择弃权，修复置信度与错判风险的单调关系，实现高概率对齐保证。

### 关键结果
在多数据集、多候选尺寸、多款评判LLM的实验验证中，该框架相比单阶段基线，保证成功率持续更优，覆盖率有大幅提升。
