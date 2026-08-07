---
title: Rethinking Modality Reliability in Multimodal Sentiment Analysis with Incomplete
  Observations
title_zh: 不完备观测场景下多模态情感分析的模态可靠性重思考
authors:
- Chunlei Meng
- Jacqueline J. Pang
- Pengbin Feng
- Zhenyu Yu
- Chun Ouyang
- Zhongxue Gan
affiliations:
- Fudan University
- J.P. Morgan Chase
- University of Southern California
arxiv_id: '2608.03611'
url: https://arxiv.org/abs/2608.03611
pdf_url: https://arxiv.org/pdf/2608.03611
published: '2026-08-04'
collected: '2026-08-07'
category: Multimodal
direction: 多模态情感分析 · 不完备观测鲁棒优化
tags:
- Multimodal Sentiment Analysis
- Incomplete Observation
- Modality Reliability
- Cross-modal Fusion
- Robustness
one_liner: 提出显式建模样本级模态可靠性的MRCF框架，解决不完备多模态情感分析的两类可靠性偏差
practical_value: '- 电商直播/短视频多模态评论、弹幕情感分析可复用模态可靠性校准逻辑，某模态（如嘈杂音频、模糊画面）缺失/降质时自动下调权重，提升情感识别准确率

  - 多模态召回、排序场景可借鉴样本级可靠性估计算法，基于模态内质量、跨模态一致性打分动态调整各模态特征融合权重，避免降质特征污染预测结果

  - 多模态交互Agent可复用可靠性引导的跨模态信息流调制方法，输入语音/图像质量差时优先依赖文本信号决策，降低决策错误率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有不完备观测下多模态情感分析（MSA）仅隐式处理模态可靠性，存在两类问题：一是可靠性不匹配，不同样本/缺失率下各模态情感证据差异大；二是可靠性传播偏差，降质模态信息会干扰跨模态交互，拉低预测性能。
### 方法关键点
提出MRCF模态可靠性校准框架，核心包含三个模块：1）可靠性感知分支，基于模态内质量特征、跨模态语义一致性估计样本级模态可靠性分数；2）可靠性引导交互分支，用可靠性分数调制跨模态信息流，抑制降质模态无效信息传播；3）可靠性校准融合模块，结合可靠性分数与语义特征输出最终预测。
### 关键结果
在CMU-MOSI、CMU-MOSEI、CH-SIMS三类标准不完备观测MSA数据集上性能显著优于基线，显式可靠性建模可有效缓解两类可靠性偏差。
