---
title: How Robust Are Automated Fact-Checking Systems? A Cross-Benchmark Evaluation
title_zh: 自动事实核查系统鲁棒性分析：跨基准综合评估
authors:
- Aida Usmanova
- Zangir Iklassov
- Markus Leippold
- Ricardo Usbeck
affiliations:
- Leuphana University of Lüneburg
- MBZUAI
- University of Zurich
arxiv_id: '2608.25934'
url: https://arxiv.org/abs/2608.25934
pdf_url: https://arxiv.org/pdf/2608.25934
published: '2026-08-26'
collected: '2026-08-27'
category: Eval
direction: 事实核查系统 · 跨基准评测
tags:
- Fact-Checking
- Evaluation
- Retrieval
- Robustness
- LLM
- Pipeline
one_liner: 跨科学/开放网络/气候多领域评测9类事实核查系统全pipeline，明确检索为核心性能瓶颈
practical_value: '- 垂直领域RAG/Agent开发可优先投入资源优化检索模块，检索是检索-验证类pipeline的核心性能瓶颈，比优化下游推理模块投入产出比更高

  - 跨域部署算法系统时不能依赖公开基准排名选型，必须在目标业务域（如电商合规、广告核验）做针对性评测，避免跨域性能暴跌

  - 接入外部证据做下游推理前必须做噪声过滤，低质量/无关证据反而会降低任务（如商品真伪校验、内容合规审核）的最终效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有自动事实核查（AFC）系统多基于单基准开发，跨域泛化性缺乏验证，过往评测仅覆盖单模块/单阶段，缺少对检索-验证全pipeline的跨域系统性评估。
### 方法
覆盖9类模型（从随机/稀疏基线、微调Transformer、零样本LLM到AVeriTeC 2025竞赛Top2系统），在科学、开放网络、气候3个领域的4个数据集上完成全pipeline基准测试。
### 关键结果
1. 噪声证据会显著降低真实性预测效果，ClimateCheck数据集上仅输入claim的微调模型效果优于零样本LLM和AVeriTeC 2025 Top系统；
2. 模型排名强依赖领域与评测指标，SciFact上macro-F1 0.70的最优模型在ClimateCheck上暴跌至0.31，AVeriTeC 2025冠亚军排名随数据集/指标变化反转；
3. 用金标准证据替换检索输出可让所有模型准确率提升14~22个百分点，证实检索是全pipeline的核心性能瓶颈。
