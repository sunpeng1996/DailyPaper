---
title: 'CLBench-V: Evaluating Multimodal Context Learning from Grounding to Knowledge
  Acquisition'
title_zh: CLBench-V：从定位到知识获取的多模态上下文学习评估基准
authors:
- Lai Wei
- Chengqi Li
- Jiapeng Li
- Ruina Hu
- Yue Wang
- Weiran Huang
affiliations:
- Shanghai Jiao Tong University School of Computer Science
- Zhongguancun Academy
- Shanghai Innovation Institute
arxiv_id: '2607.25294'
url: https://arxiv.org/abs/2607.25294
pdf_url: https://arxiv.org/pdf/2607.25294
published: '2026-07-27'
collected: '2026-07-30'
category: Eval
direction: 多模态大模型 · 上下文学习能力评估
tags:
- Multimodal LLM
- Context Learning
- Benchmark
- Evaluation
- Multimodal Understanding
one_liner: 推出覆盖多领域的多模态上下文学习基准CLBench-V，拆解三维任务维度并验证现有模型性能远未饱和
practical_value: '- 搭建多模态RAG/Agent评测集时可复用三维拆解框架：从上下文定位、新信息应用、新知识学习三层逐步定位能力缺陷，无需全量case排查

  - 多模态评测集构建可复用自动化构造+过滤流程，降低电商商品图文、财报、网页等特定领域的评测集搭建成本

  - 现有多模态大模型上下文学习最优得分不足30%，做电商多模态推荐/导购Agent时必须做针对性微调或RAG策略增强，不能直接依赖原生模型能力'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有上下文学习评估仅聚焦文本场景，无法覆盖真实业务中科学、金融、空间推理等多模态上下文（如图表、地图、网页）的能力评测需求，且难以定位模型上下文使用的具体故障点。
### 方法关键点
1. 搭建CLBench-V多模态上下文学习基准，按上下文定位、新信息应用、新知识学习三个维度组织任务，覆盖科学、金融、长文档理解、空间推理、网页VQA五大领域；
2. 评测集混合改造公开基准与新增自动化构造的数据集，降低构造成本。
### 关键结果
共覆盖3443个测试样例，测试6款当前主流多模态大模型，最优整体得分仅0.2847；其中InternVL3.5-30B-A3B在上下文定位、新知识学习维度表现最优，Qwen3.5-Plus在新信息应用维度表现最优，当前多模态上下文学习能力远未饱和。
