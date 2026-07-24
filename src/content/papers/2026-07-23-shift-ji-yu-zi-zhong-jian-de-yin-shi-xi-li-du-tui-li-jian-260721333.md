---
title: 'SHIFT: Self-reconstruction Harnesses Implicit Fine-grained Thinking for Retrieval'
title_zh: SHIFT：基于自重建的隐式细粒度推理检索框架
authors:
- Yuxiao Luo
- Da Li
- Mingjie Zhang
- Zhentao He
- Shikun Zhang
- Wei Ye
affiliations:
- Peking University
- Institute of Computing Technology, Chinese Academy of Sciences
- Beihang University
arxiv_id: '2607.21333'
url: https://arxiv.org/abs/2607.21333
pdf_url: https://arxiv.org/pdf/2607.21333
published: '2026-07-23'
collected: '2026-07-24'
category: RAG
direction: RAG检索 · LLM隐式推理检索优化
tags:
- Dense Retrieval
- Implicit Reasoning
- Contrastive Learning
- LLM
- Self-supervised Learning
one_liner: 通过残差投影、双向注意力聚合与自重建损失优化LLM隐式推理检索性能
practical_value: '- 电商搜索复杂query理解场景可复用隐式连续推理+残差投影设计，替代显式query改写链路，降低推理延迟同时提升语义匹配精度

  - 隐式推理表征聚合阶段可采用双向注意力池化替代固定权重/均值池化，适配不同query的推理深度需求，避免表征坍缩

  - 检索器训练阶段可引入细粒度next-token-prediction自重建损失辅助对比学习，解决隐式推理缺乏细粒度监督的问题，无额外推理开销

  - 商品/内容等静态文档侧无需引入推理步骤，仅在query侧做隐式推理即可，可大幅降低索引构建成本，适配大规模电商商品库场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前基于LLM的检索器存在两类核心瓶颈：一是「改写-检索」的显式推理链路延迟高，难以端到端优化；二是隐式推理检索器存在两层 mismatch：因果LLM的隐层是为生成任务优化的，和检索需要的匹配表征存在固有差异，且标准对比学习仅监督最终相似度，无法指导中间隐式推理步骤的语义塑造，容易导致隐式表征坍缩、性能受限。

### 方法关键点
- 隐式推理生成：基于因果LLM自回归生成K个连续软隐token，替代显式推理文本，保留语义信息且全程可微
- 残差投影层：轻量两层残差网络将生成导向的隐层表征转换为检索导向表征，过滤生成任务带来的冗余噪声
- 双向注意力池化：自适应聚合多步隐式推理表征，无需假设后序推理步骤更优，适配不同query的推理深度需求
- 双损失训练：对比学习损失优化检索匹配效果，新增细粒度自重建损失（基于next-token-prediction），将隐式推理状态和显式推理轨迹对齐，提供细粒度监督

### 关键实验
在ReasonEmbed数据集（81K训练样本，含GPT-4o-mini生成的推理路径）上用LoRA训练，在Bright（域内）、FollowIR、BrowseComp-Plus（跨域）三个推理密集型检索基准上测试，对比BGE-M3、E5、Qwen3-Embedding、LaSER等基线：基于Qwen3-8B的SHIFT在Bright基准nDCG@10达31.0，比SOTA基线LaSER高1.7个点，比基础对比学习基线高5.3个点，仅需3步隐式推理即可达到最优效果。

### 最值得记住的一句话
静态文档侧无需引入推理，仅在query侧做隐式推理+针对性表征转换与监督，即可同时提升检索精度与效率。
