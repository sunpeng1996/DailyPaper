---
title: 'PerceptionBench: Evaluating Atomic Visual Perception in Multimodal Large Language
  Models'
title_zh: PerceptionBench：多模态大语言模型原子视觉感知能力评测基准
authors:
- Zichao Lin
- Yifeng Xie
- Bowen Qu
- Haiming Wang
- Jia Li
- Haoning Wu
- Yuhao Dong
- Zuhao Yang
- Jinguo Zhu
- Haoyu Lu
affiliations:
- Moonshot AI
arxiv_id: '2607.24957'
url: https://arxiv.org/abs/2607.24957
pdf_url: https://arxiv.org/pdf/2607.24957
published: '2026-07-26'
collected: '2026-07-30'
category: Eval
direction: 多模态大模型 · 视觉感知能力评测
tags:
- MLLM
- Visual Perception
- Benchmark
- Atomic Capability
- Hallucination
one_liner: 构建隔离感知因素的MLLM原子视觉感知评测基准，覆盖10类能力共3000道标注题
practical_value: '- 多模态商品理解/推荐场景可复用10类原子视觉感知能力拆解框架，定位MLLM错误根因，区分感知错误与推理/知识错误，降低输出幻觉

  - 多模态Agent视觉感知模块选型时，可直接复用该基准的单能力隔离评测思路，无需从零构造测试集，快速筛选适配业务的MLLM底座

  - 电商商品图文审核、属性自动打标场景可参考该基准的错误归因方法，针对性优化计数、细粒度属性识别等感知短板，提升打标准确率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有MLLM评测存在两大缺陷：整体评测会混淆感知错误与推理、领域知识错误；应用导向的评测覆盖域狭窄碎片化，无法单独衡量纯视觉感知能力。
### 方法关键点
先诊断前沿MLLM在42个现有基准上的最早错误点，构建错误分类体系，从感知分支拆解出10类原子视觉感知能力；基于该分类构造3000道经过验证的测试题，每题仅测试单一项能力，难度仅来自感知层面，完全排除推理、知识因素干扰。
### 关键结果数字
16款前沿MLLM测试后，最高准确率仅59.7%，无模型突破60%阈值；感知相关幻觉是平均最弱的能力项，相近总分下不同模型的能力分布差异极大。
