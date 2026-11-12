---
title: 'ABRR: Transforming Temporal Sentence Grounding with Wasserstein-Adaptive Refinement
  and Precision Ranking'
title_zh: ABRR：结合Wasserstein自适应修正与精度排序的时序句子定位框架
authors:
- Xiang Fang
- Wanlong Fang
- Junhao Dong
- Daizong Liu
arxiv_id: '2611.13310'
url: https://arxiv.org/abs/2611.13310
pdf_url: https://arxiv.org/pdf/2611.13310
published: '2026-11-09'
collected: '2026-11-12'
category: Multimodal
direction: 多模态时序定位 · 后处理优化
tags:
- Temporal Sentence Grounding
- Optimal Transport
- Post-processing
- Boundary Refinement
- Re-ranking
one_liner: 提出无需重训的模型无关时序句子定位后处理框架，大幅提升高IoU阈值下的定位与排序表现
practical_value: '- 短视频/直播电商的内容检索、片段定位场景，可复用Wasserstein距离+Sinkhorn迭代的最优运输方法，解决离散化下采样带来的量化误差问题

  - 多模态召回排序的结果打分可借鉴复合得分设计，同时平衡语义匹配度与定位/推荐精度两类异质指标，提升高严格度阈值下的效果

  - 存量线上模型的效果迭代可优先采用模型无关的后处理方案，无需重训即可低成本获得性能增益，大幅降低上线成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有Temporal Sentence Grounding(TSG)方法存在两大瓶颈：时序下采样引入的量化误差导致片段边界错位，预测结果仅按语义匹配排序未考虑定位精度，高IoU阈值下表现极差。
### 方法关键点
提出模型无关的后处理框架ABRR，无需重训即可提升任意TSG模型性能，核心包含三个组件：
1. 时序分布平滑：通过高斯核卷积降低预测得分分布噪声
2. 最优运输边界修正：基于2-Wasserstein距离与Sinkhorn迭代对齐粗边界与真实时序片段
3. 质量驱动重排：采用平衡定位精度与语义相关性的复合得分重排预测结果
### 关键结果
在Charades-STA、ActivityNet Captions、QVHighlights三个基准数据集上，严格IoU阈值（如IoU=0.7）下性能获得稳定提升，同时排序表现显著优化，计算效率高且兼容所有现有TSG模型
