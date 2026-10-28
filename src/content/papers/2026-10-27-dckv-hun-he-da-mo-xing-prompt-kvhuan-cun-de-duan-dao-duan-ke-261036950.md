---
title: 'DCKV: Learned Transform Coding of the Prompt KV Cache in Hybrid Language Models'
title_zh: DCKV：混合大模型Prompt KV缓存的端到端可学习压缩编码方法
authors:
- Egor Maximov
- Aleksei Merkelov
- Vasiliy Alekseev
- Ivan Krivorotov
- Valentin Beliaev
- Nikita Arsenin
- Dmitry Bocharov
- Aleksei Goncharov
affiliations:
- MIL Team
- DAIMLD
arxiv_id: '2610.36950'
url: https://arxiv.org/abs/2610.36950
pdf_url: https://arxiv.org/pdf/2610.36950
published: '2026-10-27'
collected: '2026-10-28'
category: LLM
direction: 大模型推理优化 · KV cache压缩
tags:
- KV-cache
- LLM Inference
- Learned Codec
- Hybrid LLM
- Model Compression
one_liner: 首个端到端训练的KV缓存编解码器，在混合LLM上实现55-100倍KV缓存压缩率
practical_value: '- 做电商/广告场景的RAG导购、Agent长会话推理业务，可直接复用DCKV的冻结LLM训练范式，无需修改原有基座权重即可适配业务长prompt缓存需求，大幅降低长上下文推理的显存开销和首token延迟

  - 可直接复用条件熵模型设计思路，基于prompt token embedding与已解码相邻KV的先验信息优化压缩率，无需牺牲推理效果即可额外降低12~16%的KV缓存存储开销

  - 优先在32K以上长prompt场景落地KV缓存压缩，短prompt下混合LLM的固定大小循环状态占存储大头，压缩收益极低，不需要额外投入优化

  - 业务需要灵活调整压缩率时，可直接缩放已训好DCKV的全局量化步长，无需重新训练即可在极小效果损失下切换压缩档位，适配不同显存规格的部署环境'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
混合大模型（如Qwen3.5系列）仅少量层采用全注意力机制，KV缓存仍是唯一随prompt长度线性增长的状态；复用长prompt的KV缓存可大幅降低首token延迟，但KV缓存的存储、跨设备传输开销极高。现有KVTC等压缩方法仅优化缓存重构误差，不感知LLM输出效果损失，压缩率上限低，无法满足长上下文场景的需求。

### 方法关键点
- 端到端联合训练变换矩阵、量化器、条件熵模型，损失函数同时优化压缩码长与LLM输出分布的KL散度，面向冻结LLM训练无需修改原模型权重
- 采用统一基变换处理所有注意力层的K和V，叠加少量非线性修正提升压缩效果，初始值从PCA初始化降低训练成本
- 条件熵模型结合prompt token embedding与棋盘式相邻已解码KV的先验信息预测编码分布，无效果损失即可额外降低12~16%码长
- 采用混合量化策略解决round操作梯度消失问题，训练稳定性更高

### 关键结果
基于Qwen3.5-2B测试，对比KVTC、xKV等基线，在RULER 4K、LongBench、RULER 32K三个长上下文基准上：
- 55倍压缩率（214字节/token）下最多损失1.8分，100倍压缩率（113字节/token）下最多损失3.6分
- 相同效果下比KVTC少用62%~72%的存储空间，32K长prompt场景下同等存储开销得分比KVTC高6.5分

### 核心结论
KV缓存压缩无需盲目追求重构精度，端到端对齐LLM输出损失可在同等效果下获得数倍的压缩率提升
