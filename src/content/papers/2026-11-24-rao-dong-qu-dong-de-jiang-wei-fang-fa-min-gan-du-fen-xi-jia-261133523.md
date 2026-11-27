---
title: A Perturbation-Driven Framework for Sensitivity Analysis of Dimensionality
  Reduction
title_zh: 扰动驱动的降维方法敏感度分析框架
authors:
- Md Afridi Hasan
- Jaemin Jo
- Takanori Fujiwara
arxiv_id: '2611.33523'
url: https://arxiv.org/abs/2611.33523
pdf_url: https://arxiv.org/pdf/2611.33523
published: '2026-11-24'
collected: '2026-11-27'
category: Other
direction: 降维方法鲁棒性与敏感度评估
tags:
- Dimensionality Reduction
- Sensitivity Analysis
- Perturbation Probe
- Robustness Evaluation
- Visual Analytics
one_liner: 提出模型无关的扰动驱动框架，量化评估各类降维方法对输入微小波动的敏感度
practical_value: '- 评估推荐系统中用户/物品Embedding降维方案的鲁棒性，避免输入微小波动导致的召回池、用户分群结果大幅变动

  - 选择线上用的降维方法时不要只看传统distortion指标，需补充扰动敏感度测试，t-SNE类稳定性差的方案不适合线上敏感场景

  - 可复用扰动探针的设计思路，测试Embedding相关模块（如语义召回、向量匹配）对输入噪声的容错阈值'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有降维（DR）效果评估仅依赖可信度、连续性等distortion指标，未考虑真实场景输入存在噪声、采样波动的情况，无法衡量DR方法在微小输入变动下的输出稳定性，易导致Embedding下游应用（如聚类、召回）出现不可预期的波动。
### 方法关键点
提出模型无关的扰动驱动评估框架，将不同类型、不同强度的输入扰动作为可控探针，多次扰动输入后运行DR方法，统计低维表示的distortion指标变化，生成各DR方法的敏感度画像。
### 关键结果
传统指标表现优异的t-SNE存在显著敏感度，微小输入波动会导致聚类、轨迹等视觉结构大幅偏移；多维缩放（MDS）在特定扰动下的结构保序性更稳定，验证了敏感度分析作为DR方法补充评估维度的必要性。
