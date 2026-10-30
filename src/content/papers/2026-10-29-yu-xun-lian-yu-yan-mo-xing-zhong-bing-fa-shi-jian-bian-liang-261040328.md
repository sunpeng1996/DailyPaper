---
title: Factorized Representations of Concurrent Temporal Variables in Pretrained Language
  Models
title_zh: 预训练语言模型中并发时间变量的因子化表征
authors:
- Xinhe Zhang
- Arnau Marin-Llobet
affiliations:
- Harvard University
arxiv_id: '2610.40328'
url: https://arxiv.org/abs/2610.40328
pdf_url: https://arxiv.org/pdf/2610.40328
published: '2026-10-29'
collected: '2026-10-30'
category: LLM
direction: LLM表征可解释性 · 时间状态因子化
tags:
- representational_geometry
- factorized_representation
- temporal_state
- interpretability
- pretrained_LLM
one_liner: 发现预训练LLM对多个独立演化的时间上下文变量采用近似因子化的重叠子空间表征
practical_value: '- 做多上下文变量（如电商对话Agent的用户意图、会话时长、场景）的LLM表征提取时，可通过子空间ablation方法定位不同变量的专属表征子空间，避免特征混淆，提升多变量建模的稳定性

  - 多变量融合建模时可利用近似加性几何特性，低秩拟合联合表征降低特征维度，比如用户长短期兴趣融合时用加性因子建模，减少参数开销

  - LLM可控生成/推理干预不要仅依赖线性解码结果，必须验证表征修改对下游输出的真实影响，仅修改线性可解码的状态变量无法保证稳定控制生成效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有研究仅证实LLM能编码单个时间/上下文变量的结构化表征，但多个独立演化的并发变量（如对话中独立变化的说话人、话题、语言）的联合表征组织方式尚不明确，对LLM可控干预、多变量建模的落地缺乏理论支撑。

### 方法关键点
- 构造含独立相位语言切换、主题切换两个时间变量的受控语料，变量取值为对应事件发生后的句子数，无额外人工标记
- 提取10个不同家族预训练LLM中间层的句末残差流状态，用类质心张成的低秩子空间对应每个变量的表征平面
- 通过子空间消融、受限解码、联合质心加性拟合等方法，量化表征的选择性、重叠性和加性

### 关键结果
实验覆盖10款不同结构预训练模型、DailyDialog真实对话语料、3到51个时间步的长horizon场景、Qwen3从0.6B到14B全尺寸系列：自消融（移除对应变量子空间）可移除语言变量84%、主题变量57%的可解码信号，交叉消融仅移除不到3%的信号；联合质心的加性贡献占比超89%，交互残差均值仅为10.1%；该近似因子化特性在3-51个时间步、0.6B-14B模型范围内稳定存在；仅修改线性可解码的表征状态无法稳定控制下游生成输出。

### 核心结论
LLM对并发独立上下文变量采用近似因子化表征，重叠子空间可共存选择性可访问性，但仅修改线性可解码的表征状态不保证能稳定控制下游生成输出。
