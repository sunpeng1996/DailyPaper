---
title: 'Inter-X++: A Comprehensive Benchmark for Multimodal Human-Human Interaction
  Analysis'
title_zh: Inter-X++：面向多模态人与人交互分析的综合基准
authors:
- Liang Xu
- Chengqun Yang
- Zili Lin
- Xintao Lv
- Yichao Yan
- Xin Jin
- Zhibo Chen
- Xiaokang Yang
- Wenjun Zeng
arxiv_id: '2608.20312'
url: https://arxiv.org/abs/2608.20312
pdf_url: https://arxiv.org/pdf/2608.20312
published: '2026-08-20'
collected: '2026-08-23'
category: Other
direction: 多模态人-人交互基准与统一建模
tags:
- Multimodal Benchmark
- Human-Human Interaction
- Unified Representation
- Generative Modeling
- Perception Task
one_liner: 发布大规模多模态HHI基准Inter-X++与统一建模框架OpenHHI，覆盖感知与生成任务
practical_value: '- 电商直播数字人互动场景可参考其多模态交互标注框架（动作-语义层级映射逻辑），提升数字人对用户动作/语言的响应自然度

  - 做多模态生成+感知联合优化任务时，可复用其统一表示对齐思路，降低不同任务范式的重复建模成本

  - 建设垂直领域基准时，可参考其统一评测协议制定方法，消除不同模型横向对比的歧义'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有人与人交互（HHI）数据集普遍存在运动精度低、缺失手势细节、多模态标注不足问题，同时交互表示碎片化、评测协议不统一，严重阻碍数字人系统的研发迭代。
### 方法关键点
1. 采用新型混合动捕系统构建Inter-X++大规模基准，覆盖全身动作、手指关节细节；
2. 配套多维度标注，包括层级化细粒度文本描述、交互分类、因果顺序、主体关系/性格、接触图谱、物理约束等；
3. 统一交互表示与评测协议，覆盖生成、感知两大类共4种下游任务；
4. 提出OpenHHI统一建模框架，联合优化交互重建与语义理解。
### 关键结果
包含11388条高保真交互序列、超8.1M帧数据；OpenHHI在所有生成、感知类下游任务上均达到SOTA，验证了统一表示可同时打通交互理解与生成。
