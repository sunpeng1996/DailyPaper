---
title: 'SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding'
title_zh: SpecOPD：面向投机解码的分支并行在线策略蒸馏框架
authors:
- Tianyu Liu
- Jun Zhang
- Wenjie Huang
- Yuhao Shen
- Tianqi Xu
- Xinyue Hao
- Hongyaoxing Gu
- Xuyang Liu
- Baolin Zhang
- Yating Zhu
affiliations:
- Alibaba Qwen Business Unit
- University of Science and Technology of China
- Zhejiang University
- Carnegie Mellon University
- University of Edinburgh
arxiv_id: '2611.02846'
url: https://arxiv.org/abs/2611.02846
pdf_url: https://arxiv.org/pdf/2611.02846
published: '2026-11-01'
collected: '2026-11-05'
category: LLM
direction: LLM推理加速 · 投机解码训练优化
tags:
- Speculative Decoding
- On-Policy Distillation
- LLM Inference Acceleration
- Knowledge Distillation
- Training Optimization
one_liner: 提出分支并行在线策略蒸馏框架，无需串行rollout即可高效训练投机解码的轻量drafter模型
practical_value: '- 业务中用LLM做商品文案生成、Agent多轮交互的场景，可直接复用SpecOPD训练轻量drafter，最高可将LLM生成速度提升3.56倍，降低推理成本

  - 多分支并行共享前缀计算的思路可迁移到RAG多query生成、推荐系统多路候选召回场景，复用公共上下文计算降低算力开销

  - 针对GQA/QSA/GDN三类注意力的分支状态复用方案，可直接用到业务LLM服务的KV cache优化、长文本推理提速环节

  - 直接优化接受长度的E2E-TV损失函数，可替换传统知识蒸馏的交叉熵损失，提升小模型与大模型的行为对齐效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
投机解码（SD）是LLM推理提速的核心方案，其加速效果高度依赖轻量drafter的token接受长度；传统在线策略蒸馏（OPD）训练drafter需要串行执行draft-verify rollout，GPU利用率极低，训练吞吐量瓶颈显著，限制了SD方案的落地效率。

### 方法关键点
- 核心洞察：drafter的on-policy监督无需串行rollout，每个draft块仅需参考前缀和自身采样历史即可完成监督
- 设计提议树结构：将参考序列作为共享主干，在主干上随机采样锚点，并行生成多个独立的draft分支，彻底避免串行依赖
- 适配三类注意力的分支并行打分方案：全注意力用树掩码共享主干KV，稀疏注意力用分支一致索引器组复用前缀计算，线性注意力用索引状态回放恢复锚点状态
- 采用E2E-TV surrogate损失直接优化接受长度，提升drafter和目标大模型的分布对齐度

### 关键结果
在8B/27B/125B三类不同结构的Qwen大模型上验证，覆盖对话、代码、数学、Agent四类任务，对比串行rollout OPD基线：平均接受长度最高提升41.45%，监督token吞吐量提升16.09倍，生成速度对比自回归解码最高提升3.56倍。

### 最值得记住的一句话
对依赖采样路径对齐的蒸馏任务，去掉不必要的串行依赖、复用公共前缀计算，是同时提升训练效率和下游效果的核心思路。
