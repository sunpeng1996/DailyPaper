---
title: 'SemRF: A Semantic Reference Frame for Residual-Stream Dynamics in Language
  Models'
title_zh: SemRF：面向大语言模型残差流动态的语义参考框架
authors:
- Jian Gu
- Aldeida Aleti
- Chunyang Chen
- Hongyu Zhang
affiliations:
- Monash University
- Technical University of Munich
- Chongqing University
arxiv_id: '2606.32022'
url: https://arxiv.org/abs/2606.32022
pdf_url: https://arxiv.org/pdf/2606.32022
published: '2026-06-30'
collected: '2026-07-01'
category: LLM
direction: LLM 残差流语义可解释性分析
tags:
- Residual-Stream
- Semantic-Analysis
- LLM-Interpretability
- Semantic-Frame
- Model-Optimization
one_liner: 提出锚定的语义参考框架SemRF，解决LLM残差流跨层语义测量漂移问题
practical_value: '- 做LLM4Rec可解释性分析时，可复用SemRF的锚定语义坐标方法，避免跨层语义测量漂移，更精准定位推荐决策在LLM各层的生成节点

  - 做LLM推理优化时，可基于SemRF给出的语义轨迹曲率特征，识别可压缩的低语义复杂度层，做剪枝/量化降低推理延迟

  - 做Agent的LLM工具调用对齐时，可通过SemRF的语义轨迹tube约束，快速诊断偏离预期语义的残差层，提升指令遵循准确率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
LLM残差流跨层计算演化分析缺乏稳定语义坐标，嵌入侧锚点与 unembedding 读出层的语义跨度不一致时，观测到的隐状态变化会反映测量漂移而非真实计算逻辑。
### 方法关键点
1. 提出锚定的 Semantic Reference Frames (SemRF)，固定语义锚点测量残差状态，通过伪逆绑定实现锚点精确同步，在受限双可逆条件下生成稳定语义基坐标与失真边界
2. 基于锚点构建语义Voronoi图，定义跨层语义轨迹、层间贡献剖面与失衡诊断指标，推导约束管内的最小作用量规范轨迹
### 关键结果
低曲率语义轨迹支持分段线性压缩，低复杂度轨迹所需语义自由度更少，可直接关联模型参数效率；规范轨迹唯一且符合离散样条方程，多余作用量可量化步长、曲率、贡献剖面的匹配偏差
