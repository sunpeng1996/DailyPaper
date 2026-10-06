---
title: Improving Atomic-Fact Recall via Focused Views in Unstructured Knowledge Editing
title_zh: 基于聚焦视图提升非结构化知识编辑的原子事实召回能力
authors:
- Ding Wu
- Ye Zhang
- Haoyu Wang
- Tianci Liu
affiliations:
- Georgia Institute of Technology
- University of Pennsylvania
- University at Albany
- University of Tennessee
arxiv_id: '2610.02772'
url: https://arxiv.org/abs/2610.02772
pdf_url: https://arxiv.org/pdf/2610.02772
published: '2026-10-01'
collected: '2026-10-06'
category: LLM
direction: LLM 非结构化知识编辑优化
tags:
- Knowledge Editing
- Unstructured Knowledge Editing
- RoPE
- Atomic Fact Recall
- LoRA
one_liner: 提出FOVEATED框架，通过RoPE扰动打破上下文捷径，提升非结构化知识编辑的原子事实召回
practical_value: '- 做Agent/RAG的非结构化知识注入时，可直接复用RoPE key侧随机偏移的trick，在LoRA微调阶段加入扰动，无需修改推理逻辑即可提升片段知识召回，零推理成本

  - 电商场景注入商品/活动规则等长文本时，可复用两阶段编辑方案，无需额外生成QA对做监督，降低标注成本的同时提升原子事实查询准确率

  - 训练生成式推荐的LoRA/Prompt Tuning时，若出现模型依赖上下文前缀才能生成正确Item的问题，可借鉴该位置扰动思路，降低上下文捷径依赖，提升生成鲁棒性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
非结构化知识编辑（UKE）支持直接向LLM注入自由格式长文本，避免了结构化三元组的标注成本，但现有方法存在严重的上下文依赖问题：编辑后的LLM可以完整复述输入的长文本，但脱离原编辑上下文时无法可靠召回其中的单个原子事实，本质是teacher forcing训练模式下，后文有前文ground truth作为上下文捷径，初始损失更低被误认为更容易学习，导致相关知识实际未被充分掌握。

### 方法关键点
- 提出FOVEATED即插即用框架，编辑阶段仅对目标句子的前文上下文的key侧RoPE位置做随机偏移扰动，query侧和目标句子的RoPE保持不变，推理阶段完全移除扰动，无额外推理开销
- 适配直接优化（DO）类编辑器：将原通道NLL损失拆分为句子级损失的加权期望，每个句子对应随机扰动后的上下文视图
- 适配定位再编辑（LTE）类编辑器：采用两阶段方案，先基于聚焦视图把句子级目标写入浅层MLP，再用基础编辑器优化深层网络，通过锚点约束保留句子级编辑结果

### 关键实验
在UnFine的3个子集（UnKE/CF/MQ）上测试，覆盖5种主流UKE编辑器（LoRA/COIN/FT-M/μKE/UnKE）、2种开源LLM（Qwen2.5-7B、Llama3.1-8B），原子事实ROUGE-L平均提升4.4点，重述query下的整体召回ROUGE-L平均提升8.4点，原编辑query下的整体召回基本无损失，编辑后LLM的通用能力波动小于4.3个点。

### 核心结论
非结构化知识编辑的上下文依赖本质是上下文诱导的难度低估，仅通过编辑阶段的RoPE位置扰动即可低成本大幅提升原子事实召回能力，无需额外标注或推理逻辑改动。
