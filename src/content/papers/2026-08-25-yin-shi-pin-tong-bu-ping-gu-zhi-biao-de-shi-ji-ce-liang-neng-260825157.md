---
title: What Do Audio-Visual Synchronization Metrics Actually Measure?
title_zh: 音视频同步评估指标的实际测量能力审计
authors:
- Jai Kumar Sharma
- Peeyush Tapadiya
affiliations:
- Virginia Tech
- Accenture
arxiv_id: '2608.25157'
url: https://arxiv.org/abs/2608.25157
pdf_url: https://arxiv.org/pdf/2608.25157
published: '2026-08-25'
collected: '2026-08-28'
category: Eval
direction: 多模态生成效果评估 · 音视频同步指标
tags:
- Audio-Visual Sync
- Metric Evaluation
- Multimodal Generation
- Reliability Audit
one_liner: 针对四类主流音视频同步指标完成统一可靠性审计，给出分场景选型建议与多维度上报规范
practical_value: '- 短视频/直播生成类业务时序偏移检测优先选Synchformer/DeSync，感知对齐评估优先选ImageBind/JavisScore，避免单独使用AV-Align

  - 音视频同步效果不要上报单一分数，按指标族拆分+置信区间输出可靠性卡，降低评估偏差对业务迭代的误导

  - 无需尝试线性或简单k-NN的多指标融合方案，其效果无法超过最优单指标，可节省无效调优成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
当前音视频生成模型的排名、训练优化广泛依赖自动同步指标，但这类指标作为测量工具从未经过系统性审计，故障模式不明确，容易带偏优化方向。
### 方法关键点
针对AV-Align、ImageBind AV-relevance、JavisScore、Synchformer/DeSync四类主流同步指标，采用统一可靠性协议从6个维度审计：受控失真单调性、预处理敏感性、排序不确定性、跨指标一致性、PEAVS人工对齐代理一致性、学习融合效果。
### 关键结果
Synchformer/DeSync时序偏移跟踪能力最优，τ=0.84；ImageBind/JavisScore与人工感知对齐度最高，τ=0.20，对内容干扰类问题更敏感；指标间一致性极低，Krippendorff α=0.066，线性/k-NN融合无法提升与人工感知的对齐效果；AV-Align是表现最差的独立指标。
