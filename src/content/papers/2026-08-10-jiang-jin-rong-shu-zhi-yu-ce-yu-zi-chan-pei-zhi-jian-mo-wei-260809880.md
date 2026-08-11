---
title: Financial Numerical Prediction and Allocation as Token Generation
title_zh: 将金融数值预测与资产配置建模为Token生成任务
authors:
- Xu Ouyang
- Moontae Lee
affiliations:
- University of Illinois Chicago
arxiv_id: '2608.09880'
url: https://arxiv.org/abs/2608.09880
pdf_url: https://arxiv.org/pdf/2608.09880
published: '2026-08-10'
collected: '2026-08-11'
category: LLM
direction: LLM生成范式 · 数值预测与决策
tags:
- Token Generation
- LoRA
- SFT
- GRPO
- Financial Prediction
one_liner: 提出无任务头的FinATOM框架，通过约束Token生成实现金融收益预测与动态资产配置
practical_value: '- 可复用「无任务头Token生成」范式替代传统回归/排序头，将推荐分、广告出价、预算分配等连续数值任务转为生成任务，降低多任务架构复杂度

  - 数值类决策任务可参考「先SFT拟合基线策略+后RL优化业务目标」的两阶段训练流程，兼顾策略稳定性和业务指标提升

  - 多模态输入（用户行为、商品属性、舆情文本等）可直接接入共享LLM语义空间，无需额外特征融合头，降低工程开发成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：传统金融预测依赖任务特定的回归、排序、策略头，LLM与最终输出的数值目标解耦，多任务架构碎片化，维护成本高

**方法**：提出FinATOM框架，基于Llama 3.2 1B + LoRA，无需任务特定数值头，统一将收益预测、资产配置转为约束Token生成任务；预测模块自回归生成波动率标准化的收益Token，先做序数、排序监督训练，再做1 epoch token级策略优化；配置模块生成归一化多头权重，先SFT拟合因果均值方差基准，再用DAPO增强的GRPO优化21天Sharpe，同时保证与基准一致性

**结果**：2023-2025 ETF测试中，配置策略总毛Sharpe从1.428提升至1.529，5bp交易成本下净Sharpe从1.394提升至1.494；多模态输入的三期平均Sharpe达1.540；FinTexTS数据集上SFT和策略版本分别取得73.52%/2.68、73.72%/2.69的累计收益/Sharpe
