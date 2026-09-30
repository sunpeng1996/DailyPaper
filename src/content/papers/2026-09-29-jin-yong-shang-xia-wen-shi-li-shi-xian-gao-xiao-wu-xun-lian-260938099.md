---
title: Effective Dense Retrieval using Only In-Context Examples
title_zh: 仅用上下文示例实现高效无训练稠密检索
authors:
- Nour Jedidi
- Abdul Basit Ali
- Hang Li
- Jimmy Lin
affiliations:
- University of Waterloo
- The University of Queensland
arxiv_id: '2609.38099'
url: https://arxiv.org/abs/2609.38099
pdf_url: https://arxiv.org/pdf/2609.38099
published: '2026-09-29'
collected: '2026-09-30'
category: RecSys
direction: 无训练稠密检索 · 上下文示例增强
tags:
- Dense Retrieval
- In-Context Learning
- LLM
- Zero-Shot
- Prompt Engineering
one_liner: 提出无需训练的RICE方法，仅靠少量上下文示例即可从LLM提取高质量稠密检索表征
practical_value: '- 电商/垂类搜索冷启动阶段无标注训练数据时，可复用RICE思路，仅用10个左右同域query-doc对做上下文示例，快速构建适配业务的稠密检索能力，省掉标注和训练成本

  - 做prompt-based LLM embedding时可参考消融结论：仅需同域示例即可，不需要严格的正负例标注，甚至示例的标签对错影响很小，大幅降低示例构建成本

  - 动态选上下文示例时，仅需针对query选相似同域示例即可，针对doc做动态示例反而会降效果，无需开发冗余的doc侧动态示例逻辑

  - 中小流量长尾垂类场景（如电商细分品类搜索、垂直内容召回）可直接用RICE替代小模型训练流程，上线速度更快，效果优于HyDE等零样本方案'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于LLM的稠密检索大多需要额外有监督/自监督训练，零样本prompt生成的表征（如PromptReps）因查询和文档编码无共享上下文，效果有限；冷启动场景下拿到少量标注样本再重新训练检索模型成本高，亟需无需训练、仅靠少量样本就能快速适配新任务的稠密检索方案。

### 方法关键点
- 核心思路是在LLM生成表征词的prompt中加入少量同域query-doc对作为上下文示例，为查询和文档编码提供共享任务上下文，让生成的表征内积更贴合相关性
- 流程：先拿少量任务内的query-doc对，用PromptReps为每个文档生成对应表征词，组成上下文示例；编码查询/文档时把示例拼在prompt里，取LLM生成表征词前的最后一层隐状态作为检索表征
- 消融验证：同域示例的价值远大于示例的相关性标注准确性，跨域正例效果不如同域随机配对示例

### 关键实验
- 数据集：BEIR基准的10个跨领域检索任务，指标为Recall@100
- 对比基线：零样本方案（PromptReps-Dense、HyDE、CSQE等）、自监督训练方案（LLM2Vec-Gen）、全监督SOTA（BGE、Qwen3-Embedding）
- 核心结果：基于Qwen3.5-9B的RICE平均Recall@100达0.558，比PromptReps-Dense高2.4个点，比零样本方案最优结果高2.9个点，比同基座自监督训练的LLM2Vec-Gen高1.6个点；仅需10个左右上下文示例即可达到最优效果

### 核心结论
用LLM做无训练稠密检索时，同域上下文示例带来的领域适配价值远高于示例本身的相关性标注准确性，甚至不需要正例配对就能大幅提升效果
