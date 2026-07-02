---
title: 'AGC-Bench: Measuring Artificial General Creativity'
title_zh: AGC-Bench：通用人工智能创造力评测基准
authors:
- Roger Beaty
- Vijeta Deshpande
- Clin K. Y. Lai
- Anna Attuch
- Namrata Shivagunde
- Swastik Roy
- Rajkumar Pujari
- Paul V. DiStefano
- Sherin Muckatira
- Claire E. Stevenson
affiliations:
- Pennsylvania State University
- University of Massachusetts Lowell
- University of Amsterdam
- Amazon AGI
- Dartmouth College
arxiv_id: '2607.01152'
url: https://arxiv.org/abs/2607.01152
pdf_url: https://arxiv.org/pdf/2607.01152
published: '2026-07-01'
collected: '2026-07-02'
category: Eval
direction: 大模型通用创造力评测体系构建
tags:
- LLM
- Evaluation
- Benchmark
- LLM-as-Judge
- Creativity
one_liner: 构建多领域通用AI创造力评测基准，配套开源校准后的专用评测模型AGC-Judge
practical_value: '- 生成式推荐的文案、创意卖点/标题生成效果评测场景，可复用Judge Response Theory校准LLM-as-judge的宽严偏置，提升评测一致性

  - 电商创意素材（广告文案、直播话术、短视频脚本）的自动化评测需求，可直接微调开源AGC-Judge适配业务自定义创意评分规则

  - 设计具备创意生成能力的电商Agent（营销方案脑暴、个性化内容创作）时，可引入AGC-Bench分领域创造力维度做能力对齐'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有AI创造力评测基准零散异构，缺乏统一标准，无法验证LLM创造力是领域专属还是通用能力、与通用智能是否可分离的核心问题。
### 方法关键点
1. 系统筛查3101篇相关论文，筛选497个基准，构建首版覆盖78个数据集、横跨脑暴/STEM/叙事/幽默等6个领域的AGC-Bench，配套Agentic harness将异构基准转换为HELM标准格式
2. 引入Judge Response Theory校准LLM评审偏置，基于3个前沿大模型的校正评分微调Qwen3-30B得到开源AGC-Judge，跨基准泛化性优秀
3. 对83个LLM做因子分析、prompt对照实验、人-机对比实验验证基准有效性
### 关键结果数字
- 通用创造力因子c可解释81.5%的模型表现方差，与通用知识/推理相关但可分离
- 「要求模型更有创意」的prompt对表现提升远高于开启推理能力
- 顶级人类的创造力表现仍优于当前最好的LLM
