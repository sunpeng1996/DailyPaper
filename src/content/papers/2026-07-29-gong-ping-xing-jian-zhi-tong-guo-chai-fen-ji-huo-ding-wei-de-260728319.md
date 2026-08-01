---
title: 'Fairness Pruning: Locating Demographic Bias in GLU-MLP Layers via Differential
  Activations'
title_zh: 公平性剪枝：通过差分激活定位GLU-MLP层的人口统计学偏差
authors:
- Pere Martra
- Eugenio Martínez Cámara
- Alfonso Ureña López
affiliations:
- Universidad Internacional Menéndez Pelayo
- Universidad de Jaén
arxiv_id: '2607.28319'
url: https://arxiv.org/abs/2607.28319
pdf_url: https://arxiv.org/pdf/2607.28319
published: '2026-07-29'
collected: '2026-08-01'
category: LLM
direction: LLM公平性优化 · 神经元级偏差定位剪枝
tags:
- Fairness
- Pruning
- GLU
- Mechanistic Interpretability
- LLM
one_liner: 提出通过差分激活定位GLU架构LLM中偏差神经元的轻量公平性剪枝方法
practical_value: '- 可复用差分激活+最小对比prompt对的思路，定位业务LLM（如文案生成、客服Agent）中产生合规/偏见问题的特定神经元，避免全量微调成本

  - 对于GLU架构开源LLM的二次开发，可直接套用down_proj输入层的激活信号采集方法，实现极轻量化的不良输出干预

  - 神经元级干预仅改动不到0.03%参数即可保留99%以上基础能力，适合电商高流量、高稳定性要求场景快速迭代'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
LLM训练语料自带的人口统计学偏差会导致生成内容违反公平性要求，现有偏差缓解方法往往损伤模型通用能力，缺乏轻量、精准的偏差定位手段。

### 方法关键点
提出Fairness Pruning方法，使用最小对比prompt对，在推理阶段采集GLU架构MLP层down_proj输入的激活信号，识别对人口属性输入产生差分响应的神经元，通过置零对应神经元实现偏差干预。

### 关键结果数字
在Llama-3.2 1B/3B、Salamandra-2B上验证，仅置零最多40个神经元（占MLP总宽度不到0.031%）即可改变模型对人口变量的响应模式，同时保留99.49%的推理与常识能力；当前无符号BiasScore会同时筛选出正向/反向刻板印象神经元，整体偏差净效果取决于占优的符号方向。
