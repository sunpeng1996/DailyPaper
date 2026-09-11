---
title: 'OmniKVQuant: KV Cache Quantization for Omni-LLMs'
title_zh: OmniKVQuant：面向全模态大模型的KV Cache量化方法
authors:
- Suho Yoo
- Hyunjong Ok
- Jongmin Choi
- Jihoo Jung
- Joon Son Chung
affiliations:
- KAIST
- POSTECH
arxiv_id: '2609.11582'
url: https://arxiv.org/abs/2609.11582
pdf_url: https://arxiv.org/pdf/2609.11582
published: '2026-09-10'
collected: '2026-09-11'
category: LLM
direction: 多模态大模型 · KV Cache量化优化
tags:
- KV Cache
- Quantization
- Omni-LLM
- Efficient Inference
- Multimodal
one_liner: 训练免的全模态大模型2bit KV Cache量化方案，降显存同时大幅优于TurboQuant
practical_value: '- 业务中使用多模态LLM做商品理解、短视频文案生成、直播内容审核的场景，可直接复用该2bit量化方案，将KV cache显存占用降至1/8，支持更长上下文的音视频输入（如1分钟以上直播切片理解），精度损失控制在2%以内

  - Key的局部时间窗口min-max scaling trick可直接迁移到纯文本LLM的KV cache量化场景，针对长序列推荐/问答类Agent的长上下文推理，解决全局固定量化范围导致的漂移问题，降低量化误差

  - 分模态适配的思路可复用在多模态Embedding量化、向量数据库的多模态向量压缩场景，针对电商文本/图像/视频混合向量检索，用分模态旋转量化降低压缩损失，提升检索精度

  - 自带的融合Triton解码内核无需重构FP16缓存，可直接接入vLLM等推理框架，业务部署无需修改现有管线即可获得显存和 latency 收益'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
全模态LLM同时处理音视频、文本输入时，单分钟音视频输入对应超10000 token，KV cache显存占用很快超过模型权重本身；现有纯文本KV cache量化方法（如TurboQuant）直接应用到全模态场景会出现两个核心问题：一是temporal key drift，不同模态、不同时间窗口的Key分布差异大，全局固定量化范围适配性差；二是heterogeneous value geometry，不同模态的Value分布在特征空间的不同区域，共享Hadamard旋转压缩效果差，导致量化后性能暴跌。

### 方法关键点
- 无训练依赖，仅通过推理阶段量化策略优化实现，无需微调全模态大模型
- Key路径采用Temporal Range Adaptation：对连续32 token的局部时间窗口做min-max归一化，适配Key分布的局部漂移，无需修改固定量化码本
- Value路径采用Modality-aware Value Rotation：对文本/音频/视频三个模态分别校准专属旋转矩阵，适配不同模态Value的分布特征，降低量化误差
- 融合Triton解码内核：Attention计算时直接对2bit缓存解码，无需先重建稠密FP16缓存，同时将旋转操作移到Query侧和头输出聚合后，减少冗余计算

### 关键结果
在Qwen2.5-Omni-3B和Qwen3-Omni-30B MoE两个模型上测试，覆盖7个音视频理解基准：
- Qwen2.5-Omni-3B 2bit量化下保留98.1%的FP16平均性能，比TurboQuant高6pct以上
- Qwen3-Omni-30B MoE 2bit量化下TurboQuant仅保留51%左右的FP16性能，OmniKVQuant可保留87%左右的性能，差距达36pct
- 同等位宽下，重建MSE、注意力KL散度、输出MSE均比TurboQuant低50%以上

最值得记住的结论：全模态场景KV cache量化不能直接套用纯文本方案，针对Key的局部时间分布差异和Value的模态分布差异做适配，是低比特量化下保留高精度的核心。
