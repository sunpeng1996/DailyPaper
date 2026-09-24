---
title: 'When Learned Context Planning Fails to Beat Strong Retrieval: A Controlled
  Study of Planning, Routing, and Reranking for Long-Context QA'
title_zh: 长上下文QA场景下学习式上下文规划与强检索的对比研究
authors:
- Yingrui Li
- Han Chen
affiliations:
- Independent Researcher, United States
arxiv_id: '2609.26976'
url: https://arxiv.org/abs/2609.26976
pdf_url: https://arxiv.org/pdf/2609.26976
published: '2026-09-22'
collected: '2026-09-24'
category: RAG
direction: 长上下文RAG 上下文规划性能评估
tags:
- RAG
- Long-Context QA
- Context Planning
- BM25
- LoRA
- Controlled Experiment
one_liner: 通过受控实验验证长上下文QA中学习式上下文规划无法超越强检索基线仅为弱相关性信号
practical_value: '- 搭建RAG系统的上下文选择模块时，不要盲目投入研发学习式规划，必须先和BM25、锚定混合检索、cross-encoder重排等工业界强基线做对照测试，避免无效投入

  - 学习式规划的小幅度增益大概率为统计噪声，需通过配对显著性检验、跨域留出集验证确认有效性，不要仅凭少量样例的直观效果上线

  - 锚定混合检索策略（BM25 top块前置+混合检索结果补全）性能表现稳定，可直接复用在电商商品/评论检索、用户长期兴趣理解等RAG场景

  - 若尝试学习式上下文规划，可将其输出作为弱相关性特征加入现有重排链路，而非直接替换成熟检索模块，大幅降低试错成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前RAG领域大量研究宣称学习式上下文规划可显著提升长上下文任务效果，但大多未与工业界常用的强检索基线做严格受控对比，无法确认增益真实性，易导致研发资源浪费。

### 方法关键点
- 数据集：采用LongBench-v2 MCQ共503道长上下文选择题，拆分140训练/28验证/152无泄露测试集
- 基线体系：覆盖BM25、稠密检索、锚定混合检索、MMR、cross-encoder重排等全链路强基线
- 学习式规划实现：基于Qwen2.5-7B-Instruct做LoRA SFT，训练数据来自outcome-supervised trace mining，即采样多组规划后仅保留答对的样本训练
- 控制逻辑：严格对齐6k/9k/18k字符的上下文长度预算，规避路由数据泄露，采用配对显著性检验验证结果可靠性

### 关键结果数字
18k字符预算下，锚定混合检索准确率36.18%，BM25准确率35.98%，最优学习式规划方法仅34.19%；152道无数据泄露的测试集上，锚定混合检索准确率42.11%，规划方法仅36.84%；仅6k预算下规划加重排有1.79%的增益，但统计不显著（p=0.478）。

### 核心结论
学习式上下文规划目前仅为弱相关性信号，无法替代强检索模块，所有规划相关的增益都必须经过强基线对照、显著性检验才能确认有效。
