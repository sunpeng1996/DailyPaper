---
title: Accurate, Interdisciplinary and Transparent Structure-property Understanding
  with Deep Native Structural Reasoning
title_zh: 基于深度原生结构推理的精准跨学科透明结构-性质关系解读
authors:
- Chen Tang
- Yizhou Wang
- Jianyu Wu
- Lintao Wang
- Shixiang Tang
- Pengze Li
- Encheng Su
- Jun Yao
- Jiabei Xiao
- Yuqi Shi
affiliations:
- Shanghai Artificial Intelligence Laboratory
- The Chinese University of Hong Kong
- Shanghai Jiao Tong University
- Fudan University
- University of Sydney
arxiv_id: '2607.07708'
url: https://arxiv.org/abs/2607.07708
pdf_url: https://arxiv.org/pdf/2607.07708
published: '2026-07-07'
collected: '2026-07-12'
category: Other
direction: 跨学科科学大模型 · 结构性质推理
tags:
- Multimodal LLM
- Scientific Reasoning
- Structure Representation
- Interpretable AI
one_liner: 提出覆盖蛋白/小分子/晶体的多模态科学推理模型SciReasoner，实现高精度可解释结构性质分析
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
生物、化学、材料领域的结构-性质关系解读需同时保留领域原生结构信息，且满足科学约束下的可解释推理，现有AI方案存在表征与推理的双重瓶颈。

### 方法关键点
提出多模态科学基础模型SciReasoner，将坐标、拓扑、周期性连接离散为统一的结构感知词汇表，把结构token作为自回归推理轨迹中可寻址的证据单元，支持蛋白质、小分子、无机晶体三类跨领域场景的原生结构推理。

### 关键结果数字
- 86个基准测试中67项达到SOTA性能
- 低同源蛋白细胞组分注释F_max从0.42提升至0.55
- 单步逆合成准确率从0.63提升至0.72，同时生成片段级断键与前体验证轨迹
- 双盲专家评估显示98%案例中其推理轨迹优于或持平前沿大模型
