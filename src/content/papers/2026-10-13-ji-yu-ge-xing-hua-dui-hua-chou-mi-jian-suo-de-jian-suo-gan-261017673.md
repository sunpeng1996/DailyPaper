---
title: 'RALI@iKAT 2026: Retrieval-aware User Profile Denoising via Personalized Conversational
  Dense Retrieval'
title_zh: 基于个性化对话稠密检索的检索感知用户画像去噪
authors:
- Yuchen Hui
- Fengran Mo
- Jia Ao Sun
- Yuxing Tian
- Wenhao Xu
- Jian-Yun Nie
affiliations:
- Université de Montréal
arxiv_id: '2610.17673'
url: https://arxiv.org/abs/2610.17673
pdf_url: https://arxiv.org/pdf/2610.17673
published: '2026-10-13'
collected: '2026-10-14'
category: RecSys
direction: 个性化对话检索 · 用户画像去噪
tags:
- Conversational Search
- Dense Retrieval
- User Profile Denoising
- Personalized Search
- LoRA
one_liner: 提出个性化对话稠密检索模型PCDR，在嵌入空间隐式完成检索感知的用户画像去噪
practical_value: '- 针对电商导购Agent、会话式搜索场景的长文本用户画像噪声问题，可复用PCDR隐式去噪思路：无需显式调用LLM做画像标签筛选或查询重写，直接将对话历史+全量用户画像输入微调后的嵌入模型生成查询向量，既避免过个性化漂移，又省去LLM调用的延迟和成本

  - 小样本微调个性化检索模型可复用其训练范式：先在通用对话检索数据集上训练对话骨干模型，再用少量业务标注数据搭配LoRA（rank=64效果最优）微调，同时引入历史人工改写查询的蒸馏损失、初始化锚定损失和全局负采样，效果优于全量微调

  - 会话检索的工程链路可直接复用PCDR+异质检索器RRF融合架构：PCDR与BM25、SPLADE等检索结果做RRF融合，NDCG@5可提升3~4个百分点；完全取消LLM查询改写环节的纯稠密检索架构也能达到和带改写架构相当的效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有个性化对话检索普遍采用「LLM改写查询→检索」的流水线，需要显式从用户画像中挑选相关短语注入改写后的查询，容易引入噪声导致过个性化和查询漂移；同时用户画像随着会话推进持续累积变长，噪声问题被进一步放大，而离散token空间的改写无法表达隐式的检索相关语义，也没有面向下游检索任务优化。
### 方法关键点
- 提出PCDR（Personalized Conversational Dense Retrieval），仅微调双编码器的查询侧，文档编码器保持冻结，直接将对话历史+全量用户profile联合编码为单一查询嵌入，在隐空间完成检索感知的画像去噪，无需中间查询改写步骤
- 两阶段训练：先用TopiOCQA通用对话检索数据集微调Qwen3-Embedding 0.6B得到对话骨干conv-Qwen3，再用iKAT 2023-2025的少量个性化标注数据微调，采用组合损失：BiXSE graded ranking损失、人类改写查询的知识蒸馏损失、初始化锚定损失，搭配全局负采样稳定训练
- 超参优选：LoRA rank=64时效果最优，超过全量微调
### 关键结果
离线实验在iKAT 2023-2025的44个held-out turns上，PCDR的NDCG@3达33.1，比零样本conv-Qwen3高4.1个点，仅比人类改写的Oracle上限低3.2个点；在线iKAT 2026交互评测中，PCDR单独使用的NDCG@5达0.557，和BM25做RRF融合后可提升到0.580；完全去掉LLM查询改写的PCDR+CDR架构效果和带改写的架构相当，延迟更低。
### 核心结论
个性化用户画像的去噪不需要在离散文本空间显式做，直接在面向检索优化的稠密嵌入空间隐式完成，效果更好、成本更低
