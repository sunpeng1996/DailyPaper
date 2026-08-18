---
title: 'DumpsterCluster: From Dumpster Diving to Serving LLaMA-70B on $60 GPUs'
title_zh: 《DumpsterCluster：基于60美元二手GPU搭建集群运行LLaMA-70B推理服务》
authors:
- Zeyu Cao
- Xuan Guo
- Cheng Zhang
- Cheuk Hang Lau
- Ilia Shumailov
- Yiren Zhao
affiliations:
- University of Cambridge
- University of Oxford
- Quettaflop AI
arxiv_id: '2608.14614'
url: https://arxiv.org/abs/2608.14614
pdf_url: https://arxiv.org/pdf/2608.14614
published: '2026-07-09'
collected: '2026-08-18'
category: LLM
direction: LLM推理 · 二手硬件集群优化
tags:
- LLM Inference
- GPU Cluster
- Cost Optimization
- Pipeline Parallelism
- Sustainable AI
one_liner: 基于128块二手V100搭建低成本GPU集群，验证二手硬件跑大模型推理的经济与环境可行性
practical_value: '- 中小业务可采购二手V100等退役GPU，配合流水线并行优化，大幅降低LLM推理（生成式推荐文案、Agent决策推理等）的硬件投入成本

  - 部署二手GPU集群时优先选择电费低廉且绿电占比高的区域，可在控制TCO的同时降低碳排放合规风险

  - 70B级大模型推理如果对延迟要求不高（如离线批量生成商品推荐话术、用户标签），可优先考虑二手GPU集群方案，性价比远高于新硬件集群'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
数据中心硬件迭代速度快，大量功能完好的退役GPU流入二手市场，行业缺乏对这类硬件复用承载大模型推理的经济、环境可行性的系统性验证。
### 方法关键点
从零搭建含128块二手V100的DumpsterCluster并稳定运行1年，针对旧硬件适配流水线并行优化，对比新一代B200集群的成本、吞吐、能耗、碳排放全链路指标。
### 关键结果数字
- 集群硬件总成本仅2.2万美元，为8卡B200集群（60万美元）的3.7%，LLaMA-70B推理吞吐达到商用水平
- 旧GPU单位token能耗更高，仅在电费低廉区域TCO具备优势
- 电网平均碳排放强度下，二手集群跑8B模型单位token碳排放为新硬件的4倍，跑70B模型达40倍以上，仅搭配低碳能源才具备可持续性
