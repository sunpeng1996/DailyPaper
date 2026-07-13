---
title: Self-Guided Test-Time Training for Long-Context LLMs
title_zh: 面向长上下文大语言模型的自引导测试时训练方法
authors:
- Xinyu Zhu
- Zhe Xu
- Xiaohan Wei
- Yunchen Pu
- Fei Tian
- Chonglin Sun
- Kaushik Rangadurai
- Hua Zhi
- Frank Shyu
- Sandeep Pandey
affiliations:
- Meta AI
- University of Virginia
arxiv_id: '2607.09415'
url: https://arxiv.org/abs/2607.09415
pdf_url: https://arxiv.org/pdf/2607.09415
published: '2026-07-09'
collected: '2026-07-13'
category: LLM
direction: 长上下文LLM · 测试时训练
tags:
- Long-Context LLM
- Test-Time Training
- Span Selection
- Inference Optimization
- Reasoning
one_liner: 通过LLM自选择问题相关证据片段做测试时训练，低成本提升长上下文推理性能
practical_value: '- 做RAG/长文档问答类Agent时，可复用该证据片段筛选思路，对召回的TopN相关片段做轻量LoRA测试时微调，相比全上下文适配成本降低70%以上，同时提升回答准确率

  - 电商推荐场景处理长用户行为序列/长商品属性文档时，可先让模型筛选和当前推荐query/用户兴趣强相关的片段再做适配，避免冗余信息干扰，同时降低推理计算量

  - 所有测试时训练场景可直接复用核心结论：不要盲目用全上下文或随机采样片段做适配，高信噪比的相关片段才能带来性能收益，噪声片段反而会损害原有性能'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文LLM仅扩大上下文窗口无法保证有效利用输入，随着输入长度增长准确率明显下降；测试时训练（TTT）是优化长上下文性能的有效路径，但现有全上下文TTT计算成本极高，随机采样片段做TTT又引入大量噪声（多数片段和当前问题无关），反而会降低基础模型性能。预实验显示随机采样TTT在LongBench-v2上准确率从40.4%降到38.9%，而基于标注的oracle片段TTT能提升到45.9%，亟需低成本高信噪比的TTT方案。
### 方法关键点
- 两阶段框架S-TTT：第一阶段让基础LLM自行从长上下文中标记和当前问题相关的证据片段，无需额外标注或外部模型
- 第二阶段仅在筛选出的高相关片段上做下一词预测的测试时训练，不改动模型架构、训练目标和最终解码逻辑，仅优化适配用的训练数据
- 支持用LoRA等轻量适配方案，计算成本远低于全上下文TTT
### 关键结果
在LongBench-v2、LongBench-Pro两个长上下文推理基准上测试，对比基础模型、随机片段TTT等基线，Qwen3-4B-Thinking和Llama-3.1-8B-Instruct两个模型的准确率最高获得15%的相对提升，同时计算成本仅为全上下文TTT的1/5以下。
### 核心结论
长上下文场景下测试时训练的核心瓶颈不是适配机制，而是训练数据的信噪比，高相关片段适配能带来收益，噪声片段适配反而会损害性能
