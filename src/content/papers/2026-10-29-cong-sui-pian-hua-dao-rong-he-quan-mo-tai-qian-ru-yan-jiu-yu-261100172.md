---
title: 'From Fragmentation to Fusion: A Survey and Roadmap for Omnimodal Embeddings'
title_zh: 从碎片化到融合：全模态嵌入研究综述与路线图
authors:
- Ziyin Zhang
- Yuyu Guo
- Ying Zhang
- Siqiao Xue
- Zihan Liao
- Jin Qin
- Wenjie Yang
- Siyuan Yang
- Shijie Li
- Cheng Chen
affiliations:
- Ant Group
- Shanghai Jiao Tong University
- Australian National University
- Tongji University
- National University of Singapore
arxiv_id: '2611.00172'
url: https://arxiv.org/abs/2611.00172
pdf_url: https://arxiv.org/pdf/2611.00172
published: '2026-10-29'
collected: '2026-11-03'
category: Multimodal
direction: 全模态嵌入 · 跨模态统一建模路线
tags:
- Omnimodal Embedding
- Cross-Modal Alignment
- Joint Embedding
- Contrastive Learning
- Transformer
one_liner: 梳理多模态嵌入技术收敛趋势，提出3C能力框架与三条统一路径，构建首个全模态嵌入研究全景
practical_value: '- 搭建跨模态检索/推荐系统时可参考3C能力框架分层评估：先校验多模态输入覆盖率，再验证跨模态召回可比性，最后测试组合语义召回有效性

  - 多模态统一建模可按业务阶段对齐路径选型：初期用transformation方案快速覆盖多模态，中期用双塔对齐方案平衡效果与性能，长期迭代联合嵌入方案支撑复杂需求

  - 可复用跨模态嵌入研究的共性收敛规律，优先落地对比学习、Transformer架构等已验证的通用组件，降低模态适配研发成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
搜索、推荐等主流AI系统的底层核心是嵌入模型，当前嵌入研究按模态割裂发展，不同社区独立演进极少复用经验，掩盖了不同模态嵌入技术的深层收敛性，抬升了全模态建模的落地成本。

### 方法关键点
基于对比学习、Transformer架构、粒度对齐三大跨模态嵌入共同驱动因素，定义coverage、comparability、compositionality三层递进的3C能力评估框架，对应三条逐步升级的统一路径：transformation拓展多模态输入覆盖能力，alignment实现跨模态表征可比，joint embedding作为最终演进目标支撑复杂组合语义表达。

### 关键结果
首次输出跨7类模态（文本/代码、视觉/视频、音频、图、时序、表格）的全模态嵌入研究全景，系统梳理了不同技术路径的选型适配场景，是首个跨模态嵌入领域的统一综述框架。
