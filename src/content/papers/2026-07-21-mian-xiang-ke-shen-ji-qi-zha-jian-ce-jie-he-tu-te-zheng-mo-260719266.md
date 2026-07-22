---
title: 'Toward Auditable Fraud Detection: Combining Graph Features, Model Explanations,
  and Agentic Case Investigation'
title_zh: 面向可审计欺诈检测：结合图特征、模型解释与智能体案件调查
authors:
- Rahil Sharma
affiliations:
- Vrije Universiteit Amsterdam
arxiv_id: '2607.19266'
url: https://arxiv.org/abs/2607.19266
pdf_url: https://arxiv.org/pdf/2607.19266
published: '2026-07-21'
collected: '2026-07-22'
category: Agent
direction: Agent 风控欺诈检测场景落地验证
tags:
- Fraud Detection
- Graph Feature
- TreeSHAP
- LLM Agent
- Anomaly Detection
one_liner: 构建分层欺诈检测pipeline，验证各组件适用边界，指出智能体合理理据不代表决策更优
practical_value: '- 风控/反作弊场景迭代前优先清理数据集中的捷径特征（如本研究移除的模拟器余额捷径），避免基线性能虚高误导优化方向

  - 中等置信度待判样本子集可叠加图结构特征、异常检测信号，提升该区间违规样本排序效果，比全量加特征性价比更高

  - 对接分类模型的LLM决策辅助Agent不要直接替换阈值规则，可增加「Agent与模型结果不一致触发人工审核」的规则降低误判率

  - 不可将Agent生成理据的连贯性作为决策质量判断标准，必须完成离线准确率对比验证后再上线'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
风控欺诈检测系统需兼顾高吞吐、可解释性与可审计性，当前欺诈手段自动化程度持续提升，人工审核资源紧张，大量误报进一步消耗运营成本。
### 方法关键点
1. 先清理PaySim数据集的模拟器专属余额捷径特征，避免基线性能虚高
2. 搭建分层pipeline：梯度提升分类器做基础打分，叠加图结构特征、自编码器异常信号优化排序
3. 对分类器输出的中等置信度样本，调用可访问TreeSHAP解释、图上下文、参考案例的bounded LLM调查Agent做二次校验
4. 新增Agent与基础模型结果不一致时触发人工审核的escalation规则
### 关键结果数字
- 全量测试集下图特征、异常信号未提升平均精度，但在中等置信度子集上欺诈排序效果显著提升
- 注入多账号欺诈团伙实验中，图结构特征100%召回注入欺诈交易，tabular基线仅召回~75%
- Agent决策准确率65.0%，低于基础分类器阈值规则的71.7%；其修改的8个决策中6个为错判，且全部附带连贯生成理据
- 不一致触发审核规则可100%召回2个Agent严重错误，无误报
