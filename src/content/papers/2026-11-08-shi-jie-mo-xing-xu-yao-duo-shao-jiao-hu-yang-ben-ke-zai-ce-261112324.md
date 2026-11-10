---
title: How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics
  at Test Time
title_zh: 世界模型需要多少交互样本可在测试时学习未知游戏机制
authors:
- Ku Onoda
- Haruto Kawano
- Shota Takashiro
- Kohei Hayashi
affiliations:
- Third Intelligence, Inc.
- The University of Tokyo
arxiv_id: '2611.12324'
url: https://arxiv.org/abs/2611.12324
pdf_url: https://arxiv.org/pdf/2611.12324
published: '2026-11-08'
collected: '2026-11-10'
category: Agent
direction: Agent 世界模型小样本环境规则学习
tags:
- World Model
- Test-Time Training
- Few-Shot Learning
- Agent
- ARC Benchmark
one_liner: 提出MechEval机制评估基准与轻量化WARC世界模型，验证小样本下测试时学习未知环境机制的可行性
practical_value: '- 测试时全参数微调轻量化方案：小参数量预训练模型在新场景下实时更新全量权重，相比固定权重/RAG对新规则拟合速度提升显著，可复用至推荐冷启动场景快速适配新流量/新商品规则

  - 细粒度分规则评估方法：将业务/环境规则拆解为独立机制分别统计准确率，避免整体指标掩盖子规则拟合缺陷，可用于LLM4Rec、Agent系统的效果归因

  - 冷启动样本量参考阈值：80次左右交互即可让半数新规则达到80%预测准确率，为电商新场景冷启动的最小样本量设定提供可参考的经验值'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
世界模型是Agent规划与想象学习的核心基础，但在陌生环境下仅能通过有限交互学习环境规则，此前缺乏对所需样本量的量化结论与针对性评估框架。
### 方法关键点
1. 构建MechEval评估基准，标注ARC-AGI-3数据集20个游戏的69种重复环境机制，按每轮交互下机制作用单元格的预测准确率量化效果
2. 提出35M参数量的ViT结构WARC世界模型，预训练后在新游戏交互的每步都执行全参数更新
### 关键结果数字
80%的未知机制可达到≥80%的预测准确率并保持稳定，其中半数仅需约80次交互即可达标，无测试时更新时仅14%的机制能达标；搭配固定图探索器的WARC-Agent效率分从0.15提升3倍至0.46，Kaggle隐藏榜得分0.20
