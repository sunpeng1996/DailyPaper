---
title: 'CRIM: Composable and Reusable Item Memory for Efficient Personalized Retrieval'
title_zh: CRIM：可组合可复用物品内存，实现高效个性化检索
authors:
- Haolin Li
- Haipeng Zhang
- Mang Li
- Zhaohui Xia
- Xun Zhu
- Miao Li
- Yu Zhang
- Ji Wu
affiliations:
- Tsinghua University
- Alibaba International Digital Commerce Group
arxiv_id: '2610.35323'
url: https://arxiv.org/abs/2610.35323
pdf_url: https://arxiv.org/pdf/2610.35323
published: '2026-10-26'
collected: '2026-10-27'
category: RecSys
direction: LLM个性化检索 · 物品表示缓存复用
tags:
- LLM4Rec
- Personalized Retrieval
- Semantic Compression
- Cache Reuse
- LoRA
- Efficiency
one_liner: 解耦物品语义编码与请求历史建模，通过缓存复用物品表示，大幅降低LLM个性化检索的训练推理成本
practical_value: '- 可直接复用「物品语义离线预编码缓存+请求侧长序列建模」的解耦架构，适配电商长用户历史推荐/搜索场景，线上直接降低80%+输入长度，推理时延降低75%左右

  - 训练时仅采样少量（1-8个）历史item做实时重编码，其余用缓存表示参与训练，仅需极低计算成本即可联合优化物品/请求编码器，适配百万级物料库场景训练效率提升显著

  - REC段级监督设计可直接迁移到任意长序列推荐模型，无额外标注即可提升序列建模效果，长交互历史场景Recall@100增益达3%+'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM在个性化搜索推荐场景落地面临极高的训练推理开销：用户交互历史越长，请求输入长度持续膨胀，同一个物品的文本会在不同用户、不同请求中被重复编码，浪费算力，现有方案无法同时兼顾物品语义复用、请求上下文建模和端到端联合优化的需求。

### 方法关键点
- 解耦架构：拆分物品内存编码器（IME）和请求编码器（RE），IME离线将每个物品编码为固定4个连续内存向量，跨用户跨请求缓存复用；RE在线按交互顺序拼接缓存内存向量，结合可选query生成个性化检索表示
- 语义压缩+序列监督：每个物品附加共享可学习summary token，通过文本重构+全上下文蒸馏预训练压缩语义；历史序列每4个物品插入REC读入token，预测下一段首个物品作为中间监督，提升长序列建模效果
- 高效联合训练：每个请求仅采样最多8个历史物品做实时重编码，梯度仅通过该部分更新IME，其余用无梯度缓存表示更新RE；每轮epoch结束刷新缓存保证一致性，采用LoRA微调冻结的LLM backbone，训练成本极低

### 关键实验
在三个数据集验证：新发布的LazSeq长历史检索数据集（3万请求、5万物品、最长500次交互）、Qilin、MovieLens-1M，对比同backbone的Qwen3-Embedding-4B baseline：LazSeq上Recall@100相对提升2.49%，推理时延4.05×加速（降低75%，输入长度降低80.75%；MovieLens-1M上Recall@100相对提升33.61%；Qilin上NDCG@100相对提升5.64%；请求量超过3.15万即可覆盖离线缓存构建的额外成本，百万请求时总算力节省51%。

最值得记住的一句话：LLM个性化检索的核心效率优化方向是解耦稳定可复用的物品语义与动态请求上下文，通过缓存复用离线计算大幅降低在线开销。
