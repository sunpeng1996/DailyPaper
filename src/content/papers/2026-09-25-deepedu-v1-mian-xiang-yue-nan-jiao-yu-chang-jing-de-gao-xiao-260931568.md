---
title: 'DeepEdu-v1: Efficient and Scalable Agentic LLMs for Vietnamese Education'
title_zh: DeepEdu-v1：面向越南教育场景的高效可扩展Agent大模型系统
authors:
- Quang Nguyen
- Hieu Nguyen
- Hien Hoang
- Toan Pham
- Cong Tran
- Nam Vu
affiliations:
- Posts and Telecommunications Institute of Technology, Ha Noi, Vietnam
arxiv_id: '2609.31568'
url: https://arxiv.org/abs/2609.31568
pdf_url: https://arxiv.org/pdf/2609.31568
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: Agent 本地化自进化与长上下文优化
tags:
- Agentic LLM
- Long Context Inference
- Self-improving Agent
- Data Sovereignty
- Edge Deployment
one_liner: 提出SCALE框架，结合长上下文优化引擎与无微调自进化Agent层，适配资源受限区域本地化部署需求
practical_value: '- 可复用Similarity Chunk Rolling长上下文优化trick：对连续相似query子块做锚点聚类，单集群仅触发1次KV检索，可降低长用户行为序列、RAG长文档等场景的prefill开销，论文实测减少7.7×检索调用

  - 可复用无微调自进化Agent架构：用动态可审计的playbook存储领域知识替代LoRA微调，适配电商新品规则、大促话术等需要快速迭代的场景，避免灾难性遗忘和重训成本

  - 可直接复用Retrieval-Augmented Execution设计：Agent推理时仅拉取query相关的top-K条playbook规则，而非全量传入，实测同时降低TTFT、减少长prompt干扰提升准确率，可直接落地到业务Agent的prompt工程'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
发展中区域本地化AI落地面临双重矛盾：云服务违反数据主权法规，且通用大模型对区域特有知识幻觉率高；自部署开源模型则面临长上下文KV cache占用高、prefill latency高的硬件瓶颈，同时持续微调适配本地化知识成本高、易出现灾难性遗忘，教育场景对知识准确性、部署成本的要求更加严苛。

### 方法关键点
1. 长上下文推理引擎Similarity Chunk Rolling（SCR）：对prefill阶段的连续query子块做锚点聚类，余弦相似度≥阈值的子块归为同一集群，单集群仅触发1次KV缓存检索，并行计算集群内稀疏注意力，大幅降低冗余检索开销
2. 自进化Agent层：采用Generator-Reflector-Curator三角色架构，通过动态维护结构化可审计的playbook存储本地化知识，无需权重更新即可迭代知识；搭配Retrieval-Augmented Execution（RAE），每次推理仅调用query相关的top-K条playbook条目，避免长prompt的干扰

### 关键结果
对比TokenSelect基线，SCR减少7.7×检索调用，prefill latency降低约35%，精度持平或优于基线；部署版本对比标准vLLM服务，TTFT提升近2倍，复杂任务Agent准确率从70.0%提升至79.5%，金融推理、交互Agent赛道增益最显著。

最值得记住的一句话：资源受限区域的本地化Agent落地无需盲目堆大模型参数，长上下文推理优化结合无权重更新的自进化上下文工程，是兼顾成本、准确率、数据主权的可行路径。
