---
title: 'RPTune: Learned Context Curation for LLM Catalog Search'
title_zh: RPTune：面向LLM商品目录搜索的上下文自动优化框架
authors:
- Chuxuan Hu
- Hejie Cui
- Norman Huang
- Shubham Kumar Bharti
- Wang-Chiew Tan
- Sercan Ö. Arık
affiliations:
- Google
- University of Illinois Urbana-Champaign
arxiv_id: '2610.00964'
url: https://arxiv.org/abs/2610.00964
pdf_url: https://arxiv.org/pdf/2610.00964
published: '2026-10-01'
collected: '2026-10-02'
category: RecSys
direction: 中小商家LLM商品搜索 · 上下文选排优化
tags:
- LLM4Rec
- Context Curation
- Catalog Search
- RLHF
- Synthetic Data
one_liner: 无需人工标注的LLM商品搜索框架，通过上下文选排+后训练提升准确率同时降低延迟
practical_value: '- 中小商家冷启动无用户行为数据场景，可直接复用全LLM驱动的搜索方案，放弃传统多阶段检索，长上下文LLM全目录推理的准确率比RAG高9个点以上，部署成本更低

  - 上下文优化trick可直接复用：高相关性商品优先放在上下文末尾（升序排列）比随机/原生排序提升16+个EM点，25%的目录裁剪率是准确率与延迟的最优平衡点

  - 零标注训练数据生成方案可迁移：针对每个商品用大模型生成10条对应query，再用大模型批量输出全目录相关性分数，适配所有缺少标注的垂直搜索场景

  - 后训练奖励设计可复用：采用context-relative reward，仅要求LLM选当前上下文内的最优商品，不要求全局最优，训练信号有效性比DPO/IRPO更高'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
92.9%的中小商家商品目录token数低于1M，适配长上下文LLM直接全目录推理，相比传统多阶段检索成本更低、准确率更高，但LLM存在长上下文利用不均、中间信息易被忽略的问题，且传统检索依赖用户行为数据，中小商家普遍缺失此类数据也无算法团队维护复杂pipeline，亟需轻量高效的LLM搜索方案。

### 方法关键点
- 全合成训练数据：针对每个商品用前沿大模型生成10条对应搜索query，再批量输出全目录下每个商品对每条query的0-1相关性分数，无需人工标注或用户行为数据
- 上下文选排模块：Encoder用MNRL损失训练语义相似度，Reorganizer用MLP生成任务自适应调整分数，综合两部分分数排序后保留前25%商品，按优先级升序排列（高相关商品放上下文末尾，适配LLM对首尾信息更敏感的特性），Reorganizer用下游LLM反馈做RL训练优化排序效果
- LLM后训练：用GRPO在裁剪后的上下文上训练，采用context-relative reward：选到当前上下文最优商品给+1，选到不存在的商品给-1，其余给0，避免全局最优要求带来的训练信号浪费

### 关键实验
在7个不同垂直领域的真实中小商家数据集上测试，每个商家含100条复杂多约束对话式query，对比9款开源/闭源LLM、传统RAG、RAG-Fusion、LongLLMLingua等基线：上下文选排阶段平均提升14个EM点，最高31.4个点，延迟平均降低28%，效果相当于升级一档大模型，最高比基线快21倍；加后训练后Gemma 4B的EM提升20.3个点，从10.7%升至31%，准确率追平前沿大模型；零样本迁移到新商家/新商品平均仍有18个EM点的提升，无需重新训练。

最值得记住的一句话：中小商家商品搜索场景下，全LLM驱动的in-context搜索方案比传统多阶段检索性价比更高，通过针对性上下文选排和轻量化后训练，小模型即可达到前沿大模型的效果。
