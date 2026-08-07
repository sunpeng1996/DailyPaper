---
title: 'SIGNPOST-Bench: Benchmarking Text-Vision Conflict Resolution in Multimodal
  Large Language Models'
title_zh: SIGNPOST-Bench：多模态大模型图文冲突解决能力基准
authors:
- Sirun Li
- Minghao Liu
- Ling Dai
- Yong Li
- Haoxin Lyu
- Junting Zhou
- Fan Zhang
affiliations:
- Peking University
- 2077AI
- The Hong Kong University of Science and Technology
arxiv_id: '2608.04244'
url: https://arxiv.org/abs/2608.04244
pdf_url: https://arxiv.org/pdf/2608.04244
published: '2026-08-03'
collected: '2026-08-07'
category: Eval
direction: 多模态大模型评估 · 图文冲突仲裁
tags:
- MLLM
- Multimodal Benchmark
- Conflict Resolution
- Counterfactual Evaluation
- Geolocation
one_liner: 构建受控反事实基准SIGNPOST-Bench，量化评估20款MLLM的图文冲突仲裁能力
practical_value: '- 多模态商品/内容排序场景可复用反事实变量构造方法，测试模型对图文冲突（如商品图与标题不符）的鲁棒性

  - 多模态Agent落地时可借鉴该基准的受控干预框架，定量评估不同模态信号的权重分配合理性

  - 电商虚假内容检测场景可参考对抗文本注入思路，构造测试集校验多模态审核模型的抗干扰能力'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有MLLM评估基准多针对图文对齐场景，无法衡量模型在多模态信号冲突时的证据仲裁能力，缺少可控的量化评估框架。

### 方法关键点
构建SIGNPOST-Bench反事实基准，对每张原始图像生成空白、相似、随机、对抗4类变体，仅修改局部场景文本、保留其余视觉内容，可配对测量冲突文本对模型推理结果的影响；基准包含5111组反事实样本、25555张图像变体，覆盖4个数据集。

### 关键结果数字
测试20款MLLM发现，对抗文本变体使中位定位误差从282km升至1347km，涨幅达4.8倍；6.5%-20.1%的对抗样本预测结果距离注入目标小于50km；所有模型在对抗场景下的目标距离相较空白场景均出现平均下降，且干净输入的性能无法预测冲突场景下的鲁棒性。
