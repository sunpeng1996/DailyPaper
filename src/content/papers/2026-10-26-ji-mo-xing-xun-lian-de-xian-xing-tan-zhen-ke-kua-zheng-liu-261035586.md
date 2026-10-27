---
title: Linear Probes Transfer from Base to Distilled Language Models despite Rotation
title_zh: 基模型训练的线性探针可跨蒸馏/指令微调模型迁移
authors:
- Marios Tsatsos
affiliations:
- Independent Researcher
arxiv_id: '2610.35586'
url: https://arxiv.org/abs/2610.35586
pdf_url: https://arxiv.org/pdf/2610.35586
published: '2026-10-26'
collected: '2026-10-27'
category: LLM
direction: LLM安全 · 线性探针跨模型迁移
tags:
- Linear Probe
- Model Distillation
- Instruction Tuning
- LLM Safety
- Representation Alignment
one_liner: 验证基模型有害请求检测线性探针无需重训即可在同基座后继模型保持相近AUC
practical_value: '- 搭建LLM Agent/生成式推荐的安全审核链路时，同基座下基模型训练的线性探针可直接复用在蒸馏/指令微调模型上，无需重训，AUC波动不超过±0.053，大幅降低标注和训练成本

  - 评估业务场景的探针效果必须加纯文本分类baseline，且搭配跨分布业务测试集验证，避免探针实际仅为关键词检测器，上线后泛化失效

  - 同基座模型哪怕内部安全表征方向旋转高达35°，线性探针效果几乎不受影响，无需纠结表征对齐的微小角度差异，可直接复用

  - 探针的判定阈值不可跨数据集复用，必须在业务真实样本上重新校准，否则会出现29%~42%的良性请求误拦截率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
线性探针是LLM内部状态检测的低成本方案，仅需少量标注样本、单次矩阵乘法即可完成推理，被广泛用于有害请求拦截。但当前基模型迭代速度快，蒸馏、指令微调等后继版本发布频繁，每次重训探针需要重新标注数据、提取激活值，成本极高；且此前没有验证蒸馏这类大权重改动场景下探针是否可迁移，也不清楚内部表征旋转对探针效果的影响。

### 方法关键点
- 测试4个主流基座：Qwen2.5-Math-7B、Llama-3.1-8B、Qwen2.5-14B、Qwen2.5-32B，对应后继模型为DeepSeek-R1蒸馏推理模型、原厂指令微调Chat模型
- 训练集用XSTest有害请求数据集，独立测试集为OR-Bench+Alpaca混合的2474条跨分布样本
- 探针取Transformer残差流激活，对最后8个token激活取平均后训练逻辑回归分类器，迁移时完全不改动探针权重和归一化参数，直接应用到后继模型同层激活
- 对比baseline为纯文本TF-IDF分类器，度量指标包括AUC变化、安全表征方向旋转角度

### 关键结果
- 跨模型迁移后探针AUC波动极小：XSTest上蒸馏模型为-0.011~+0.010，指令微调模型为-0.006~+0.027；独立OR-Bench上蒸馏模型为-0.015~+0.042，指令微调模型为+0.011~+0.053
- 后继模型的安全表征方向相比基模型旋转了17°~35°，但旋转角度与AUC变化无相关性，探针实际能捕获比旋转角度预测高6~16个百分点的分类间隔
- XSTest上探针比纯文本分类器AUC高0.15~0.20，OR-Bench上优势缩小到0.03~0.20，默认阈值下会误拦截29%~42%听起来有害但实际良性的请求

**最值得记住的一句话**：线性探针跨同基座模型迁移的效果远好于表征旋转角度的预测，只有跨分布测试+文本baseline才能验证探针的真实业务价值。
