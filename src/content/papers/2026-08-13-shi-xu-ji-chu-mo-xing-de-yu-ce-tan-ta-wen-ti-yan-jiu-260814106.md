---
title: Forecast Collapse in Time-Series Foundation Models
title_zh: 时序基础模型的预测坍塌问题研究
authors:
- Shu Wan
- Miles Ma
- Hank Zhu
- Guangqi Liu
- Stephen Wang
- Qingsong Wen
- Huan Liu
affiliations:
- Abel AI Lab
- Arizona State University
- University of Oxford
arxiv_id: '2608.14106'
url: https://arxiv.org/abs/2608.14106
pdf_url: https://arxiv.org/pdf/2608.14106
published: '2026-08-13'
collected: '2026-08-17'
category: Other
direction: 时序基础模型 · 预测优化
tags:
- Time-Series Foundation Model
- Forecast Collapse
- Calibration
- Ranking
- Objective Optimization
one_liner: 发现时序基础模型预测坍塌现象，揭示校准-排序权衡，提出CalibRank目标平衡两类指标
practical_value: '- 电商/推荐多目标优化场景可参考校准-排序权衡分析框架，避免单优化MSE等校准指标导致排序效果退化的问题

  - 多序列排序类业务（如多商品销量预测选品、多广告出价排序）需补充跨序列相关性评估，避免传统单序列指标的评估盲点

  - 可直接复用CalibRank的加权目标设计，无需修改模型架构就能同时兼顾预测校准度和跨序列排序效果'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
时序基础模型在1000只美股小时收益率预测任务中出现预测坍塌：输出几乎平坦，跨序列排序（截面相关性）表现极差，但同设置下交易量预测无该问题，传统单序列评估指标无法发现该缺陷。
### 方法关键点
覆盖12个深度学习预测模型、多款时序基础模型、97个公开基准配置做验证，定位两个核心诱因：低可预测性限制校准点预测的振幅，单序列优化目标无法捕捉跨序列结构；揭示校准-排序权衡，提出CalibRank加权目标，融合校准损失与截面相关性损失平衡两类需求。
### 关键结果
在Finance1K数据集上，CalibRank将截面相关性提升近3倍，同时保持预测振幅接近真实值，在所有测试模型上均能提升排序指标。
