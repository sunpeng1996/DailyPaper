---
title: 'Caved or Convinced: Temporal Sampling Gates Claim Deference in Video Large
  Language Models'
title_zh: 妥协还是信服：时序采样控制视频大模型的主张服从性
authors:
- Yuxin Cao
- Wei Song
- Jingling Xue
- Jin Song Dong
affiliations:
- National University of Singapore
- University of New South Wales
arxiv_id: '2608.03160'
url: https://arxiv.org/abs/2608.03160
pdf_url: https://arxiv.org/pdf/2608.03160
published: '2026-08-04'
collected: '2026-08-07'
category: Multimodal
direction: 多模态大模型 · 时序推理鲁棒性优化
tags:
- Video-LLM
- Temporal Reasoning
- Sampling Strategy
- Model Robustness
- Sycophancy Mitigation
one_liner: 拆分视频大模型时序判断错误的两类成因，设计反转测试大幅提升时序判断准确率
practical_value: '- 做短视频内容理解、时序事件判断的多模态Agent，可复用正反向帧打分的反转测试方法，消除模型时序先验偏差，提升判断准确率

  - 视频内容标签生成、电商短视频合规审核场景，可拆分「采样是否覆盖关键事件」和「证据权重分配」两类错误，针对性优化采样策略和对齐目标，避免盲目校准用户信任度同时恶化漏判、误判

  - Agent决策可靠性优化场景，可参考本文的干预测试方法，定位错误根源是输入信息缺失还是模型权重分配问题，降低调优试错成本'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
视频大模型时序判断存在两类相反错误：接受虚假主张（妥协）、拒绝正确主张（拒真），仅针对妥协问题的优化会恶化拒真问题，且现有研究未区分两类错误的核心成因：采样是否覆盖关键事件、模型是否优先信任视频证据而非用户主张。
### 方法关键点
1. 设计两类固定主张的干预实验：保持帧不变重排翻转主张真伪、固定帧预算偏移采样控制是否捕获事件，拆分采样可用性和证据权重的影响；
2. 反转测试：对采样帧做正反向打分抵消时序先验，无需读取主张即可选择回答、重采样或弃权。
### 关键结果
9个评测模型中，反转测试可将能识别时序的模型的时序准确率提升至0.92-1.00，对无法识别时序的模型触发弃权而非随机猜测
